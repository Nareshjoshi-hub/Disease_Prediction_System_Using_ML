import streamlit as st
import pickle
import pandas as pd
import pickle
from streamlit_option_menu import option_menu
import warnings
warnings.filterwarnings("ignore")

# Load the saved model
with open('heart_disease_model.pkll', 'rb') as f:
    heart_disease_model = pickle.load(f)
with open('Lung_disease_model.pkl', 'rb') as f:
    lung_disease_model = pickle.load(f)
with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

# Get text input from the user
# text_input = st.text_input("Enter a category:", "")

# # Use the loaded LabelEncoder to transform text input into numeric format
# if text_input:
#     transformed_input = label_encoder.transform([text_input])[0]
#     st.write("Transformed input:", transformed_input)


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Heart Disease Prediction',
                           'Lung Disease Prediction',
                           ],
                          icons=['heart','activity'],
                          default_index=0)
    
 # Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age',value=None)
        
    with col2:
        sex = st.number_input('Sex 1=Male,0=Female',value=None)
        
    with col3:
        cp = st.number_input('Chest Pain types',value=None)
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure',value=None)
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl',value=None)
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',value=None)
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',value=None)
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',value=None)
        
    with col3:
        exang = st.number_input('Exercise Induced Angina',value=None)
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',value=None)
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',value=None)
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',value=None)
        
    with col1:
        thal = st.number_input('thal: 1 = normal; 2 = fixed defect; 3 = reversable defect',value=None)
        
        
     
     
    # code for Prediction
    heart_diagnosis =''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)

# Lung Disease Prediction Page
if (selected == 'Lung Disease Prediction'):

     # page title
     st.title('Lung Disease Prediction using ML')

     col1, col2, col3 = st.columns(3)

     with col1:
         GENDER = st.number_input('Gender 1=Male,0=Female',value=None)

     with col2:
         AGE = st.number_input('Age ,Enter your age',value=None)

     with col3:
         SMOKING = st.number_input('Smoking 1=Non Smoker 2=Smoker ',value=None)

     with col1:
         YELLOW_FINGERS = st.number_input('Yellow_Fingers YES=2 , NO=1',value=None)

     with col2:
         ANXIETY = st.number_input('Anxiety YES=2 , NO=1',value=None)

     with col3:
         PEER_PRESSURE = st.number_input('Peer Pressure YES=2 , NO=1',value=None)

     with col1:
         CHRONIC_DISEASE = st.number_input('Chronic Disease YES=2 , NO=1',value=None)

     with col2:
         FATIGUE = st.number_input('Fatigue YES=2 , NO=1',value=None)

     with col3:
         ALLERGY = st.number_input('Allergy YES=2 , NO=1',value=None)

     with col1:
         WHEEZING = st.number_input('Wheezing YES=2 , NO=1',value=None)

     with col2:
         ALCOHOL_CONSUMING = st.number_input('Alcohol Consuming YES=2 , NO=1',value=None)

     with col3:
         COUGHING = st.number_input('Coughing YES=2 , NO=1',value=None)

     with col1:
         SHORTNESS_OF_BREATH = st.number_input('Shortness Of Breath YES=2 , NO=1',value=None)
     with col2:
         SWALLOWING_DIFFICULTY=st.number_input('Swallowing difficulty YES=2 , NO=1',value=None)
     with col3:
         CHEST_PAIN=st.number_input('Chest pain YES=2 , NO=1',value=None)    


     # code for Prediction
     lung_diagnosis =''

     # creating a button for Prediction

     if st.button('Lung Disease Test Result'):
         lung_prediction = lung_disease_model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,	COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,	CHEST_PAIN]])                          

         if (lung_prediction[0] == 1):
           lung_diagnosis = 'The person is having lung disease'
         else:
           lung_diagnosis = 'The person does not have any lung disease'

     st.success(lung_diagnosis) 
