# Weather Forecast

My first self-initiated Python project, a web app built with Flask that fetches weather data from a weather API.

It connects to the Claude API to give clothing recommendations based on weather data. 

Experimenting with learning Python and Flask using Claude Code, mainly for learning and not generating code. 

Will probably add more features in the future. Just exploring right now. 

> Work in progress.

## Tech stack

- Python 3.13
- Flask 3.1
- Jinja2 templates
- requests
- python-dotenv
- [Open-Meteo](https://open-meteo.com/) — free weather API, no API key required
- [Claude API](https://docs.anthropic.com/) — outfit suggestions, requires an API key

## Getting started

Clone the repo and enter the folder:

```bash
git clone <repo-url>
cd weather-forecast
```

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows (PowerShell)
source venv/bin/activate     # macOS / Linux
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the app

```bash
python run.py
```

The app runs in debug mode at http://127.0.0.1:5000

## Configuration

Copy the template and fill in your key:

```bash
cp .env.example .env
```

| Variable | Required | Used for |
| --- | --- | --- |
| `ANTHROPIC_API_KEY` | Yes, for outfit suggestions | Calls the Claude API in `app/weather.py` |

Open-Meteo needs no key, so the weather itself works without any configuration.

`.env` is listed in `.gitignore`, so real keys never end up in the repo. `.env.example` holds placeholders only and is committed.

## Project structure

```
weather-forecast/
├── app/
│   ├── __init__.py       # creates the Flask app, loads .env
│   ├── routes.py         # routes and form handling
│   ├── weather.py        # Open-Meteo and Claude API calls
│   ├── static/           # stylesheet and SVG art
│   └── templates/
│       └── index.html    # renders the weather data
├── run.py                # entry point
├── .env.example          # template for .env
└── requirements.txt
```
