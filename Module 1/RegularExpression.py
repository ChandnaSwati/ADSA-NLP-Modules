import re
text = "There are 45 students and 12 laptops."
numbers = re.findall(r'\d+', text)
print(numbers)