# My Try discord bots project


This project it's only a personal practice about discord bots made following some video tutorials from YouTube. Does not pretend to be a professional approach of bot development. Anyone is allowed and encouraged to clone, fork and use this code for personal use.

## Usage

#### First you need to have installed Python, 
You can follow any of this How to for your OS [Windows](https://phoenixnap.com/kb/how-to-install-python-3-windows), [Mac](https://kinsta.com/knowledgebase/install-python/#mac) or [Linux](https://kinsta.com/knowledgebase/install-python/#linux) if you need.

#### Clone or download this repository
You can download this repository from [GitHub](https://github.com/ReynaldoCC/DiscordTube) or you can use [Git](https://git-scm.com/) to clone it using the following command

    git clone https://github.com/ReynaldoCC/DiscordTube.git

#### Install python requirements

    cd DiscordTube
    pip install -r requirements.txt

#### Create configuration environment

Need to create a .env file based on [example.env](./example.env) file and add in that new file the values of environment variables *'YT_KEY'* and *'DISCORD_TOKEN'*

    cp ./example.env ./.env
    nano .env

#### Run the bot

    python main.py


## Credits

##### Based on these sources

 - This video tutorial from [El Taller de TD](https://www.youtube.com/@ElTallerDeTD) on [Youtube](https://www.youtube.com/watch?v=U5oqrXWRzek), the example code is here on [GitHub](https://github.com/eltallerdetd/DiscordBotTemplate.git)