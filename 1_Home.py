# Package / Library
import streamlit as st

# MAIN PAGE
def main():
    # Set Page Config
    set_page()

    # Content
    # Welcome
    st.markdown("<h1 style='text-align: center; color: white;'>Welcome</h1>", unsafe_allow_html=True)

# FUNCTIONS
# Set Page Config
def set_page():
    st.set_page_config(
        page_title="HOME",
        page_icon=":house_buildings:",
        layout="centered",
        initial_sidebar_state="auto",
    )

# MAIN CONFIG
if __name__ == "__main__":
    main()
