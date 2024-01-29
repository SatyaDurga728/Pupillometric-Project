# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 20:32:04 2023

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('C:/Users/DELL/Downloads/durga/pages/trained_model.sav', 'rb'))

# creating a function for Prediction

def prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    predic= loaded_model.predict(input_data_reshaped)
    print(predic)

    if (predic[0] == "Mitochondrial genetic inheritance disorders"): 
        return 'The person has a Mitochondrial genetic inheritance disorders'
    elif(prediction[0] =="Single-gene inheritance diseases" ):
        return 'The person has a Single-gene inheritance diseases'
    elif(predic[0] == "Mitifactorial genetic inheritance disorders"): 
        return 'The person has a Mitifactorial genetic inheritance disorders'
    else:
        return 'The person doesnot have a genetic disease'
    
  
def main():
    
    
    # giving a title
    st.title('Prediction Genetic Retinal Disease')
    
    
    # getting the input data from the user
    

    Patient_Age = st.number_input(label="Patient Age",max_value=14,min_value=0,help="Enter age in between 0 to 14")
    Gene_mother_side= st.number_input(label='Genes in mother side',min_value=0,max_value=1,help="Enter 1 for Yes,0 for No")
    Inherited_from_father = st.number_input(label='Inherited_from_father',min_value=0,max_value=1,help="Enter 1 for Yes,0 for No")
    Maternal_gene= st.number_input(label='Maternal gene',min_value=0,max_value=1,help="Enter 1 for Yes,0 for No")
    Paternal_gene= st.number_input(label='Paternal gene',min_value=0,max_value=1,help="Enter 1 for Yes,0 for No")
    Blood_cell_count= st.number_input(label='Blood cell count (mcL)',min_value=4,max_value=5,help="Blood cells count is in between 4 to 5")
    Mother_age= st.number_input(label='Mother age',max_value=51,min_value=18,help="Enter age in between 18 to 51")
    Father_age = st.number_input(label='Father age',max_value=64,min_value=20,help="Enter age in between 20 to 64")
    Status= st.number_input(label='Status',help="Enter 1 for Alive, 0 for Deceased",min_value=0,max_value=1)
    RespiratoryRate= st.number_input(label='Respiratory Rate (breaths/min)',help="Enter 1 for Tachypnea,0 for Normal",min_value=0,max_value=1)
    HeartRate= st.number_input(label='Heart Rate (rates/min)',help="Enter 1 for Tachycardia,0 for Normal",min_value=0,max_value=1)
    Parental_consent= st.number_input(label='Parental consent',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    Follow_up= st.number_input(label='Follow-up',help="Enter 1 for High, 0 for Low",min_value=0,max_value=1)
    Gender=st.number_input(label='Gender',help="Enter 1 for Ambiguous,0 for Male,2 for Female",min_value=0,max_value=2)
    Birth_asphyxia=st.number_input(label='Birth asphyxia',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    Autopsy_shows_birth_defect=st.number_input(label='Autopsy shows birth defect (if applicable)',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    Folic_acid_details=st.number_input(label='Folic acid details (peri-conceptional)',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    H_or_O_serious_maternal_illness=st.number_input(label='H/O serious maternal illness',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    H_or_O_radiation_exposure_xRay=st.number_input(label='H/O radiation exposure (x-ray)',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    H_or_O_substance_abuse=st.number_input(label='H/O substance abuse',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    Assisted_conception_IVF_or_ART=st.number_input(label='Assisted conception IVF/ART',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    History_of_anomalies_in_previous_pregnancies=st.number_input(label='History of anomalies in previous pregnancies',help="Enter 1 for Yes, 0 for No",min_value=0,max_value=1)
    Number_of_previous_abortion=st.number_input(label='No. of previous abortion',help="In between 0 to 4",min_value=0,max_value=4)
    Birth_defects=st.number_input(label='Birth defects',help="Enter 1 for Single, 0 for Multiple",min_value=0,max_value=1)
    White_Blood_cell_count=st.number_input(label='White Blood cell count (thousand per microliter)',min_value=3,max_value=12,help="Blood cells count is in between 3 to 12")
    Blood_test=st.number_input(label='Blood test result',max_value=3,min_value=0,help="Enter 1 for Anormal, 0 for Normal,2 for inconclusive,3 for slightly abnormal")
    Symptom1=st.number_input(label='Symptom 1',min_value=0,max_value=1,help="Enter 1 for Yes, 0 for No")
    Symptom2=st.number_input(label='Symptom 2',min_value=0,max_value=1,help="Enter 1 for Yes, 0 for No")
    pupil_size=st.number_input(label='pupil_size',help="In between 0 to 4",min_value=0,max_value=4)
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Retinal Test Result'):
        diagnosis = prediction([Patient_Age,Gene_mother_side,Inherited_from_father,Maternal_gene,Paternal_gene,Blood_cell_count,Mother_age,Father_age,Status,RespiratoryRate,HeartRate,Parental_consent,Follow_up,Gender,Birth_asphyxia,Autopsy_shows_birth_defect,Folic_acid_details,H_or_O_serious_maternal_illness,H_or_O_radiation_exposure_xRay,H_or_O_substance_abuse,Assisted_conception_IVF_or_ART,History_of_anomalies_in_previous_pregnancies,Number_of_previous_abortion,Birth_defects,White_Blood_cell_count,Blood_test,Symptom1,Symptom2,pupil_size])
        
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
    