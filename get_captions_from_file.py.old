import os
import re
from database import insere_captions


for filename in os.listdir('captions'):
	with open(os.path.join('captions', filename), 'r') as f:
		data = f.read()
		a = []
		b = {}
		for line in data.splitlines():
			if line:
				if re.match(r'^([\d]+)$', line):
					b["order"] = line
				elif re.search('-->', line):
					b['time'] = line
				else:
					b['line'] = line
					a.append(b)
					b = {}

		insere_captions(a, os.path.splitext(filename)[0])
	
	os.remove(os.path.join('captions', filename))

