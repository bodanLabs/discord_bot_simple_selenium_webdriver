# Discord News Bot

## Description
This Discord bot is designed to fetch the latest news based on a keyword provided by the user. Utilizing Discord's Python API and Selenium for web scraping, it searches for news articles on Google News and returns the most recent articles to the Discord channel.

## Features
- Fetches latest news based on user-provided keywords.
- Uses Selenium for web scraping and Discord.py for bot interactions.
- Sends news articles as embedded messages in Discord.

## Requirements
- Python 3.6 or newer
- discord.py
- Selenium
- ChromeDriver (matching the version of the installed Chrome browser)

## Installation

1. Clone this repository or download the code.
2. Install the required Python packages using pip:
`pip install discord.py selenium`
3. Download ChromeDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it is in your PATH.

## Configuration

1. Replace `BOT_TOKEN` in the script with your Discord bot token.
2. (Optional) Adjust the command prefix and intents as needed.

## Usage

1. Run the bot:
`python bot.py`
2. In Discord, use the command `!news <keyword>` to fetch news related to the `<keyword>`.

## Note
- Ensure you have the necessary permissions set for your bot in the Discord developer portal.
- The bot requires the `messages`, `message_content`, and `embed links` permissions to function correctly.

## Contributing
Feel free to fork the repository and submit pull requests.

## Acknowledgements
- This bot uses the [discord.py](https://github.com/Rapptz/discord.py) library.
- Web scraping is done using [Selenium](https://selenium-python.readthedocs.io/).

