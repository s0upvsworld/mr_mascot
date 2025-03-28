# Mr. Mascot ⚾

A personalized AI baseball companion that delivers daily email updates about your favorite MLB team. Mr. Mascot combines real-time MLB data with an AI personality to create informative and entertaining updates about games, series progress, and team facts.

## 🌟 Features

- **Smart Game Recaps**: 
  - Detailed game summaries with scores and key moments
  - Key game highlight from yesterday's game
  - Ballpark information
  - AI-crafted commentary that celebrates wins and stays hopeful after losses

- **Series Intelligence**: 
  - Tracks multi-game series progress
  - Provides context about series length
  - Updates on upcoming matchups and opponents

- **Special Off-Day Content**:
  - Engaging team facts during non-game days
  - Special coverage during All-Star break
  - Monday updates include division standings

- **Personality-Driven Communication**:
  - Dynamic AI personality that adapts to game outcomes
  - Concise emails for readability
  - Friendly, conversational tone

- **User Signup via Flask Server**:
  - Run the Flask server to sign up users 

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
Create a `.users.json` file based on `.users_example.json`:
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

Run the Flask server:
```bash
flask run
```

## 📝 License

This project is licensed under the terms included in the LICENSE file.