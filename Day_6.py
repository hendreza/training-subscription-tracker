# ============================================================
# Day 6: Functions with one parameter and simple validation
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: function input, output, one-parameter logic
# App Feature: Create and validate simple subscription values
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code reading section and answer the questions.
3. Try the bug spotting section before running the code.
4. Complete the writing tasks yourself.
5. Run the file with:
   python Day_6.py

6. Later, run pytest with:
   pytest Day_6.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today we are focusing on functions with one parameter.

A parameter is the variable name inside the function definition.

Example:

def format_subscription_name(subscription_name):
    return subscription_name

Here, subscription_name is the parameter.

When we call the function:

result = format_subscription_name("Netflix")

"Netflix" is the argument.
It is the real value passed into the function.

The function then returns a value.

Important flow:

argument -> parameter -> function logic -> return value -> stored result

Example:

result = format_subscription_name("Netflix")

- "Netflix" is the argument
- subscription_name receives "Netflix"
- the function returns "Netflix"
- result stores the returned value

In the Subscription Tracker app, one-parameter functions are useful for small jobs like:

- checking if a name is empty
- formatting a subscription name
- checking if a cost is valid
- turning a cost into yearly cost
- checking if a subscription should be shown

Important reminder from Day 5:

Type hints do not force Python to validate data at runtime.

Example:

def check_active_status(is_active: bool):
    return is_active

check_active_status("True")

Python will still allow this unless we write validation ourselves.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

# Do not edit this section yet.
# Read it and answer the questions.

def format_subscription_name(subscription_name):
    return f"Subscription: {subscription_name}"


result = format_subscription_name("Netflix")
print(result)

# Questions:
# 1. What is the parameter name?
# Answer: subscription_tracker
#
# 2. What argument is passed into the function?
# Answer:Netflix
#
# 3. What value is stored in result?
# Answer: Subscription: Netflix
#
# 4. What will be printed?
# Answer: Subscription: Netflix
#
# 5. Does the function print the value or return the value?
# Answer: return
#


# ============================================================
# 3. CODE READING: SIMPLE VALIDATION
# ============================================================

def is_valid_subscription_name(subscription_name):
    if subscription_name == "":
        return False

    return True


print(is_valid_subscription_name("Netflix"))
print(is_valid_subscription_name(""))

# Questions:
# 1. What does is_valid_subscription_name("Netflix") return?
# Answer: True
#
# 2. What does is_valid_subscription_name("") return?
# Answer: False
#
# 3. Why should an empty subscription name be invalid?
# Answer: the system wont know what to assaign and the user will forget what the bank charge is
#
# 4. What data type does this function return?
# Answer: bool
#
# 5. What would happen if subscription_name was None?
# Answer: currently the system will accept it, but it will give an empty value
#


# ============================================================
# 4. BUG SPOTTING SECTION
# ============================================================

# Read this code before running it.

def is_valid_monthly_cost(monthly_cost: int):
    if monthly_cost < 0:
        return False

    return True


# This line is risky:
# result = is_valid_monthly_cost("199")

# Questions:
# 1. Why is this risky even though monthly_cost has a type hint?
# Answer:that line should not be allowed as the system shouldnt take a string value
#
# 2. Does monthly_cost: int automatically stop strings from being passed in?
# Answer: no, it hints as to what ype it should be
#
# 3. What error could happen inside the function?
# Answer: type error
#
# 4. What should we check before comparing monthly_cost < 0?
# Answer: to make sure that monthly cost is an int
#
# 5. Rewrite the validation idea in your own words:
# Answer: 
#


# ============================================================
# 5. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete the function below.
#
# It must accept:
# - subscription_name
#
# It must return:
# "Subscription: Netflix"
#
# Example:
# create_subscription_label("Netflix")
# should return "Subscription: Netflix"

def create_subscription_label(subscription_name):
    return f"Subscription: {subscription_name}"


result = create_subscription_label("Netflix")
print(result)
# Expected output: Subscription: Netflix


# Task 2:
# Complete the function below.
#
# It must accept:
# - subscription_name
#
# Rules:
# - If subscription_name is an empty string, return False
# - Otherwise, return True

def has_valid_subscription_name(subscription_name):
    
    if subscription_name == "":
        return False
    
    return True


result = has_valid_subscription_name("Spotify")
print(result)
# Expected output: True

result = has_valid_subscription_name("")
print(result)
# Expected output: False


# Task 3:
# Complete the function below.
#
# It must accept:
# - monthly_cost
#
# Rules:
# - If monthly_cost is less than 0, return False
# - Otherwise, return True

def has_valid_monthly_cost(monthly_cost):
    if monthly_cost < 0:
        return False
    return True


result = has_valid_monthly_cost(199)
print(result)
# Expected output: True

result = has_valid_monthly_cost(-50)
print(result)
# Expected output: False


# Task 4:
# Complete the function below.
#
# It must accept:
# - monthly_cost
#
# It must return the yearly cost.
#
# Example:
# calculate_yearly_cost(199)
# should return 2388

def calculate_yearly_cost(monthly_cost):
    yearly_cost = monthly_cost * 12

    return yearly_cost


result = calculate_yearly_cost(199)
print(result)
# Expected output: 2388


# ============================================================
# 6. PYTEST MINI-LESSON
# ============================================================

"""
Today pytest checks simple one-parameter functions.

When a function has one parameter, we test it by passing one argument.

Example:

def double_number(number):
    return number * 2


def test_double_number():
    assert double_number(5) == 10

That means:

- call double_number with the argument 5
- expect the returned value to be 10

For validation functions, we usually test both:

1. Valid input
2. Invalid input

Example:

def is_valid_name(name):
    if name == "":
        return False
    return True


def test_is_valid_name_accepts_normal_name():
    assert is_valid_name("Netflix") is True


def test_is_valid_name_rejects_empty_name():
    assert is_valid_name("") is False

This proves both paths work.
"""


# ============================================================
# 7. PYTEST SECTION
# ============================================================

def test_create_subscription_label():
    assert create_subscription_label("Netflix") == "Subscription: Netflix"


def test_has_valid_subscription_name_accepts_name():
    assert has_valid_subscription_name("Spotify") is True


def test_has_valid_subscription_name_rejects_empty_string():
    assert has_valid_subscription_name("") is False


def test_has_valid_monthly_cost_accepts_positive_cost():
    assert has_valid_monthly_cost(199) is True


def test_has_valid_monthly_cost_rejects_negative_cost():
    assert has_valid_monthly_cost(-50) is False


def test_calculate_yearly_cost():
    assert calculate_yearly_cost(199) == 2388


# ============================================================
# 8. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Today we are validating simple user input.

A real app should not trust user input directly.

Questions:

1. Why should an empty subscription name be rejected?
Answer: the user wont be able to track or know all the expenses

2. Why should a negative monthly cost be rejected?
Answer: it is a logic error as the company wont be paying you

3. What could go wrong if monthly_cost is "199" as text instead of 199 as a number?
Answer: the system will give a false amount so the user could miss paymnets 

4. Why are type hints useful even though they do not automatically validate values?
Answer: they indicate what you should be reciveing and guide you on how and what to validate
 
5. Later, should validation happen before or after saving data?
Answer: before
"""


# ============================================================
# 9. STRETCH TASK
# ============================================================

"""
Stretch task:
Only do this if the main tasks felt comfortable.

This task adds runtime type validation.

Remember:
Type hints do not enforce types by themselves.
If you want runtime protection, you must check the type in your code.
"""


# Stretch:
# Complete the function below.
#
# Rules:
# - If monthly_cost is not an int or float, return "Invalid cost type"
# - If monthly_cost is less than 0, return "Invalid monthly cost"
# - Otherwise, return True
#
# Hint:
# You can check types with:
#
# type(monthly_cost) not in [int, float]

def validate_monthly_cost(monthly_cost):
    pass


result = validate_monthly_cost(199)
print(result)
# Expected output: True

result = validate_monthly_cost(199.99)
print(result)
# Expected output: True

result = validate_monthly_cost(-50)
print(result)
# Expected output: Invalid monthly cost

result = validate_monthly_cost("199")
print(result)
# Expected output: Invalid cost type


# Optional stretch pytest:

def test_validate_monthly_cost_accepts_int():
    assert validate_monthly_cost(199) is True


def test_validate_monthly_cost_accepts_float():
    assert validate_monthly_cost(199.99) is True


def test_validate_monthly_cost_rejects_negative_cost():
    assert validate_monthly_cost(-50) == "Invalid monthly cost"


def test_validate_monthly_cost_rejects_string():
    assert validate_monthly_cost("199") == "Invalid cost type"


# ============================================================
# 10. DAILY REFLECTION
# ============================================================

"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
Answer:

2. What part took the longest to reason through?
Answer:

3. What is the difference between a type hint and runtime validation?
Answer:

4. What is the difference between an argument and a returned value?
Answer:

5. Why should validation happen before saving data?
Answer:

6. Which pytest case made the most sense to me?
Answer:

7. Which pytest case confused me?
Answer:

8. What should tomorrow become?
   - easier reinforcement
   - same level with more practice
   - harder/stretch level

Answer:
"""