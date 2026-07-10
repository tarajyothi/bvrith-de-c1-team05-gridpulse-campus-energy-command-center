"""
Data Quality Rules Template

Week: 6
Purpose:
    Keep reusable data quality helper functions here.

Note:
    Teams may implement DQ rules directly in SQL notebooks.
    Use this file only when reusable Python/PySpark helper logic is useful.
"""


def required_field_rule(df, field_name):
    """Return records where a required field is null."""
    return df.filter(df[field_name].isNull())


def non_negative_rule(df, field_name):
    """Return records where a numeric field is negative."""
    return df.filter(df[field_name] < 0)


def duplicate_key_rule(df, key_field):
    """Return duplicate keys and their counts."""
    return (
        df.groupBy(key_field)
        .count()
        .filter("count > 1")
    )


def valid_reference_rule(fact_df, reference_df, fact_key, reference_key):
    """
    Return records from fact_df where fact_key does not exist in reference_df.

    Example:
        invalid_records = valid_reference_rule(silver_df, ref_df, "zone_id", "zone_id")
    """
    return fact_df.join(reference_df, fact_df[fact_key] == reference_df[reference_key], "left_anti")
