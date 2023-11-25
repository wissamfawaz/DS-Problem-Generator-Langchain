import langchain_helper as lch
import streamlit as st
import textwrap

st.title("Data Structures Problems Generator")

topic = st.sidebar.selectbox(
    "Choose a topic for the problem...",
    ("Recursion", "Stacks", "Queues"))

difficulty = st.sidebar.selectbox(
    "Choose a difficulty level for the problem...",
    ("Easy", "Medium", "Hard"))

if topic and difficulty:
    response = lch.generate_DS_problem(
        topic=topic, difficulty=difficulty)
    st.subheader("Coding problem: ")
    coding_problem = response["coding_problem"]
    st.markdown(coding_problem)
