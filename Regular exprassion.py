"""import re
pattern = r"colour"
if(re.match(pattern,"Red is a colour, I love red colour")):
    print("Match")
else:
    print("Not Match")"""

"""import re
pattern = r"colour"
if(re.search(pattern,"Red is a colour, I love red colour")):
    print("Match")
else:
    print("Not Match")"""



"""
import re
pattern = r"colour"
print(re.findall(pattern,"Red is a colour, I love red colour"))"""


"""import re
pattern = r"colour"
text = "My favourite colour is red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())"""

import re
pattern = r"colour"
text1 = "My favourite colour is red i love red colour"
text2 = re.sub(pattern,"color",text1)
print(text2)