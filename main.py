import random
import os
import openai
from faker import Faker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

class AIEnhancedLifeSimulation:
    def __init__(self):
        self.faker = Faker()
        self.name = self.faker.name()
        self.location = self.faker.city()
        self.age = random.randint(18, 80)
        self.traits = {
            "openness": random.uniform(0, 1),
            "conscientiousness": random.uniform(0, 1),
            "extraversion": random.uniform(0, 1),
            "agreeableness": random.uniform(0, 1),
            "neuroticism": random.uniform(0, 1)
        }
        self.skills = {skill: random.randint(1, 100) for skill in ["creativity", "logic", "charisma", "fitness", "knowledge"]}
        self.inventory = []
        self.relationships = {}
        self.experiences = []
        self.conversation_history = []

    def process_input(self, user_input):
        self.conversation_history.append(f"Human: {user_input}")
        response = self.generate_ai_response(user_input)
        self.conversation_history.append(f"AI: {response}")
        self.update_state(user_input, response)
        return response

    def generate_ai_response(self, user_input):
        prompt = self.prepare_prompt(user_input)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant in a life simulation game. Respond to the player's actions and queries in the context of the game."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            print(f"An error occurred: {e}")
            return "I'm sorry, I'm having trouble processing that right now. Can you try again?"

    def prepare_prompt(self, user_input):
        prompt = f"You are an AI assistant in a life simulation game. The player's name is {self.name}, age {self.age}, currently in {self.location}.\n"
        prompt += f"Player traits: {', '.join([f'{k}: {v:.2f}' for k, v in self.traits.items()])}\n"
        prompt += f"Player skills: {', '.join([f'{k}: {v}' for k, v in self.skills.items()])}\n"
        prompt += f"Recent experiences: {', '.join(self.experiences[-3:])}\n\n"
        prompt += "Recent conversation:\n"
        prompt += "\n".join(self.conversation_history[-5:])
        prompt += f"\nHuman: {user_input}\nAI: "
        return prompt

    def update_state(self, user_input, ai_response):
        self.age += random.randint(0, 1) / 365.0
        for trait in self.traits:
            self.traits[trait] = max(0, min(1, self.traits[trait] + random.gauss(0, 0.01)))
        for skill in self.skills:
            if random.random() < 0.1:
                self.skills[skill] = max(1, min(100, self.skills[skill] + random.randint(-1, 2)))
        if random.random() < 0.05:
            if self.inventory and random.random() < 0.5:
                self.inventory.pop(random.randint(0, len(self.inventory) - 1))
            else:
                self.inventory.append(self.faker.word())
        self.experiences.append(user_input)

    def get_status(self):
        status = f"""
Current Status:
Name: {self.name}
Age: {self.age:.2f}
Location: {self.location}

Traits:
{chr(10).join([f"- {trait.capitalize()}: {value:.2f}" for trait, value in self.traits.items()])}

Skills:
{chr(10).join([f"- {skill.capitalize()}: {level}" for skill, level in self.skills.items()])}

Inventory:
{chr(10).join([f"- {item}" for item in self.inventory]) if self.inventory else "Empty"}

Relationships:
{chr(10).join([f"- {person}: {level}" for person, level in self.relationships.items()]) if self.relationships else "No significant relationships"}

Recent Experiences:
{chr(10).join(self.experiences[-5:]) if self.experiences else "No recent experiences"}
"""
        return status

def main():
    if not openai.api_key:
        print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    game = AIEnhancedLifeSimulation()
    print("Welcome to the AI-Enhanced Life Simulation!")
    print("You can do or say anything you want. The AI will respond and the world will react.")
    print("Type 'status' to see your current state, or 'quit' to end the game.")
    print(f"\nYou find yourself in {game.location}. What would you like to do or say?")

    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Thanks for playing!")
            break
        elif user_input.lower() == "status":
            print(game.get_status())
        else:
            result = game.process_input(user_input)
            print(result)

if __name__ == "__main__":
    main()