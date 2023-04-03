#-------------------------------------------------------------------------------

import requests
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
import streamlit as st
from include import *

#-------------------------------------------------------------------------------

html_title = "<h1 style='text-align:center;color:#1ED760'>Spotify Artists Informations</h1>"
st.markdown(html_title, unsafe_allow_html=True)

espace(2)

html_text = "<div style='text-align:left;color:#00000;font-size:30px'>Enter the name of an artist or band:</div>"
st.markdown(html_text, unsafe_allow_html=True)

artist_name = st.text_input("", "Boris Brejcha")

espace(2)

headers = get_authorization_headers()
artist_id = artist_id_from_name(artist_name, headers=headers)

html_artist_name = f"<div style='text-align:left;color:#00000;font-size:30px'><b>Artist Name:</b> {artist_name}</div>"
html_artist_id = f"<div style='text-align:left;color:#00000;font-size:30px'><b>Artist ID:</b> {artist_id}</div>"
st.markdown(html_artist_name, unsafe_allow_html=True)
st.markdown(html_artist_id , unsafe_allow_html=True)

base_url = "https://open.spotify.com/artist/"
artist_url = f"{base_url}{artist_id}"
artist_html = f"<div style='text-align:left;color:#00000;font-size:30px'><b>Artist Spotify URL</b>: <a href='{artist_url}' >  {artist_url}</a></div>"
st.markdown(artist_html, unsafe_allow_html=True)

artist_genres_list =  artist_styles_from_id(artist_id, headers)
artist_genres_string = ", ".join(artist_genres_list)
artist_genres_html = f"<div style='text-align:left;color:#00000;font-size:30px'><b>Artist Genres</b>: {artist_genres_string} </div>"
st.markdown(artist_genres_html, unsafe_allow_html=True)


related_artists_list_of_dicts = related_artists(artist_id, headers)
related_artists_list = [artist["name"] for artist in related_artists_list_of_dicts]
related_artists_string = ", ".join(related_artists_list)
related_artists_html = f"<div style='text-align:left;color:#00000;font-size:30px'><b>Related Artists</b>: {related_artists_string} </div>"
st.markdown(related_artists_html, unsafe_allow_html=True)

espace(2)

st.write("To be continued...")

espace(2)

st.write("Sources...")
