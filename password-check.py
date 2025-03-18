import streamlit as st
import re
def password_check(password):
    strenght = 0
    remarks = ""

    if len(password)>= 8:
        strenght +=1

    if re.search(r"[A-Z]",password):
        strenght +=1

    if re.search(r"[a-z]",password):
         strenght +=1

    if re.search(r"\d",password):
         strenght +=1
    
    if re.search(r"[!@#$%^&?*]",password):
         strenght +=1

    if strenght <= 2:
        remarks =  "❌ Weak Password"
        color = "red"
    
    elif strenght == 3:
         remarks = "⚠️ Medium Strength Password"
         color = "orange"

    else:
         remarks = "✅ Strong Password"
         color = "green"
         
    return remarks,color

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password",type="password")

if password:
     strenght_msg,color = password_check(password)
     st.markdown(f"<h3 style='color : {color};'> {strenght_msg} </h3>",unsafe_allow_html=True)