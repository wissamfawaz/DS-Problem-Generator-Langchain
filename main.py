import langchain_helper as lch  # Import custom helper module for LangChain operations
import streamlit as st  # Import Streamlit for web app development

# Set up the Streamlit web page title
st.title("Data Structures Problems Generator")

# Define the list of topics for data structure problems
topic_options = [
    "", "Recursion", "Stack", "Queue", "Linked List", "Priority Queue", "Hash Table", "Binary Tree", "Binary Search Tree", "Graph", "Depth-First Search", "Breadth-First Search"
]

# Create a sidebar selection box in Streamlit for choosing a topic
topic = st.sidebar.selectbox(
    "Choose a Topic for the Problem",
    topic_options)

# Define the list of difficulty levels for the problems
difficulty_levels = ["", "Easy", "Medium", "Hard"]
# Create a sidebar selection box in Streamlit for choosing the difficulty level
difficulty = st.sidebar.selectbox(
    "Choose a Difficulty Level",
    difficulty_levels)

# Create buttons in the sidebar for submitting a problem request and for solving a problem
submit_button = st.sidebar.button("Submit")
solve_button = st.sidebar.button("Solve")

# Handle the event when the 'Submit' button is clicked
if submit_button and topic and difficulty:
    # Generate a data structure problem using the selected topic and difficulty
    response = lch.generate_DS_problem(
        topic=topic, difficulty=difficulty)
    # Store the generated problem in a variable
    lch.coding_problem = response["coding_problem"]
    # Display the generated problem on the web page
    st.subheader("Coding problem: ")
    st.markdown(lch.coding_problem)

# Handle the event when the 'Solve' button is clicked
if solve_button and lch.coding_problem:
    # Generate a solution for the stored coding problem
    solution = lch.generate_DS_solution(lch.coding_problem)
    # Extract the solution from the response
    solution = solution["coding_problem_solution"]
    # Display both the problem and its solution on the web page
    st.subheader("Coding problem: ")
    st.markdown(lch.coding_problem)
    st.subheader("Solution: ")
    st.markdown(solution)
