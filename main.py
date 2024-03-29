from stash import StashParser
from filter import FilterUpdater
from filter_strings import ITEM_FILTER_DICT
from config import GLOBAL_CONFIG
import time

def main():
    print("Starting up the chaos helper...")
    sp = StashParser(
        GLOBAL_CONFIG['tab_index'],
        GLOBAL_CONFIG['account_name'],
        GLOBAL_CONFIG['league'],
        GLOBAL_CONFIG['session_id'],
    )
    fu = FilterUpdater(GLOBAL_CONFIG['filter_path'])

    while True:
        print("\nRefreshing...")
        stash_contents = sp.get_stash_contents()
        fu.update_filter(
            stash_contents,
            GLOBAL_CONFIG['jewellery_threshold'],
            GLOBAL_CONFIG['other_threshold'],
        )
        count = float('inf')
        for item_type in ITEM_FILTER_DICT.keys():
            if stash_contents[item_type] < count:
                count = stash_contents[item_type]
        print(stash_contents)
        print(f"Currently we can make {count} chaos recipe sets.")
        print(f"Clicking order: big items -> belts/rings/ammys")
        time.sleep(GLOBAL_CONFIG['refresh_interval'])


if __name__ == "__main__":
    main()
