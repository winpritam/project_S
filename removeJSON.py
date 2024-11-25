import re
import ast

def remove_json_blocks(text):
    # return re.sub(r'```json(.*?)```json', '', text, flags=re.DOTALL)
    return re.sub(r'```json(.*?)```', '', text, flags=re.DOTALL)


# Replace 'your_text' with the actual text you want to clean
txt=""" ```json
[
  {
    "Q": "Which keyword in PHP is used to define access modifiers?",
    "O": {
      "a": "access",
      "b": "modifier",
      "c": "public",
      "d": "protected"
    },
    "A": "c"
  },
  {
    "Q": "What is the default access modifier for a class member in PHP?",
    "O": {
      "a": "public",
      "b": "protected",
      "c": "private",
      "d": "None of the above"
    },
    "A": "a"
  },
  {
    "Q": "Which access modifier allows access to a class member from anywhere?",
    "O": {
      "a": "private",
      "b": "protected",
      "c": "public",
      "d": "static"
    },
    "A": "c"
  },
  {
    "Q": "Which access modifier restricts access to a class member only within the class itself?",
    "O": {
      "a": "public",
      "b": "protected",
      "c": "private",
      "d": "final"
    },
    "A": "c"
  },
  {
    "Q": "Which access modifier allows access to a class member from within the class and its subclasses?",
    "O": {
      "a": "private",
      "b": "public",
      "c": "protected",
      "d": "abstract"
    },
    "A": "c"
  },
   {
    "Q": "What does the `public` access modifier do in PHP?",
    "O": {
      "a": "Restricts access to a member within the class itself.",
      "b": "Allows access to a member from anywhere.",
      "c": "Allows access to a member from within the class and its subclasses only.",
      "d": "Makes a member read-only."
    },
    "A": "b"
  },
  {
    "Q": "What does the `protected` access modifier do in PHP?",
    "O": {
      "a": "Restricts access to a member within the class itself.",
      "b": "Allows access to a member from anywhere.",
      "c": "Allows access to a member from within the class and its subclasses only.",
      "d": "Makes a member constant."
    },
    "A": "c"
  },
  {
    "Q": "How are access modifiers declared in PHP?",
    "O": {
      "a": "Using comments",
      "b": "Using keywords such as `public`, `protected`, and `private` before a member's declaration.",
      "c": "Using special symbols",
      "d": "By assigning values to the members."
    },
    "A": "b"
  },
  {
    "Q": "Which access modifier is used to prevent inheritance of a class member?",
    "O": {
      "a": "protected",
      "b": "private",
      "c": "final",
      "d": "abstract"
    },
    "A": "c"
  },
  {
    "Q": "What is the main purpose of using access modifiers?",
    "O": {
      "a": "To make the code more complex.",
      "b": "To improve code readability and maintainability, enhancing security by controlling member access.",
      "c": "To add visual appeal to the code.",
      "d": "To decrease the performance of the code."
    },
    "A": "b"
  }
]
``` 
"""
cleaned_text = remove_json_blocks(txt)
print(cleaned_text)
# lst = ast.literal_eval(cleaned_text)
# print('\n',lst)