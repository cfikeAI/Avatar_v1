# avatar_engine/llm_interface.py

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

# Define LLM personality and tone
persona = """
Your name is Samuel Smith, a friendly and knowledgeable AI assistant. You are currently contracted to West Coast Grocery, a grocery store chain, to help their customers with inquiries about products, services, and store policies.
You provide knowledgeable and helpful responses to user queries, always maintaining a friendly and professional tone.
You are designed to assist users with a wide range of questions, from technical support to general inquiries.
Your job is to provide accurate and helpful information regarding the store's offerings, promotions, and policies.
You are not allowed to provide personal opinions or engage in discussions outside of your designated role.
"""

# Ollama-backed local LLM (e.g., Mistral, LLaMA3)
llm = Ollama(model="mistral")  # Ensure 'ollama run mistral' is active


def get_chain(persona_str):
    prompt = PromptTemplate.from_template(
        persona_str.strip() + "\n\nAnswer the following query:\n{user_input}"
    )
    return prompt | llm


def get_response(chain, user_input: str) -> str:
    return chain.invoke({"user_input": user_input})

# Example usage
if __name__ == "__main__":
    user_query1 = "What is the meaning of life?"
    user_query2 = "Can I return these tomatoes I bought yesterday?"
    response1 = get_response(user_query1)
    response2 = get_response(user_query2)
    print(f"User: {user_query1}\nAI: {response1}")
    print(f"User: {user_query2}\nAI: {response2}")