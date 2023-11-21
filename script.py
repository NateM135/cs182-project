import os
from transformers import pipeline, set_seed

OUTPUT_FILENAME = "generated_text.xml"
SEED = 42
MAX_RESPONSE_LENGTH = 250
NUM_ITERATIONS = 50
VALIDATION_BINARY_NAME = "a.out"

SAMPLE_PROMPT = """
Generate a well-formed XML document that represents information about a book. The XML should include the following elements:

1. <book> - representing the entire book.
   - <title> - the title of the book.
   - <author> - the author of the book.
   - <published_year> - the year the book was published.

Here is an example using the elements:

<book>
  <title>The Adventures of GPT-2</title>
  <author>AI Writer</author>
  <published_year>2023</published_year>
</book>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
"""

set_seed(SEED)
generator = pipeline('text-generation', model='gpt2-large')

num_successful = 0
for _ in range(NUM_ITERATIONS):
    x = generator(SAMPLE_PROMPT, max_length=MAX_RESPONSE_LENGTH, num_return_sequences=1)
    for i, response in enumerate(x):
        with open(OUTPUT_FILENAME, "w") as file:
            file.write(response["generated_text"][len(prompt_template):])
        status = os.popen(f"./{VALIDATION_BINARY_NAME} {OUTPUT_FILENAME}").read()
        if status.strip() == "Successfully Validated XML Syntax!":
            num_successful+=1

print("Generated XML files successfully.")
print(f"{num_successful}/{NUM_ITERATIONS} Iterations Successful")