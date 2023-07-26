from rapidfuzz import process, fuzz 

match, score = process.extractOne('city','city22', scorer=fuzz.partial_ratio)