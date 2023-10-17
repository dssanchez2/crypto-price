import streamlit as st
import requests

# Define the CoinGecko API URL
base_url = "https://api.coingecko.com/api/v3"

# Create a Streamlit web app
st.title("Cryptocurrency Data App")

# Allow users to select a cryptocurrency
crypto_id = st.selectbox("Select a cryptocurrency:", ["bitcoin", "ethereum", "dogecoin", "hex",'tether'])

# Define the API endpoint for cryptocurrency data
crypto_endpoint = f"{base_url}/simple/price"
params = {
    "ids": crypto_id,
    "vs_currencies": "usd",
}

# Fetch data from the CoinGecko API
response = requests.get(crypto_endpoint, params=params)

if response.status_code == 200:
    crypto_data = response.json()
    price = crypto_data[crypto_id]["usd"]
    st.write(f"Price of {crypto_id.capitalize()}: ${price}")
else:
    st.write("Error fetching data. Please try again later.")
