import re
"""
Meta characters: . ^ $ * + ? { } [ ] \ | ( )
| == or
. == Any characters 
{ } == min or max or n
[ ] == group characters range
* == 0 or n
+ == 0 or n
? == 0 ou 1
 

"""

email = 'adilsonsimiao@gmail.com I have been using my email to work this moment, people called me as' \
        ' Adilsooooon I am from Brazil at home town my family call me Dukaaa duuka'
print(re.findall(r'Adilson|com', email))
print(re.findall(r'[Aa]dilson', email))
print(re.findall(r'adilson', email, flags=re.I))
print(re.findall(r'adilso{1,}n', email, flags=re.I))
print(re.findall(r'du{1}ka{1}', email, flags=re.I))
# print(re.sub(r'adilso+n', 'adilson', email, flags=re.I))

# expression = '[a-z\.]+'
# matches = re.findall(expression, email)
# domain = matches[0]
# print(matches)
# print(domain)
# price = 'Price: $18,9648.50'
# expression1 = 'Price: \$([0-9,]*\.[0-9]*)'
# matches1 = re.search(expression1, price)
# print(matches1.group(0))
# print(matches1.group(1))
