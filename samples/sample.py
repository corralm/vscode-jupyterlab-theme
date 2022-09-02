# functions
def func1(i: int) -> list:
    """Docstring"""
    return [i for i in range(9) if i % 2 == 0]

def func2():
    try:
        print(x)
    except:
        print("Something went wrong")
    finally:
        print("The 'try except' is finished")

x = lambda a, b : a * b

func1(10)

# classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@person('something')

p1 = Person('Iris', 25)

print(p1.name)
print(p1.age)

thisdict = {
  "country": "brazil",
  "year": 2022,
  "occupation": None
}

import re

txt = "The rain in Curitiba"
x = re.search("^The.*Curitiba$", txt)

# strings
['single quotes', "double quotes",]

"""multi line double quotes
"""

'''multi line single quotes
'''

b = "Hello, World!"
print(b[2:5])
print(f'{b}')

# numerical
[5, 5.0, 5_000_000, 5e6, 5j]

# operators
= != <> % / * | & ~ ^
[and, is, not, or, in,]

# bracket pairs
{{(())}} {(

# data types
[str, bool, int, dict,]
x = int('one')
    
# magic
%run
%%time