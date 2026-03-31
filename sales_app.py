import streamlit as st
import pandas as pd

data = {
    "Product": ["Laptop", "Phone", "Mouse", "Headphones", "Monitor"],
    "Category": ["Electronics", "Electronics", "Accessories", "Accessories", "Electronics"],
    "Sales": [1200, 800, 600, 150, 400]
}

df = pd.DataFrame(data)

st.title("Sales Summary")
st.subheader("This app contain sales summary")

# category_filter = st.selectbox("Select a Category:",  options=["Electronics", "Accessories"])
#filtered_df = df[df["Category"] == category_filter]

st.sidebar.title("Filters")
st.sidebar.markdown("---")

category_filter = st.sidebar.selectbox("Select a Category:",  options=["Electronics", "Accessories"])
filtered_df = df[df["Category"] == category_filter]

st.dataframe(filtered_df)
st.line_chart(filtered_df.set_index("Product")["Sales"])