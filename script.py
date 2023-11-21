import os
from transformers import pipeline, set_seed
import numpy as np
import matplotlib.pyplot as plt
import random

from prompts import PROMPTS

OUTPUT_FILENAME = "generated_text.xml"
SEED = random.getrandbits(32)
MAX_ADDITIONAL_RESPONSE_LENGTH = 250
NUM_RESP_PER_PROMPT = 3
VALIDATION_BINARY_NAME = "a.out"
OUTPUT_GRAPH_FILEAME = "output_graph.png"

# Setup Model
set_seed(SEED)
generator = pipeline('text-generation', model='gpt2-large')

# Setup Graph
objects = tuple([x.replace(" ", "\n") for x in PROMPTS.keys()])
y_pos = np.arange(len(objects))
performance = []


for prompt_id in PROMPTS:
    num_successful = 0
    x = generator(PROMPTS[prompt_id], max_length=len(PROMPTS[prompt_id])+MAX_ADDITIONAL_RESPONSE_LENGTH, num_return_sequences=NUM_RESP_PER_PROMPT)
    for i, response in enumerate(x):
        extracted_xml = response["generated_text"][len(PROMPTS[prompt_id]):].split("\n")[1]
        with open(OUTPUT_FILENAME, "w") as file:
            file.write(extracted_xml)
        status = os.popen(f"./{VALIDATION_BINARY_NAME} {OUTPUT_FILENAME}").read()
        if status.strip() == "Successfully Validated XML Syntax!":
            num_successful+=1
    performance.append(num_successful)


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel(f"Num Successful Iterations / {NUM_RESP_PER_PROMPT}")
plt.title("Performance by Prompt")
plt.ylim(0, NUM_RESP_PER_PROMPT)

plt.savefig(OUTPUT_GRAPH_FILEAME)