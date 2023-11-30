PROMPTS = {

"PROMPT ONE":"""
An example of a valid XML on a single line is:
""",

"PROMPT TWO":"""
Write a well-formed XML document that represents information about a book. The XML should include the following elements:

<book> - representing the entire book.
   - <title> - the title of the book.
   - <author> - the author of the book.
   - <published_year> - the year the book was published.

Here is an example output:

<book><title>The Adventures of GPT-2</title> <author>AI Writer</author> <published_year>2023</published_year> </book>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT THREE":"""
Write a well-formed XML document that represents information about a book. The XML should include the following elements:

Here is an example output:

<book><title>The Adventures of GPT-2</title> <author>AI Writer</author> <published_year>2023</published_year> </book>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT FOUR":"""
Write a well-formed XML document that represents information about a schedule. Each schedule contains a lecture element withe following elements.

<schedule> - representing the entire schedule.
   - <lecture> - the title of the lecture.
   - <topic> - the topic of the lecture
   - <instructor> - the name of the instructor
   - <time> - the week # for when this lecture takes place

Here is an example output:

<schedule><lecture><topic>Testing Overview</topic><instructor>Qian Zhang</instructor><time>Week 1</time></lecture><lecture><topic>Input Space Partitioning</topic><instructor>Qian Zhang</instructor><time>Week 2</time></lecture><lecture><topic>Test Coverage</topic><instructor>Qian Zhang</instructor><time>Week 3</time></lecture></schedule>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT FIVE":"""
Write a well-formed XML document that represents information about a schedule. 

Here is an example output:

<schedule><lecture><topic>Testing Overview</topic><instructor>Qian Zhang</instructor><time>Week 1</time></lecture><lecture><topic>Input Space Partitioning</topic><instructor>Qian Zhang</instructor><time>Week 2</time></lecture><lecture><topic>Test Coverage</topic><instructor>Qian Zhang</instructor><time>Week 3</time></lecture></schedule>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
"""

}