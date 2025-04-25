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
st.title("🎤 TikTok Rhyme Video Generator")

# Upload TikTok comments file
uploaded = st.file_uploader("Upload TikTok comments .txt", type="txt")
if uploaded:
    comments_path = Path("comments/raw_comments.txt")
    comments_path.write_text(uploaded.read().decode())
    st.success("Comments saved!")

# Show rhyming groups (preview)
if st.button("🧠 Group Rhymes with GPT"):
    os.system("python scripts/2_group_rhymes.py")
    st.success("Grouped rhymes with GPT!")

rhymes = load_rhymes()
if rhymes:
    st.subheader("🎶 Rhyming Comment Groups")
    for group in rhymes:
        st.markdown(f"**Group {group['group']}**")
        for comment in group['comments']:
            st.write(f"• {comment}")

# Generate TTS
if st.button("🎙️ Generate Voiceovers"):
    os.system("python scripts/3_generate_tts.py")
    st.success("TTS audio generated!")

# Make video scenes
if st.button("🎬 Create Video Scenes"):
    os.system("python scripts/4_create_scenes.py")
    st.success("Scene clips created!")

# Merge final video
if st.button("🎞️ Merge Final Video"):
    os.system("python scripts/5_merge_video.py")
    st.video("final_video/output.mp4")
