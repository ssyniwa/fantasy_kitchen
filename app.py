import streamlit as st
import random

import os
# 8種類の食材：それぞれの特徴（タイプ）と価値（レアリティ）を設定
INGREDIENTS = {
    "ドラゴンの肉": {"type": "肉類", "rarity": 5},
    "ミノタウロスの肉": {"type": "肉類", "rarity": 3},
    "光るキノコ": {"type": "野菜", "rarity": 3},
    "エルフの聖なるハーブ": {"type": "野菜", "rarity": 4},
    "妖精のハチミツ": {"type": "甘味", "rarity": 4},
    "魔力のクリスタルシュガー": {"type": "甘味", "rarity": 5},
    "スライムのゼリー": {"type": "その他", "rarity": 2},
    "深海魚の鱗": {"type": "その他", "rarity": 2},
}

# 8種類の種族
RACES = ["人間", "エルフ", "ドワーフ", "オーク", "魔法使い", "獣人", "ハーフリング", "精霊"]

# 各種族の「好きなタイプ」の傾向
# 複数のタイプを設定すると、客の反応が多様になります
PREFERENCES = {
    "人間": ["肉類", "野菜", "甘味"],
    "エルフ": ["野菜", "甘味"],
    "ドワーフ": ["肉類", "その他"],
    "オーク": ["肉類", "その他"],
    "魔法使い": ["甘味", "その他"],
    "獣人": ["肉類", "肉類"],  # 肉類を好む確率が高い設定
    "ハーフリング": ["甘味", "野菜"],
    "精霊": ["野菜", "その他"]
}

RECIPES = {
    ("ドラゴンの肉", "光るキノコ"): {"name": "灼熱の竜肉と蓄光茸のシチュー", "trait": "ドラゴンの肉は煮込むと独特の熱を帯びる性質があります。これを冷涼な洞窟で採れる光るキノコと一緒に煮込むことで、味が調和するのです。効果: 身体の芯から温まり、氷雪地帯でも寒さを感じなくなるほどの強靭な耐性を授けてくれます。", "image": "images/dragon_mushroom.png"},
    ("ドラゴンの肉", "ミノタウロスの肉"): {"name": "竜と牛の究極ミートパイ", "trait": "濃厚な旨味をパイ生地の中に閉じ込めた、冒険者のための携帯食です。効果: 強固な鎧を纏ったかのような防御力と、身体を内側から強化する力が宿ると言われています。", "image": "images/dragon_mino.png"},
    ("ドラゴンの肉", "エルフの聖なるハーブ"): {"name": "ドラゴン・タルタルステーキ", "trait": "素材の生命力をそのまま味わう、贅沢な一品です。効果: 身体の重さを取り払い、驚異的な跳躍力や俊敏さを授けてくれます。高い崖を登る際や、素早い敵との戦いにおいて真価を発揮するでしょう。", "image": "images/dragon_tea.png"},
    ("妖精のハチミツ", "エルフの聖なるハーブ"): {"name": "妖精のハーブティー", "trait": "癒やし効果", "image": "images/fairy_tea.png"},
    
    
}
st.set_page_config(page_title="ファンタジーキッチン")

# セッション状態の初期化
if 'score' not in st.session_state:
    st.session_state.score = 0
    st.session_state.current_customer = random.choice(RACES)

st.title("🧙‍♂️ ファンタジーキッチンへようこそ！")
st.sidebar.metric("現在の評価合計", st.session_state.score)

st.subheader(f"来店中の客: {st.session_state.current_customer}")
st.write(f"{st.session_state.current_customer}さんが注文を考えています...")

# 食材選択
selected = st.multiselect("食材を2つ選んでください", list(INGREDIENTS.keys()), max_selections=2)

if st.button("料理を提供する！"):
    if len(selected) != 2:
        st.error("食材を2つ選んでください！")
    else:
        # 食材をソートしてレシピキーを作成
        recipe_key = tuple(sorted(selected))
        recipe = RECIPES.get(recipe_key)
        # 評価ロジック
        score_gain = 0
        pref = PREFERENCES[st.session_state.current_customer]
        for item in selected:
            if INGREDIENTS[item]["type"] in pref:
                score_gain += (10 * INGREDIENTS[item]["rarity"])
        
        st.session_state.score += score_gain
        st.success(f"評価: {score_gain}点獲得！")
        
        # 料理画像の表示（食材の組み合わせに応じたファイル名で管理）
        # 例: images/肉_キノコ.png など
        st.subheader("提供した料理")
        st.write(f"### {recipe['name']}")
        st.info(f"特徴: {recipe['trait']}")
        st.write(f"現在のディレクトリ: {os.getcwd()}")
        if os.path.exists("images"):
            st.write(f"imagesフォルダの中身: {os.listdir('images')}")
        else:
            st.write("エラー: 'images' というフォルダが見つかりません。")
        # 画像表示
        
        st.image(recipe['image'], width=600)
        
        
        # 次の客へ
        if st.button("次の客へ"):
            st.session_state.current_customer = random.choice(RACES)
            st.rerun()
