import requests
import json


class Listing:
    def __init__(self, id, query):
        self.id = id
        self.query = query
        print("INFO: Requesting listing id {}".format(id))

        response = json.loads(requests.get("https://www.pathofexile.com/api/trade/fetch/{}?query={}".format(id, query)).content)["result"][0]

        self.itemName = ""
        self.ilvl = ""
        self.itemProperties = ""
        self.itemRequirements = ""
        self.itemSockets = ""
        self.itemTypeLine = ""
        self.itemCorrupted = False
        self.itemIdentified = ""
        self.itemMods = ""
        self.itemCategory = ""
        self.itemExtended = ""
        self.itemFlavourText = ""
        self.itemIcon = ""
        self.verified = False
        self.language = ""
        self.accountName = ""
        self.ign = ""
        self.league = ""
        self.price = None
        self.currency = ""
        self.stashName = ""
        self.stashPos = ["", ""]
        self.whisper = ""

        if "item" in response:
            item = response["item"]
            if item is not None:
                if "name" in item:
                    self.itemName = item["name"]
                if "ilvl" in item:
                    self.ilvl = item["ilvl"]
                if "properties" in item:
                    self.itemProperties = item["properties"]
                if "itemRequirements" in item:
                    self.itemRequirements = item["requirements"]
                if "sockets" in item:
                    self.itemSockets = item["sockets"]
                if "typeLine" in item:
                    self.itemTypeLine = item["typeLine"]
                if "corrupted" in item:
                    self.itemCorrupted = item["corrupted"]
                if "identified" in item:
                    self.itemIdentified = item["identified"]
                if "explicitMods" in item:
                    self.itemMods = item["explicitMods"]
                if "category" in item:
                    self.itemCategory = item["category"]
                if "extended" in item:
                    self.itemExtended = item["extended"]
                if "flavourText" in item:
                    self.itemFlavourText = item["flavourText"]
                if "icon" in item:
                    self.itemIcon = item["icon"]
                if "verified" in item:
                    self.verified = item["verified"]
                if "league" in item:
                    self.league = item["league"]

        if "listing" in response:
            listing = response["listing"]
            if "whisper" in listing:
                self.whisper = listing["whisper"]

            if "account" in listing:
                account = listing["account"]
                if account is not None:
                    if "language" in account:
                        self.language = account["language"]
                    if "name" in account:
                        self.accountName = account["name"]
                    if "lastCharacterName" in account:
                        self.ign = account["lastCharacterName"]

            if "price" in listing:
                price = listing["price"]
                if price is not None:
                    if "amount" in price:
                        self.price = price["amount"]
                    if "currency" in price:
                        self.currency = price["currency"]

            if "stash" in listing:
                stash = listing["stash"]
                if stash is not None:
                    if "name" in stash:
                        self.stashName = stash["name"]
                    if "x" or "y" in stash:
                        self.stashPos = [stash["x"], stash["y"]]
