# Eric Chien Line Bot

Welcome to my LINE bot repository! I've developed this bot to provide information about myself, including my work experience, education, skill set, personal portfolio, and competitions.

## Features

- **Starting Card**: An introduction card about me.
- **Work Experience**: A display of my professional journey.
- **Education**: Insights into my educational background.
- **Skill Set**: A list showcasing my skills.
- **Personal Portfolio**: A glimpse into my portfolio.
- **Competitions**: A section detailing the competitions I've participated in.
- **Magic 8-Ball Feature**: Ask any question, and my bot will respond with a random answer, reminiscent of the classic "Magic 8-Ball" toy. Responses range from "Don't count on it" to "As I see it, yes", and more.

## How My Bot Works

1. The bot starts by loading various JSON files containing the content for the flex messages.
2. When a POST request hits the `callback` endpoint, the bot verifies the request's signature.
3. It then parses the incoming events to check for message events.
4. Depending on the message content, the bot sends the appropriate flex message in response.
5. If the message doesn't match any predefined commands, the bot gives a random "Magic 8-Ball" response.

## Setup and Installation

1. Clone this repository.
2. Install the necessary packages with `pip install -r requirements.txt`.
3. Launch the Django application using `python manage.py runserver`.

## Contributions

If you have suggestions or improvements, please feel free to open pull requests or issues. I appreciate your input!
