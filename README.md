# Mr. Mascot 🎭⚾

A personalized AI baseball companion that delivers daily email updates about the New York Mets. Mr. Mascot combines real-time MLB data with an engaging AI personality to create informative and entertaining updates about games, series progress, and team facts.

## 🌟 Features

- **Smart Game Recaps**: 
  - Detailed game summaries with scores and key moments
  - Play-by-play highlights from yesterday's game
  - Venue and series progress information
  - AI-crafted commentary that celebrates wins and stays hopeful after losses

- **Series Intelligence**: 
  - Tracks multi-game series progress
  - Provides context about series length and game numbers
  - Updates on upcoming matchups and opponents

- **Special Off-Day Content**:
  - Engaging team facts during non-game days
  - Special coverage during All-Star break
  - Monday updates include division standings
  - Maintains fan engagement even without games

- **Personality-Driven Communication**:
  - Dynamic AI personality that adapts to game outcomes
  - Concise 35-character email subjects
  - Friendly, conversational tone
  - Word-limited responses for optimal readability

## 📋 Prerequisites

- Python 3.x
- OpenAI API key
- SendGrid API key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mr_mascot.git
cd mr_mascot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables:
Create a `.env` file with:
```
OPENAI_API_KEY="your-openai-api-key"
SENDGRID_API_KEY="your-sendgrid-api-key"
```

4. Configure email recipients:
Create a `.users.json` file based on `.users.example.json`:
```json
[
    {
        "id": 1,
        "name": "Friend",
        "email": "friend@example.com"
    }
]
```

## ⚙️ Usage

Run the application:
```bash
python main.py
```

## 📝 License

This project is licensed under the terms included in the LICENSE file.