import spacy

spacy.prefer_gpu()

# LOADING PIPELINES
nlp = spacy.load("en_core_web_sm")


# Linguistic annotations
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_)
