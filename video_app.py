import streamlit as st

# 動画ファイルのパスと表示名を設定
videos = {
    "Test Video 1": "C:/Users/鈴木脩大/Videos/test1.mp4",
    "Test Video 2": "C:/Users/鈴木脩大/Videos/test2.mp4",
    "Test Video 3": "C:/Users/鈴木脩大/Videos/test3.mp4",
}

# アプリのタイトル
st.title("動画再生アプリ")

# 動画選択のドロップダウンメニュー
selected_video = st.selectbox("再生する動画を選択してください", list(videos.keys()))

# 選択された動画のパスを取得
video_path = videos[selected_video]

# 動画の表示
with open(video_path, "rb") as video_file:
    video_bytes = video_file.read()
    st.video(video_bytes)

# 簡単な説明
st.write("上記のドロップダウンメニューから再生したい動画を選択してください。")
