# import streamlit as st

# import pandas as pd
# import pickle

# import numpy as np





# @st.cache_resource



# def load_model():
#     with open("model.pkl", "rb") as file:
#         model = pickle.load(file)
#     return model




# model = load_model()  

# def load_model():
#     with open("scaler.pkl", "rb") as file:
#         model = pickle.load(file)
#     return model


# # Page Config
# # -----------------------------
# st.set_page_config(
#     page_title="House Price Prediction",
#     page_icon="🏠",
#     layout="centered"
# )


# # UI
# # -----------------------------
# st.title("🏠 House Price Prediction")
# st.write("Enter the house details below to predict the price")

# def predict():
#      if request.method == "POST":
#          session.permanent = True
#          vals=[]
#          location_map={'Karjat': 0,'Bhavnagar': 1,'Rudrapur': 2,'Palghar': 3,'Junagadh': 4,'Durgapur': 5,'Ratnagiri': 6,
#                        'Bharuch': 7,'Vapi': 8,'Neemrana': 9,'Bhiwadi': 10,'Valsad': 11,'Bhilai': 12,'Navsari': 13,'Asansol': 14,
#                        'Vizianagaram': 15,'Jamnagar': 16,'Haridwar': 17,'Mathura': 18,'Raigad': 19,'Meerut': 20,'Sindhudurg': 21,
#                        'Bilaspur': 22,'Solan': 23,'Dhanbad': 24,'Bhopal': 25,'Aurangabad': 26,'Nellore': 27,'Hubli': 28,'Raipur': 29,
#                        'Amravati': 30,'Ajmer': 31,'Dharuhera': 32,'Solapur': 33,'Kolhapur': 34,'Siliguri': 35,'Gwalior': 36,'Others': 37,
#                        'Ahmednagar': 38,'Agra': 39,'Udupi': 40,'Aligarh': 41,'Jodhpur': 42,'Gandhinagar': 43,'Guntur': 44,'Anand': 45,
#                        'Bahadurgarh': 46,'Belgaum': 47,'Indore': 48,'Jamshedpur': 49,'Margao': 50,'Rajkot': 51,'Palakkad': 52,'Madurai': 53,
#                        'Sonipat': 54,'Kota': 55,'Vijayawada': 56,'Jabalpur': 57,'Pondicherry': 58,'Guwahati': 59,'Jalandhar': 60,'Allahabad': 61,
#                        'Tirupati': 62,'Udaipur': 63,'Secunderabad': 64,'Vadodara': 65,'Visakhapatnam': 66,'Ghaziabad': 67,'Jaipur': 68,'Thrissur': 69,
#                        'Patna': 70,'Faridabad': 71,'Bhubaneswar': 72,'Surat': 73,'Shimla': 74,'Varanasi': 75,'Mysore': 76,'Mangalore': 77,'Dehradun': 78,
#                        'Nagpur': 79,'Coimbatore': 80,'Ernakulam': 81,'Ludhiana': 82,'Panchkula': 83,'Lucknow': 84,'Chandigarh': 85,'Kolkata': 86,'Kanpur': 87,
#                        'Kottayam': 88,'Panaji': 89,'Jalgaon': 90,'Mohali': 91,'Pune': 92,'Kochi': 93,'Ranchi': 94,'Noida': 95,'Chennai': 96,'Bangalore': 97,
#                        'Goa': 98,'Lalitpur': 99,'Mumbai': 100,'Maharashtra': 101,'Gurgaon': 102}
#          posted_map = {'Owner': 0, 'Dealer': 1, 'Builder': 2}
#          yes_map = {"Yes": 1, "No": 0}
#          posted = request.form["posted"]
#          vals.append(posted_map[posted])
#          rera=request.form["rera"]
#          vals.append(yes_map[rera])
#          rooms=request.form["rooms"]
#          vals.append(rooms)
#          square_foot=request.form["foot"]
#          vals.append(square_foot)
#          ready=request.form["ready_to_move"]
#          vals.append(yes_map[ready])
#          resale=request.form["resale"]
#          vals.append(yes_map[resale])
#          location=request.form["location"]
#          vals.append(location_map[location])






#          vals=scaler.transform([vals])
#          resale=model.predict(vals)
#      for val in resale:
#              st.success(f"The Price of the House is around {int(val)} Lacs","info")



# # -----------------------------
# posted_by_map = {
#     "Owner": 0,
#     "Dealer": 1,
#     "Builder": 2
# }

# yes_no_map = {
#     "Yes": 1,
#     "No": 0


# }









# posted_by = st.selectbox("Posted By", list(posted_by_map.keys()))
# rera = st.radio("RERA Approved?", list(yes_no_map.keys()))
# bhk = st.number_input("Number of Bedrooms (BHK)", min_value=1, max_value=10, step=1)
# square_ft = st.number_input("Area (Square Feet)", min_value=100, max_value=10000, step=50)



# ready_to_move = st.radio("Ready To Move?", list(yes_no_map.keys()))
# resale = st.radio("Resale Property?", list(yes_no_map.keys()))

# longitude = st.number_input(
#     "Longitude",
#     min_value=68.0,
#     max_value=98.0,
#     value=77.1025,
#     format="%.6f"
# )

# latitude = st.number_input(
#     "Latitude",
#     min_value=8.0,
#     max_value=38.0,
#     value=28.7041,
#     format="%.6f"
# )












         

#          # Predict Button
# # -----------------------------
# if st.button("🔮 Predict Price"):
#     input_data = np.array([[
#         posted_by_map[posted_by],
#         yes_no_map[rera],
#         bhk,
#         square_ft,
#         yes_no_map[rera],             # 4 RERA
#         yes_no_map[ready_to_move],    # 5 READY_TO_MOVE
#         yes_no_map[resale],           # 6 RESALE
#         longitude,                    # 7 LONGITUDE
        












#     ]])


    




#     prediction = model.predict(input_data)

#     st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")









































































import streamlit as st
import pickle
import numpy as np

# -------------------------------
# Load model & scaler
# -------------------------------
@st.cache_resource
def load_model_and_scaler():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    return model, scaler

model, scaler = load_model_and_scaler()

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the price")

# -------------------------------
# Mappings
# -------------------------------
posted_by_map = {"Owner": 0, "Dealer": 1, "Builder": 2}
yes_no_map = {"Yes": 1, "No": 0}

location_map = {
    'Karjat': 0,'Bhavnagar': 1,'Rudrapur': 2,'Palghar': 3,'Junagadh': 4,'Durgapur': 5,
    'Ratnagiri': 6,'Bharuch': 7,'Vapi': 8,'Neemrana': 9,'Bhiwadi': 10,'Valsad': 11,
    'Bhilai': 12,'Navsari': 13,'Asansol': 14,'Vizianagaram': 15,'Jamnagar': 16,
    'Haridwar': 17,'Mathura': 18,'Raigad': 19,'Meerut': 20,'Sindhudurg': 21,
    'Bilaspur': 22,'Solan': 23,'Dhanbad': 24,'Bhopal': 25,'Aurangabad': 26,
    'Nellore': 27,'Hubli': 28,'Raipur': 29,'Amravati': 30,'Ajmer': 31,
    'Dharuhera': 32,'Solapur': 33,'Kolhapur': 34,'Siliguri': 35,'Gwalior': 36,
    'Others': 37,'Ahmednagar': 38,'Agra': 39,'Udupi': 40,'Aligarh': 41,
    'Jodhpur': 42,'Gandhinagar': 43,'Guntur': 44,'Anand': 45,'Bahadurgarh': 46,
    'Belgaum': 47,'Indore': 48,'Jamshedpur': 49,'Margao': 50,'Rajkot': 51,
    'Palakkad': 52,'Madurai': 53,'Sonipat': 54,'Kota': 55,'Vijayawada': 56,
    'Jabalpur': 57,'Pondicherry': 58,'Guwahati': 59,'Jalandhar': 60,
    'Allahabad': 61,'Tirupati': 62,'Udaipur': 63,'Secunderabad': 64,
    'Vadodara': 65,'Visakhapatnam': 66,'Ghaziabad': 67,'Jaipur': 68,
    'Thrissur': 69,'Patna': 70,'Faridabad': 71,'Bhubaneswar': 72,'Surat': 73,
    'Shimla': 74,'Varanasi': 75,'Mysore': 76,'Mangalore': 77,'Dehradun': 78,
    'Nagpur': 79,'Coimbatore': 80,'Ernakulam': 81,'Ludhiana': 82,
    'Panchkula': 83,'Lucknow': 84,'Chandigarh': 85,'Kolkata': 86,
    'Kanpur': 87,'Kottayam': 88,'Panaji': 89,'Jalgaon': 90,'Mohali': 91,
    'Pune': 92,'Kochi': 93,'Ranchi': 94,'Noida': 95,'Chennai': 96,
    'Bangalore': 97,'Goa': 98,'Lalitpur': 99,'Mumbai': 100,
    'Maharashtra': 101,'Gurgaon': 102
}

# -------------------------------
# UI Inputs
# -------------------------------
posted_by = st.selectbox("Posted By", posted_by_map.keys())
location = st.selectbox("Location", location_map.keys())

bhk = st.number_input("BHK", min_value=1, max_value=10, step=1)
square_ft = st.number_input("Area (Square Feet)", min_value=100, max_value=10000, step=50)

rera = st.radio("RERA Approved?", yes_no_map.keys())
ready_to_move = st.radio("Ready To Move?", yes_no_map.keys())
resale = st.radio("Resale Property?", yes_no_map.keys())

# -------------------------------
# Prediction
# -------------------------------
if st.button("🔮 Predict Price"):
    input_data = np.array([[
        posted_by_map[posted_by],        # 1
        yes_no_map[rera],                # 2
        bhk,                             # 3
        square_ft,                       # 4
        yes_no_map[ready_to_move],       # 5
        yes_no_map[resale],              # 6
        location_map[location],          # 7
        0                                # 8 (dummy / bias feature if used in training)
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    st.success(f"💰 Estimated House Price: ₹ {int(prediction[0])} Lakhs")





























