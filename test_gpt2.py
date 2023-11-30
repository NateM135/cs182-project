import os
from transformers import pipeline, set_seed
import numpy as np
import matplotlib.pyplot as plt
import random

from prompts import PROMPTS

OUTPUT_FILENAME = "test_generated_text"
SEED = random.getrandbits(32)
MAX_ADDITIONAL_RESPONSE_LENGTH = 50
NUM_RESP_PER_PROMPT = 3
VALIDATION_BINARY_NAME = "a.out"
OUTPUT_GRAPH_FILEAME = "output_graph.png"

set_seed(SEED)
generator = pipeline('text-generation', model='gpt2-large')

num_successful = 0
prompt_id =  "PROMPT TWO" # change this to whatever prompt you want to test
# prompt_id = int(prompt_input) - 1

x = generator(PROMPTS[prompt_id], max_length=len(PROMPTS[prompt_id])+MAX_ADDITIONAL_RESPONSE_LENGTH, num_return_sequences=NUM_RESP_PER_PROMPT, num_beams=1)
for i, response in enumerate(x):
    extracted_xml = response["generated_text"][len(PROMPTS[prompt_id]):].split("\n")[1]
    fileoutput = f"test_prompt_{OUTPUT_FILENAME}_{i+1}.xml"  # Added underscore before the index

    with open(fileoutput, "w") as file:
        file.write(extracted_xml)

    status = os.popen(f"./{VALIDATION_BINARY_NAME} {fileoutput}").read()
    if status.strip() == "Successfully Validated XML Syntax!":
        num_successful += 1

print(f"Num Successful for {prompt_id}: {num_successful}")
