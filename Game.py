
import streamlit as st
import random

# Page title
st.set_page_config(page_title="Guess the Number", layout="centered")
st.title("🎯 Guess the Number Game")

# Initialize the number (only once using session state)
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.tries = 0

# Input from user
guess = st.number_input("Enter a number between 1 and 100:", min_value=1, max_value=100, step=1)

# Button to check guess
if st.button("Guess"):
    st.session_state.tries += 1

    if guess < st.session_state.secret_number:
        st.warning("Too low! Try a higher number.")
    elif guess > st.session_state.secret_number:
        st.warning("Too high! Try a lower number.")
    else:
        st.success(f"🎉 You guessed it right in {st.session_state.tries} tries!")
        # Reset game
        if st.button("Play Again"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.tries = 0
else:
    st.info("Click the button to make your guess!")

# Show the number of attempts
st.caption(f"Attempts: {st.session_state.tries}")
