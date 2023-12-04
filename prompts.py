PROMPTS = {

"PROMPT ONE":"""
An example of a valid XML on a single line is:
""",

"PROMPT TWO":"""
Write a well-formed XML document that represents information about a game. The XML should include the following elements:

<game> represents the entire game.
<name> is the title of the game.
<year_released> is the year the game was released.
<genre> represents the genre of the game.
<creator> represents the creator of the game.

Here is an example output:

<game><name>Minecraft</name><year_released>2011</year_released><genre>Survival</genre><creator>Notch</creator></game>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT THREE":"""
Here is an example of a XML document that represents information about a game:

<game><name>Minecraft</name><year_released>2011</year_released><genre>Survival</genre><creator>Notch</creator></game>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT FOUR":"""
Write a well-formed XML document that represents information about a class. The XML should include the following elements:

<class> represents the entire class.
<assignment> represents an assignment object that contains a <name> element and <percentage> element.
<name> represents the name of the assignment.
<percentage> represents the percentage weight of the assignment.

Here is an example output:

<class><assignment><name>Homework #1</name><percentage>20%</percentage></assignment><assignment><name>Homework #2</name><percentage>20%</percentage></assignment><assignment><name>Final</name><percentage>60%</percentage></assignment></class>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
""",

"PROMPT FIVE":"""
Here is an example of a XML document that represents information about a class.:

<class><assignment><name>Homework #1</name><percentage>20%</percentage></assignment><assignment><name>Homework #2</name><percentage>20%</percentage></assignment><assignment><name>Final</name><percentage>60%</percentage></assignment></class>

Another example of an XML like this where the elements are properly nested, and include sample data within each element is:
"""

}