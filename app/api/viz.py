from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import logging
import pandas as pd
from pydantic import BaseModel, Field, validator
import os
from dotenv import load_dotenv
from app.spotify_client import SpotifyAPI

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET", default="super secret")

spotify = SpotifyAPI(client_id, client_secret)
router = APIRouter()


@router.get('/viz/{song_name}')
async def viz(search_term: str, type_of_search: str):
    """(CURRENTLY IN TEST MODE) Make song predictions from favorite songs
     and return Song ID's in an array"""
    songs = spotify.search(search_term, search_type=type_of_search)
    return songs    
