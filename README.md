# Colorselect
A python/Flask application for manipulating RGB LED's attached to a Raspberry
Pi, for fun and profit.

**Quick and dirty implementation, don't rely on this code**

Using the RPi.GPIO library for pulse-width modulation (PWM) and other GPIO pin
settings, we can pretty easily link the RGB output of some LEDs to a form
control on a webpage.

Since we're using the RPi.GPIO library, this application needs to run as root
for the time being.

## Usage
- After you clone the repository, create a virtualenv on your Raspberry Pi
  (`virtualenv -p python3 colorselect`).

- Activate the virtualenv (`source bin/activate` from within the virtualenv
  directory) and run a pip install to acquire the dependencies
  (`pip install -r requirements.txt`).

- Run the application as `root` using
  `export FLASK_APP=colorselect.py && flask run`) from the base directory of the
  application. Flask will start serving up the app on port 5000.

## Contributing
Pull requests are welcome! I'd like to add websocket capability in the near
future, so that colors can be updated from multiple clients without surprising
users with an older version of the page. 