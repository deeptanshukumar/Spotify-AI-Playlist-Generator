# 🎵 Spotify AI Playlist Generator 🎶

## 📹 Video Demo

[Insert your video demo link here]

## 📜 Description

The AI Playlist Generator is a Python-based application that automatically creates personalized Spotify playlists based on user input. By leveraging the Spotify API and ytmusicapi, this project generates dynamic playlists tailored to user preferences, such as mood, genre, or specific artists. The application provides a seamless way to curate music based on user-defined parameters.

## 🌟 Features

- **Automated Playlist Creation**: Generates a new Spotify playlist based on user input.
- **User Authentication**: Securely connects to Spotify using OAuth.
- **Song Selection**: Fetches and adds relevant tracks based on the input criteria.
- **Error Handling**: Ensures proper API communication and catches common errors.
- **Testing with Pytest**: Includes unit tests to validate core functionalities.

## 🔍 How It Works

1. **User Input**: The user provides details such as mood, favorite artists, or genres.
2. **Spotify API Integration**: The program authenticates the user and interacts with Spotify’s API.
3. **Playlist Generation**: The script fetches recommended songs and creates a new playlist.
4. **Adding Tracks**: The selected songs are added to the newly created playlist.

## ⚙️ Installation

### Prerequisites

Ensure you have Python 3.12 installed.

### Setup

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/playlist-generator
   cd playlist-generator
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Set up a Spotify Developer account and get your credentials:

   - Visit [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create an application and get your **Client ID** and **Client Secret**
   - Set up a **Redirect URI**

4. Create a `.env` file and add your credentials:

   ```sh
   SPOTIPY_CLIENT_ID='your_client_id'
   SPOTIPY_CLIENT_SECRET='your_client_secret'
   SPOTIPY_REDIRECT_URI='your_redirect_uri'
   ```

## 🚀 Usage

Run the main script:

```sh
python project.py
```

Follow the on-screen instructions to generate your playlist.

## 📂 File Structure

```
├── project.py          # Main script
├── test_project.py     # Unit tests
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
```

## 🛠️ Testing

Run tests using pytest:

```sh
pytest test_project.py
```

## ⚠️ Challenges Faced

- Handling API rate limits
- Ensuring playlist name constraints are met
- Debugging authentication issues with Spotify API
- And for the biggest of all... I had to use ytmusicapi to get suggestions from YouTube Music and then pass them through Spotify's API to get song URLs and make it a playlist. This decision was made due to the realization that the `get_recommendations` endpoint of Spotify API has been deprecated! 🎧

## 🔮 Future Improvements

- Improve recommendation logic with AI-based suggestions
- Add support for multiple streaming platforms
- Implement a web-based UI for better user experience

## 🙌 Acknowledgments

- Built as part of CS50P Final Project
- Uses [Spotipy](https://spotipy.readthedocs.io/) for Spotify API interaction
- Uses ytmusicapi for interaction with YouTube Music database

**💡 A note from my end:** I initially designed this project to allow users to input a query, which would be processed by Gemini to generate a set of parameters for Spotify's recommendation API. However, since Spotify's `get_recommendations` endpoint has been deprecated, I adapted the approach. Instead, the project now utilizes Gemini to generate search parameters, constructs a refined query, and retrieves song recommendations from the YouTube Music API. These songs are then searched on Spotify to obtain their URIs, which are used to create a curated playlist.

I hope you liked this project! - [Deeptanshu Kumar](https://github.com/deeptanshukumar) 🎵

