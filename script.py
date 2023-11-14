import os

from transformers import pipeline, set_seed

OUTPUT_FILENAME = "generated_text.xml"
SEED = 42
MAX_RESPONSE_LENGTH = 100
NUM_ITERATIONS = 50
VALIDATION_BINARY_NAME = "a.out"

SAMPLE_PROMPT = """
<doc>
    <clean> </clean>
    <dirty> A B </dirty>
    <mixed>
        A
        <clean> </clean>
        B
        <dirty> A B </dirty>
        C
    </mixed>
</doc>
"""

set_seed(SEED)
generator = pipeline('text-generation', model='gpt2')

num_successful = 0
for _ in range(NUM_ITERATIONS):
    x = generator(SAMPLE_PROMPT, max_length=105, num_return_sequences=1)
    for i, response in enumerate(x):
        with open(OUTPUT_FILENAME, "w") as file:
            file.write(response["generated_text"])
        status = os.popen(f"./{VALIDATION_BINARY_NAME} {OUTPUT_FILENAME}").read()
        if status.strip() == "Successfully Validated XML Syntax!":
            num_successful+=1

print("Generated XML files successfully.")
print(f"{num_successful}/{NUM_ITERATIONS} Iterations Successful")
