# PyFyPi

A **PY**thon-based visualizer that uses spoti**FY** as a source and runs on raspberry **PI**

## An LED visualizer with no connection required

PyFyPi only asks you to authenticate with Spotify; after that, you can walk away and have the lights keep going. No Bluetooth or AUX connection required. This is enabled by the Spotify API, which the Pi is constantly pinging to figure out what track you're playing, and then using Spotify's track data to represent it on the LED strip.

This also means its easy to switch who's controlling the music. Just have your guest connect to the webserver from their phone and login, and they get to be the DJ.

## Installation

Start by cloning the repo to the Pi.
```bash
git clone https://github.com/P-bibs/PyFyPi
cd PyFyPi
```

Then initialize the virtual environment for the python packages and install node dependencies.
```bash
python3.5 -m virtualenv env
source env/bin/activate
python -m pip install requirements.txt

npm i
```
**NOTE:** PyFyPi is only compatible with Python3.5

## Usage
First, start the authentication server:
```bash
node src/server/app.js
```
Then, navigate to the IP of the Pi on port 3000 in a web browser and authenticate with Spotify. After doing this, the Pi can successfully get info about your current Spotify playback.

Next, connect the LEDs to power and GPIO 18.

Finally, start the script:

```bash
#the script must be run with sudo
sudo -s
source env/bin/activate
python src/PyFyPi/__main__.py
```

If all goes well, you should see the LEDs pulsing in time with the music.

## Configuration Files
To get everything working smoothly, you'll to place two configuration files int he `data` directory.

`secret.txt` should contain your client secret from your Spotify for Developers Dashboard.

`redirect.txt` should contain the URL of your PI that you've specified as your redirect URL in the Spotify for Developers Dashboard.
