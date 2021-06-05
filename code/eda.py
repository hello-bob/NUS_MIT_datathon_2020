import pandas as pd
import numpy as np
import glob
import os
from pandas_profiling import ProfileReport
import sqlalchemy

os.getcwd()
#wd =
#os.chdir(wd)

"""MIMIC_IV"""
# Loading data + EDA pipeline
cols_to_use = ['subject_id', 'hadm_id', 'admittime', 'dischtime', 'deathtime',
       'admission_type', 'admission_location', 'discharge_location',
       'insurance', 'language', 'marital_status', 'ethnicity', 'edregtime',
       'edouttime', 'hospital_expire_flag', 'gender', 'stay_id', 'intime',
       'outtime', 'los', 'age', 'inpatient_stroke', 'min_mbp', 'max_mbp', 'avg_mbp', 'min_sbp', 'max_sbp', 'avg_sbp',
       'first_gcs', 'last_gcs', 'gcs_change',
       'afib', 'hyperlipidemia', 'diabetes', 'hypertension', 'cor_art_d',
       'peri_vasc_d', 'car_art_stent', 'smoking', 'tia', 'heparin_iv',
       'antihypertensive_iv_non_tight_control',
       'antihypertensive_iv_tight_control', 'inotropes', 'antiplatelets', 'anticoag',
       'antihypertensive_non_iv', 'first_glu', 'first_cre']

### Time from ICU admission --> discharge: intime - dischtime

mimic_iv_df_url = '/Users/hydraze/Documents/MIT-NUS Datathon/data/final_raw/mimic_clean_v2.csv'
df = pd.read_csv(mimic_iv_df_url, usecols=cols_to_use)
df_to_analyse = df[['subject_id', 'hadm_id',
       'admission_type', 'admission_location', 'discharge_location',
       'marital_status', 'ethnicity', 'hospital_expire_flag', 'gender', 'stay_id',
       'los', 'age', 'inpatient_stroke', 'min_mbp', 'max_mbp', 'avg_mbp', 'min_sbp', 'max_sbp', 'avg_sbp',
       'first_gcs', 'last_gcs', 'gcs_change',
       'afib', 'hyperlipidemia', 'diabetes', 'hypertension', 'cor_art_d',
       'peri_vasc_d', 'car_art_stent', 'smoking', 'tia', 'heparin_iv',
       'antihypertensive_iv_non_tight_control',
       'antihypertensive_iv_tight_control', 'inotropes', 'antiplatelets', 'anticoag',
       'antihypertensive_non_iv', 'first_glu', 'first_cre'

]].copy()
df_to_analyse.info()


#binary = ['afib', 'hyperlipidemia', 'diabetes', 'hypertension', 'cor_art_d',
#       'peri_vasc_d', 'car_art_stent', 'smoking', 'tia', 'heparin_iv',
#       'antihypertensive_iv_non_tight_control',
#       'antihypertensive_iv_tight_control', 'inotropes', 'antiplatelets', 'anticoag',
#       'antihypertensive_non_iv']

#for binary_var in binary:
#       df_to_analyse[binary_var] = np.where(df_to_analyse[binary_var]>0, 1, 0)

### Some minor cleaning

profile = ProfileReport(df_to_analyse, title="Pandas Profiling Report", explorative=True)
profile.to_file("MIMIC_IV.html")

"""eICU"""
# Loading df to EDA
eICU_df_url = '/Users/hydraze/Documents/MIT-NUS Datathon/data/final_raw/eicu_clean_v3.csv'
cols_to_use = ['patientunitstayid', 'patienthealthsystemstayid', 'gender', 'age',
       'ethnicity', 'apacheadmissiondx',
       'admissionheight', 'hospitaladmittime24', 'hospitaladmitoffset',
       'hospitaladmitsource', 'hospitaldischargeyear',
       'hospitaldischargetime24', 'hospitaldischargeoffset',
       'hospitaldischargelocation', 'hospitaldischargestatus', 'unittype',
       'unitadmittime24', 'unitdischargetime24',
       'unitdischargeoffset', 'unitdischargelocation', 'unitdischargestatus',
       'uniquepid', 'hosp_mortality', 'icu_los_hours', 'is_primary',
       'correct_age', 'min_nibp', 'max_nibp', 'avg_nibp', 'min_ibp', 'max_ibp',
       'avg_ibp', 'min_nibp_systolic', 'max_nibp_systolic',
       'avg_nibp_systolic', 'min_ibp_systolic', 'max_ibp_systolic',
       'avg_ibp_systolic', 'glucose',
       'creatinine', 'first_gcs', 'last_gcs',
       'antihypertensive_iv_tight_control',
       'antihypertensive_iv_non_tight_control', 'heparin_iv', 'inotropes',
       'antiplatelets', 'anticoag', 'antihypertensive_non_iv', 'hypertension',
       'ischemic_heart_disease', 'peripheral_vascular_disease',
       'atrial_fibrillation', 'transient_ischemic_attack', 'previous_stroke',
       'diabetes']

df = pd.read_csv(eICU_df_url, usecols=cols_to_use)
df.columns
df.info()
len(df['patientunitstayid'].unique())
#
df_to_analyse = df[['patientunitstayid', 'gender', 'age',
       'ethnicity',
       'hospitaldischargelocation', 'hospitaldischargestatus', 'unittype',
       'icu_los_hours', 'is_primary',
       'min_nibp', 'max_nibp', 'avg_nibp', 'min_ibp', 'max_ibp', 'avg_ibp',
       'min_nibp_systolic', 'max_nibp_systolic', 'avg_nibp_systolic',
       'min_ibp_systolic', 'max_ibp_systolic', 'avg_ibp_systolic', 'glucose', 'creatinine', 'gcs',
       'antihypertensive_iv_tight_control', 'antihypertensive_iv_non_tight_control', 'heparin_iv', 'inotropes',
       'antiplatelets', 'anticoag', 'antihypertensive_non_iv', 'hypertension',
       'ischemic_heart_disease', 'peripheral_vascular_disease', 'atrial_fibrillation',
       'transient_ischemic_attack', 'previous_stroke', 'diabetes', 'hosp_mortality'
]].copy()

df_to_analyse
profile = ProfileReport(df_to_analyse, title="Pandas Profiling Report", explorative=True)
profile.to_file("eICU.html")


###


