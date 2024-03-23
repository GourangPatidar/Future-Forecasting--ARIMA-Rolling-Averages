import streamlit as st
from scipy.stats import norm
import numpy as np

def perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level):
    # Calculate conversion rates
    control_conversion_rate = control_conversions / control_visitors
    treatment_conversion_rate = treatment_conversions / treatment_visitors
    
    # Calculate pooled probability
    pooled_prob = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    
    # Calculate pooled standard error
    pooled_se = np.sqrt(pooled_prob * (1 - pooled_prob) * (1 / control_visitors + 1 / treatment_visitors))
    
    # Calculate z-score based on confidence level
    if confidence_level == 90:
        z_score = norm.ppf(0.95)
    elif confidence_level == 95:
        z_score = norm.ppf(0.975)
    elif confidence_level == 99:
        z_score = norm.ppf(0.995)
    else:
        raise ValueError("Confidence level must be one of 90, 95, or 99.")
    
    # Calculate margin of error
    margin_of_error = z_score * pooled_se
    
    # Calculate the difference in conversion rates
    diff_conversion_rate = treatment_conversion_rate - control_conversion_rate
    
    # Perform hypothesis testing
    if diff_conversion_rate > margin_of_error:
        return "Experiment Group is Better"
    elif diff_conversion_rate < -margin_of_error:
        return "Control Group is Better"
    else:
        return "Indeterminate"

# Streamlit app
st.title('A/B Test Hypothesis Testing App')

control_visitors = st.slider('Enter Control Group Visitors:', min_value=1)
control_conversions = st.slider('Enter Control Group Conversions:', min_value=0)
treatment_visitors = st.slider('Enter Treatment Group Visitors:', min_value=1)
treatment_conversions = st.slider('Enter Treatment Group Conversions:', min_value=0)
confidence_level = st.selectbox('Select Confidence Level:', [90, 95, 99])

if st.button('Perform Hypothesis Test'):
    result = perform_ab_test(control_visitors, control_conversions, treatment_visitors, treatment_conversions, confidence_level)
    st.write(f'Result of A/B test: {result}')