# ============================================================
# Day 3: Function parameters and basic cost calculations
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: numbers, arithmetic, parameters, return values
# App Feature: Calculate subscription costs
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code reading section and answer the questions.
3. Try the bug spotting section before running the code.
4. Complete the writing tasks yourself.
5. Run the file with:
   python Day_3.py

6. Later, run pytest with:
   pytest Day_3.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today we are moving from fixed values to reusable functions.

Yesterday we had functions like this:

def get_monthly_cost():
    return 199

That works, but it always returns the same value.

Today we use parameters.

A parameter is a value the function receives.

Example:

def calculate_yearly_cost(monthly_cost):
    return monthly_cost * 12

result = calculate_yearly_cost(199)
print(result)

What happens here?

1. monthly_cost receives the value 199
2. The function calculates 199 * 12
3. The function returns the answer
4. print(result) shows the answer on screen

In the Subscription Tracker app, this matters because each subscription can have
a different monthly cost.

Netflix may cost R199.
Spotify may cost R69.
Canva may cost R120.

We do not want a separate function for every subscription.
We want one reusable function that can calculate any subscription.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

# Do not edit this section yet.
# Read it and answer the questions.

def calculate_yearly_cost(monthly_cost):
    return monthly_cost * 12


netflix_yearly_cost = calculate_yearly_cost(199)
spotify_yearly_cost = calculate_yearly_cost(69)

print(netflix_yearly_cost)
print(spotify_yearly_cost)

# Questions:
# 1. What value is passed into the function the first time?
# Answer:199
#
# 2. What value is passed into the function the second time?
# Answer:69
#
# 3. What will be printed line by line?
# Answer:2388, 828
#
# 4. Why is this better than creating a different function for Netflix and Spotify?
# Answer: you have less code overall so less places to have bugs. code reusability is very important
#
# 5. Does calculate_yearly_cost print the answer or return the answer?
# Answer: return
#


# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

# Read this code before running it.

def calculate_discounted_cost(monthly_cost, discount):
    final_cost = monthly_cost - discount
    return final_cost


# This line has a bug:
# result = calculate_discounted_cost("199", 20)

# Questions:
# 1. Why would this cause an error?
# Answer: the math in line "   final_cost = monthly_cost - discount" requiers both items to be ints but he monthly_cost being passed is a string
#
# 2. Which value has the wrong data type?
# Answer:199
#
# 3. Rewrite the function call correctly below:
# result = calculated_discounted_cost(199, 20)
#
# 4. What should the correct result be?
# Answer: 179
#


# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete the function below.
#
# It must accept one parameter:
# - monthly_cost
#
# It must return the yearly cost.
#
# Example:
# calculate_yearly_subscription_cost(100)
# should return 1200

def calculate_yearly_subscription_cost(monthly_cost):
    yearly_cost = monthly_cost * 12
    
    return yearly_cost


result = calculate_yearly_subscription_cost(100)
print(result)
# Expected output: 1200


# Task 2:
# Complete the function below.
#
# It must accept:
# - monthly_cost
# - discount
#
# It must return the monthly cost after discount.
#
# Example:
# calculate_monthly_cost_after_discount(199, 20)
# should return 179

def calculate_monthly_cost_after_discount(monthly_cost, discount):
    monthly_cost_after_discount= monthly_cost - discount
    
    return monthly_cost_after_discount


result = calculate_monthly_cost_after_discount(199, 20)
print(result)
# Expected output: 179


# Task 3:
# Complete the function below.
#
# It must accept:
# - subscription_name
# - monthly_cost
#
# It must return this exact sentence:
# "Netflix costs R199 per month and R2388 per year."
#
# Hint:
# You need to calculate yearly_cost inside the function.

def create_cost_summary(subscription_name, monthly_cost):
    yearly_cost = monthly_cost * 12

    return f"{subscription_name} costs R{monthly_cost} per month and R{yearly_cost} per year."


result = create_cost_summary("Netflix", 199)
print(result)
# Expected output: Netflix costs R199 per month and R2388 per year.


# ============================================================
# 5. PYTEST MINI-LESSON
# ============================================================

"""
Pytest checks if a function returns the value we expect.

Example:

def double_number(number):
    return number * 2

def test_double_number():
    assert double_number(5) == 10

Read that as:

When I call double_number(5),
I expect the returned value to be 10.

If the function returns 10, the test passes.
If the function returns anything else, the test fails.

Important:
pytest checks return values, not print output.
"""


# ============================================================
# 6. PYTEST SECTION
# ============================================================

def test_calculate_yearly_subscription_cost():
    assert calculate_yearly_subscription_cost(100) == 1200


def test_calculate_yearly_subscription_cost_with_netflix_price():
    assert calculate_yearly_subscription_cost(199) == 2388


def test_calculate_monthly_cost_after_discount():
    assert calculate_monthly_cost_after_discount(199, 20) == 179


def test_create_cost_summary():
    assert create_cost_summary("Netflix", 199) == "Netflix costs R199 per month and R2388 per year."


# ============================================================
# 7. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Today we are working with numbers.

A real app should not blindly trust numbers from a user form.

Questions:

1. What could go wrong if monthly_cost is entered as "199" instead of 199?
Answer: the app will not get the right data and the numbers will be wrong that end up being retuerned to the user

2. What could go wrong if monthly_cost is -50?
Answer: the any direct math will only make the number go more negative ( the company owes you money technically is what is being said then)

3. What could go wrong if discount is bigger than monthly_cost?
Example:
monthly_cost = 100
discount = 150

Answer: the discount being bigger would mean that the comapy needs to pay you, and the cost would be nagative

4. Should a subscription tracker allow a negative final monthly cost?
Answer: no

5. What validation rule could we add later to protect this?
Answer: we could a monthly_cost !< 0
"""


# ============================================================
# 8. STRETCH TASK
# ============================================================

"""
Stretch task:
Only do this if the main tasks felt comfortable.

This task introduces basic defensive validation.

For now, keep it simple.
"""


# Stretch:
# Complete the function below.
#
# Rules:
# - If monthly_cost is less than 0, return "Invalid monthly cost"
# - If discount is less than 0, return "Invalid discount"
# - If discount is greater than monthly_cost, return "Discount too high"
# - Otherwise, return the discounted cost

def calculate_safe_discounted_cost(monthly_cost, discount):
    monthly_discount = monthly_cost - discount
    if monthly_cost < 0:
        return "Invalid monthly costs"
    elif discount < 0:
        return "Invalid discount"
    elif discount > monthly_cost:
        return " Discount too high"
    else:
        return monthly_discount


result = calculate_safe_discounted_cost(199, 20)
print(result)
# Expected output: 179

result = calculate_safe_discounted_cost(100, 150)
print(result)
# Expected output: Discount too high


# Optional stretch pytest:

def test_calculate_safe_discounted_cost_valid():
    assert calculate_safe_discounted_cost(199, 20) == 179


def test_calculate_safe_discounted_cost_discount_too_high():
    assert calculate_safe_discounted_cost(100, 150) == "Discount too high"


def test_calculate_safe_discounted_cost_negative_monthly_cost():
    assert calculate_safe_discounted_cost(-50, 10) == "Invalid monthly cost"


def test_calculate_safe_discounted_cost_negative_discount():
    assert calculate_safe_discounted_cost(100, -10) == "Invalid discount"


# ============================================================
# 9. DAILY REFLECTION
# ============================================================

"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
Answer: i understand how to pass the variables into a function to make the code reusable

2. What part took the longest to reason through?
Answer: the stretch task was a bit challanging i think

3. What is the difference between a parameter and an argument?
Answer: argument is perminantly stated and paramater is user added

4. What is the difference between print and return?
Answer: print shows on screen vlaue, return is what the function calculates/ the result of what the function did, you need a print to see the result on screen though

5. What bug or risk did I spot?
Answer: the same style string bug, but within the paramaters being passed

6. Which pytest case made the most sense to me?
Answer: the pytest still feel a bit off, i found it cool the the assert works as " use this function with this value and it should return this " 

7. Which pytest case confused me?
Answer: i am not quite sure how this is evolving, will we eventually get to the point where we cant really give a value but we can still test the code

8. What should tomorrow become?
   - easier reinforcement
   - same level with more practice
   - harder/stretch level

Answer: we seem to be at a good flow, now we start moving and adapting the difficulties and practices so we reach our goal
"""