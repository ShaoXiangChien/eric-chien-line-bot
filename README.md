# 🤖 Eric Chien's LINE Bot

Hello and welcome! This is the official repository for my LINE bot, designed to give you a quick overview of who I am, from my professional journey to personal projects.

## 📌 Features

- **Starting Card**: A brief introduction to me.
- **Work Experience**: A timeline of my professional experiences.
- **Education**: A look into my academic background.
- **Skill Set**: An overview of my technical and soft skills.
- **Personal Portfolio**: Dive into projects and initiatives I'm proud of.
- **Competitions**: Highlights from competitions I've taken part in.
- **Magic 8-Ball Feature**: For a bit of fun, ask a question and get a random answer, inspired by the classic "Magic 8-Ball" toy.

## 🔧 How It Works

1. The bot initializes by reading content from various JSON files for the flex messages.
2. On receiving a POST request at the `callback` endpoint, the bot verifies the request's signature.
3. It then processes incoming events, specifically looking for message events.
4. Depending on the message content, it sends back the relevant flex message.
5. If the message isn't recognized, it defaults to a playful "Magic 8-Ball" response.

## 🚀 Getting Started

1. Clone this repository to your local machine.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Start the Django server with `python manage.py runserver`.

## 🤝 Contribute

Your feedback and contributions are valuable! If you have ideas or suggestions, please open pull requests or issues. Let's make this bot even better together!
