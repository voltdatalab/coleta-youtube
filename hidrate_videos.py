# import pafy
from pyyoutube import Api
from json import load
from database import lista_videos
from database import update_video

with open("coleta-youtube/config.json") as jsonfile:
    config = load(jsonfile)['youtube']

# pafy.set_api_key(config["key"])
api = Api(api_key=config["key"])

videos = lista_videos(False, 2)
for video in videos:
	try:
		# source = pafy.new(video.yt_video_id, gdata=True)
		source = api.get_video_by_id(video_id=video.yt_video_id)
		update_video(source)
		
	except Exception as e:
		print(e)
		print("removido: " + video.yt_video_id) 
		print()