import spacy
# from spacy.symbols import ORTH

nlp = spacy.blank("en")
doc = nlp("Allen B. Downey is a Professor of Computer Science at the Franklin W. Olin College of Engineering in "
          "Needham, MA.")
for token in doc:
    print(token)

# Using index to grab tokens
print('\n')
print(doc[0])
token = doc[1]
print(token.text)
print(dir(token))

print(nlp.pipe_names)

# Span Object

span = doc[0:6]
print(span)
print(type(span),'\n')

# Token Attributes

doc1 = nlp("Tony gave two $ to Peter.")
token0 = doc1[0]
print(token0)
print(token0.is_alpha, "\n")

token2 = doc1[2]
print(token2)
print(token2.is_alpha)
print(token2.is_digit)
print(token2.like_num, '\n')

token3 = doc1[3]
print(token3)
print(token3.is_alpha)
print(token3.is_currency)

# Support in other languages
nlp = spacy.blank("hi")
doc = nlp("भैया जी! 5000 ₹ उधार थे वो वापस देदो")
for token in doc:
    print(token, token.is_currency)

# Customizing Tokenizer
print('\n')
nlp = spacy.blank("en")
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]
print(tokens, '\n')

# nlp.tokenizer.add_special_case("gimme", [
#    {ORTH: "gim"},
#    {ORTH: "me"},
# ])
# doc = nlp("gimme double cheese extra large healthy pizza")
# tokens = [token.text for token in doc]
# print(tokens)

# Sentence Tokenization or Segmentation

print(nlp.pipeline)
print(nlp.add_pipe('sentencizer'))
doc = nlp("Allen B. Downey is a Professor of Computer Science at the Franklin W. Olin College of Engineering in "
          "Needham, MA.")
for sentence in doc.sents:
    print(sentence)
print(nlp.pipeline)
