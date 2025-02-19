import pytest
from project import generate_yt_query, get_yt_songs, get_spotify_uris, generate_playlist

def test_generate_yt_query():      
    values = ["120", "0.8", "0.9", "0.7", "0.2", "0.1", "0.8", "20"]
    query, num_songs = generate_yt_query(values)
    
    assert "english" in query
    assert "high energy" in query
    assert "dance" in query
    assert num_songs == 20
    
    values = ["90", "0.2", "0.3", "0.2", "0.8", "0.9", "0.2", "10"]
    query, num_songs = generate_yt_query(values)
    
    assert "chill" in query
    assert "relaxed" in query
    assert num_songs == 10

def test_get_spotify_uris():
    songs = [{"title": "Test Song", "artist": "Test Artist"}]
    uris = get_spotify_uris(songs)    
    assert isinstance(uris, list)
    
    empty_songs = []
    empty_uris = get_spotify_uris(empty_songs)
    assert empty_uris == []

def test_generate_playlist():
    with pytest.raises(Exception):
        generate_playlist("")
    
    try:
        generate_playlist("test query")
    except Exception as e:
        assert str(e) != ""


