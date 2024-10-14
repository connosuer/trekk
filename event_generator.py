import random

class EventGenerator:
    @staticmethod
    def generate_event(player):
        events = [
            EventGenerator.health_event,
            EventGenerator.financial_event,
            EventGenerator.relationship_event,
            EventGenerator.skill_event,
            EventGenerator.discovery_event,
            EventGenerator.location_event
        ]
        return random.choice(events)(player)

    @staticmethod
    def health_event(player):
        if random.random() < 0.5:
            player.health = min(100, player.health + random.randint(1, 10))
            return "You've been feeling great lately and your health has improved!"
        else:
            player.health = max(0, player.health - random.randint(1, 10))
            return "You've caught a mild cold and your health has decreased slightly."

    @staticmethod
    def financial_event(player):
        amount = random.randint(10, 1000)
        if random.random() < 0.5:
            player.money += amount
            return f"You've unexpectedly received ${amount}!"
        else:
            player.money = max(0, player.money - amount)
            return f"You've had an unexpected expense of ${amount}."

    @staticmethod
    def relationship_event(player):
        person = random.choice(list(player.relationships.keys()) + [player.faker.name()])
        if random.random() < 0.5:
            player.relationships[person] = min(100, player.relationships.get(person, 0) + random.randint(1, 10))
            return f"Your relationship with {person} has improved!"
        else:
            player.relationships[person] = max(0, player.relationships.get(person, 0) - random.randint(1, 10))
            return f"You've had a minor disagreement with {person}."

    @staticmethod
    def skill_event(player):
        skill = random.choice(list(player.skills.keys()))
        improvement = random.randint(1, 5)
        player.skills[skill] = min(100, player.skills[skill] + improvement)
        return f"You've made progress in your {skill} skill! It has increased by {improvement} points."

    @staticmethod
    def discovery_event(player):
        discoveries = [
            "a hidden talent for painting",
            "a passion for cooking exotic cuisines",
            "an interest in learning a new language",
            "a knack for solving complex puzzles",
            "an aptitude for public speaking"
        ]
        discovery = random.choice(discoveries)
        return f"You've discovered {discovery}!"

    @staticmethod
    def location_event(player):
        return player.current_location.get_random_event()