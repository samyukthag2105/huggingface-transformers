from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

paragraph = input("Enter a paragraph:\n")

prompt = f"Title: "

result = generator(
    prompt + paragraph,
    max_length=40,
    num_return_sequences=1
)

print("\nGenerated Text:")
print(result[0]["generated_text"])
