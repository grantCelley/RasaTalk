# Intro to Rasa
This is a talk for [Lancaster AI](http://lancasterai.com) meet up for October 2019.
I talked about [Rasa](rasa.com) a conversational framework that can automate costumer service to making a virtual assistant. I did not cover deploying the application.

## Install
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install rasa
rasa train
rasa run action
rasa shell
```
This uses python virtual environment.
The Rras action server needs to run while Rasa shell is running
