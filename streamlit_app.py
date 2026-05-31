
import streamlit as st
import pandas as pd
import plotly.express as px

from app.analysis import (
    load_data,
    calculate_total_average,
    pass_fail_analysis,
    add_grade_column
)

from app.ranking import student_ranking

from app.ml_model import (
    load_saved_model,
    custom_prediction
)

  

st.set_page_config(
    page_title="AI Student Analytics Platform",
    page_icon="🎓",
    layout="wide"
)

def kpi_card(title, value, color):
    st.markdown(f"""
    <div style="background:#111827;padding:20px;border-radius:18px;
    border-left:6px solid {color};">
    <p style="color:#94A3B8;">{title}</p>
    <h2 style="color:white;">{value}</h2>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg,#0B1120,#111827,#1E293B);
}
[data-testid="stSidebar"]{
    background:#0F172A;
}
#MainMenu, footer, header {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = load_data("StudentsPerformance.csv")

df = calculate_total_average(df)
df = pass_fail_analysis(df)
df = add_grade_column(df)
df = student_ranking(df)

pass_rate = (df["Status"] == "Pass").mean() * 100

st.markdown(f"""
<div style="background:linear-gradient(135deg,#1E293B,#0F172A);
padding:30px;border-radius:20px;">
<h1 style="color:white;">🎓 AI Student Analytics Platform</h1>
<p style="color:#94A3B8;">Academic Intelligence & Performance Monitoring</p>
<p style="color:white;">👨‍🎓 {len(df)} Students | ✅ {pass_rate:.1f}% Pass Rate | 🤖 AI Enabled</p>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("# 🎓 AI Analytics")
option = st.sidebar.radio(
    "Navigation",
    ["Dashboard","Dataset","Search Student","Top Students","Visualizations","ML Prediction"]
)

if option == "Dashboard":
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        kpi_card("Students", len(df), "#3B82F6")
    with col2:
        kpi_card("Pass Rate", f"{pass_rate:.1f}%", "#10B981")
    with col3:
        kpi_card("Average Score", f"{df['Average'].mean():.1f}", "#F59E0B")
    with col4:
        kpi_card("Top Score", f"{df['Average'].max():.1f}", "#EF4444")

    subject_avg = pd.DataFrame({
        "Subject":["Math","Reading","Writing"],
        "Average":[
            df["math score"].mean(),
            df["reading score"].mean(),
            df["writing score"].mean()
        ]
    })

    fig_subject = px.bar(subject_avg, x="Subject", y="Average",
                         title="Subject Performance")

    fig_grade = px.pie(df, names="Grade", title="Grade Distribution")

    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_subject, use_container_width=True)
    with col2:
        st.plotly_chart(fig_grade, use_container_width=True)

    top_student = df.iloc[0]
    st.info(
        f"🏆 Top Grade: {top_student['Grade']} | "
        f"📈 Average Score: {df['Average'].mean():.2f} | "
        f"✅ Pass Rate: {pass_rate:.2f}%"
    )

elif option == "Dataset":
    st.header("📁 Dataset")
    st.dataframe(df, use_container_width=True)

elif option == "Search Student":
    grade = st.selectbox("Grade", ["All"] + list(df["Grade"].unique()))
    status = st.selectbox("Status", ["All"] + list(df["Status"].unique()))
    filtered = df.copy()
    if grade != "All":
        filtered = filtered[filtered["Grade"] == grade]
    if status != "All":
        filtered = filtered[filtered["Status"] == status]
    st.dataframe(filtered, use_container_width=True)

elif option == "Top Students":
    st.subheader("🏆 Top Student Leaderboard")
    st.dataframe(
        df[["Rank","Grade","Average","Status"]].head(10),
        use_container_width=True
    )

elif option == "Visualizations":
    col1,col2 = st.columns(2)

    fig1 = px.pie(df, names="Grade", title="Grade Distribution")
    fig2 = px.pie(df, names="Status", title="Pass vs Fail")

    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.scatter(
        df,
        x="math score",
        y="writing score",
        color="Grade",
        title="Math vs Writing"
    )
    st.plotly_chart(fig3, use_container_width=True)

elif option == "ML Prediction":

    st.header("🤖 AI Prediction Engine")

    model = load_saved_model()

    math_mark = st.slider(
        "Math Score",
        0,
        100,
        50
    )

    reading_mark = st.slider(
        "Reading Score",
        0,
        100,
        50
    )

    if st.button("Predict Writing Score"):

        prediction = custom_prediction(
            model,
            math_mark,
            reading_mark
        )

        st.markdown(
            f"""
            <div style="
            background:linear-gradient(
            135deg,
            #1E293B,
            #0F172A
            );
            padding:30px;
            border-radius:20px;
            border-left:6px solid #06B6D4;
            ">

            <h2 style="color:white;">
            Predicted Writing Score
            </h2>

            <h1 style="
            color:#06B6D4;
            font-size:60px;
            ">
            {prediction:.1f}
            </h1>

            </div>
            """,
            unsafe_allow_html=True
        )