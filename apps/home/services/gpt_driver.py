import os
import openai
import json
from dotenv import load_dotenv
from .proposal_template_details import template

# Load environment variables from .env
load_dotenv()

# Set your OpenAI GPT-3.5 Turbo API key
openai.api_key = os.getenv("OPENAI_API_KEY")

start_prompt = "I want to write a project proposal for Grameenphone. The project is about GPS tracking software. "


def ask_gpt3(current_prompt):
    response = openai.completions.create(
        model="text-davinci-003",
        prompt=current_prompt,
        max_tokens=500,
        n=1
    )
    return response.choices[0].text.strip()

def generate_prompt(default_prompt, word_limit):
    return start_prompt + default_prompt + " within "+ word_limit +" words"

def gpt_driver():
    generated_text = []

    for item in template:
        current_prompt = generate_prompt(default_prompt=item["default_prompt"], word_limit=str(item["word_limit"]))
        # print(current_prompt)
        query_response = ask_gpt3(current_prompt)
        generated_text.append(query_response)
        #print(current_prompt)
        # print("______________________ SECTION ____________________")
        # print(query_response)
        # print("_____________________________________________________")
    return generated_text
        





