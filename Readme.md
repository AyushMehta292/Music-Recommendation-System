# Music-Recommendation-System

This project is a music recommendation system that utilizes Spotify's API to fetch trending playlist data and provides song recommendations based on content and popularity. The system uses a hybrid recommendation approach combining content-based filtering and popularity weighting.

## Project Structure

- `spotify_auth.py`: Handles Spotify authentication and access token retrieval.
- `spotify_data.py`: Fetches playlist data from Spotify using the access token.
- `recommendation_system.py`: Contains the logic for generating music recommendations.
- `main.py`: The main script to run the entire process and display recommendations.

## Features

- **Spotify Authentication**: Securely authenticate and obtain access tokens using [Spotify's API](https://developer.spotify.com/dashboard/).
- **Data Retrieval**: Fetch trending playlist data including track details and audio features.
- **Recommendation System**: Generate song recommendations using a hybrid approach combining content-based filtering and popularity weighting.

## Requirements

- Python 3.6 or higher
- Required Python packages:
  - [`requests`](https://requests.readthedocs.io/)
  - [`spotipy`](https://spotipy.readthedocs.io/)
  - [`pandas`](https://pandas.pydata.org/)
  - [`numpy`](https://numpy.org/)
  - [`scikit-learn`](https://scikit-learn.org/stable/)

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AyushMehta292/Music-Recommendation-System.git
   cd Music-Recommendation-System

2. **Run the Code**

    ```bash
    #in mac
    python3 main.py

    #in windows
    python main.py