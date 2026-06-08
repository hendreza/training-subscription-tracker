# ============================================================
# Day 4: Boolean active status and simple decisions
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: booleans, if statements, True/False return values
# App Feature: Check if a subscription is active
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code reading section and answer the questions.
3. Try the bug spotting section before running the code.
4. Complete the writing tasks yourself.
5. Run the file with:
   python Day_4.py

6. Later, run pytest with:
   pytest Day_4.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today we are learning how to make simple decisions with booleans.

A boolean is either:

True
False

In the Subscription Tracker app, we need booleans for questions like:

- Is this subscription active?
- Should this subscription be included in the monthly total?
- Has this subscription been cancelled?
- Should we show this subscription on the dashboard?

Example:

is_active = True

if is_active:
    print("Subscription is active")
else:
    print("Subscription is inactive")

Important:
A function can also return True or False.

Example:

def is_subscription_active(is_active):
    return is_active

Later, this becomes very important for filtering, permissions, security,
and deciding whether records should be included in reports.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

# Do not edit this section yet.
# Read it and answer the questions.

def is_subscription_active(is_active):
    return is_active


netflix_active = is_subscription_active(True)
old_app_active = is_subscription_active(False)

print(netflix_active)
print(old_app_active)

# Questions:
# 1. What argument is passed into the function the first time?
# Answer: netflix_active
#
# 2. What argument is passed into the function the second time?
# Answer:old_app_active
#
# 3. What will be printed line by line?
# Answer:True
#
# 4. Does this function return a string, number, or boolean?
# Answer:bool
#
# 5. Why would this be useful in a Subscription Tracker app?
# Answer: to determine if the app is in use to add to montly bills or remove it from the calculations
#


# ============================================================
# 3. CODE READING: IF STATEMENT
# ============================================================

def get_subscription_status(is_active):
    if is_active:
        return "Active"

    return "Inactive"


print(get_subscription_status(True))
print(get_subscription_status(False))

# Questions:
# 1. What does get_subscription_status(True) return?
# Answer:"Active"
#
# 2. What does get_subscription_status(False) return?
# Answer:"Inactive"
#
# 3. Why does the function not need an else block?
# Answer:the return is currently acting as an else, so there is no other data transformation taking place. the return, returns the "else" value
#
# 4. What is the difference between returning True and returning "Active"?
# Answer: you can set true to actually mean it is not active. but returning "Active" shows the user what its state actually is
#


# ============================================================
# 4. BUG SPOTTING SECTION
# ============================================================

# Read this code before running it.

def should_count_subscription(is_active):
    if is_active == "True":
        return True

    return False


# Questions:
# 1. What is wrong with comparing is_active to "True"?
# Answer: the "True" is a string value therfore a bool wont read
#
# 2. What data type is "True"?
# Answer: string
#
# 3. What data type is True?
# Answer: bool
#
# 4. What would should_count_subscription(True) return with the current code?
# Answer: i would say either "True" or empty return
#
# 5. Rewrite the condition correctly below:
# if is_active:
#


# ============================================================
# 5. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete the function below.
#
# It must accept:
# - is_active
#
# It must return the same boolean value.
#
# Example:
# check_active_status(True)
# should return True

def check_active_status(is_active):
    if is_active:
        return True
    
    return False


result = check_active_status(True)
print(result)
# Expected output: True


# Task 2:
# Complete the function below.
#
# It must accept:
# - is_active
#
# If is_active is True, return "Active"
# If is_active is False, return "Inactive"

def get_active_status_label(is_active):
    if is_active:
        return "Active"
    
    return "Inactive"


result = get_active_status_label(True)
print(result)
# Expected output: Active

result = get_active_status_label(False)
print(result)
# Expected output: Inactive


# Task 3:
# Complete the function below.
#
# It must accept:
# - monthly_cost
# - is_active
#
# If the subscription is active, return the monthly_cost.
# If the subscription is inactive, return 0.
#
# Example:
# get_counted_monthly_cost(199, True)
# should return 199
#
# get_counted_monthly_cost(199, False)
# should return 0

def get_counted_monthly_cost(monthly_cost, is_active):
    if is_active:
        return monthly_cost
    return 0


result = get_counted_monthly_cost(199, True)
print(result)
# Expected output: 199

result = get_counted_monthly_cost(199, False)
print(result)
# Expected output: 0


# ============================================================
# 6. PYTEST MINI-LESSON
# ============================================================

"""
Today pytest checks boolean results and decision results.

Example:

def is_active(value):
    return value

def test_is_active_true():
    assert is_active(True) is True

def test_is_active_false():
    assert is_active(False) is False

Important:
For booleans, we often use:

is True
is False

This is clearer than:

== True
== False

Both can work, but `is True` and `is False` make your intent obvious.
"""


# ============================================================
# 7. PYTEST SECTION
# ============================================================

def test_check_active_status_true():
    assert check_active_status(True) is True


def test_check_active_status_false():
    assert check_active_status(False) is False


def test_get_active_status_label_active():
    assert get_active_status_label(True) == "Active"


def test_get_active_status_label_inactive():
    assert get_active_status_label(False) == "Inactive"


def test_get_counted_monthly_cost_when_active():
    assert get_counted_monthly_cost(199, True) == 199


def test_get_counted_monthly_cost_when_inactive():
    assert get_counted_monthly_cost(199, False) == 0


# ============================================================
# 8. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Today we are working with True/False values.

A real app must be careful with booleans from user input.

Questions:

1. What could go wrong if a form sends "True" as text instead of True as a boolean?
Answer: the subscription amount might not be added to the bill and the user can either over budget or not pay

2. Should an inactive subscription be included in the monthly total?
Answer:no

3. What could go wrong if a cancelled subscription is still counted as active?
Answer:the user would pay or budget the wrong amount for services he/she no longer uses

4. Why is it dangerous to trust user-submitted active/inactive status without validation?
Answer: this would change the bill/total for the user and they would blame the software, but they corrupted the data

5. In a real app, should a normal user be allowed to set any subscription as active/inactive directly?
Answer: no
"""


# ============================================================
# 9. STRETCH TASK
# ============================================================

"""
Stretch task:
Only do this if the main tasks felt comfortable.

This task combines Day 3 cost calculation with Day 4 boolean decisions.
"""


# Stretch:
# Complete the function below.
#
# It must accept:
# - subscription_name
# - monthly_cost
# - is_active
#
# Rules:
# - If active, return:
#   "Netflix is active and costs R199 per month."
#
# - If inactive, return:
#   "Netflix is inactive and costs R0 per month."

def create_active_cost_summary(subscription_name, monthly_cost, is_active):
    pass


result = create_active_cost_summary("Netflix", 199, True)
print(result)
# Expected output: Netflix is active and costs R199 per month.

result = create_active_cost_summary("Netflix", 199, False)
print(result)
# Expected output: Netflix is inactive and costs R0 per month.


# Optional stretch pytest:

def test_create_active_cost_summary_active():
    assert create_active_cost_summary("Netflix", 199, True) == "Netflix is active and costs R199 per month."


def test_create_active_cost_summary_inactive():
    assert create_active_cost_summary("Netflix", 199, False) == "Netflix is inactive and costs R0 per month."


# ============================================================
# 10. DAILY REFLECTION
# ============================================================

"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
Answer:

2. What part took the longest to reason through?
Answer:

3. What is the difference between True and "True"?
Answer:

4. What is the difference between returning True and returning "Active"?
Answer:

5. Which pytest case made the most sense to me?
Answer:

6. Which pytest case confused me?
Answer:

7. What bug or risk did I spot?
Answer:

8. What should tomorrow become?
   - easier reinforcement
   - same level with more practice
   - harder/stretch level

Answer:
"""