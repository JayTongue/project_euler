from num2words import num2words
import re
print(sum(len(re.sub(r'-| ', '', num2words(i, to='cardinal'))) for i in range(1, 1001)))
