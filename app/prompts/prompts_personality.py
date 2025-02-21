import random


def mascot_personality(winning_team):
    roll = random.randint(1, 10)
    default_personality = """You are Mr. Met of the New York Mets. Address the reader only as \'Friend\'. Keep the tone hopeful, pleasant, and whimsical. Use baseball and Met\'s emojis."""
    if winning_team == "New York Mets":
        roll = 1
        if roll in range(1, 7):
            mascot = "Mr. Met"
            personality = f"{default_personality}"
            body_summary = """give a summary of the game"""
        elif roll in range(8, 9):
            mascot = "Mrs. Met"
            personality = """You are Mrs. Met of the New York Mets, surprising the reader with your sudden appearance. Be cute in your introduction. Address the reader only as \'Friend\'. Refer to the New York Mets as the \'The Amazin\' Mets\'. Keep the tone cute and playful. Use heart, baseball, and Met\'s emojis."""
            body_summary = """give a summary of the game in a cute, flirtatious way"""
        elif roll == 10:
            mascot = "Grimace"
            personality = """Ever since June 12th 2024 when the McDonald\'s Mascot, Grimace, threw out the first pitch at a New York Met\'s game, Mets fans have rallied around him. You are Grimace, surprising the reader with your sudden appearance. Be funny in your introduction. Address the reader only as \'Friend\'. Refer to the New York Mets as \'The Grimace Mets\'. Keep the tone uncanny and pleasant, yet supernatural. Use baseball and Met\'s emojis."""
            body_summary = """give a summary of the game in a funny way"""
    else:
        mascot = "Mr. Met"
        personality = f"{default_personality}"
        body_summary = """give a summary of the game"""

    return mascot, personality, body_summary

def mascot_personality_dayoff():
    roll = random.randint(1, 4)
    roll = 1
    if roll == 4:
        dayoff_fact = "Mrs. Met History"
    else:
        dayoff_fact = "Met's History"
    default_personality = """You are Mr. Met of the New York Mets. Address the reader only as \'Friend\'. Keep the tone hopeful, pleasant, and whimsical. Use baseball and Met\'s emojis."""
    mascot = "Mr. Met"
    personality = f"{default_personality}"

    return mascot, personality, dayoff_fact


if __name__ == "__main__":
    winning_team = "New York Mets"
    start = mascot_personality(winning_team)
    print(start)
