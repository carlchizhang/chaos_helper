from stash import StashParser
from filter import FilterUpdater
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
        print(stash_contents)
        time.sleep(10)


if __name__ == "__main__":
    main()
