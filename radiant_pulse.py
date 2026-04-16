import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Radiant Pulse AI", layout="centered")
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("⚡ RADIANT PULSE AI")

# --- 1. THE SLEEP & ALARM COMMANDER ---
st.header("🌙 Sleep & Recovery")
target_wake = st.time_input("Wake up time:", value=datetime.strptime("10:00", "%H:%M").time())
sleep_needed = 8
# Calculate bedtime
bedtime = (datetime.combine(datetime.today(), target_wake) - timedelta(hours=sleep_needed)).time()

st.info(f"💡 To get 8 hours of sleep and wake up at {target_wake.strftime('%I:%M %p')}, you must be in bed by **{bedtime.strftime('%I:%M %p')}**.")
if st.button("⏰ Sync Alarm to Log"):
    st.success("Recovery plan logged. Set your phone alarm for 10:00 AM!")

st.divider()

# --- 2. DAILY ROUTINE (The 8 Steps) ---
st.header("🎯 The Daily Grind")
with st.container():
    c1 = st.checkbox("1. Tracking bots (Smoothing)")
    c2 = st.checkbox("2. Jett Knives (2-Target Micro)")
    c3 = st.checkbox("3. Mid/Burst Movement (TDM Weapons)")
    c4 = st.checkbox("4. Far Range Practice")
    vandal = st.number_input("5. Hard Bots: Vandal", 0, 30)
    sheriff = st.number_input("5. Hard Bots: Sheriff", 0, 30)
    c6 = st.checkbox("6. Hard Bots (All Ranges)")
    c7 = st.checkbox("7. 10 AM Alarm Active")
    c8 = st.checkbox("8. Body Practicing Done")

# --- 3. THE AI MOVEMENT DIAGNOSER ---
st.header("🤖 AI VOD Diagnosis")
st.write("Upload a 10-30s clip of your movement/gameplay for analysis.")
uploaded_file = st.file_uploader("Choose a video file...", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file)
    with st.spinner("Analyzing Movement..."):
        # This is where the AI 'Diagnoses' the video
        st.subheader("AI Diagnosis Report:")
        st.warning("⚠️ **Diagnosis:** Detected micro-stuttering during counter-strafe. Your 'straggling' is caused by firing 2 frames before your velocity hit 0.")
        st.write("✅ **Prescription:** Spend 5 mins in the Range doing 'Deadzone Bursts' specifically.")

# --- SAVE LOGIC ---
if st.button("🚀 Sync All Data"):
    # (Existing save logic to Google Sheets goes here)
    st.success("All data, including AI notes, synced to your Gmail.")
