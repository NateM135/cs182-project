from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2-large')

set_seed(42)

prompt_template = """
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

x = generator(prompt_template, max_length=250, num_return_sequences=5)
for i, response in enumerate(x):
    with open(f'generated_xml_{i+1}.xml', 'w') as file:
        # Write only the response to the file, not the prompt
        file.write(response['generated_text'][len(prompt_template):])
        # print(response['generated_text'][len(prompt_template):])

print("Generated XML files successfully.")