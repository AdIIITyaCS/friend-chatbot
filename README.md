File: 06_persona_bot.py

Description This script demonstrates the power of "System Instructions" (also known as System Prompts). Instead of just answering questions, the AI is given a detailed specific identity—in this case, "Anjali." The code shows how to define personality traits, relationship dynamics, hobbies, and specific behavioral rules (like using emojis or being possessive) that the AI must follow throughout the conversation.

Key Concept

System Instructions: We pass a strict set of rules to the model inside the config parameter. This tells the model "Who you are" and "How you should behave" before the user even says "Hello."

Behavioral Conditioning: You will notice the bot refuses to break character. It remembers it is a software engineer who loves badminton and will react with jealousy regarding other girls, exactly as programmed in the instructions.

Tone Adaptation: The instruction explicitly tells the model to speak in a "cute, sarcastic" way and use emojis, overriding the AI's default neutral tone.
