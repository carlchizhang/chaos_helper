from datetime import datetime
from filter_strings import ITEM_FILTER_DICT, HIDE_ALL, OVERRIDE_AREA_2_TEXT, RARE_ITEMS_TEXT

class FilterUpdater():
    def __init__(self, filter_path):
        self.filter_path = filter_path
        with open(filter_path, 'r') as f:
            lines = [x.strip() for x in f.readlines()]
            output = []
            within_override = False
            for i in range(len(lines)):
                line = lines[i]
                if line.startswith(RARE_ITEMS_TEXT):
                    within_override = False

                if not within_override:
                    output.append(line)

                if line.startswith(OVERRIDE_AREA_2_TEXT):
                    within_override = True
                    self.override_index = i + 1

        self.output = output
    
    def update_filter(self, stash_contents, jewellery_threshold, other_threshold):
        enable = set(ITEM_FILTER_DICT.keys())
        for item_class, count in stash_contents.items():
            if item_class in {'Rings', 'Amulets', 'Belts'} and count >= jewellery_threshold:
                enable.remove(item_class)
            elif count >= other_threshold:
                enable.remove(item_class)
        self._write_filter(enable)

    def _write_filter(self, item_classes):
        output = self.output.copy()
        print("Showing: ", item_classes)
        filter_content = (
            "#===============================================================================================================\n\n"
        )

        for item_class in item_classes:
            if item_class not in ITEM_FILTER_DICT:
                print(f"Unrecognized item class while writing the filter: {item_class}")
                continue
            filter_content += ITEM_FILTER_DICT[item_class]

        filter_content += HIDE_ALL
        filter_content += (
            "#==============================================================================================================="
        )

        with open(self.filter_path, 'w') as f:
            output.insert(self.override_index, filter_content)
            for line in output:
                f.write(line + "\n")
