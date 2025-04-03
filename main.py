from addition import addition
from def_openai import testing_with_ai

print("hello world")
print(addition(5,6))

function_string = """
def addition(a, b):
    return a + b
    
"""

print(testing_with_ai(function_string))