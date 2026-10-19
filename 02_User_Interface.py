import joblib
import pandas as pd
import streamlit as st

# Load the trained model
model = joblib.load("05 Car Price/car_price_model.joblib")

st.set_page_config(page_title="Car Price Prediction", page_icon="🚗")

st.title("🚗 Car Price Prediction")
st.markdown("Predict your car's price using Machine Learning!")

st.subheader("Enter Car Details")

# Categorical inputs
symboling = st.selectbox("Symboling", [-2, -1, 0, 1, 2, 3])

fueltype = st.selectbox("Fuel Type", ["diesel", "gas"])
aspiration = st.selectbox("Aspiration", ["std", "turbo"])
doornumber = st.selectbox("Number of Doors", ["four", "two"])

carbody = st.selectbox(
    "Car Body",
    ["convertible", "hardtop", "hatchback", "sedan", "wagon"]
)

drivewheel = st.selectbox("Drive Wheel", ["4wd", "fwd", "rwd"])
enginelocation = st.selectbox("Engine Location", ["front", "rear"])

enginetype = st.selectbox(
    "Engine Type",
    ["dohc", "dohcv", "l", "ohc", "ohcf", "ohcv", "rotor"]
)

cylindernumber = st.selectbox(
    "Number of Cylinders",
    ["eight", "five", "four", "six", "three", "twelve", "two"]
)

fuelsystem = st.selectbox(
    "Fuel System",
    ["1bbl", "2bbl", "4bbl", "idi", "mpfi", "spdi", "spfi"]
)

# Numerical inputs
wheelbase = st.number_input("Wheelbase", min_value=0.0, value=95.0)
carlength = st.number_input("Car Length", min_value=0.0, value=170.0)
carwidth = st.number_input("Car Width", min_value=0.0, value=65.0)
carheight = st.number_input("Car Height", min_value=0.0, value=53.0)
curbweight = st.number_input("Curb Weight", min_value=0.0, value=2500.0)

enginesize = st.number_input("Engine Size", min_value=0.0, value=120.0)
boreratio = st.number_input("Bore Ratio", min_value=0.0, value=3.0)
stroke = st.number_input("Stroke", min_value=0.0, value=3.0)
compressionratio = st.number_input("Compression Ratio", min_value=0.0, value=9.0)
horsepower = st.number_input("Horsepower", min_value=0.0, value=100.0)
peakrpm = st.number_input("Peak RPM", min_value=0.0, value=5000.0)
citympg = st.number_input("City MPG", min_value=0.0, value=25.0)
highwaympg = st.number_input("Highway MPG", min_value=0.0, value=30.0)

# Encode categorical values
encoding_maps = {
    "fueltype": {"diesel": 0, "gas": 1},
    "aspiration": {"std": 0, "turbo": 1},
    "doornumber": {"four": 0, "two": 1},
    "carbody": {
        "convertible": 0, "hardtop": 1, "hatchback": 2,
        "sedan": 3, "wagon": 4
    },
    "drivewheel": {"4wd": 0, "fwd": 1, "rwd": 2},
    "enginelocation": {"front": 0, "rear": 1},
    "enginetype": {
        "dohc": 0, "dohcv": 1, "l": 2, "ohc": 3,
        "ohcf": 4, "ohcv": 5, "rotor": 6
    },
    "cylindernumber": {
        "eight": 0, "five": 1, "four": 2, "six": 3,
        "three": 4, "twelve": 5, "two": 6
    },
    "fuelsystem": {
        "1bbl": 0, "2bbl": 1, "4bbl": 2, "idi": 3,
        "mpfi": 4, "spdi": 5, "spfi": 6
    }
}

if st.button("Predict Car Price 🚘"):

    input_data = pd.DataFrame([{
        "symboling": symboling,
        "fueltype": encoding_maps["fueltype"][fueltype],
        "aspiration": encoding_maps["aspiration"][aspiration],
        "doornumber": encoding_maps["doornumber"][doornumber],
        "carbody": encoding_maps["carbody"][carbody],
        "drivewheel": encoding_maps["drivewheel"][drivewheel],
        "enginelocation": encoding_maps["enginelocation"][enginelocation],
        "wheelbase": wheelbase,
        "carlength": carlength,
        "carwidth": carwidth,
        "carheight": carheight,
        "curbweight": curbweight,
        "enginetype": encoding_maps["enginetype"][enginetype],
        "cylindernumber": encoding_maps["cylindernumber"][cylindernumber],
        "enginesize": enginesize,
        "fuelsystem": encoding_maps["fuelsystem"][fuelsystem],
        "boreratio": boreratio,
        "stroke": stroke,
        "compressionratio": compressionratio,
        "horsepower": horsepower,
        "peakrpm": peakrpm,
        "citympg": citympg,
        "highwaympg": highwaympg
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Car Price: {prediction[0]:,.2f}")





# py -m streamlit run "C:\Users\Jay Mankotia\Desktop\AI ML\05 Car Price\02_User_Interface.py"
# s1 e6 not a stranger 28min






# 'symboling', 'fueltype', 'aspiration', 'doornumber',
# 'carbody', 'drivewheel', 'enginelocation', 'wheelbase', 'carlength',
# 'carwidth', 'carheight', 'curbweight', 'enginetype', 'cylindernumber',
# 'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio',
# 'horsepower', 'peakrpm', 'citympg', 'highwaympg', 