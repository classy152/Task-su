import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.set_page_config(page_title="Team Task Manager")

st.title("Team Task Manager")

menu = st.sidebar.selectbox(
    "Menu",
    ["Signup", "Login", "Dashboard"]
)

# SIGNUP
if menu == "Signup":

    st.subheader("Create Account")

    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Signup"):

        response = requests.post(
            f"{BASE_URL}/auth/signup",
            json={
                "name": name,
                "email": email,
                "password": password
            }
        )

        st.write(response.json())


# LOGIN
elif menu == "Login":

    st.subheader("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )

        data = response.json()

        if "token" in data:

            st.session_state.token = data["token"]

            st.success("Login Successful")

        else:
            st.error(data)


# DASHBOARD
elif menu == "Dashboard":

    st.subheader("Dashboard")

    if "token" not in st.session_state:

        st.warning("Please login first")

    else:

        headers = {
            "Authorization": f"Bearer {st.session_state.token}"
        }

        response = requests.get(
            f"{BASE_URL}/dashboard/stats",
            headers=headers
        )

        data = response.json()

        st.write("Total Projects:", data.get("total_projects"))
        st.write("Total Tasks:", data.get("total_tasks"))
        st.write("Completed Tasks:", data.get("completed_tasks"))
        st.write("Pending Tasks:", data.get("pending_tasks"))