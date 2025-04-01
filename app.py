import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="🔐 Password Generator", page_icon="🔑", layout="centered")

st.title("🔐 Random Password Generator")
st.write("Generate strong and secure passwords instantly!")

num_passwords = st.number_input("🔢 Number of Passwords:", min_value=1, max_value=10, step=1, value=1)
password_length = st.number_input("🔠 Password Length:", min_value=4, max_value=32, step=1, value=12)

if st.button("⚡ Generate Passwords"):
    st.subheader("🔑 Generated Passwords:")
    for _ in range(num_passwords):
        st.code(generate_password(password_length), language="")
