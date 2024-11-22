import streamlit as st

# Vimeoの埋め込みリンク
video_links = {
    "Vimeo Video 1": "https://player.vimeo.com/video/1032216683",
    "Vimeo Video 2": "https://player.vimeo.com/video/1032216715",
    "Vimeo Video 3": "https://player.vimeo.com/video/1032216750",
}

# アプリのタイトル
st.title("Vimeo 動画再生アプリ")

# 動画選択のドロップダウンメニュー
selected_video = st.selectbox("再生する動画を選択してください", list(video_links.keys()))

# 選択された動画の埋め込みリンクを取得
video_url = video_links[selected_video]

# 動画を再生
st.video(video_url)

# 簡単な説明
st.write("Vimeoに保存された動画を選択して再生できます。")
