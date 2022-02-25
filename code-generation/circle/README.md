# The Circle Family

I've had trouble getting most code-generation models to usefully complete a function named `area_of_circle` or `circle_area`.

Things to test:
- does the function attempt pi r^2?
- if a float is used in place of pi, how precise is it?
- does `import math`, or `from math import pi`, help prompt the model?
- does the model suggest using math.pi even without a pre-existing import?
- does the model suggest math.pi after it is used in other files or previous use in the tool?

Findings so far:

Co-Pilot / Codex does OK on this, I have had issues in other models.

It helps to include a comment `# include imports`
