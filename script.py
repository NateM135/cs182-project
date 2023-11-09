from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

set_seed(42)

x = generator("Hello, what is AI?", max_length=30, num_return_sequences=5)
print(x)