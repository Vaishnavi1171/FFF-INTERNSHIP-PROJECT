import pickle
import streamlit as st
import pandas as pd

# load the trained machine learning model
with open('C:/Users/Shree/Desktop/Vaishu Project/RandomizedSearchCV_model.pkl', 'rb') as f:
    model = pickle.load(f)
    
    
def predict_price(input_df):
    prediction = model.predict(input_df)
    return prediction

def app():
    st.title("Car Price Prediction")

    # create input fields for user inputs
    Present_Price = st.number_input ('Present Price of car')
    Kms_driven = st.number_input("Kilometers Driven")
    Owner = st.selectbox("Owner Type", options=["First Owner","Second Owner","Other"])
    Number_of_years = st.number_input("Year of Registration")
    Fuel_type = st.selectbox("Fuel Type", options=['Petrol', 'Diesel'])
    Seller_type = st.selectbox("Seller Type", options=['Individual', 'Dealer'])
    Transmission_type = st.selectbox("Transmission Type", options=['Manual', 'Automatic'])
    
    # map owner type to numerical values
    owner_map = {'First Owner': 1, 'Second Owner': 2, 'Other': 3}
    Owner = owner_map[Owner]
    
    # create binary variables for fuel type, seller type, and transmission type
    is_petrol = 1 if Fuel_type == 'Petrol' else 0
    is_diesel = 1 if Fuel_type == 'Diesel' else 0    
    is_individual = 1 if Seller_type == 'Individual' else 0
    is_automatic = 1 if Transmission_type == 'Automatic' else 0
    
    input_df = pd.DataFrame({"Present_Price": Present_Price,
                             'Kms_driven': Kms_driven, "Owner" : Owner,
                             'Number_of_years':Number_of_years, 
                             'Fuel_Type_Diesel': is_diesel,
                             'Fuel_Type_Petrol': is_petrol,
                             'Seller_Type_Individual': is_individual,
                             'Transmission_Automatic': is_automatic}, index = [0])
    
    

    if st.button("Predict Price"):
         predicted_price = predict_price(input_df)
         # convert the NumPy array to a list
         predicted_price_list = predicted_price.tolist() 
         st.success(f"Predicted Price is {predicted_price_list[0]:,.2f} INR")

if __name__ == '__main__':
    app()
