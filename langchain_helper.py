# Import necessary modules from LangChain and other libraries
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

# Load environment variables, particularly the OpenAI API key
load_dotenv()

# Define a function to generate data structures problems
def generate_DS_problem(topic, difficulty):
    # Initialize the OpenAI model with a specified temperature setting
    # Temperature controls the randomness of the model's responses
    llm = OpenAI(temperature=0.7)

    # Define a prompt template with placeholders for topic and difficulty
    # This template guides the model to generate a problem based on the inputs
    prompt_template_name = PromptTemplate(
        input_variables=['topic', 'difficulty'],
        template="""
        You are a data structures instructor that can develop coding problems based on a user-supplied data structures topic and difficulty level for the problem.
        Generate a coding problem that is related to the {topic} topic. The problem should have {difficulty} difficulty level.
        Format the answer as follows. First, show the question prompt. Then go to a new line and display a first clarifying example before going to a new line and showing a second clarifying example.
        """
    )

    # Create a LangChain object (LLMChain) that uses the OpenAI model and the prompt template
    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="coding_problem")

    # Generate a response based on the provided topic and the difficulty
    response = name_chain({'topic': topic, 'difficulty': difficulty})

    # Return the generated coding problem
    return response

# Main execution block to test the function
if __name__ == "__main__":
    # Example usage of the function with "Recursion" as the topic and "Easy" as the difficulty
    print(generate_DS_problem("Recursion", "Easy")["coding_problem"])
