from def_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()

def testing_with_ai(function: str):
    prompt = f"""

    Below is given a python based funtion.
    {function} \n

    your job is to study this function and build a different set of use cases for testing. Test it thoroughly.

    The response should be in json format as given:
    {{
    "status": "success or failed",
    "message": "if failed where it failed with details and if success just mention a summary message",
    "optimized_function": "if there are failed and invalid cases rewtire the function here"
    }}

    """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text
