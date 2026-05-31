import pandas as pd


def load_data(path):

    df = pd.read_csv(path)

    return df


def dataset_summary(df):

    print("\nFIRST 5 ROWS:\n")
    print(df.head())

    print("\nDATASET INFO:\n")
    print(df.info())

    print("\nSTATISTICAL SUMMARY:\n")
    print(df.describe())


def calculate_total_average(df):

    subjects = [
        "math score",
        "reading score",
        "writing score"
    ]

    df["Total"] = df[subjects].sum(axis=1)

    df["Average"] = df[subjects].mean(axis=1)

    return df


def pass_fail_analysis(df):

    subjects = [
        "math score",
        "reading score",
        "writing score"
    ]

    df["Status"] = df[subjects].apply(
        lambda row: "Pass"
        if all(mark >= 40 for mark in row)
        else "Fail",
        axis=1
    )

    return df


def calculate_grade(score):

    if score >= 90:
        return "A+"

    elif score >= 80:
        return "A"

    elif score >= 70:
        return "B"

    elif score >= 60:
        return "C"

    elif score >= 50:
        return "D"

    else:
        return "FAIL"


def add_grade_column(df):

    df["Grade"] = df[
        "writing score"
    ].apply(calculate_grade)

    return df