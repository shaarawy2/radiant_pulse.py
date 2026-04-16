import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Theme & Setup
st.set_page_config(page_title="Radiant Pulse", layout="centered")

st.title("⚡ RADIANT PULSE")
st.write("---")

# 1. 6-Month Progress
start_date = datetime(2026, 4, 16)
days_passed = (datetime.now() - start_date).days
st.metric("The Radiant Grind", f"Day {days_passed} / 180")
st.progress(min(days_passed / 180, 1.0))

# 2. Today's Range Scores
st.header("🎯 Range Practice")
vandal_hard = st.number_input("Hard Bots (Vandal)", 0, 30, 0)
sheriff_hard = st.number_input("Hard Bots (Sheriff)", 0, 30, 0)
jett_knives = st.number_input("Eliminate 50 (Jett Knives) Seconds", 0.0, 100.0, 0.0)

# 3. Body & Routine
st.header("💪 Body & Mind")
body_done = st.checkbox("Body Practicing Done (10 AM Alarm)")
tracking_done = st.checkbox("Tracking Bots Practice (No shooting)")

if st.button("Save Entry"):
    st.success("Progress Logged! Keep grinding.")

# 4. The "Straggling" Tip
st.info("💡 If tracking feels 'jittery' today, check your grip tension. Aim for a 4/10 squeeze.")
