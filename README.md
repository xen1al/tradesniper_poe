# tradesniper_poe
 A tool for making fast offers for items listed on [pathofexile.com/trade/](https://www.pathofexile.com/trade/)
 Uses the [pathofexile.com/trade/](https://www.pathofexile.com/trade/) api. Use at your own risk, main program should be ToS compliant, not sure about the autowhisper though.
## Requirements
* Python 3.7
* AutoHotkey (for autowhisper)
* Pynput
* Pyperclip
* Requests
* Websocket-client
## Usage
* Run setup.bat to install requirements
* Alternatively, you can just run pipenv install if you have pipenv installed
* Run client.py
* [How to get POESESSID by Stickymaddness](https://github.com/Stickymaddness/Procurement/wiki/SessionID)
## Things to note
* The program changes your clipboard every time a listing comes up
* The autowhisper will focus on your game and send keystrokes, might have unwanted side-effects if the game is not running
