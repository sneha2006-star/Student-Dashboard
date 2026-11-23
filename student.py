import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)

# Student Data
student_name = "Preeti"
sem1_cgpa = 8.6
sem2_cgpa = 8.1

# Calculate Overall CGPA
overall_cgpa = (sem1_cgpa + sem2_cgpa) / 2

# Custom CSS
st.markdown("""
<style>
.stApp {
    background-color: #f4f7fb;
}

[data-testid="stSidebar"] {
    background-color: #243b55;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

h1 {
    color: #1e293b;
}

h2, h3 {
    color: #243b55;
}

</style>
""", unsafe_allow_html=True)


# Sidebar Navigation
st.sidebar.title("Student Portal")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Academic Performance", "About Student"]
)

st.sidebar.markdown("---")
st.sidebar.write("Student:", student_name)
st.sidebar.write("Academic Year: 1st Year")


# =========================
# OVERVIEW PAGE
# =========================

if page == "Overview":

    st.title("Student Dashboard")
    st.subheader(f"Welcome, {student_name}!")

    st.write("Here is your academic performance overview.")

    # CGPA Cards
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "1st Semester CGPA",
        f"{sem1_cgpa:.1f}"
    )

    col2.metric(
        "2nd Semester CGPA",
        f"{sem2_cgpa:.1f}",
        "-0.5"
    )

    col3.metric(
        "1st Year Overall CGPA",
        f"{overall_cgpa:.2f}"
    )

    st.markdown("---")

    # Performance Chart
    st.subheader("Semester Performance")

    data = pd.DataFrame({
        "Semester": ["1st Semester", "2nd Semester"],
        "CGPA": [sem1_cgpa, sem2_cgpa]
    })

    st.bar_chart(
        data.set_index("Semester")
    )

    # Academic Summary
    st.subheader("Academic Summary")

    st.success(
        f"{student_name}'s overall 1st year CGPA is {overall_cgpa:.2f}."
    )

    st.info(
        "The CGPA changed from 8.6 in the first semester "
        "to 8.1 in the second semester."
    )


# =========================
# ACADEMIC PERFORMANCE
# =========================

elif page == "Academic Performance":

    st.title("Academic Performance")

    st.write("Semester-wise CGPA details")

    data = pd.DataFrame({
        "Semester": ["1st Semester", "2nd Semester"],
        "CGPA": [sem1_cgpa, sem2_cgpa]
    })

    st.dataframe(
        data,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("CGPA Comparison")

    st.bar_chart(
        data.set_index("Semester")
    )

    st.metric(
        "Overall 1st Year CGPA",
        f"{overall_cgpa:.2f}"
    )


# =========================
# ABOUT STUDENT
# =========================

elif page == "About Student":

    st.title("Student Information")

    st.write("### Student Details")

    st.write("**Name:** Preeti")
    st.write("**Academic Year:** 1st Year")
    st.write("**Semesters Completed:** 2")
    st.write(f"**1st Semester CGPA:** {sem1_cgpa}")
    st.write(f"**2nd Semester CGPA:** {sem2_cgpa}")
    st.write(f"**Overall CGPA:** {overall_cgpa:.2f}")

    st.info(
        "This dashboard displays Preeti's academic performance "
        "for the first year."
    )