import langchain_helper as lch  # Import the helper module for langchain operations
import streamlit as st  # Import the Streamlit library for web app development

# Set the title of the web application
st.title("Data Structures Problems Generator")

# Define a list of topic options for the coding problems
topic_options = [
    "", "Recursion", "Stack", "Queue", "Linked List", "Priority Queue", "Hash Table", 
    "Binary Tree", "Binary Search Tree", "Graph", "Depth-First Search", "Breadth-First Search"
]

# Create a sidebar selection box for choosing a topic
topic = st.sidebar.selectbox(
    "Choose a Topic for the Problem",
    topic_options)

# Define a list of difficulty levels for the coding problems
difficulty_levels = ["", "Easy", "Medium", "Hard"]

# Create a sidebar selection box for choosing a difficulty level
difficulty = st.sidebar.selectbox(
    "Choose a Difficulty Level",
    difficulty_levels)

# Create a submit button in the sidebar
submit_button = st.sidebar.button("Submit")

# Check if the submit button is clicked and both topic and difficulty are selected
if submit_button and topic and difficulty:
    # Call a function from the langchain_helper module to generate a coding problem
    response = lch.generate_DS_problem(topic=topic, difficulty=difficulty)
    
    # Extract the coding problem from the response
    coding_problem = response["coding_problem"]
    
    # Display the coding problem on the web application
    st.subheader("Coding problem: ")
    st.markdown(coding_problem)
