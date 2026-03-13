from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
topic = input("Enter a topic: ")
result = generator(topic, max_length=60)
print("\nGenerated Text:\n")
print(result[0]['generated_text'])