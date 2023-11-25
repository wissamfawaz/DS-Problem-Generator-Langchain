# DS-Problem-Generator-Langchain

## Overview
The DS-Problem-Generator-Langchain is an innovative application designed to support students in their data structures studies, particularly in preparation for exams. By allowing users to select a topic within data structures and specify a difficulty level, the application dynamically generates a coding problem tailored to these preferences. This is made possible through the integration with Large Language Models (LLMs), which power the application's ability to present relevant and challenging questions.

## Key Features
- **Customization**: Users can choose from a variety of data structures topics and set the difficulty level (Easy, Medium, Hard) for the coding problem.
- **Powered by LLMs**: Utilizes advanced language models to generate unique and pertinent coding problems.
- **User-Friendly Interface**: Simple and intuitive interface for seamless user experience.

## Getting Started

### Prerequisites
Before running the application, ensure you have Python installed on your system. If not, download and install it from [Python's official website](https://www.python.org/downloads/).

### Installation
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/DS-Problem-Generator-Langchain.git
   ```
2. Navigate to the cloned directory:
   ```
   cd DS-Problem-Generator-Langchain
   ```
3. Install the required libraries:
   ```
   pip install langchain openai streamlit python-dotenv
   ```

### Running the Application
1. Before running the application, you need to set up an OpenAI API key. Follow the instructions [here](https://platform.openai.com/api-keys) to obtain your key.
2. Store your API key in a `.env` file within the application directory:
   ```
   OPENAI_API_KEY="your-api-key"
   ```
3. Launch the application:
   ```
   streamlit run main.py
   ```

## Usage
Once the application is running:
- Use the sidebar to select a data structures topic and a difficulty level.
- The application will generate and display a coding problem based on your selections.

## Contributing
Contributions to this Data Structures problems generator are welcome! 
