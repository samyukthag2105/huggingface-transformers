from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

article = input("Paste your article:\n")

summary = summarizer(
    article,
    max_length=50,
    min_length=10,
    do_sample=False
)

print("\nSummary:")
print(summary[0]["summary_text"])