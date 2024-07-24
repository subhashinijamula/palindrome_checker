import streamlit as st
st.title("Palindrome Checker")
a=str(st.text_input(label="enter the input"))
b=a[::-1]
if(a==b):
    st.write("Palindrome")
else:
    st.write("not Palindrome")

