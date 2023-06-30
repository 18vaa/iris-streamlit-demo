#%%
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
# %%

st.title("Iris Dataset Flower Classification")
st.markdown("UI for classifying flowers into setosa, versicolor, virginica")

# %%
st.header("Plant Features")
col1, col2 = st.columns(2)
with col1:
    st.text("Sepal Characteristics")
    sepal_l = st.slider("Sepal Length (cm)", 1.0, 0.8, 0.5)
    sepal_w = st.slider("Sepal Width (cm)",2.0,4.4,0.5)

with col2:
    st.text("Petal Characteristics")
    petal_l = st.slider("Petal Length (cm)", 1.0, 7.0, 0.5)
    # petal_w = st.slider("Petal Width (cm)",0.1,2.5,0.5)

# %%
if st.button("Predict type of Iris"):
    result = predict(np.array([[sepal_l, sepal_w, petal_l]]))
    st.text(result[0])