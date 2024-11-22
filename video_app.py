import streamlit as st
import json

# JSONファイルの読み込み
with open("videos.json", "r") as file:
    video_links = json.load(file)

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

