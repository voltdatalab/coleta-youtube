# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import googleapiclient.discovery
import googleapiclient.errors
from database import insere_videos, lista_playlists


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
	os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
	api_key = "AIzaSyAkkqX1yihsMmu0yfYzbdqjsgKV7FtDyvU"
	api_service_name = "youtube"
	api_version = "v3"
	# client_secrets_file = "youtube_secret.json"

    # Get credentials and create an API client
	youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey=api_key)

	playlists = lista_playlists()
	for playlist in playlists:
		request = youtube.playlistItems().list(
			part="id,snippet",
			maxResults=50,
			playlistId=playlist.yt_playlist_id
		)
		response = request.execute()

		insere_videos(response['items'])

if __name__ == "__main__":
    main()