import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
import pandas as pd
import requests
from PIL import Image
from model import func
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()    

if 's_s' not in st.session_state:
    st.session_state['s_s']=0

if 'damn' not  in st.session_state:
    st.session_state['damn']=0

# load assets
l = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_jrkcz8oc.json")
ll = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_xv1gn5by.json")
lll = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_kkxqs4gg.json")

st.set_page_config(page_title="CardioVascular Disease Detection",page_icon=":tada:")
# --- header section

with st.container():
    st.title("Heart Disease Prediction")
    st.write("This is AI based heart disease prediction website")
    st.write("To know more about heart disease, click in this link https://en.wikipedia.org/wiki/Cardiovascular_disease")

# --- body

st.write("---")

with st.container():
    st_lottie(l,height=300,key="coding")

with st.container():
    st.title("Predict now")
    name=st.text_input("Name")
    age=st.number_input("Age in year",0)
    gender=st.selectbox("Gender",['Male','Female'])
    height=st.number_input("Height in cm",0)
    weight=st.number_input("Weight in Kg")
    # st.select_slider("Gender",['male','female'])
    ap_hi=st.slider("Systolic blood pressure",0,200)
    ap_lo=st.slider("Diastolic blood pressure",0,200)
    cholesterol=st.select_slider(" Cholesterol : 1=normal,2=above normal,3=well above normal",[1,2,3])
    gluc=st.select_slider(" Glucose : 1=normal,2=above normal,3=well above normal",[1,2,3])
    smoke=st.radio("Smoke ?",['Yes','No'])
    alco=st.radio("Alcohol ?",['Yes','No'])
    active=st.radio("Active ?",['Yes','No'])
    columns=['age','gender','height','weight','ap_hi','ap_lo','cholesterol','gluc','smoke','alco','active']
    def predict():
        if gender=='Male':
            g=2
        else:
            g=1
        if smoke=='Yes':
            s=1
        else:
            s=0
        if alco=='Yes':
            al=1
        else:
            al=0
        if active=='Yes':
            ac= 1
        else:
            ac=0       
        row=np.array([age*365,g,height,weight,ap_hi,ap_lo,cholesterol,gluc,s,al,ac])

        ZZZ=pd.DataFrame([row],columns=columns)

        if(func(ZZZ)==0):
            st.session_state.s_s=1
        else:
            st.session_state.s_s=2
            
bt1 =st.button("Predict Now 👈",on_click=predict)

with st.container():
    z=name
    if st.session_state.s_s==0:
        st.write("No verdict yet.Submit First")
    elif st.session_state.s_s==1 and bt1==True :
        st.subheader("Prediction Result:")
        st_lottie(ll,height=300,key="codinggg")

        x= f"""

         <div style="color:green; font-size:50px;">
            {z} , you are not in the risk of heart disease !!!
            </div>
          """
        st.markdown(x,unsafe_allow_html=True)

    elif st.session_state.s_s==2 and bt1==True:
        st.subheader("Prediction Result:")
        st_lottie(lll,height=300,key="codingg")
        y= f"""
           <div style="color:red; font-size:50px;">
            {z} , you are in risk of heart disease !!!
            </div>
            """
        st.markdown(y,unsafe_allow_html=True)
        st.subheader("Seek emergency medical care if you have these heart disease symptoms:")
        a= f"""
           <div>
            <p style="color:red;font-size:20px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.Chest pain</p>
            <p style="color:red;font-size:20px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.Shortness of breath</p>
            <p style="color:red;font-size:20px;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.Fainting</p>
            <p style="font-size:20px;">Always call 911 or emergency medical help if you think you might be having a heart attack.</p>
           </div>
        """
        st.markdown(a,unsafe_allow_html=True)
        st.write("For more inforamtion, please visit this site https://www.heart.org/en/health-topics/consumer-healthcare/what-is-cardiovascular-disease")
