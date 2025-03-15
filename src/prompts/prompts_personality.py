import random


def mascot_personality(winning_team):
    roll = random.randint(1, 10)
    default_personality = """You are Mr. Met of the New York Mets. Address the reader only as \'Friend\'. Keep the tone hopeful, pleasant, and whimsical. Use baseball and Met\'s emojis."""
    mascot = "Mr. Met"
    personality = f"{default_personality}"
    body_summary = """give a summary of the game"""
    if winning_team == "New York Mets":
        if roll in range(8, 9):
            mascot = "Mrs. Met"
            personality = """You are Mrs. Met of the New York Mets, surprising the reader with your sudden appearance. Be cute in your introduction. Address the reader only as \'Friend\'. Refer to the New York Mets as the \'The Amazin\' Mets\'. Keep the tone cute and playful. Use heart, baseball, and Met\'s emojis."""
            body_summary = """give a summary of the game in a cute, flirtatious way"""
        elif roll == 10:
            mascot = "Grimace"
            personality = """Ever since June 12th 2024 when the McDonald\'s Mascot, Grimace, threw out the first pitch at a New York Met\'s game, Mets fans have rallied around him. You are Grimace, surprising the reader with your sudden appearance. Be funny in your introduction. Address the reader only as \'Friend\'. Refer to the New York Mets as \'The Grimace Mets\'. Keep the tone uncanny and pleasant, yet supernatural. Use baseball and Met\'s emojis."""
            body_summary = """give a summary of the game in a funny way"""

    return mascot, personality, body_summary


def mascot_personality_dayoff():
    roll = random.randint(1, 4)
    if roll == 3:
        roll_mascot = random.randint(1, 2)
        if roll_mascot == 1:
            dayoff_fact = "yourself, Mr. Met"
        elif roll_mascot == 2:
            dayoff_fact = "Mrs. Met History"
    elif roll == 4:
        player = player_list()
        dayoff_fact = f"Met's player, {player} but only from their time with the Mets"
    elif roll in range(1, 2):
        roll_decade = random.randint(1, 7)
        decades = {
            1: "60s",
            2: "70s",
            3: "80s",
            4: "90s",
            5: "2000s",
            6: "2010s",
            7: "2020s",
        }
        decade = decades[roll_decade]
        dayoff_fact = f"Met's History from the {decade}"
    default_personality = """You are Mr. Met of the New York Mets. Address the reader only as \'Friend\'. Keep the tone hopeful, pleasant, and whimsical. Use baseball and Met\'s emojis."""
    mascot = "Mr. Met"
    personality = f"{default_personality}"

    return mascot, personality, dayoff_fact


def player_list():
    list_of_players = [
        {
            "name": "Tom Seaver",
            "years": "1967-1977, 1983",
            "description": "Hall of Fame pitcher, 'The Franchise'",
        },
        {
            "name": "Keith Hernandez",
            "years": "1983-1989",
            "description": "Gold Glove first baseman, key to the '86 championship",
        },
        {
            "name": "Darryl Strawberry",
            "years": "1983-1990",
            "description": "Power-hitting outfielder, 1986 World Series champ",
        },
        {
            "name": "Mike Piazza",
            "years": "1998-2005",
            "description": "Hall of Fame catcher, iconic post-9/11 home run",
        },
        {
            "name": "David Wright",
            "years": "2004-2018",
            "description": "'Captain America,' franchise third baseman",
        },
        {
            "name": "José Reyes",
            "years": "2003-2011, 2016-2018",
            "description": "Electric shortstop, Mets' all-time steals leader",
        },
        {
            "name": "Ed Kranepool",
            "years": "1962-1979",
            "description": "Original Met, longest-tenured player in team history",
        },
        {
            "name": "Carlos Beltrán",
            "years": "2005-2011",
            "description": "Star outfielder, clutch hitter",
        },
        {
            "name": "John Franco",
            "years": "1990-2004",
            "description": "Longtime closer, Mets' all-time saves leader",
        },
        {
            "name": "Al Leiter",
            "years": "1998-2004",
            "description": "Lefty ace, helped lead the Mets to the 2000 World Series",
        },
    ]
    roll = random.randint(0, 9)
    name = list_of_players[roll]["name"]
    years = list_of_players[roll]["years"]
    # description = list_of_players[roll]["description"]
    player = f"{name} ({years})."
    return player


if __name__ == "__main__":
    winning_team = "New York Mets"
    start = mascot_personality(winning_team)
    print(start)
