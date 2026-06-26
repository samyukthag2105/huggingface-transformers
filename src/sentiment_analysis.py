from transformers import pipeline

print("Loading sentiment analysis model...")

classifier = pipeline("sentiment-analysis")

sentence = input("Enter a sentence: ")

result = classifier(sentence)

print("\nResult:")
print(result)
