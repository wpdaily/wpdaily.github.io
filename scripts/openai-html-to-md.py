import glob
import os
import sys

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI configuration settings
openai.api_type = os.getenv("API_TYPE")
openai.api_base = os.getenv("API_BASE")
openai.api_version = os.getenv("API_VERSION")
openai.api_key = os.getenv("API_KEY")

# system prompt
with open('utilities/oai-system-prompt.txt') as f:
    system_prompt = f.read()

# user prompt mask
with open('utilities/oai-user-prompt-mask.txt') as f:
    user_prompt_mask = f.read()

# Get all html files from html_input directory
html_files = glob.glob('html_input/*.html')

if not html_files:
    print("No HTML files found in html_input directory.")
    sys.exit()

for html_file_path in html_files:
    with open(html_file_path) as f:
        text = f.read()
    text = user_prompt_mask + "\n" + text

    print(f"Full user prompt: \n{text}\n")

    # Send request to Azure OpenAI model
    print("Sending request to Azure OpenAI endpoint...\n\n")
    response = openai.ChatCompletion.create(
        engine="gpt3-16k",
        temperature=0.8,
        max_tokens=8000,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )

    print("Converted: \n" + response.choices[0].message.content + "\n")

    # Write to file
    filename = os.path.basename(html_file_path).replace(".html", "")
    with open("../md/" + filename + ".md", "w") as f:
        f.write(response.choices[0].message.content)

# Execute generate-md-index.py
os.system("python3 generate-md-index.py")
