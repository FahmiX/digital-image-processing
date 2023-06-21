# Package / Library
import streamlit as st

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content
    # Coming Soon
    st.markdown("<h1 style='text-align: center; color: white;'>Coming Soon</h1>", unsafe_allow_html=True)

# FUNCTIONS
# Set Page
def set_page():
    st.set_page_config(
        page_title="About",
        page_icon="1️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# MAIN CONFIG
if __name__ == "__main__":
    main()