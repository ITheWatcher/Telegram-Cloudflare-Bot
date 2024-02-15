# Telegram Cloudflare Detector Bot

A Telegram bot that detects whether a given website is using Cloudflare services.

## Overview

This Python script utilizes the Telebot library to create a Telegram bot capable of detecting whether a specified website is using Cloudflare services. Users can interact with the bot by providing a website URL, and the bot responds with whether Cloudflare is used on the website or not.

## Features

- Detects Cloudflare usage on a website.
- Simple and intuitive Telegram interface.
- Inline keyboard for user interaction.
- Error handling for invalid inputs and website connection issues.

## Installation

1. Clone or download the repository to your local machine.
   ```
    git clone https://github.com/ITheWatcher/Telegram-Cloudflare-Bot.git
    ```
3. Install the required dependencies using pip:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the script `cloudflare_bot.py`.
2. Start a conversation with the bot in your Telegram app.
3. Use the `/cloudflare` command to initiate the Cloudflare detection process.
4. Choose 'Yes' to proceed or 'No' to exit the conversation.
5. If 'Yes' is selected, enter the website URL when prompted.
6. The bot will respond with whether Cloudflare is detected on the specified website.

## Configuration

- Replace `'YOUR_BOT_TOKEN'` in the script with your Telegram bot token.

## Contributions

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
