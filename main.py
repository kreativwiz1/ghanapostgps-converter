import streamlit as st
import requests

# Function to get location details from GhanaPostGPS API
def get_location_details(ghanapostgps: str):
    url = "https://ghanapostgps.sperixlabs.org/get-location"
    payload = f'address={ghanapostgps}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error: Received status code {response.status_code}")
        return None

# Function to generate Google Maps link with a marker
def generate_google_maps_embed(latitude: float, longitude: float):
    google_maps_url = (
        f"https://www.google.com/maps?q={latitude},{longitude}&hl=es;z=14&output=embed"
    )
    return f'<iframe width="100%" height="500" frameborder="0" style="border:0" src="{google_maps_url}" allowfullscreen></iframe>'

# Function to generate Google Maps link
def generate_google_maps_link(latitude: float, longitude: float):
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# Streamlit App
st.title("GhanaPostGPS to Google Maps")

ghanapostgps = st.text_input("Enter GhanaPostGPS Address (e.g., GG-935-8464):")

if st.button("Show Map"):
    if ghanapostgps:
        location_details = get_location_details(ghanapostgps)

        if location_details and location_details.get('found'):
            lat = location_details['data']['Table'][0]['CenterLatitude']
            lon = location_details['data']['Table'][0]['CenterLongitude']
            area = location_details['data']['Table'][0]['Area']
            district = location_details['data']['Table'][0]['District']
            region = location_details['data']['Table'][0]['Region']
            street = location_details['data']['Table'][0]['Street']
            postcode = location_details['data']['Table'][0]['PostCode']

            # Display auxiliary information
            st.subheader("Location Details")
            st.write(f"**Area:** {area}")
            st.write(f"**District:** {district}")
            st.write(f"**Region:** {region}")
            st.write(f"**Street:** {street}")
            st.write(f"**Postcode:** {postcode}")

            # Embed Google Maps focused on the area
            google_maps_embed = generate_google_maps_embed(lat, lon)
            st.components.v1.html(google_maps_embed, height=500)

            # Provide a link to open the location in Google Maps
            google_maps_link = generate_google_maps_link(lat, lon)
            st.write(f"[Open in Google Maps]({google_maps_link})")

        else:
            st.error("Location not found or an error occurred.")
    else:
        st.warning("Please enter a valid GhanaPostGPS address.")
