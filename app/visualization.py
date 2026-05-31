import matplotlib.pyplot as plt


def math_vs_writing(df):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["math score"],
        df["writing score"]
    )

    plt.xlabel("Math Score")
    plt.ylabel("Writing Score")

    plt.title(
        "Math Score vs Writing Score"
    )

    plt.savefig(
        "charts/math_vs_writing.png"
    )

    plt.close()


def reading_vs_writing(df):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        df["reading score"],
        df["writing score"]
    )

    plt.xlabel("Reading Score")
    plt.ylabel("Writing Score")

    plt.title(
        "Reading Score vs Writing Score"
    )

    plt.savefig(
        "charts/reading_vs_writing.png"
    )

    plt.close()


def grade_distribution(df):

    grade_counts = df[
        "Grade"
    ].value_counts()

    plt.figure(figsize=(8, 5))

    plt.bar(
        grade_counts.index,
        grade_counts.values
    )

    plt.xlabel("Grades")
    plt.ylabel("Number of Students")

    plt.title(
        "Grade Distribution"
    )

    plt.savefig(
        "charts/grade_distribution.png"
    )

    plt.close()


def pass_fail_chart(df):

    counts = df[
        "Status"
    ].value_counts()

    plt.figure(figsize=(6, 6))

    plt.pie(
        counts,
        labels=counts.index,
        autopct='%1.1f%%'
    )

    plt.title(
        "Pass vs Fail Analysis"
    )

    plt.savefig(
        "charts/pass_fail_chart.png"
    )

    plt.close()


def subject_comparison(df):

    subjects = [
        "math score",
        "reading score",
        "writing score"
    ]

    averages = df[
        subjects
    ].mean()

    plt.figure(figsize=(8, 5))

    averages.plot(kind="bar")

    plt.title(
        "Subject Comparison"
    )

    plt.ylabel("Average Marks")

    plt.savefig(
        "charts/subject_comparison.png"
    )

    plt.close()


def ranking_chart(df):

    top_students = df.head(10)

    plt.figure(figsize=(10, 5))

    plt.bar(
        top_students.index.astype(str),
        top_students["Average"]
    )

    plt.title(
        "Top Student Rankings"
    )

    plt.xlabel("Student Index")
    plt.ylabel("Average Score")

    plt.savefig(
        "charts/ranking_chart.png"
    )

    plt.close()


def actual_vs_predicted(
    y_test,
    predictions
):

    plt.figure(figsize=(8, 5))

    plt.scatter(
        y_test,
        predictions
    )

    plt.xlabel("Actual Scores")
    plt.ylabel("Predicted Scores")

    plt.title(
        "Actual vs Predicted Scores"
    )

    plt.savefig(
        "charts/actual_vs_predicted.png"
    )

    plt.close()