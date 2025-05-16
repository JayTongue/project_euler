from num2words import num2words
import re
print(sum(len(re.sub(r'-| ', '', num2words(i, to='cardinal'))) for i in range(1, 1001)))

# for i in range(1, 1001):
#     print(re.sub(r'-| ', '', num2words(i, to='cardinal')))
print(num2words(36))

# Other variants, according to the type of article.
print(num2words(36, to = 'ordinal'))
print(num2words(36, to = 'ordinal_num'))
print(num2words(36, to = 'year'))
print(num2words(36, to = 'currency'))

# Language Support.
print(num2words(36, lang ='es'))
