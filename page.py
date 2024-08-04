import streamlit as st

user_db = {"admin": {"password": "admin", "email": "admin@example.com"}}

def login(username, password):
    if username in user_db and user_db[username]["password"] == password:
        return True
    return False

def signup(username, password, email):
    if username in user_db:
        return False
    user_db[username] = {"password": password, "email": email}
    return True

def main():
    st.title("Login / Sign Up Page")

    # Use session state to keep track of the current view
    if "view" not in st.session_state:
        st.session_state.view = "Login"

    if st.session_state.view == "Login":
        st.subheader("Login Section")
        username_login = st.text_input("Login Username")
        password_login = st.text_input("Login Password", type='password')
        if st.button("Login"):
            if login(username_login, password_login):
                st.success(f"Welcome {username_login}")
            else:
                st.error("Invalid Username/Password")
        if st.button("Go to Sign Up"):
            st.session_state.view = "Sign Up"
    else:
        st.subheader("Create New Account")
        new_username = st.text_input("Sign Up Username")
        new_password = st.text_input("Sign Up Password", type='password')
        new_email = st.text_input("Email")
        if st.button("Sign Up"):
            if signup(new_username, new_password, new_email):
                st.success("Account created successfully!")
            else:
                st.error("Username already taken")
        if st.button("Go to Login"):
            st.session_state.view = "Login"

if __name__ == '__main__':
    main()
