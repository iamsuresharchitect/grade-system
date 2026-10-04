"""Student Grade Manager.

Run with:  streamlit run grade_app.py
"""

import streamlit as st

# Grading scale: (minimum mark, grade), checked from the top down.
# Swap these values to match a different scale.
GRADE_SCALE = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]

MIN_MARK = 0
MAX_MARK = 100


def get_grade(mark):
    """Return the letter grade for a mark using GRADE_SCALE."""
    for minimum, grade in GRADE_SCALE:
        if mark >= minimum:
            return grade
    return GRADE_SCALE[-1][1]


def validate(name, mark):
    """Return an error message, or None if the input is valid."""
    if not name.strip():
        return "Please enter a student name."
    if mark is None:
        return "Please enter a mark."
    if mark < MIN_MARK or mark > MAX_MARK:
        return f"Mark must be between {MIN_MARK} and {MAX_MARK}."
    return None


st.set_page_config(page_title="Student Grade Manager", page_icon="🎓")
st.title("🎓 Student Grade Manager")

# The student list lives in session_state so it survives reruns.
if "students" not in st.session_state:
    st.session_state.students = []

with st.form("add_student", clear_on_submit=True):
    st.subheader("Add a student")
    name = st.text_input("Name")
    # No min/max on the widget so out-of-range marks reach validate()
    # and get a clear error instead of being silently clamped.
    mark = st.number_input("Mark (0-100)", value=None, step=1.0, format="%.1f")
    submitted = st.form_submit_button("Add student")

if submitted:
    error = validate(name, mark)
    if error:
        st.error(error)
    else:
        st.session_state.students.append({"name": name.strip(), "mark": float(mark)})
        st.success(f"Added {name.strip()} ({get_grade(mark)}).")

students = st.session_state.students

st.subheader("Class summary")
if students:
    marks = [s["mark"] for s in students]
    col1, col2, col3 = st.columns(3)
    col1.metric("Class average", f"{sum(marks) / len(marks):.1f}")
    col2.metric("Highest", f"{max(marks):g}")
    col3.metric("Lowest", f"{min(marks):g}")

    st.subheader("Students")
    st.dataframe(
        [
            {"Name": s["name"], "Mark": s["mark"], "Grade": get_grade(s["mark"])}
            for s in students
        ],
        hide_index=True,
    )

    if st.button("Clear all students"):
        st.session_state.students = []
        st.rerun()
else:
    st.info("No students yet. Add one using the form above.")

with st.expander("Grading scale"):
    st.table([{"Grade": g, "Minimum mark": m} for m, g in GRADE_SCALE])
