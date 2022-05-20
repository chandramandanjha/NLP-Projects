from nltk.stem import PorterStemmer
import spacy

# Stemming in NLTK
stemmer = PorterStemmer()
words = ["eating", "eats", "eat", "ate", "adjustable", "rafting", "ability", "meeting"]

for word in words:
    print(word, "|", stemmer.stem(word))

# Lemmatization in Spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Mando talked for 3 hours although talking isn't his thing")
for token in doc:
    print(token, " | ", token.lemma_)

doc1 = nlp("eating eats eat ate adjustable rafting ability meeting better")
for token in doc1:
    print(token, " | ", token.lemma_)

# Customizing lemmatizer
print(nlp.pipe_names)
ar = nlp.get_pipe('attribute_ruler')
print(ar)
doc2 = nlp("Bro, you wanna go? Brah, don't say no! I am exhausted")
ar.add([[{"TEXT": "Bro"}], [{"TEXT": "Brah"}]], {"LEMMA": "Brother"})
for token in doc2:
    print(token.text, "|", token.lemma_)
