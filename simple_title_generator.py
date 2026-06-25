from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

paragraph = input("Enter a paragraph:\n")

prompt = f"Generate a short title for the following article:\n\n{paragraph}\n\nTitle:"

result = generator(
    prompt,
    max_length=50,
    num_return_sequences=1
)

print("\nAI Output:")
print(result[0]["generated_text"])