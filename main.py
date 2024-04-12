import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

user_animal_type = st.sidebar.selectbox("What pet do you want to name",("Cat","Dog","Hamster","Parrot"))

if user_animal_type == "Cat":
    user_pet_color = st.sidebar.text_area(label="What color is your cat?",max_chars=15)
if user_animal_type == "Dog":
    user_pet_color = st.sidebar.text_area(label="What color is your dog?",max_chars=15)
if user_animal_type == "Hamster":
    user_pet_color = st.sidebar.text_area(label="What color is your hamster?",max_chars=15)
if user_animal_type == "Parrot":
    user_pet_color = st.sidebar.text_area(label="What color is your parrot?",max_chars=15)

button =  st.sidebar.button("Submit")

if button:
    response = lch.generate_pet_name(user_animal_type,user_pet_color)
    st.text(response['pet_name'])