# Mr. Mascot

A Python-based project for managing and interacting with mascot-related functionalities.

## 🚀 Features

- OpenAI integration for mascot interactions
- Game information management
- Scheduling system
- Statistics tracking
- Utility functions for data processing

## 📋 Prerequisites

- Python 3.x
- Virtual environment (recommended)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/mr_mascot.git
cd mr_mascot
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .env_mr_mascot
source .env_mr_mascot/bin/activate  # On Unix/macOS
# or
.env_mr_mascot\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with required configuration (see `.env.example` for reference)

## 🏗️ Project Structure

```
mr_mascot/
├── app/                    # Main application code
│   ├── prompts/           # Prompt templates
│   ├── game_info.py       # Game information handling
│   ├── open_ai.py         # OpenAI integration
│   ├── utils.py           # Utility functions
│   ├── z_schedule.py      # Scheduling functionality
│   └── z_stats.py         # Statistics tracking
├── tests/                 # Test suite
├── main.py               # Application entry point
└── requirements.txt      # Project dependencies
```

## 🚀 Usage

Run the main application:
```bash
python main.py
```

## 📝 License

This project is licensed under the terms included in the LICENSE file.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!