from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()


def generate_DS_problem(topic, difficulty):
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=['topic', 'difficulty'],
        template="""
        You are a data structures instructor that can develop coding problems based on a user-supplied data structures topic and difficulty level for the problem.
        Generate a coding problem that is related to the {topic} topic. The problem should have {difficulty} difficulty level.
        Format the answer as follows. First, show the question prompt. Then go to a new line and display a first clarifying example before going to a new line and showing a second clarifying example.
        """
    )
    name_chain = LLMChain(
        llm=llm, prompt=prompt_template_name, output_key="coding_problem")
    response = name_chain({'topic': topic, 'difficulty': difficulty})
    return response


if __name__ == "__main__":
    print(generate_DS_problem("Recursion", "Easy")["coding_problem"])
