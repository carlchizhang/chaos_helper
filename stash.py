import requests
import json
import os
from collections import defaultdict

STASH_API_URL = "https://www.pathofexile.com/character-window/get-stash-items"
BASE_ITEMS_JSON_PATH = "repoe_base_items.json"

class StashParser():
    """
    StashParser is used to call the PoE API, retrieve dump tab items,
    and classify them into chaos recipe components
    """

    def __init__(self, tab_index, account_name, league, sessid):
        print(f"StashParser init for tab {tab_index} for account {account_name} in league {league}")
        self.payload = {
            'accountName': account_name,
            'league': league,
            'tabIndex': tab_index,
        }
        self.cookies = {
            'POESESSID': sessid,
        }
        self.item_mapping = self._create_item_class_name_mapping()

    def get_stash_contents(self):
        """
        get_stash_contents retrieves items from the PoE API
        and returns a dict of chaos recipe components
        """
        try:
            resp = requests.get(STASH_API_URL, params=self.payload, cookies=self.cookies)
        except requests.HTTPError as e:
            print(e)
        items = resp.json()['items']
        return self._classify_items(items)

    def _classify_items(self, items):
        res = defaultdict(float)
        for item in items:
            type_line = item['typeLine']
            if type_line.startswith('Superior'):
                type_line = type_line[len('Superior '):]
            if type_line in self.item_mapping['Rings']:
                res['Rings'] += 0.5
            elif type_line in self.item_mapping['Amulets']:
                res['Amulets'] += 1
            elif type_line in self.item_mapping['Belts']:
                res['Belts'] += 1
            elif type_line in self.item_mapping['One Hand Weapons']:
                res['Weapons'] += 0.5
            elif type_line in self.item_mapping['Two Hand Weapons']:
                res['Weapons'] += 1
            elif type_line in self.item_mapping['Body Armours']:
                res['Body Armours'] += 1
            elif type_line in self.item_mapping['Boots']:
                res['Boots'] += 1
            elif type_line in self.item_mapping['Gloves']:
                res['Gloves'] += 1
            elif type_line in self.item_mapping['Helmets']:
                res['Helmets'] += 1
            else:
                print(f"Unrecognized base type while classifying items: {type_line}")
        return res

    def _create_item_class_name_mapping(self):
        script_dir = os.path.dirname(__file__) # absolute dir the script is in
        abs_path = os.path.join(script_dir, BASE_ITEMS_JSON_PATH)

        with open(abs_path, 'r') as f:
            data = json.load(f)
            res = defaultdict(set)
            for item in data.values():
                type_name, item_class = item['name'], item['item_class']
                if item_class in {'Ring'}:
                    res['Rings'].add(type_name)
                elif item_class in {'Amulet'}:
                    res['Amulets'].add(type_name)
                elif item_class in {'Belt'}:
                    res['Belts'].add(type_name)
                elif item_class in {'Thrusting One Hand Sword', 'Dagger', 'Claw', 'One Hand Mace', 'Wand', 'One Hand Sword', 'One Hand Axe', 'Quiver', 'Shield', 'Sceptre', 'Rune Dagger'}:
                    res['One Hand Weapons'].add(type_name)
                elif item_class in {'Two Hand Mace', 'Bow', 'Two Hand Axe', 'Warstaff', 'Two Hand Sword', 'Staff'}:
                    res['Two Hand Weapons'].add(type_name)
                elif item_class in {'Body Armour'}:
                    res['Body Armours'].add(type_name)
                elif item_class in {'Boots'}:
                    res['Boots'].add(type_name)
                elif item_class in {'Gloves'}:
                    res['Gloves'].add(type_name)
                elif item_class in {'Helmet'}:
                    res['Helmets'].add(type_name)

        return res
