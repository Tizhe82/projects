from collections import namedtuple
 
a = namedtuple('courses', 'name, technology')
s = a('data science','python')
print(s)