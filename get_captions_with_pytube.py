from pytube import YouTube
from database import lista_videos


videos = lista_videos(True)
print(len(videos))
for video in videos:
	source = YouTube('https://www.youtube.com/watch?v=' + video.yt_video_id)
	# print(source.captions)
	
	if 'a.pt' in source.captions:
		caption = source.captions.get_by_language_code('a.pt')

		caption_convert_to_srt = (caption.generate_srt_captions())

		# print(caption_convert_to_srt)
		# save the caption to a file named Output.txt
		text_file = open("captions/"+video.yt_video_id + ".txt", "w")
		text_file.write(caption_convert_to_srt)
		text_file.close()
