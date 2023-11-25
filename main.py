import langchain_helper as lch  # This imports the custom module for generating data structures problems.
import streamlit as st          # Streamlit library for creating the web app interface.

st.title("Data Structures Problems Generator")  # Sets the title of the web app.

# Creating a sidebar for user input
# Sidebar for selecting a topic
topic = st.sidebar.selectbox(
    "Choose a topic for the problem...",  # Text prompt for the select box.
    ("Recursion", "Stacks", "Queues"))    # Options for the user to choose from.

# Sidebar for selecting difficulty level
difficulty = st.sidebar.selectbox(
    "Choose a difficulty level for the problem...",  # Text prompt for the select box.
    ("Easy", "Medium", "Hard"))                      # Options for the user to choose from.

# Generating and displaying the problem
if topic and difficulty:  # Checks if both topic and difficulty have been selected.
    # Calls the generate_DS_problem function from the langchain_helper module
    # with the selected topic and difficulty.
    response = lch.generate_DS_problem(
        topic=topic, difficulty=difficulty)

    st.subheader("Coding problem: ")  # Adds a subheader to the web app.

    # Extracts the coding problem from the response.
    coding_problem = response["coding_problem"]

    # Displays the coding problem on the web app.
    st.markdown(coding_problem)
