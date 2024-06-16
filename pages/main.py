
import streamlit as st

def run():
    st.header("FIRST PAGE")
    st.write("This is the first page in our Streamlit app!")

# Set up the app title and sidebar
st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide")
st.title("Welcome to My Multi-Page Streamlit App")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

# Function to load the selected page
def load_page(page_name):
    if page_name == "Home":
        import pages.home as page
    page.run()

# Load the selected page
load_page(page)