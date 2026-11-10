
import pandas as pd


def profile_dataset(df):
    """
    Generate a verified data-quality and statistical
    profile using Pandas.
    """

    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame.")

    if df.empty:
        raise ValueError("The uploaded dataset is empty.")

    total_rows, total_columns = df.shape

    # Column-level information
    column_details = []

    for column in df.columns:
        series = df[column]

        missing = int(series.isna().sum())
        non_missing = int(series.notna().sum())

        column_details.append({
            "column_name": str(column),
            "data_type": str(series.dtype),
            "non_null_count": non_missing,
            "missing_count": missing,
            "missing_percentage": round(
                (missing / total_rows) * 100, 2
            ),
            "unique_values": int(series.nunique()),
        })

    # Numeric statistics
    numeric_summary = {}

    numeric_columns = df.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:
        series = df[column]

        numeric_summary[str(column)] = {
            "mean": round(float(series.mean()), 2),
            "median": round(float(series.median()), 2),
            "minimum": float(series.min()),
            "maximum": float(series.max()),
            "standard_deviation": round(
                float(series.std()), 2
            ) if non_missing_count(series) > 1 else 0
        }

    # Categorical distributions
    categorical_summary = {}

    categorical_columns = df.select_dtypes(
        include=["object", "category", "bool"]
    ).columns

    for column in categorical_columns:
        categorical_summary[str(column)] = (
            df[column]
            .value_counts(dropna=False)
            .head(5)
            .to_dict()
        )

    # Duplicate records
    duplicate_rows = int(df.duplicated().sum())

    # Duplicate column names
    duplicate_columns = [
        str(column)
        for column in df.columns[
            df.columns.duplicated()
        ]
    ]

    # Constant columns
    constant_columns = [
        str(column)
        for column in df.columns
        if df[column].nunique(dropna=False) <= 1
    ]

    return {
        "dataset_overview": {
            "total_rows": total_rows,
            "total_columns": total_columns,
            "total_missing_values": int(
                df.isna().sum().sum()
            ),
            "duplicate_rows": duplicate_rows,
        },
        "column_details": column_details,
        "numeric_summary": numeric_summary,
        "categorical_summary": categorical_summary,
        "duplicate_columns": duplicate_columns,
        "constant_columns": constant_columns,
    }


def non_missing_count(series):
    return int(series.notna().sum())
