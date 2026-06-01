# ============================================================
# Day 1: Subscription basics with variables
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: variables, strings, numbers, booleans
# App Feature: Create simple subscription values
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code and answer the questions in comments or in your own notes.
3. Try the bug spotting section before looking anything up.
4. Complete or modify the writing tasks.
5. Run the file with:
   python Day_1.py

6. Later, run pytest with:
   pytest Day_1.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today starts small and app-focused.

Main idea:
- variables, strings, numbers, booleans
- App feature: Create simple subscription values

In the Subscription Tracker app, every subscription starts as simple data:
a name, a cost, and whether it is active.

Do not rush. The goal is to understand the code without hints.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

subscription_name = "Netflix"
monthly_cost = 199
is_active = True

print(subscription_name)
print(monthly_cost)
print(is_active)

# Questions:
# 1. What three values are stored?
# 2. What will be printed?
# 3. Which value is a string?
# 4. Which value is a boolean?



# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

monthly_cost = "199"
discount = 20

# Bug question:
# Why would this line be a problem?
# final_cost = monthly_cost - discount



# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Create three variables for a subscription:
# - subscription_name
# - monthly_cost
# - is_active
# Then print them.

def create_basic_subscription_summary():
    subscription_name = "Spotify"
    monthly_cost = 69
    is_active = True

    return f"{subscription_name} costs R{monthly_cost} per month. Active: {is_active}"


result = create_basic_subscription_summary()
print(result)
# Expected output: Spotify costs R69 per month. Active: True



# ============================================================
# 5. PYTEST SECTION
# ============================================================

# Pytest practice:
# To run later: pytest Day_X.py

def test_create_basic_subscription_summary():
    assert create_basic_subscription_summary() == "Spotify costs R69 per month. Active: True"



# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Even simple data can be dangerous if we trust it blindly.

Questions:
1. What if monthly_cost is entered as text instead of a number?
2. What if subscription_name is empty?
3. Should a real app trust values directly from a user form?
"""



# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task: only do this if the main tasks felt comfortable without help.
"""

# Stretch:
# Change the function so it accepts name, cost, and active as parameters.
# Then return the same kind of sentence.




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

