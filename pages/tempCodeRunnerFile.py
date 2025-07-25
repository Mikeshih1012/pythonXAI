import streamlit as st

number = st.number_input("請輸入一個數字", step=1, min_value=0, max_value=100, value=60)

st.write(f"你輸入的數字是: {number}")

number = st.number_input("請輸入成績", min_value=0, max_value=100, value=60)
number = int(number)
if number >= 90:
    st.write(f"你的等級為A")
elif number >= 80 and number < 90:
    st.write(f"你的等級為B")
elif number >= 70 and number < 80:
    st.write(f"你的等級為C")
elif number >= 60 and number < 70:
    st.write(f"你的等級為D")
else:
    st.write(f"你的等級為E")

st.button("點我")

if st.button("**點我**"):
    st.snow()
if st.button("點我", key="unique_key"):
    st.balloons()
