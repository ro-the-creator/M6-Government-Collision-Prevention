# app.py
import streamlit as st
import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib

#  style + title
st.set_page_config(page_title="Government Vehicle Collision Injury/Death Predictor", page_icon="🚓", layout="centered")
st.title("Government Vehicle Collisions: Injury/Death Prediction Model", text_alignment='center')


st.image('dcas.png')

#text1 = '''
#        In some cases, we can find that there is an increase vehicle collisions resulting injury/death when there 
#        is a government vehicle involved. Our model aims to find the implications of these issues, as to help the Department of
#        Citywide Administrative Services (DCAS) better locate where government employee training is failing.
#'''
#st.markdown(text1, text_alignment='center')

md1 = st.subheader(':blue[**Adjust the features on the left to see the likelihood of government vehicle collisions causing injury/death ⬅️**]', text_alignment='center')

# caches, model + pipeline

@st.cache_data
def load_data():
    model = joblib.load('collisions_model.pkl')
    var_cols = ['is_government', 'boroname_Brooklyn', 'boroname_Manhattan',	'boroname_Queens', 'boroname_Staten Island', 'season_Spring', 'season_Summer', 'season_Winter']
    return model, var_cols

#@st.cache_resource
#def train_model(df: pd.DataFrame):
 #   X = df[['is_government', 'boroname_Brooklyn', 'boroname_Manhattan',	'boroname_Queens', 'boroname_Staten Island', 'season_Spring', 'season_Summer', 'season_Winter']]
  #  y = df['total_injury_death_flag']
   # x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.7, test_size=0.3, stratify=y, random_state=42)
    #model = LogisticRegression(class_weight='balanced', multi_class='auto')
    #model.fit(x_train, y_train)

    #ranges ={}
    #classes = pipe.classes_.tolist()
    #return pipe, ranges, classes

# since model is loaded from .pkl, I don't believe @st.cache_resource is needed?


# load model
model, var_cols = load_data()


# selector for categorical variables

categories1 = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
categories2 = ['Winter', 'Spring', 'Summer', 'Fall']

with st.sidebar:
    # Boroughs
    st.header("Features")
    boro = st.selectbox(
        'Select Borough(s)',
        categories1
    )
    # Seasons
    szn = st.select_slider(
        'Select Season(s)',
        categories2
    )
    # Government Vehicles
    on = st.toggle(
        'Government Vehicles'
    )
    prediction_btn = st.button('Predict')

# displaying preds
if prediction_btn:
        
        # dummies
        X_dict = {
        'is_government': int(on),
        'boroname_Brooklyn': 0,
        'boroname_Manhattan': 0,
        'boroname_Queens': 0,
        'boroname_Staten Island': 0,
        'season_Spring': 0,
        'season_Summer': 0,
        'season_Winter': 0
        }
        # dropped Bronx
        if boro != 'Bronx':
             X_dict[f'boroname_{boro}'] = 1
        # dropped Fall
        if szn != 'Fall':
             X_dict[f'season_{szn}'] = 1

        # inputs new and preds + proba
        X_new = pd.DataFrame([X_dict])[var_cols]
        pred = model.predict(X_new)[0]
        proba = model.predict_proba(X_new)[0]
        risk = proba[1] * 100

        st.write(f'Probability of Injury/Death: **{risk:.2f}%**')

        if pred == 1:
            st.error('⚠️ Injury/Death is Likely ⚠️')
        else:
             st.success('😪 Injury/Death Unlikely 😅')