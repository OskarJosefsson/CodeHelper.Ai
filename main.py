import os
from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    
    print(response.text)
    print('Prompt tokens: ' + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

if __name__ == "__main__":
    main()