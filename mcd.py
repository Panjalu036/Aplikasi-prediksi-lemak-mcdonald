import pickle
import streamlit as st


mcd_dataset_model = pickle.load(open('mcd_fat_model.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Tingkat Kandungan Lemak Pada Makanan di Mcdonalds')



col1, col2 = st.columns(2)


with col1 :
    Calories = st.text_input('input Calories', 0, 100)
with col1 :
    CaloriesFat = st.text_input('input CaloriesFat', 0, 500)
with col1 :
    TransFat = st.text_input('input TransFat', 0, 1)
with col1 :
    Cholesterol = st.text_input('input Cholesterol', 0 , 500)
with col2 :
    Sodium = st.text_input('input Sodium', 0 , 500)
with col2 :
    Carbohydrates = st.text_input('input Carbohydrates', 0 , 300)
with col2 :
    Sugars = st.text_input('input Sugars', 0 , 300)
with col2 :
    Protein = st.text_input('input Protein', 0 , 300)
    
    #code untuk prediksi
mcd_fatty = ''

if st.button('Prediksi Kandungan Lemak'):
    mcd_fatty_prediction = mcd_dataset_model.predict([[Calories,CaloriesFat,TransFat,Cholesterol,Sodium,Carbohydrates,Sugars,Protein]])
    
    if (mcd_fatty_prediction [0]== 1):
        mcd_fatty = 'Kandungan Lemak Tinggi'
    else: 
        mcd_fatty = 'Kandungan Lemak Rendah'
        
    st.success(mcd_fatty, icon="✅")
  

    