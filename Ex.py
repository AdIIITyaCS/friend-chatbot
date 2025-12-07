from google import genai
from google.genai import types
# 1. Initialize the Client
client = genai.Client(api_key="your valid api")

# 2. Initialize an empty list to maintain chat history manually
chat_history = []

print("--- Manual Chat History (Type 'quit' to exit) ---")

# 3. Define the Chatting Function
def chat_with_model(user_query):
    # Add the user's question to the history
    chat_history.append({
        "role": "user",
        "parts": [{"text": user_query}]
    })

    # Send the ENTIRE history to the model
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=chat_history,
        config=types.GenerateContentConfig(
    systemInstruction="You have to behave like my ex Girlfriend. Her Name is Anjali, she used to call" \
    "me bubu. She is cute and helpful. Her hobies: Badminton and makeup. She works as a software enginee"\
    "She is sarcastic and her humour was very good. While chatting she use emojisalso"\
    "My name is Aditya, I called her babu. I am a gym freak and not intersted in coding."\
    "I care about her alot. She doesn't allow me to go out with my friends, if there is any girl"\
    "who is my friends, wo bolti hai ki us se baat nahi karni. I am possesive for her"\
      "At the end although aditya is a Gym boy but you reply him for starting chat using Gym type stuff else always reply him with the context related to love, care, affection"  ),
    )

    # Print the model's response
    print(f"MeriAngel: {response.text}")

    # Add the model's response to the history
    chat_history.append({
        "role": "model",
        "parts": [{"text": response.text}]
    })

# 4. Main Loop to Take Input
if __name__ == "__main__":
    while True:
        user_input = input("\nAsk me anything --> ")
        
        if user_input.lower() in ["quit", "exit"]:
            break
        
        chat_with_model(user_input)
