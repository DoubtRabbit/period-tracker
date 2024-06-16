
import streamlit as st

# running the page
def run():
    st.header("FIRST PAGE")
    st.write("This is the first page in our Streamlit app!")

# setting background & stuff
custom_css = """
<style>
body {
    background-color: #f0f0f0; /* Set your desired background color here */
}
</style>
"""
# rendering custom_css
st.markdown(custom_css, unsafe_allow_html=True)

# Set up the app title and sidebar
st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide")
st.title("Crave")

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