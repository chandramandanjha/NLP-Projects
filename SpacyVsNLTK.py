import spacy
from nltk.tokenize import sent_tokenize,word_tokenize
import nltk
nltk.download('punkt')

nlp = spacy.load("en_core_web_sm")

doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for sentence in doc.sents:
    print(sentence)
for sentence in doc.sents:
    for word in sentence:
        print(word)

print(sent_tokenize("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi"))
print(word_tokenize("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi"))
