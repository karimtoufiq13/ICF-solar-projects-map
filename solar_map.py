import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Set Streamlit config
st.set_page_config(page_title="Solar One Analytics Map", layout="wide")
st.title("Solar PV Projects Map – Solar One Analytics")

# Load data
data_path =  r"C:\Users\ktouf\Desktop\In Construction and Complete Solar PV Projects 1_7_25 (1).xlsx"
df = pd.read_excel(data_path)

# Rename columns for easier access
df.columns = df.columns.str.strip()
df = df.dropna(subset=["Latitude", "Longitude"])

# Define color function
def get_market_color(status):
    if status == "Complete":
        return "green"
    elif status == "In Construction":
        return "orange"
    else:
        return "blue"

# Create folium map
m = folium.Map(location=[40.7128, -74.0060], zoom_start=11)

# Add markers with popup details and colored pins
for _, row in df.iterrows():
    color = get_market_color(row["Project Status"])
    folium.Marker(
        location=[row["Latitude"], row["Longitude"]],
        popup=folium.Popup(
            f"<b>{row['Project Name']}</b><br>Status: {row['Project Status']}<br>Address: {row['Address']}", max_width=300),
        icon=folium.Icon(color=color)
    ).add_to(m)

# Show map in Streamlit
st_folium(m, width=1100, height=600)