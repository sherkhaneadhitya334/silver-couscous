import streamlit as st
import pandas as pd
st.logo("artifacts\\images\\first1.png", size="large", link=None, icon_image="artifacts\\images\\first1.png")
st.header("Animal Info Viewer")
st.subheader("Select an animal to know about it's details")
option = st.selectbox(
    "which type of animal info you want's to know?",
    ("Reptiles", "Birds", "Mammals","Sea Animals"),
    index=None,
    placeholder="Select Animal Type...",
)
st.write("You selected:", option)
if option:
    st.session_state.animal_type = option
    if option == "Reptiles":
        st.image("artifacts\\images\\reptiles.png", caption="Reptiles")
        st.write("Reptiles are cold-blooded vertebrates that typically have scaly skin and lay eggs. They include snakes, lizards, turtles, and crocodiles.")
    elif option == "Birds":        
        st.image("artifacts\\images\\birds.png", caption="Birds")
        st.write("Birds are warm-blooded vertebrates that have feathers, wings, and beaks. They are known for their ability to fly, although some species are flightless. Birds include species such as sparrows, eagles, and penguins.")
    elif option == "Mammals":       
        st.image("artifacts\\images\\mammals.png", caption="Mammals")
        st.write("Mammals are warm-blooded vertebrates that have hair or fur and produce milk to feed their young. They include a wide variety of animals such as humans, dogs, cats, elephants, and whales.")     
    else:
        st.write("Please select an animal type to view its details.") 
    if st.button("View Classifications"):
        st.switch_page('pages\\classification.py') 