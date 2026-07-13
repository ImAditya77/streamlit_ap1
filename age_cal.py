import streamlit as st
from datetime import date

st.title("🎂 Age Calculator")

name = st.text_input("Enter your name:")
dob = st.date_input("Enter your date of birth:")

if st.button("Calculate Age"):
    today = date.today()

    age = today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )

    st.success(f"Hello {name}, you are {age} years old.")

    # Check if birthday has occurred this year
    if (today.month, today.day) < (dob.month, dob.day):
        st.info("🎉 Your birthday has not occurred yet this year.")
    elif (today.month, today.day) == (dob.month, dob.day):
        st.balloons()
        st.success("🎂 Happy Birthday!")
    else:
        st.info("✅ Your birthday has already occurred this year.")