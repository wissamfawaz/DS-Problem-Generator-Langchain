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
        As a data structures instructor with expertise in creating coding challenges, I need a problem tailored to a specific topic and difficulty level.
        Please generate a method design coding problem focused on the {topic} topic. It is essential that the problem is of {difficulty} difficulty level.
        Format your response as follows:
        1. Problem Statement: Clearly articulate the question prompt.
        2. First Clarifying Example: On a new line, provide an example that helps clarify the problem.
        3. Second Clarifying Example: Follow with another example on a new line for further clarification.
        4. Solution in Java: Present an optimal Java solution. The solution must be syntactically-valid, well-documented, complete, and formatted using Markdown syntax. Use triple backticks (```) to enclose the code, ensuring it is displayed in a readable and well-formatted manner. Ensure that all the necessary import statements are included in the solution.
        5. Complexity Analysis: Conclude with a detailed analysis of the time and space complexity of the provided solution, explaining how it achieves optimality.
        Ensure finally that the problem, examples, and solution are closely related to the specified topic and appropriate for the stated difficulty level.
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
