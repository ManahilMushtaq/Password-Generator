import streamlit as st
import random
import string

def generate_easy_password(length=12):
    """Generates a relatively easy-to-remember password."""
    lowercase = string.ascii_lowercase
    digits = string.digits
    characters = lowercase + digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    st.title("Easy Password Generator")
    st.write("Generates a password with lowercase letters and numbers.")

    if st.button("Generate Easy Password"):
        password = generate_easy_password()
        st.subheader("Generated Password:")
        st.code(password, language="text")

if __name__ == "__main__":
    main()