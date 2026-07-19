# data.py
INGREDIENTS = {
    "ドラゴンの肉": {"type": "meat", "rarity": 5},
    "妖精のハチミツ": {"type": "sweet", "rarity": 4},
    "光るキノコ": {"type": "veggie", "rarity": 3},
    "スライムのゼリー": {"type": "misc", "rarity": 2},
}

RACES = ["人間", "エルフ", "ドワーフ", "オーク"]

# 客の好み（例: エルフは甘いものや野菜が好き）
PREFERENCES = {
    "エルフ": ["sweet", "veggie"],
    "ドワーフ": ["meat"],
    "人間": ["meat", "sweet", "veggie", "misc"],
    "オーク": ["meat", "misc"]
}
