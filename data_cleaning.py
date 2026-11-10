
import pandas as pd


def generate_cleaning_report(df):
    """
    Inspect a dataset and identify common data-quality issues.
    Does not modify the original dataset.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")

    if df.empty:
        raise ValueError("Cannot inspect an empty dataset.")

    missing_by_column = (
        df.isna().sum()
        .astype(int)
        .to_dict()
    )

    duplicate_rows = int(df.duplicated().sum())

    # Identify text cells with unnecessary leading/trailing spaces
    text_columns = df.select_dtypes(
        include=["object", "string"]
    ).columns

    whitespace_cells = 0

    for column in text_columns:
        whitespace_cells += int(
            df[column].map(
                lambda value: (
                    isinstance(value, str)
                    and value != value.strip()
                )
            ).sum()
        )

    return {
        "total_rows": int(len(df)),
        "total_columns": int(len(df.columns)),
        "missing_by_column": missing_by_column,
        "total_missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": duplicate_rows,
        "whitespace_cells": whitespace_cells,
        "numeric_columns": list(
            df.select_dtypes(include="number").columns
        ),
        "categorical_columns": list(text_columns),
    }


def clean_dataset(
    df,
    missing_strategy="keep",
    duplicate_action="keep",
    trim_whitespace=True
):
    """
    Clean a copy of the dataset using user-selected options.

    Missing strategies:
        keep
        drop_rows
        fill_numeric_median_categorical_mode

    Duplicate actions:
        keep
        remove
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")

    if df.empty:
        raise ValueError("Cannot clean an empty dataset.")

    valid_missing_strategies = [
        "keep",
        "drop_rows",
        "fill_numeric_median_categorical_mode",
    ]

    valid_duplicate_actions = [
        "keep",
        "remove",
    ]

    if missing_strategy not in valid_missing_strategies:
        raise ValueError("Invalid missing-value strategy.")

    if duplicate_action not in valid_duplicate_actions:
        raise ValueError("Invalid duplicate action.")

    # Work on a copy. Never modify the original dataset.
    cleaned_df = df.copy(deep=True)

    cleaning_log = []

    original_rows = len(cleaned_df)

    # 1. Trim unnecessary whitespace
    if trim_whitespace:

        text_columns = cleaned_df.select_dtypes(
            include=["object", "string"]
        ).columns

        trimmed_cells = 0

        for column in text_columns:

            mask = cleaned_df[column].map(
                lambda value: (
                    isinstance(value, str)
                    and value != value.strip()
                )
            )

            trimmed_cells += int(mask.sum())

            cleaned_df[column] = cleaned_df[column].map(
                lambda value: (
                    value.strip()
                    if isinstance(value, str)
                    else value
                )
            )

        cleaning_log.append(
            f"Trimmed whitespace in {trimmed_cells} text cells."
        )

    # 2. Handle missing values
    if missing_strategy == "drop_rows":

        before = len(cleaned_df)

        cleaned_df = cleaned_df.dropna().copy()

        removed = before - len(cleaned_df)

        cleaning_log.append(
            f"Removed {removed} rows containing missing values."
        )

    elif missing_strategy == "fill_numeric_median_categorical_mode":

        filled_cells = 0

        for column in cleaned_df.columns:

            missing_count = int(
                cleaned_df[column].isna().sum()
            )

            if missing_count == 0:
                continue

            if pd.api.types.is_numeric_dtype(
                cleaned_df[column]
            ):

                median_value = cleaned_df[column].median()

                if pd.notna(median_value):

                    cleaned_df[column] = (
                        cleaned_df[column].fillna(median_value)
                    )

                    filled_cells += missing_count

            else:

                modes = cleaned_df[column].mode(
                    dropna=True
                )

                if not modes.empty:

                    cleaned_df[column] = (
                        cleaned_df[column].fillna(modes.iloc[0])
                    )

                    filled_cells += missing_count

        cleaning_log.append(
            f"Filled {filled_cells} missing cells "
            "using numeric medians and categorical modes."
        )

    else:

        cleaning_log.append(
            "Missing values were left unchanged."
        )

    # 3. Handle duplicate rows
    if duplicate_action == "remove":

        before = len(cleaned_df)

        cleaned_df = (
            cleaned_df.drop_duplicates()
            .reset_index(drop=True)
        )

        removed = before - len(cleaned_df)

        cleaning_log.append(
            f"Removed {removed} duplicate rows."
        )

    else:

        cleaning_log.append(
            "Duplicate rows were retained."
        )

    # 4. Generate final report
    final_report = generate_cleaning_report(cleaned_df)

    return {
        "cleaned_df": cleaned_df,
        "cleaning_log": cleaning_log,
        "original_rows": original_rows,
        "cleaned_rows": len(cleaned_df),
        "rows_removed": original_rows - len(cleaned_df),
        "final_missing_values": final_report[
            "total_missing_values"
        ],
        "final_duplicate_rows": final_report[
            "duplicate_rows"
        ],
    }
