import streamlit as st

# Google Driveの動画リンクを再生可能な形式に変換
video_links = {
    "Video 1": "https://drive.google.com/uc?id=17r_7nOhtB5M2u3QI86vEWtPWgQG-e18C",
    "Video 2": "https://drive.google.com/uc?id=1ESqo0wQF8jEq5sqZWbQ7OyreQh8E4bWF",
    "Video 3": "https://drive.google.com/uc?id=1OVfIqaGQcfEupYCPJ1VF0roL9arx9jr6",
}

# アプリのタイトル
st.title("Google Drive 動画再生アプリ")

# 動画選択のドロップダウンメニュー
selected_video = st.selectbox("再生する動画を選択してください", list(video_links.keys()))

# 選択された動画のリンクを取得
video_url = video_links[selected_video]

# 動画を再生
st.video(video_url)

# 簡単な説明
st.write("Google Driveに保存された動画を選択して再生できます。")
