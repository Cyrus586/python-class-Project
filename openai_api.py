import openai
openai.api_key = "api key"
def generate_response(user_message):
    response = openai.Completion.create(
        engine = "chatgpt",
        prompt = user_message,
        temperature = 0.7,
        max_tokens = 50
    )
    return response.choices[0].text.strip()