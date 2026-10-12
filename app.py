import streamlit as st

# Label the smoke-test app in the browser.
st.title("Hello from Streamlit")

# Collect a name so the button can personalize the greeting.
name = st.text_input("What is your name?")

# Show a greeting when the user submits the button.
if st.button("Say hello"):
    st.success(f"Hello, {name}!")

# Confirm that the Streamlit app rendered successfully.
st.write("The app is live.")
