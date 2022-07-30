import os
import re
from database import insere_captions
from database import insere_video


for filename in os.listdir('coleta-youtube/Edit'):
	with open(os.path.join('coleta-youtube/Edit', filename), 'r', encoding="utf8") as f:
		
		insere_video(filename.split('.')[0])

		data = f.read()
		a = []
		b = {}
		for line in data.splitlines():
			if line:
				if re.match(r'^([0-9]+:[0-9]+)$', line):
					b["minute"] = int(line.split(':')[0])*60 + int(line.split(':')[1])
					print(b["minute"])
				else:
					if 'line' in b:
						b['line'] = b['line'] + " " + line
					else:
						b['line'] = line
					
			else:
				if b:
					a.append(b)
					b = {}

		insere_captions(a, os.path.splitext(filename)[0])
	
	# os.remove(os.path.join('captions', filename))

