import os

from app.analysis import (
    load_data,
    dataset_summary,
    calculate_total_average,
    pass_fail_analysis,
    add_grade_column
)

from app.ranking import (
    student_ranking
)

from app.visualization import (
    math_vs_writing,
    reading_vs_writing,
    grade_distribution,
    pass_fail_chart,
    subject_comparison,
    ranking_chart,
    actual_vs_predicted
)

from app.ml_model import (
    train_model,
    custom_prediction
)


# CREATE CHARTS FOLDER
if not os.path.exists("charts"):
    os.makedirs("charts")


# LOAD DATASET
df = load_data(
    "StudentsPerformance.csv"
)


# DATASET ANALYSIS
dataset_summary(df)


# ADD ANALYSIS COLUMNS
df = calculate_total_average(df)

df = pass_fail_analysis(df)

df = add_grade_column(df)

df = student_ranking(df)


# VISUALIZATIONS
math_vs_writing(df)

reading_vs_writing(df)

grade_distribution(df)

pass_fail_chart(df)

subject_comparison(df)

ranking_chart(df)


# MACHINE LEARNING
(
    model,
    predictions,
    y_test,
    mae,
    r2
) = train_model(df)


# ML VISUALIZATION
actual_vs_predicted(
    y_test,
    predictions
)


# RESULTS
print("\nMEAN ABSOLUTE ERROR:")
print(round(mae, 2))

print("\nR2 SCORE:")
print(round(r2, 2))


# MODEL CONCEPT
print("\nMODEL FORMULA:")

print(
    "y = b0 + b1*x1 + b2*x2"
)

print("\nWhere:")

print("x1 = Math Score")
print("x2 = Reading Score")
print("y = Writing Score")


# CUSTOM PREDICTION
math_mark = float(
    input("\nEnter Math Score: ")
)

reading_mark = float(
    input("Enter Reading Score: ")
)

predicted_score = custom_prediction(
    model,
    math_mark,
    reading_mark
)

print(
    f"\nPredicted Writing Score: "
    f"{predicted_score:.2f}"
)


# TOP STUDENTS
print(
    "\nTOP 10 STUDENTS:\n"
)

print(df.head(10))


# AVERAGES
print("\nAVERAGE SCORES:\n")

print(
    "Math Average:",
    round(
        df["math score"].mean(),
        2
    )
)

print(
    "Reading Average:",
    round(
        df["reading score"].mean(),
        2
    )
)

print(
    "Writing Average:",
    round(
        df["writing score"].mean(),
        2
    )
)


print(
    "\nPROJECT COMPLETED "
    "SUCCESSFULLY 🚀"
)