from database import get_captions, get_terms
from database import update_caption, update_caption_term



captions = get_captions(False)
terms = get_terms()

for caption in captions:
	for term in terms:
		for spelling in term.spellings.split(','):
			if (caption.line).lower().find(spelling.lower()) > 0:
				update_caption_term(caption, term)
		
	update_caption(caption)
