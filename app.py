import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fashion Store Dashboard", layout="wide")
st.title("👗Fashion Store Analytics Dashhboard")

data = {
  "Product": ["Shirt", "T-shirt", "Jacket", "Shoes", "Watch", "Handbag"],
  "Price": [1000, 600, 1500, 2000, 1200, 2500],
  "Cost": [600, 300, 800, 1000, 700, 1300]
}

df = pd.DataFrame(data)
df["Profit"] = df["Price"] - df["Cost"]

st.subheader("Product Data")
st.dataframe(df)

st.subheader("Profit Chart")
fig = px.bar(df, x="Product", y="Profit", color="Product", title="Profit by Product")
st.plotly_chart(fig)
