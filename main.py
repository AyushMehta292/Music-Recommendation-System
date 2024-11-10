# main.py
from spotify_auth import get_access_token
from spotify_data import get_trending_playlist_data
from recommendation_system import hybrid_recommendations

# Obtain access token
access_token = get_access_token()

# Define the playlist ID
playlist_id = '37i9dQZF1DX76Wlfdnj7AP'

# Get the music data from the playlist
music_df = get_trending_playlist_data(playlist_id, access_token)

# Define the input song name
input_song_name = "I'm Good (Blue)"

# Get hybrid recommendations
recommendations = hybrid_recommendations(music_df, input_song_name, num_recommendations=5)

# Display the recommendations
print(f"Hybrid recommended songs for '{input_song_name}':")
print(recommendations)
