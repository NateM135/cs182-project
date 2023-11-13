from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2')

set_seed(42)

prompt_template = """
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

x = generator(prompt_template, max_length=100, num_return_sequences=5)
for i, response in enumerate(x):
    with open(f'generated_xml_{i+1}.xml', 'w') as file:
        file.write(response['generated_text'])

print("Generated XML files successfully.")
