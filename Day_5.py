# ============================================================
# Day 5: If/else decisions and included subscription costs
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: if/else decision making, arguments, return values
# App Feature: Decide whether to include inactive subscriptions
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code reading section and answer the questions.
3. Try the bug spotting section before running the code.
4. Complete the writing tasks yourself.
5. Run the file with:
   python Day_5.py

6. Later, run pytest with:
   pytest Day_5.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today we are focusing on if/else decisions.

In the Subscription Tracker app, we often need to decide:

- Should this subscription be counted?
- Should this subscription be skipped?
- Should we return the real monthly cost?
- Should we return 0?

Example:

def get_counted_cost(monthly_cost, is_active):
    if is_active:
        return monthly_cost
    else:
        return 0

If the subscription is active, we count the cost.
If the subscription is inactive, we return 0.

Important recap from Day 4:

def check_active_status(is_active):
    return is_active

result = check_active_status(True)

In this line:

result = check_active_status(True)

- True is the argument passed into the function.
- is_active is the parameter inside the function.
- result is the variable that stores the returned value.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

# Do not edit this section yet.
# Read it and answer the questions.

def get_counted_cost(monthly_cost, is_active):
    if is_active:
        return monthly_cost
    else:
        return 0


netflix_cost = get_counted_cost(199, True)
old_app_cost = get_counted_cost(99, False)

print(netflix_cost)
print(old_app_cost)

# Questions:
# 1. What arguments are passed into the function the first time?
# Answer:199, True
#
# 2. What arguments are passed into the function the second time?
# Answer:99, false
#
# 3. What value is stored in netflix_cost?
# Answer:199
#
# 4. What value is stored in old_app_cost?
# Answer:0
#
# 5. What will be printed line by line?
# Answer:199, 0
#
# 6. Why does the inactive subscription return 0?
# Answer: the code  looks for is_active and it is Flase so it does not meet the requiremts to return the monthly_cost, so it returns 0
#


# ============================================================
# 3. CODE READING: IF/ELSE FLOW
# ============================================================

def get_subscription_message(subscription_name, is_active):
    if is_active:
        return f"{subscription_name} is active."

    return f"{subscription_name} is inactive."


print(get_subscription_message("Netflix", True))
print(get_subscription_message("Old App", False))

# Questions:
# 1. What does get_subscription_message("Netflix", True) return?
# Answer: Netflix is active
#
# 2. What does get_subscription_message("Old App", False) return?
# Answer: Old App is inactive
#
# 3. Why does the function not need an else block after the first return?
# Answer: the code is looking at 1 item in total, if there a second " calculation"/check you would need an else block
#
# 4. What is the parameter name that receives "Netflix"?
# Answer:subscription_name
#
# 5. What is the parameter name that receives True?
# Answer:is_active
#


# ============================================================
# 4. BUG SPOTTING SECTION
# ============================================================

# Read this code before running it.

def should_include_cost(is_active):
    if is_active == False:
        return True
    else:
        return False


# Questions:
# 1. What is this function supposed to decide?
# Answer: it is supposed to find out if the monthly_cost of an item should be added to the monthly bill or skipped
#
# 2. Why is the logic wrong?
# Answer: if you account is inactive it returns true but means to return inactive, else it is return its false but wants to return it is active
#
# 3. What does should_include_cost(True) currently return?
# Answer: False
#
# 4. What should should_include_cost(True) return?
# Answer: True
#
# 5. Rewrite the function correctly below in your own words or code:
# Answer: 
#
# def should_include_cost(is_active):
#     if is_active:
#         return True
    
#     return False


# ============================================================
# 5. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete the function below.
#
# It must accept:
# - is_active
#
# If is_active is True, return True.
# If is_active is False, return False.
#
# This is simple, but it reinforces boolean returns.

def should_include_subscription(is_active):
    if is_active:
        return True
    return False


result = should_include_subscription(True)
print(result)
# Expected output: True

result = should_include_subscription(False)
print(result)
# Expected output: False


# Task 2:
# Complete the function below.
#
# It must accept:
# - monthly_cost
# - is_active
#
# If active, return monthly_cost.
# If inactive, return 0.

def get_included_monthly_cost(monthly_cost, is_active):
    if is_active:
        return monthly_cost
    return 0


result = get_included_monthly_cost(199, True)
print(result)
# Expected output: 199

result = get_included_monthly_cost(199, False)
print(result)
# Expected output: 0


# Task 3:
# Complete the function below.
#
# It must accept:
# - subscription_name
# - monthly_cost
# - is_active
#
# If active, return:
# "Netflix is active and counts as R199."
#
# If inactive, return:
# "Netflix is inactive and counts as R0."

def create_included_cost_message(subscription_name, monthly_cost, is_active):
    if is_active:
        return f"{subscription_name} is active and counts as R{monthly_cost}"
    return f"{subscription_name} is inactive and counts a R0"


result = create_included_cost_message("Netflix", 199, True)
print(result)
# Expected output: Netflix is active and counts as R199.

result = create_included_cost_message("Netflix", 199, False)
print(result)
# Expected output: Netflix is inactive and counts as R0.


# ============================================================
# 6. PYTEST MINI-LESSON
# ============================================================

"""
Today pytest checks both sides of an if/else decision.

That means every decision usually needs at least two tests:

1. One test for the True path
2. One test for the False path

Example:

def get_label(is_active):
    if is_active:
        return "Active"

    return "Inactive"


def test_get_label_active():
    assert get_label(True) == "Active"


def test_get_label_inactive():
    assert get_label(False) == "Inactive"

Why two tests?

Because this function has two possible paths:
- active path
- inactive path

If we only test one path, the other path might be broken without us knowing.
"""


# ============================================================
# 7. PYTEST SECTION
# ============================================================

def test_should_include_subscription_true():
    assert should_include_subscription(True) is True


def test_should_include_subscription_false():
    assert should_include_subscription(False) is False


def test_get_included_monthly_cost_active():
    assert get_included_monthly_cost(199, True) == 199


def test_get_included_monthly_cost_inactive():
    assert get_included_monthly_cost(199, False) == 0


def test_create_included_cost_message_active():
    assert create_included_cost_message("Netflix", 199, True) == "Netflix is active and counts as R199."


def test_create_included_cost_message_inactive():
    assert create_included_cost_message("Netflix", 199, False) == "Netflix is inactive and counts as R0."


# ============================================================
# 8. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Today we are deciding what data should be counted.

This matters because bad decisions create bad reports.

Questions:

1. What could go wrong if inactive subscriptions are included in the monthly total?
Answer: the users bill is incorrect and would be paying for things not in use

2. What could go wrong if active subscriptions are accidentally excluded?
Answer: the user would miss payments and the app would be shut down

3. What could go wrong if a user sends "False" as text instead of False as a boolean?
Answer: the app would not know if is_active is true or flase so the app should error

4. Should the app trust a user's submitted active/inactive value without checking it?
Answer: no

5. Later, what rule should we add before letting a user change active/inactive status?
Answer: we will need to make sure it for that user only not across all users
"""


# ============================================================
# 9. STRETCH TASK
# ============================================================

"""
Stretch task:
Only do this if the main tasks felt comfortable.

This task combines:
- if/else
- booleans
- cost calculation
- simple validation
"""


# Stretch:
# Complete the function below.
#
# Rules:
# - If monthly_cost is less than 0, return "Invalid monthly cost"
# - If is_active is not True or False, return "Invalid active status"
# - If active, return monthly_cost
# - If inactive, return 0
#
# Hint:
# To check if something is not a boolean, you can use:
#
# type(is_active) is not bool

def get_safe_included_monthly_cost(monthly_cost:int , is_active:bool):
    if monthly_cost < 0:
        return "Invalid monthly cost"
    if is_active:
        return monthly_cost
    return 0


result = get_safe_included_monthly_cost(199, True)
print(result)
# Expected output: 199

result = get_safe_included_monthly_cost(199, False)
print(result)
# Expected output: 0

result = get_safe_included_monthly_cost(-50, True)
print(result)
# Expected output: Invalid monthly cost

result = get_safe_included_monthly_cost(199, "True")
print(result)
# Expected output: Invalid active status


# Optional stretch pytest:

def test_get_safe_included_monthly_cost_active():
    assert get_safe_included_monthly_cost(199, True) == 199


def test_get_safe_included_monthly_cost_inactive():
    assert get_safe_included_monthly_cost(199, False) == 0


def test_get_safe_included_monthly_cost_negative_cost():
    assert get_safe_included_monthly_cost(-50, True) == "Invalid monthly cost"


def test_get_safe_included_monthly_cost_invalid_active_status():
    assert get_safe_included_monthly_cost(199, "True") == "Invalid active status"


# ============================================================
# 10. DAILY REFLECTION
# ============================================================

"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
Answer: not much new today, we combined some more complex code from earlier days to the new knowledge

2. What part took the longest to reason through?
Answer: the last question on security and the stretch task

3. What is the difference between an argument and a returned value?
Answer: argument is the valuse a user puts in the function and a return is what the function calculates

4. Why should we test both the True path and the False path?
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