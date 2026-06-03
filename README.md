# Weather Forecast

My first self-initiated Python project — a web app built with Flask that fetches weather data from a weather API.

Experimenting with learning Python and Flask using Claude Code, mainly for learning and not generating code. See [CLAUDE.md](CLAUDE.md) for details.

> Work in progress.

## Ideas

### AI outfit advice with Claude API
Connect to Claude API to give clothing recommendations based on weather data.

**Flow:**
1. Fetch weather from Open-Meteo (already done in `routes.py`)
2. Send temperature + wind speed to Claude: *"It's 8 degrees and windy — what should I wear?"*
3. Display the response in `index.html`

**Requirements:**
- Anthropic API key from [anthropic.com](https://anthropic.com)
- `anthropic` package in `requirements.txt`
- API key in `.env` (never in code)
