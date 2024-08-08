import spacy
import random
from locations import LocationManager


class LifeSimulation:
    def __init__(self):
        self.name = "Player"
        self.location_manager = LocationManager()
        self.location = self.location_manager.get_random_location_name()
        self.age = 18
        self.job = None
        self.money = 1000
        self.health = 100
        self.happiness = 70
        self.education = "High School"
        self.relationships = {}
        self.skills = {"communication": 5, "technology": 5, "fitness": 5}
        self.nlp = spacy.load("en_core_web_sm")
        self.action_handlers = {
            "move": self.handle_movement,
            "go": self.handle_movement,
            "walk": self.handle_movement,
            "work": self.handle_work,
            "apply": self.handle_job_application,
            "get": self.handle_job_application,
            "learn": self.handle_learning,
            "study": self.handle_learning,
            "interact": self.handle_interaction,
            "talk": self.handle_interaction,
            "kiss": self.handle_romantic_action,
            "hug": self.handle_romantic_action,
            "jump": self.handle_physical_action,
            "run": self.handle_physical_action,
        }



    def process_input(self, user_input):
        doc = self.nlp(user_input.lower())
        
        if user_input.lower() == "status":
            return self.get_status()
        elif user_input.lower() == "help":
            return self.get_help()

        main_verb = None
        objects = []
        for token in doc:
            if token.pos_ == "VERB" and not main_verb:
                main_verb = token.lemma_
            if token.dep_ in ["dobj", "pobj", "attr", "compound"]:
                objects.append(token.text)

        if main_verb in self.action_handlers:
            return self.action_handlers[main_verb](objects)
        else:
            return self.handle_unknown_action(main_verb, objects)

    def handle_movement(self, objects):
        if objects:
            destination = " ".join(objects)
            return self.location_manager.move_to(self, destination)
        return "You wander around aimlessly."

    def handle_work(self, objects):
        if self.job:
            self.money += 100
            self.skills["work"] = min(100, self.skills.get("work", 0) + 1)
            return f"You work at your job as a {self.job}. You earn $100 and improve your work skills."
        return "You don't have a job. Maybe you should apply for one?"

    def handle_job_application(self, objects):
        if "job" in objects:
            objects.remove("job")
        if objects:
            job = " ".join(objects)
            chance = random.random()
            if chance > 0.7:
                self.job = job
                return f"Congratulations! You've been hired as a {job}."
            else:
                return f"Unfortunately, your application for {job} was not successful this time."
        return "What kind of job would you like to apply for?"

    def handle_learning(self, objects):
        if objects:
            skill = " ".join(objects)
            self.skills[skill] = min(100, self.skills.get(skill, 0) + 5)
            return f"You spend some time learning about {skill}. Your skill has improved!"
        return "What would you like to learn?"

    def handle_interaction(self, objects):
        if objects:
            person = " ".join(objects)
            self.relationships[person] = min(100, self.relationships.get(person, 0) + 5)
            return f"You interact with {person}. Your relationship has improved!"
        return "Who would you like to interact with?"

    def handle_romantic_action(self, objects):
        if objects:
            person = " ".join(objects)
            if person in self.relationships and self.relationships[person] > 50:
                self.relationships[person] = min(100, self.relationships[person] + 10)
                return f"You share a romantic moment with {person}. Your relationship has significantly improved!"
            else:
                return f"You try to get romantic with {person}, but they don't seem interested. Maybe you need to build a better relationship first."
        return "Who would you like to be romantic with?"

    def handle_physical_action(self, objects):
        action = "do physical activity"
        if objects:
            action = " ".join(objects)
        self.health = min(100, self.health + 5)
        self.happiness = min(100, self.happiness + 5)
        return f"You {action}. You feel healthier and happier!"

    def handle_unknown_action(self, verb, objects):
        if verb:
            return f"You try to {verb} {' '.join(objects)}. It's an interesting experience, but you're not sure what effect it had."
        return "I'm not sure what you're trying to do. Can you be more specific?"

    def get_status(self):
        location_info = self.location_manager.get_or_create_location(self.location)
        status = f"""
Current Status:
Name: {self.name}
Age: {self.age}
Location: {self.location}, {location_info.country}
Job: {self.job if self.job else 'Unemployed'}
Money: ${self.money}
Health: {self.health}%
Happiness: {self.happiness}%
Education: {self.education}

Skills:
{self.format_skills()}

Relationships:
{self.format_relationships()}

Current Location: {self.location}
Location Description: {location_info.description}
Available Jobs: {', '.join(location_info.available_jobs)}
"""
        return status

    def format_skills(self):
        return "\n".join([f"- {skill.capitalize()}: {level}" for skill, level in self.skills.items()])

    def format_relationships(self):
        if not self.relationships:
            return "No significant relationships"
        return "\n".join([f"- {person}: {status}" for person, status in self.relationships.items()])

    def get_help(self):
        return """
Available commands:
- status: Check your current life status
- move [location]: Move to a new location
- work: Go to work (if employed)
- apply [job]: Apply for a job
- learn [skill]: Learn or improve a skill
- interact [person]: Interact with someone
- help: Show this help message
You can also try other actions, and the game will respond accordingly!
"""

def main():
    game = LifeSimulation()
    start_location = game.location_manager.get_or_create_location(game.location)
    print(f"Welcome to Life Simulation!")
    print(f"You wake up one day in {game.location}, {start_location.country}. {start_location.description}")
    print("What would you like to do? Type 'help' for some ideas.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "quit":
            print("Thanks for playing!")
            break
        result = game.process_input(user_input)
        print(result)

if __name__ == "__main__":
    main()