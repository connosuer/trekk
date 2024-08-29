import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIInterface:
    @staticmethod
    def generate_response(prompt, max_tokens=150):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return "I'm sorry, I'm having trouble processing that right now. Can you try again?"

    @staticmethod
    def prepare_prompt(game_state, user_input, conversation_history):
        prompt = f"You are an AI assistant in a life simulation game. The player's name is {game_state['name']}, age {game_state['age']}, currently in {game_state['location']}.\n"
        prompt += f"Player traits: {', '.join([f'{k}: {v:.2f}' for k, v in game_state['traits'].items()])}\n"
        prompt += f"Player skills: {', '.join([f'{k}: {v}' for k, v in game_state['skills'].items()])}\n"
        prompt += f"Recent experiences: {', '.join(game_state['experiences'][-3:])}\n\n"
        prompt += "Recent conversation:\n"
        prompt += "\n".join(conversation_history[-5:])
        prompt += f"\nHuman: {user_input}\nAI: "
        return prompt
