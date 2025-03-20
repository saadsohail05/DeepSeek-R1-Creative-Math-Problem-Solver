import streamlit as st
import requests

# Replace with your actual ngrok URL
API_URL = "https://448a-35-240-200-96.ngrok-free.app"  

st.title("Math Emojis Solver ")
st.write("Give emoji-based math problems, and I'll solve them for you!")

# Example problems for easy selection
examples = {
    "Select an example problem": "",
    "Problem 1": "🎨 + 🎨 + 🎨 = 27. Find the value of 🎨.",
    "Problem 2": "🐉 + 🐉 + 🐉 + 🐉 = 28. Find the value of 🐉.",
    "Problem 3": "🎁 + 🎀 = 14, and 🎁 - 🎀 = 2. Find the values of 🎁 and 🎀."
}

selected_example = st.selectbox("Try an example problem:", list(examples.keys()))

# Prefill text area if an example is selected
emoji_problem = st.text_area(
    "Enter your emoji problem:", 
    value=examples[selected_example] if selected_example != "Select an example problem" else "",
    height=100
)

if st.button("Solve Emojis "):
    if emoji_problem:
        try:
            with st.spinner("Thinking... 🤔"):
                response = requests.post(f"{API_URL}/generate", json={"emoji": emoji_problem})

                if response.status_code == 200:
                    solution = response.json().get("solution", "No solution found!")
                    st.success("### Solution:")
                    st.markdown(f"```xml\n{solution}\n```")
                else:
                    st.error(f"API Error: {response.status_code}\n{response.text}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter an emoji problem first!")
