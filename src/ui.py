import streamlit as st
from main import results

st.title("AI-Powered Root Cause Demo")

for result in results:
    st.subheader(f"Alert on {result['alert']['ci']}")
    st.write(f"Message: {result['alert']['message']}")
    st.write(f"Potential Root Cause: {result['cause']['change']}")
