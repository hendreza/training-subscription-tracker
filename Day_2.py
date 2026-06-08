# ============================================================
# Day 2: Printing, returning, and reading simple output
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: print(), return values, simple tracing, expected output
# App Feature: Display subscription details
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code reading section and answer the questions.
3. Try the bug spotting section before running the code.
4. Complete the writing tasks yourself.
5. Run the file with:
   python Day_2.py

6. Later, run pytest with:
   pytest Day_2.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today we are focusing on output.

There are two important ideas:

1. print()
   - Shows something on the screen.
   - Useful when testing, debugging, or checking what your code is doing.

2. return
   - Sends a value back from a function.
   - This is what other code and pytest usually check.

Example:

def get_subscription_name():
    return "Netflix"

result = get_subscription_name()
print(result)

The function RETURNS "Netflix".
The print() SHOWS "Netflix" on the screen.

In real backend code, we usually care more about return values than print statements,
because return values can be tested and reused.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

# Do not edit this section yet.
# Read it and answer the questions.

subscription_name = "Netflix"
monthly_cost = 199
is_active = True

print(subscription_name)
print(monthly_cost)
print(is_active)

# Questions:
# 1. What three values are stored?
# Answer: Netflix , 199 and True
#
# 2. What will be printed, line by line?
# Answer: Netflix, 199, True
#
# 3. Which value is a string?
# Answer: Netflix (subscription_name)
#
# 4. Which value is an integer?
# Answer:199 (monthly_cost)
#
# 5. Which value is a boolean?
# Answer:True (is_active)
#


# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

# Read this code before running it.

monthly_cost = "199"
discount = 20

# final_cost = monthly_cost - discount

# Questions:
# 1. Why would final_cost cause an error?
# Answer: python cannot subtract 20 from 199 because 199 is stored as a string
#
# 2. What data type is monthly_cost currently?
# Answer: string
#
# 3. What data type should monthly_cost be if we want to do maths with it?
# Answer: int
#
# 4. Rewrite the monthly_cost line correctly below:
# monthly_cost = 199
#


# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete the function below.
#
# It must create these three variables:
# - subscription_name = "Spotify"
# - monthly_cost = 69
# - is_active = True
#
# Then it must return this exact sentence:
# "Spotify costs R69 per month. Active: True"

def create_basic_subscription_summary():
   subscription_name = "Spotify"
   monthly_cost = 69
   is_active = True


    # Return the final sentence here
   return f"{subscription_name} costs R{monthly_cost} per month. Active: {is_active}"


result = create_basic_subscription_summary()
print(result)
# Expected output: Spotify costs R69 per month. Active: True


# Task 2:
# Complete the function below.
#
# It must return only the subscription name.
# Expected return value:
# "Netflix"

def get_subscription_name():
    subscription_name = "Netflix"

    return subscription_name


result = get_subscription_name()
print(result)
# Expected output: Netflix


# Task 3:
# Complete the function below.
#
# It must return only the monthly cost.
# Expected return value:
# 199

def get_monthly_cost():
    monthly_cost = 199

    return monthly_cost


result = get_monthly_cost()
print(result)
# Expected output: 199


# ============================================================
# 5. PYTEST SECTION
# ============================================================

"""
These tests check your return values.

Important:
pytest does not care what your function prints.
pytest checks what your function returns.
"""

def test_create_basic_subscription_summary():
    assert create_basic_subscription_summary() == "Spotify costs R69 per month. Active: True"


def test_get_subscription_name():
    assert get_subscription_name() == "Netflix"


def test_get_monthly_cost():
    assert get_monthly_cost() == 199


# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Even simple display logic can become risky if we trust bad input.

Questions:

1. What could go wrong if monthly_cost is stored as text instead of a number?
Answer: the system will give incorrect data as the Math will be wrong because the string number will be seen as None,
we should create an error saysing that and the data needs to be an int

2. What could go wrong if subscription_name is empty?
Answer: the system wont know what the number belongs to so we will need to error to say incomplete information

3. Should a real app trust subscription data directly from a user form?
Answer: no

4. Why is it safer to validate data before displaying or saving it?
Answer: to keep data integraty and accuracy
"""


# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task:
Only do this if the main tasks felt comfortable.

This task practises function parameters.

A parameter is a value a function receives.

Example:

def greet(name):
    return f"Hello {name}"

result = greet("Hendre")
print(result)
# Output: Hello Hendre
"""


# Stretch:
# Complete the function below.
#
# It must accept:
# - subscription_name
# - monthly_cost
# - is_active
#
# It must return the same kind of sentence:
# "Canva costs R120 per month. Active: True"

def create_subscription_summary(subscription_name, monthly_cost, is_active):
    return f"{subscription_name} costs R{monthly_cost} per month. Active: {is_active}"


result = create_subscription_summary("Canva", 120, True)
print(result)
# Expected output: Canva costs R120 per month. Active: True


# Extra stretch:
# Call create_subscription_summary again with:
# - "YouTube Premium"
# - 72
# - False
#
# Then print the result.
#
def create_subscription_summary(subscription_name, monthly_cost, is_active):
    return f"{subscription_name} costs R{monthly_cost} per month. Active: {is_active}"


result = create_subscription_summary("Youtube Premium", 72, False)
print(result)

# Expected output:
# YouTube Premium costs R72 per month. Active: False


# ============================================================
# 8. DAILY REFLECTION
# ============================================================

"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
Answer: today seemed very similar to day 1 in the questions. i got lost a bit in a few sections that i think you can add a bit of clarity on in the pre lesson for it, for example add a how we create the pytest for it and give a small lesson then we write the pytest

2. What part took the longest to reason through?
Answer: today was more of a copy and paste of day 1 so i moved faily fast through everything

3. What bug or risk did I spot?
Answer: i spotted the same string/int bug and the same security/data issues

4. What is the difference between print and return?
Answer: print gives you a value on you screen where return stores the data that will need to be called by a print to see the data 

5. Which pytest case would I add next?
Answer: my pytests are really weak right now and dont really understand them all to well

6. What should tomorrow become?
   - easier reinforcement
   - same level with more practice
   - harder/stretch level

Answer: tomorrow can be a similar dificulty but with more direction before we just send me off to do things. we are getting closer to the right style that will help me a lot
"""