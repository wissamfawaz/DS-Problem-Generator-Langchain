from langchain.llms import OpenAI  # Import the OpenAI class for language model interactions
from langchain.prompts import PromptTemplate  # Import PromptTemplate for structured language model prompts
from langchain.chains import LLMChain  # Import LLMChain to create a chain of language model operations
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from a .env file

# Load environment variables, particularly the OpenAI API key
load_dotenv()
coding_problem = ""

def generate_DS_problem(topic, difficulty):
    # Initialize the OpenAI language model with a specific temperature setting
    llm = OpenAI(temperature=0.7)

    # Create a prompt template for generating data structure problems
    prompt_template_name = PromptTemplate(
        input_variables=['topic', 'difficulty'],
        template="""
        As a data structures instructor with expertise in creating coding challenges, I need a problem tailored to a specific topic and difficulty level.
        Please generate a method design coding problem focused on the {topic} topic. It is essential that the problem is of {difficulty} difficulty level.
        Organize your response as follows:
        - Problem Statement: Clearly articulate the question prompt.
        - Clarifying Example: On a new line, provide an example that helps clarify the problem.
        """
    )

    # Create a language model chain for generating the problem
    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="coding_problem")

    # Generate the problem using the provided topic and difficulty
    response = name_chain({'topic': topic, 'difficulty': difficulty})
    return response

def generate_DS_solution(problem):
    # Initialize the OpenAI language model with a specific temperature setting
    llm = OpenAI(temperature=0.7)

    # Create a prompt template for generating solutions to data structure problems
    prompt_template_name = PromptTemplate(
        input_variables=['problem'],
        template="""
        As a data structures instructor with expertise in solving coding challenges, I need you to solve the following problem:
        {problem}
        Organize your response as follows:
        - Solution in Java: Present an optimal Java solution. The solution must be syntactically-valid and formatted using Markdown syntax. Use triple backticks (```) to enclose the code, ensuring it is displayed in a readable and well-formatted manner. Ensure that all the necessary import statements are included in the solution. Don't include comments in the code.
        - Complexity Analysis: Conclude with an analysis of the time and space complexity of the provided solution.
        """
    )

    # Create a language model chain for generating the solution
    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="coding_problem_solution")

    # Generate the solution using the provided problem
    response = name_chain({'problem': coding_problem})
    return response

# Main execution block
if __name__ == "__main__":
    # Generate and print a data structure problem based on specified parameters
    print(generate_DS_problem("Recursion", "Easy")["coding_problem"])
