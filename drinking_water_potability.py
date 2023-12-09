import streamlit as st
import pandas as pd
# load Model
from keras.models import load_model
model = load_model('example_model.h5')

# สร้างฟังก์ชันสำหรับทำนาย
def predict_water_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    # สร้าง DataFrame จากข้อมูลที่รับมา
    data = {
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
    }
    df = pd.DataFrame(data)

    # ทำนาย
    prediction = model.predict(df)

    # แสดงผลลัพธ์
    return prediction[0][0]

# สร้างแอป Streamlit
def main():
    st.title("Water Potability Prediction")

    # รับค่าจากผู้ใช้
    ph = st.slider("pH", 0.0, 14.0, 7.0)
    hardness = st.slider("Hardness", 0, 500, 250)
    solids = st.slider("Solids", 0, 5000, 2500)
    chloramines = st.slider("Chloramines", 0.0, 10.0, 5.0)
    sulfate = st.slider("Sulfate", 0.0, 500.0, 250.0)
    conductivity = st.slider("Conductivity", 0.0, 1000.0, 500.0)
    organic_carbon = st.slider("Organic Carbon", 0.0, 50.0, 25.0)
    trihalomethanes = st.slider("Trihalomethanes", 0.0, 150.0, 75.0)
    turbidity = st.slider("Turbidity", 0.0, 10.0, 5.0)

    # ทำนาย
    if st.button("Predict"):
        data = {
        'ph': [ph],
        'Hardness': [hardness],
        'Solids': [solids],
        'Chloramines': [chloramines],
        'Sulfate': [sulfate],
        'Conductivity': [conductivity],
        'Organic_carbon': [organic_carbon],
        'Trihalomethanes': [trihalomethanes],
        'Turbidity': [turbidity]
        }
        df = pd.DataFrame(data)

        # ทำนาย
        prediction = model.predict(df)
        st.success(f"The predicted water potability is: {prediction[0][0]}")

# เรียกใช้ฟังก์ชัน main()
if __name__ == "__main__":
    main()