from stash import StashParser
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

    while True:
        print("Refreshing...")
        stash_contents = sp.get_stash_contents()
        print(stash_contents)
        time.sleep(10)


if __name__ == "__main__":
    main()
