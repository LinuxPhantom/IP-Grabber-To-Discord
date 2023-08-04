# IP Grabber To Discord

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Discord](https://img.shields.io/discord/1234567890.svg?color=blueviolet&label=Discord&logo=discord)](https://discord.com/invite/2nvdyy9e9j)

## Description

Linux Phantom IP Grabber is a Python script that allows you to retrieve the public IP address of a user and send it to a specified Discord webhook. This tool can be useful for various purposes, including network troubleshooting, remote monitoring, or just for fun!

> **Note**: Included in this repository is an executable file (Main.exe)(Can Rename!) that, when executed, will send the victim's information to our Discord server. You must join our [Discord server](https://discord.io/HackMe) to see the information. Alternatively, you can set up your own server by modifying the `config.json` file.

## Features

- Retrieves public IP address
- Sends IP address to Discord webhook
- Lightweight and easy to use

## Screenshots

![Webhook Setup](/screenshots/webhookdisplay.gif)
- Creating a WebHook in Discord is simple as going to the channel you wish, hit the settings wheel, go to intergrations, and Webhooks

![Generated Files](/screenshots/GeneratedFiles.jpg)
- Information Generated from this

![Changing Webhook & API](/screenshots/ChangingWebhookAPI.jpg)
- Changing the Webhook and API are as simple as going to the Config.json and editing to yours. You must also edit the API Key in the Main.py file. I had created a tag to look for when making the edit "#Your API Key WILL GO HERE AFTER key="

# Installation

### Clone the repository:
git clone https://github.com/YourUsername/Linux-Phantom-IP-Grabber.git

### Install the required Python packages:
pip install -r requirements.txt

# Usage

### Navigate to the project folder:
cd Linux-Phantom-IP-Grabber

### Edit the config.json file:
- Replace the webhook_url with your Discord webhook URL.
- Get a free API key from http://extreme-ip-lookup.com and replace the api_key in the file.
- Note: Modifying the config.json file is essential for sending data to your own server. (Otherwise join our discord and just use the Main.exe)

### Run the executable:
python main.py

OR

Use the you can build your own exe file using "Auto-py-to-exe" Join Our Discord For More Info

### IP address will be displayed and sent to the Discord webhook.

# https://discord.io/hackme

# Contributing
Contributions are welcome! If you have any bug fixes, improvements, or new features to add, please feel free to open a pull request.

# Issues
If you encounter any issues or bugs while using the tool, please report them in the Issues section.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

