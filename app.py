import streamlit as st
import random
from data import INGREDIENTS, RACES, PREFERENCES

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
    if len(selected) < 2:
        st.error("食材を2つ選んでください！")
    else:
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
        st.image(f"images/default_dish.png", caption="完成した料理")
        
        # 次の客へ
        if st.button("次の客へ"):
            st.session_state.current_customer = random.choice(RACES)
            st.rerun()
