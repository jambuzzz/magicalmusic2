import streamlit as st
import os
import json
from pathlib import Path

# Load rhyming groups
def load_rhymes():
    file_path = Path("comments/rhyming_groups.json")
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []

# UI
st.set_page_config(page_title="TikTok Rhyme Video Generator", page_icon="🎤")
st.title("🎤 TikTok Rhyme Video Generator")

# Upload TikTok comments file
uploaded = st.file_uploader("Upload TikTok comments (.txt)", type="txt")
if uploaded:
    comments_path = Path("comments/raw_comments.txt")
    comments_path.parent.mkdir(parents=True, exist_ok=True)
    comments_path.write_text(uploaded.read().decode("utf-8"))
    st.success("✅ Comments saved!")

if st.button("🧠 Group Rhymes with GPT"):
    os.system("python scripts/2_group_rhymes.py")
    st.success("🧠 Grouped rhymes with GPT!")

rhymes = load_rhymes()
if rhymes:
    st.subheader("🎶 Rhyming Comment Groups")
    for group in rhymes:
        st.markdown(f"**Group {group['group']}**")
        for comment in group['comments']:
            st.write(f"• {comment}")

if st.button("🎙️ Generate Voiceovers"):
    os.system("python scripts/3_generate_tts.py")
    st.success("🎧 TTS audio generated!")

if st.button("🎬 Create Video Scenes"):
    os.system("python scripts/4_create_scenes.py")
    st.success("🎬 Scene clips created!")

if st.button("🎞️ Merge Final Video"):
    os.system("python scripts/5_merge_video.py")
    video_path = "final_video/output.mp4"
    if Path(video_path).exists():
        st.video(video_path)
    else:
        st.warning("⚠️ Output video not found.")
