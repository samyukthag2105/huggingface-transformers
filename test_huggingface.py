from transformers import pipeline

print("Transformers imported successfully!")
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I love learning Python")

print(result)
from transformers import pipeline

print("Transformers works!") 

from transformers import pipeline

classifier = pipeline("sentiment-analysis")

sentence = input("today was terrible ")

result = classifier(sentence)

print(result)