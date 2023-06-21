# Package / Library
import streamlit as st

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content

# FUNCTIONS
# Set Page
def set_page():
    st.set_page_config(
        page_title="ABOUT",
        page_icon="1️⃣",
        layout="centered",
        initial_sidebar_state="auto",
    )

# MAIN CONFIG
if __name__ == "__main__":
    main()