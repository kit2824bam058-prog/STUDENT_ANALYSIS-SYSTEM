def student_ranking(df):

    df = df.sort_values(
        by="Average",
        ascending=False
    )

    df["Rank"] = df[
        "Average"
    ].rank(
        ascending=False,
        method="dense"
    ).astype(int)

    return df