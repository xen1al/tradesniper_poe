# tradesniper_poe
 A tool for making fast offers for items listed on [pathofexile.com/trade/](https://www.pathofexile.com/trade/).  
 Uses the [pathofexile.com/trade/](https://www.pathofexile.com/trade/) api. Main program is ToS compliant, not sure about the autowhisper though. Use at your own risk. Very rarely updated, might want to look for alternatives.
## Setup
### From source
* Run setup.bat to install requirements
* Alternatively, you can just run pipenv install if you have pipenv installed
* Run client.py and enter your POESESSID ([How to get POESESSID by Stickymaddness](https://github.com/Stickymaddness/Procurement/wiki/SessionID))
Note: the POESESSID should be in the following format: POESESSID=**poesessid**
### From release
* Download the [latest release](https://github.com/xen1al/tradesniper_poe/releases/latest)
* Run the .exe file and enter your POESESSID ([How to get POESESSID by Stickymaddness](https://github.com/Stickymaddness/Procurement/wiki/SessionID)). 
Note: the POESESSID should be in the following format: POESESSID=**poesessid**
## Usage
* Use [pathofexile.com/trade/](https://www.pathofexile.com/trade/) to get the query. Put in your desired filters and click "search". The last part of the url is the query. Example: http://www.pathofexile.com/trade/search/Standard/<b>9JPQ8OTK</b>
* For automatic whispering, just run autowhisper.ahk alongside the client. [Download autohotkey here](https://www.autohotkey.com)
## Things to note
* The program changes your clipboard every time a listing comes up
* The autowhisper will focus on your game and send keystrokes, might have unwanted side-effects if the game is not running
