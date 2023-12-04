import os
from transformers import pipeline, set_seed
import numpy as np
import matplotlib.pyplot as plt
import random

from prompts import PROMPTS

OUTPUT_FILENAME_PREFIX = "generated_text"
SEED = random.getrandbits(32)
MAX_ADDITIONAL_RESPONSE_LENGTH = 50
NUM_RESP_PER_PROMPT = 5
VALIDATION_BINARY_NAME = "a.out"
OUTPUT_GRAPH_FILEAME = "output_graph.png"

# Setup Model
set_seed(SEED)
generator = pipeline('text-generation', model='gpt2-large')

# Setup Graph
objects = tuple([x.replace(" ", "\n") for x in PROMPTS.keys()])
y_pos = np.arange(len(objects))
performance = []

# Dictionary to store results for each prompt
results_by_prompt = {}

for prompt_id, (prompt_key, prompt_text) in enumerate(PROMPTS.items(), start=1):
    print(prompt_text)
    num_successful = 0
    x = generator(prompt_text, max_length=len(prompt_text) + MAX_ADDITIONAL_RESPONSE_LENGTH, num_return_sequences=NUM_RESP_PER_PROMPT, num_beams=1)

    for i, response in enumerate(x):
        # Extract the second line, prompts are formed for generated xml to be here
        extracted_xml = response["generated_text"][len(prompt_text):].split("\n")[1]
        # Generate filename 
        iteration_output_filename = f"prompt{prompt_id}_{OUTPUT_FILENAME_PREFIX}_{i+1}.xml"

        # Save generated text to local system
        with open(iteration_output_filename, "w") as file:
            file.write(extracted_xml)

        # Call binary that checks XML validity with libxml
        status = os.popen(f"./{VALIDATION_BINARY_NAME} {iteration_output_filename}").read()
        if status.strip() == "Successfully Validated XML Syntax!":
            num_successful += 1

    results_by_prompt[prompt_id] = num_successful  # Store the result for the current prompt

# Print results for each prompt
for prompt_id, num_successful in results_by_prompt.items():
    print(f"Num Successful for Prompt {prompt_id}: {num_successful}")
    performance.append(num_successful)

# use matplotlib to make bar chart with results 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel(f"Num Successful Iterations / {NUM_RESP_PER_PROMPT}")
plt.title("Performance by Prompt")
plt.ylim(0, NUM_RESP_PER_PROMPT)

plt.savefig(OUTPUT_GRAPH_FILEAME)