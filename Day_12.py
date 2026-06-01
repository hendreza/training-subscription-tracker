# ============================================================
# Day 12: Adding costs in a list
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: accumulators
# App Feature: Calculate total monthly cost
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code and answer the questions in comments or in your own notes.
3. Try the bug spotting section before looking anything up.
4. Complete or modify the writing tasks.
5. Run the file with:
   python Day_12.py

6. Later, run pytest with:
   pytest Day_12.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today builds practical app logic.

Main idea:
- accumulators
- App feature: Calculate total monthly cost

The Subscription Tracker now works with functions and lists.
A function should do one clear job and return a predictable result.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

def calculate_monthly_total(costs):
    total = 0

    for cost in costs:
        total = total + cost

    return total


example_costs = [199, 69, 120]
result = calculate_monthly_total(example_costs)
print(result)

# Questions:
# 1. What value does total start as?
# 2. How many times does the loop run?
# 3. What is the final result?
# 4. What input could break this function?



# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

def count_active_subscriptions(subscriptions):
    count = 0

    for subscription in subscriptions:
        if subscription["active"] == True:
            count + 1

    return count

# Bug questions:
# 1. Why does count stay 0?
# 2. Which line needs to change?
# 3. What test would catch this?



# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Return the total monthly cost from a list of subscription costs.

def calculate_total_cost(costs):
    total = 0

    for cost in costs:
        total += cost

    return total


result = calculate_total_cost([199, 69, 120])
print(result)
# Expected output: 388


# Task 2:
# Return True if the subscription name exists in the list.

def has_subscription(subscription_names, target_name):
    for name in subscription_names:
        if name == target_name:
            return True

    return False


result = has_subscription(["Netflix", "Spotify", "Canva"], "Canva")
print(result)
# Expected output: True



# ============================================================
# 5. PYTEST SECTION
# ============================================================

def test_calculate_total_cost():
    assert calculate_total_cost([199, 69, 120]) == 388


def test_calculate_total_cost_empty_list():
    assert calculate_total_cost([]) == 0


def test_has_subscription_found():
    assert has_subscription(["Netflix", "Spotify"], "Spotify") is True


def test_has_subscription_not_found():
    assert has_subscription(["Netflix", "Spotify"], "YouTube Premium") is False



# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
A user may submit unexpected values.

Questions:
1. What happens if costs contains "free"?
2. Should negative costs be allowed?
3. Should subscription matching be case-sensitive?
"""



# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task: only do this if the main tasks felt comfortable without help.
"""

# Stretch:
# Write a function that ignores inactive subscriptions when calculating the total.
# Use dictionaries like:
# {"name": "Netflix", "cost": 199, "active": True}




# ============================================================
# 7. DAILY REFLECTION
# ============================================================
"""
Answer these after completing the lesson:

1. What did I understand without looking anything up?
2. What part took the longest to reason through?
3. What bug or risk did I spot?
4. Which pytest case would I add next?
5. What should tomorrow become:
   - easier reinforcement
   - same level with more practice
   - harder/stretch level
"""

