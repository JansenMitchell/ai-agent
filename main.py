import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import available_functions
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key is None:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")

parser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("user_prompt", type=str, help="Prompt for the AI agent")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=messages,
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt, temperature=0
    ),
)

if response.usage_metadata is not None:
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
    if response.function_calls:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    print(response.text)
else:
    raise RuntimeError("Usage metadata is missing")
