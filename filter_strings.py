HIDE_ALL = (
    'Hide # hiding all rares first\n'
    '    Class "Helmets" "Gloves" "Boots" "Body Armours" "Shields" "Quivers" "Wands" "Rune Dagger" "Warstaves" "Daggers" "Sceptres" "Bows" "Claws" "One Hand Swords" "Thrusting One Hand Swords" "One Hand Axes" "One Hand Maces" "Staves" "Two Hand Swords" "Two Hand Axes" "Two Hand Maces"\n'
    '    SetFontSize 18\n'
    '    ItemLevel >= 65\n'
    '    Identified False\n'
    '    Rarity Rare\n\n'
)

OVERRIDE_AREA_2_TEXT = "# [[2900]] OVERRIDE AREA 2"

RARE_ITEMS_TEXT = "# [[3000]] RARE ITEMS"

ITEM_FILTER_DICT = {
    'Rings': (
        'Show # rings\n'
        '    SetBorderColor 255 255 255 255\n'
        '    SetFontSize 45\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    Class "Rings"\n'
        '    SetTextColor 0 0 0 255\n'
        '    SetBackgroundColor 170 225 70 255\n'
        '    Identified False\n'
        '    ItemLevel <= 74\n\n'
    ),

    'Amulets': (
        'Show # amulets\n'
        '    SetBorderColor 255 255 255 255\n'
        '    SetFontSize 45\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    Class "Amulets"\n'
        '    SetTextColor 0 0 0 255\n'
        '    SetBackgroundColor 170 225 70 255\n'
        '    Identified False\n'
        '    ItemLevel <= 74\n\n'
    ),

    'Belts': (
        'Show # belts\n'
        '    SetBorderColor 255 255 255 255\n'
        '    SetFontSize 45\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    Class "Belts"\n'
        '    SetTextColor 0 0 0 255\n'
        '    SetBackgroundColor 170 225 70 255\n'
        '    Identified False\n'
        '    ItemLevel <= 74\n\n'
    ),

    'Weapons': (
        'Show # weapons\n'
        '    SetBorderColor 200 0 0\n'
        '    SetFontSize 38\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    ItemLevel <= 74\n'
        '    Class "Wands" "Daggers" "Sceptres" "One Hand Swords" "One Hand Maces" "Warstaves" "Staves" "Two Hand Swords" "Two Hand Axes" "Two Hand Maces"\n'
        '    Identified False\n'
        '    Height = 3\n'
        '    Width = 1\n\n'
    ),

    'Body Armours': (
        'Show # body armours\n'
        '    SetBorderColor 255 255 255\n'
        '    SetFontSize 38\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    ItemLevel <= 74\n'
        '    Class "Body Armours"\n'
        '    Identified False\n\n'
    ),

    'Boots': (
        'Show # boots\n'
        '    SetBorderColor 255 0 215\n'
        '    SetFontSize 38\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    ItemLevel <= 74\n'
        '    Class "Boots"\n'
        '    Identified False\n\n'
    ),

    'Gloves': (
        'Show # gloves\n'
        '    SetBorderColor 0 200 162\n'
        '    SetFontSize 38\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    ItemLevel <= 74\n'
        '    Class "Gloves"\n'
        '    Identified False\n\n'
    ),

    'Helmets': (
        'Show # helmets\n'
        '    SetBorderColor 16 200 0\n'
        '    SetFontSize 38\n'
        '    ItemLevel >= 60\n'
        '    Rarity Rare\n'
        '    Class "Helmets"\n'
        '    Identified False\n'
        '    ItemLevel <= 74\n\n'
    ),
}
