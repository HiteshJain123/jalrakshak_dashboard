import streamlit as st

# Set up Streamlit page
st.set_page_config(page_title="Dashboard", layout="wide")

# Read the HTML file
with open("dashboard.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Display the HTML content
# st.components.v1.html(html_data, height=800, scrolling=False)


# st.components.v1.html(html_data, height=st.session_state.get('height', 800), scrolling=False)

st.components.v1.html(html_data, height = 2000)


