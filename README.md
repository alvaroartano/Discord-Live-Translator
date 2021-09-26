
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
    <img src="https://i.imgur.com/jA4WZPH.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Discord Live Translator</h3>

  <p align="center">
    A bot which will keep your server clean of other languages!
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

This project is a project which was made for the 2021's [Hackapalooza](https://hackapalooza.dev). It consists on a live translator for discord which allows to limit languages to channels and translates which aren't written in it.

This means, you can set up a channel so it only accepts messages on English and if they're not written in it, it just translates the message in real time

### Built With

This bot uses several libraries and technologies to work:
* [Discord.py](https://github.com/Rapptz/discord.py) for the discord Bot
* [Gspread](https://github.com/burnash/gspread) for the Google Sheets API integration with Python
* [LibreTranslate PY](https://github.com/argosopentech/LibreTranslate-py) for the detection and translation using [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

You just need to have [Python](https://www.python.org/) and Pip installed on your machine

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/alvaroartano/Discord-Live-Translator.git
   ```
2. Install NPM packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create a new google sheet
4. Create a  `.env` file and fill it up with your discord bot token
   ```JS
   DISCORD_TOKEN=<token>
   GOOGLE_SHEET_NAME=
   ```
 5. Create a new Google Cloud API key for google sheets and download the key in your folder with the name `google_sheets_api_key.json`
 6. Give read and write perms to the google sheet to the email that was created during the api key creation




<!-- USAGE EXAMPLES -->
## Usage
1. For running the bot just run `python bot.py`
2. Then, add it to a server and set up a channel using `!setup <iso code>` *[Here](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) you have a list of ISO codes*, for example `!setup en` for English
3. Test it!






<!-- CONTACT -->
## Contact

Alvaro Artano - [@alvaroartano](https://twitter.com/alvaroartano) - hello@alvaroartano.me






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/alvaroartano/Discord-Live-Translator.svg?style=for-the-badge
[contributors-url]: https://github.com/alvaroartano/Discord-Live-Translator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alvaroartano/Discord-Live-Translator.svg?style=for-the-badge
[forks-url]: https://github.com/alvaroartano/Discord-Live-Translator/network/members
[stars-shield]: https://img.shields.io/github/stars/alvaroartano/Discord-Live-Translator.svg?style=for-the-badge
[stars-url]: https://github.com/alvaroartano/Discord-Live-Translator/stargazers
[issues-shield]: https://img.shields.io/github/issues/alvaroartano/Discord-Live-Translator.svg?style=for-the-badge
[issues-url]: https://github.com/alvaroartano/Discord-Live-Translator/issues
[product-screenshot]: https://i.imgur.com/jA4WZPH.png
