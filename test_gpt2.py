import os

from transformers import pipeline, set_seed

OUTPUT_FILENAME = "generated_text.xml"
SEED = 42

set_seed(SEED)
generator = pipeline('text-generation', model='gpt2-large')

num_successful = 0
while True:
    prompt = input("Enter prompt: ")
    x = generator(prompt, max_length=len(prompt)+100, num_return_sequences=1)
    print("==Start Response==")
    print(x[0]["generated_text"])
    print("==End Response==")


