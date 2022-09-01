import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/diabetes_model.sav","rb",))
heart_disease_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/heart_disease_model.sav","rb",))
parkinsons_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/parkinsons_model.sav","rb",))
cancer_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/cancer_model.sav","rb",))
obesity_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/obesity_model.sav","rb",))
pressure_model = pickle.load(open("C:/Users/shaddad_tech/Desktop/Multiple Disease Prediction System/Saved models/pressure_model.sav","rb",))


# sidebar for navigation
with st.sidebar:

    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Prediction",
            "Lung Cancer Prediction",
            "Obesity Prediction",'Blood Pressure Prediction',
        ],
        icons=["activity", "heart", "person", "bandaid", "person-plus",'emoji-angry'],
        default_index=0,
    )
# Diabetes Prediction Page
if selected == "Diabetes Prediction":

    # page title
    st.title("Diabetes Prediction using ML")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies", step = 1, min_value = 0)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value = 0.00)
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value(mm Hg)", min_value = 0.00)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value = 0.00)
    with col2:
        Insulin = st.number_input("Insulin level (mu U/ml)", min_value = 0.00)
    with col3:
        BMI = st.number_input("BMI(weight in kg/(height in m)^2", min_value = 0.00)
    with col1:
        DiabetesPedigreeFunction = st.number_input(
            "Diabetes Pedigree Function value", format="%g", min_value = 0.00
        )
    with col2:
        Age = st.number_input("Age of the Person", min_value = 0.00)
    # code for Prediction
    # creating a button for Prediction

    if st.button("Diabetes Test Result"):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if diab_prediction[0] == 1:
            st.error("The person is Diabetic")
        else:
            st.success("The person is not Diabetic")
# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":

    # page title
    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value = 0.00)
    with col2:
        sex = st.selectbox("Sex (Male=1 / Female=0)", (0,1))
    with col3:
        cp = st.number_input("Chest Pain types(4 values)", min_value = 0.00)
    with col1:
        trestbps = st.number_input("Resting Blood Pressure", min_value = 0.00)
    with col2:
        chol = st.number_input("Serum Cholestoral in mg/dl", min_value = 0.00)
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120.00 mg/dl", min_value = 0.00)
    with col1:
        restecg = st.number_input("Resting Electrocardiographic results", min_value = 0.00)
    with col2:
        thalach = st.number_input("Maximum Heart Rate achieved", min_value = 0.00)
    with col3:
        exang = st.number_input("Exercise Induced Angina", min_value = 0.00)
    with col1:
        oldpeak = st.number_input("ST depression induced by exercise", min_value = 0.00)
    with col2:
        slope = st.number_input("Slope of the peak exercise ST segment", min_value = 0.00)
    with col3:
        ca = st.number_input("Number of major vessels (0-3)", min_value = 0.00)
    with col1:
        thal = st.number_input(
            "thal: normal=0.00 / fixed defect=1 / reversable defect=2", min_value = 0.00
        )
    # code for Prediction
    # creating a button for Prediction

    if st.button("Heart Disease Test Result"):
        heart_prediction = heart_disease_model.predict(
            [
                [
                    age,
                    sex,
                    cp,
                    trestbps,
                    chol,
                    fbs,
                    restecg,
                    thalach,
                    exang,
                    oldpeak,
                    slope,
                    ca,
                    thal,
                ]
            ]
        )

        if heart_prediction[0] == 1:
            st.error("The person has heart disease")
        else:
            st.success("The person doesn't have any heart disease")
# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", format="%g", min_value = 0.00)
    with col2:
        fhi = st.number_input("MDVP:Fhi(Hz)", format="%g", min_value = 0.00)
    with col3:
        flo = st.number_input("MDVP:Flo(Hz)", format="%g", min_value = 0.00)
    with col4:
        Jitter_percent = st.number_input("MDVP:Jitter(%)", format="%g", min_value = 0.00)
    with col1:
        Jitter_Abs = st.number_input("MDVP:Jitter(Abs)", format="%g", min_value = 0.00)
    with col2:
        RAP = st.number_input("MDVP:RAP", format="%g", min_value = 0.00)
    with col3:
        PPQ = st.number_input("MDVP:PPQ", format="%g", min_value = 0.00)
    with col4:
        DDP = st.number_input("Jitter:DDP", format="%g", min_value = 0.00)
    with col1:
        Shimmer = st.number_input("MDVP:Shimmer", format="%g", min_value = 0.00)
    with col2:
        Shimmer_dB = st.number_input("MDVP:Shimmer (dB)", format="%g", min_value = 0.00)
    with col3:
        APQ3 = st.number_input("Shimmer:APQ3", format="%g", min_value = 0.00)
    with col4:
        APQ5 = st.number_input("Shimmer:APQ5", format="%g", min_value = 0.00)
    with col1:
        APQ = st.number_input("MDVP:APQ", format="%g", min_value = 0.00)
    with col2:
        DDA = st.number_input("Shimmer:DDA", format="%g", min_value = 0.00)
    with col3:
        NHR = st.number_input("NHR", format="%g", min_value = 0.00)
    with col4:
        HNR = st.number_input("HNR", format="%g", min_value = 0.00)
    with col1:
        RPDE = st.number_input("RPDE", format="%g", min_value = 0.00)
    with col2:
        DFA = st.number_input("DFA", format="%g", min_value = 0.00)
    with col3:
        spread1 = st.number_input("Spread1", format="%g")
    with col4:
        spread2 = st.number_input("Spread2", format="%g", min_value = 0.00)
    with col1:
        D2 = st.number_input("D2", format="%g", min_value = 0.00)
    with col2:
        PPE = st.number_input("PPE", format="%g", min_value = 0.00)
    # code for Prediction
    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [
                [
                    fo,
                    fhi,
                    flo,
                    Jitter_percent,
                    Jitter_Abs,
                    RAP,
                    PPQ,
                    DDP,
                    Shimmer,
                    Shimmer_dB,
                    APQ3,
                    APQ5,
                    APQ,
                    DDA,
                    NHR,
                    HNR,
                    RPDE,
                    DFA,
                    spread1,
                    spread2,
                    D2,
                    PPE,
                ]
            ]
        )

        if parkinsons_prediction[0] == 1:
            st.error("The person has Parkinson's disease")
        else:
            st.success("The person does not have Parkinson's disease")
# Lung Cancer Prediction Page
if selected == "Lung Cancer Prediction":

    # page title
    st.title("Lung Cancer Prediction using ML")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        AGE = st.number_input("Age of the patient", min_value = 0.00)
    with col2:
        SMOKING = st.selectbox("Smoking: YES=1 , NO=0", (0, 1))
    with col3:
        YELLOW_FINGERS = st.selectbox("Yellow fingers: YES=1 , NO=0", (0, 1))
    with col1:
        ANXIETY = st.selectbox("Anxiety: YES=1 , NO=0", (0, 1))
    with col2:
        PEER_PRESSURE = st.selectbox("Peer_pressure: YES=1 , NO=0", (0, 1))
    with col3:
        CHRONIC_DISEASE = st.selectbox("Chronic Disease: YES=1 , NO=0", (0, 1))
    with col1:
        FATIGUE = st.selectbox("Fatigue: YES=1 , NO=0", (0, 1))
    with col2:
        ALLERGY = st.selectbox("Allergy: YES=1 , NO=0", (0, 1))
    with col3:
        WHEEZING = st.selectbox("Wheezing: YES=1 , NO=0", (0, 1))
    with col1:
        ALCOHOL_CONSUMING = st.selectbox("Alcohol: YES=1 , NO=0", (0, 1))
    with col2:
        COUGHING = st.selectbox("Coughing: YES=1 , NO=0", (0, 1))
    with col3:
        SHORTNESS_OF_BREATH = st.selectbox("Shortness of Breath: YES=1 , NO=0", (0, 1))
    with col1:
        SWALLOWING_DIFFICULTY = st.selectbox(
            "Swallowing Difficulty: YES=1 , NO=0", (0, 1)
        )
    with col2:
        CHEST_PAIN = st.selectbox("Chest pain: YES=1 , NO=0", (0, 1))
    # code for Prediction
    # creating a button for Prediction

    if st.button("Lung Cancer Test Result"):
        cancer_prediction = cancer_model.predict(
            [
                [
                    AGE,
                    SMOKING,
                    YELLOW_FINGERS,
                    ANXIETY,
                    PEER_PRESSURE,
                    CHRONIC_DISEASE,
                    FATIGUE,
                    ALLERGY,
                    WHEEZING,
                    ALCOHOL_CONSUMING,
                    COUGHING,
                    SHORTNESS_OF_BREATH,
                    SWALLOWING_DIFFICULTY,
                    CHEST_PAIN,
                ]
            ]
        )

        if cancer_prediction[0] == 1:
            st.error("The person has Lung Cancer")
        else:
            st.success("The person doesn't have Lung Cancer")
# Obesity Prediction Page
if selected == "Obesity Prediction":


    # page title
    st.title("Obesity Prediction using ML")

    # getting the input data from the user
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender (Female = 0 / Male = 1)", (0, 1))
    with col2:
        age = st.number_input("Age", min_value = 0.00)
    with col1:
        height = st.number_input("Height (m)", min_value = 0.00)
    with col2:
        weight = st.number_input("Weight (kg)", min_value = 0.00)
    with col1:
        family_history_with_overweight = st.selectbox(
            "Family history with overwight: (Yes=1/No=0)", (0,1)
        )
    with col2:
        caloric_food = st.selectbox(
            "Consumption of high caloric food: (Yes=1/No=0)", (0,1)
        )
    with col1:
        vegetables = st.number_input(
            "Frequency of consumption of vegetables: (1, 2 or 3)", min_value = 0.00
        )
    with col2:
        number_meals = st.number_input(
            "Number of main meals: ", step = 1 , min_value = 0
        )
    with col1:
        food_between_meals = st.number_input(
            "Food between meals frequancy : (1, 2, 3 or 4)", min_value = 0.00
        )
    with col2:
        smoke = st.selectbox("Smoking: (Yes=1/No=0)", (0, 1))
    with col1:
        water = st.number_input("Consumption of water daily: (1, 2 or 3)", min_value = 0.00)
    with col2:
        calories = st.selectbox("Calories consumption monitoring: (Yes=1/No=0)", (0, 1))
    with col1:
        activity = st.number_input(
            "Physical activity frequency: (0, 1, 2 or 3)", min_value = 0.00
        )
    with col2:
        tech0logy = st.number_input(
            "Time using technology devices: (0, 1 or 2)", min_value = 0.00
        )
    with col1:
        alcohol = st.number_input(
            "Consumption of alcohol frequency: (0, 1, 2 or 3)", min_value = 0.00
        )
    # code for Prediction
    # creating a button for Prediction

    if st.button("Obesity Test Result"):
        obesity_prediction = obesity_model.predict(
            [
                [
                    gender,
                    age,
                    height,
                    weight,
                    family_history_with_overweight,
                    caloric_food,
                    vegetables,
                    number_meals,
                    food_between_meals,
                    smoke,
                    water,
                    calories,
                    activity,
                    tech0logy,
                    alcohol,
                ]
            ]
        )

        if obesity_prediction[0] == 1:
            st.success("Insufficient_Weight")
        elif obesity_prediction[0] == 2:
            st.success("Normal_Weight")
        elif obesity_prediction[0] == 3:
            st.success("Overweight_Level_I")
        elif obesity_prediction[0] == 4:
            st.success("Overweight_Level_II")
        elif obesity_prediction[0] == 5:
            st.error("Obesity_Type_I")
        elif obesity_prediction[0] == 6:
            st.error("Obesity_Type_II")
        elif obesity_prediction[0] == 7:
            st.error("Obesity_Type_III")
# Blood Pressure Prediction
if selected == "Blood Pressure Prediction":

    # page title
    st.title("Blood Pressure Prediction using ML")

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input("Age of the person", min_value = 0.00)
    with col2:
        Obese = st.selectbox("Obtisity (Yes=1 / No=0)",(0,1))
    with col3:
        bmi = st.number_input("Body mass index (BMI)", min_value = 0.00)
    with col1:
        wc = st.number_input("Waist (WC)", min_value = 0.00)
    with col2:
        hc = st.number_input("Hip Circumference (HC)", min_value = 0.00)
    with col3:
        whr = st.number_input("Waist hip ratio (WHR)", min_value = 0.00)
    with col1:
        SBP = st.number_input("Systolic blood pressure (SBP)", min_value = 0.00)
    with col2:
        DBP = st.number_input("Diastolic Blood Pressure (DBP)", min_value = 0.00)
    # code for Prediction
    # creating a button for Prediction


    if st.button("Blood Pressure Test Result"):
        pressure_prediction = pressure_model.predict([[Age,Obese,bmi,wc,hc,whr,SBP,DBP]])

        if pressure_prediction[0] == 1:
            st.error("The person has a Hyper Blood Pressure")
        else:
            st.success("The person has a regular Blood Pressure")
















