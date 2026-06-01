# ============================================================
# Day 43: IDs and generated records
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: simple id generation
# App Feature: Assign subscription ids
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code and answer the questions in comments or in your own notes.
3. Try the bug spotting section before looking anything up.
4. Complete or modify the writing tasks.
5. Run the file with:
   python Day_43.py

6. Later, run pytest with:
   pytest Day_43.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today moves into realistic backend-style data.

Main idea:
- simple id generation
- App feature: Assign subscription ids

The app now uses dictionaries to represent subscription records.
This is closer to how API payloads and database rows feel in Python.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

def find_subscription_by_id(subscriptions, subscription_id):
    for subscription in subscriptions:
        if subscription.get("id") == subscription_id:
            return subscription

    return None


subscriptions = [
    {"id": 1, "name": "Netflix", "cost": 199, "active": True},
    {"id": 2, "name": "Spotify", "cost": 69, "active": True},
]

result = find_subscription_by_id(subscriptions, 2)
print(result)

# Questions:
# 1. Why is .get("id") safer than subscription["id"]?
# 2. What is returned if id 2 is found?
# 3. What is returned if no record is found?



# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

def calculate_active_total(subscriptions):
    total = 0

    for subscription in subscriptions:
        if subscription["active"]:
            total += subscription["amount"]

    return total

# Bug questions:
# 1. What key does this function expect for cost?
# 2. What happens if the records use "cost" instead of "amount"?
# 3. How could a test reveal this mismatch?



# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Find a subscription by name. Return the dictionary if found.
# Return None if not found.

def find_subscription_by_name(subscriptions, target_name):
    for subscription in subscriptions:
        if subscription.get("name") == target_name:
            return subscription

    return None


sample_subscriptions = [
    {"id": 1, "name": "Netflix", "cost": 199, "active": True},
    {"id": 2, "name": "Spotify", "cost": 69, "active": True},
]

result = find_subscription_by_name(sample_subscriptions, "Netflix")
print(result)
# Expected output: {"id": 1, "name": "Netflix", "cost": 199, "active": True}


# Task 2:
# Validate that a subscription has a name and a cost greater than 0.

def is_valid_subscription(subscription):
    if not subscription.get("name"):
        return False

    if subscription.get("cost", 0) <= 0:
        return False

    return True


result = is_valid_subscription({"name": "Canva", "cost": 120})
print(result)
# Expected output: True



# ============================================================
# 5. PYTEST SECTION
# ============================================================

def test_find_subscription_by_name_found():
    subscriptions = [
        {"id": 1, "name": "Netflix", "cost": 199, "active": True},
        {"id": 2, "name": "Spotify", "cost": 69, "active": True},
    ]

    assert find_subscription_by_name(subscriptions, "Spotify") == {
        "id": 2,
        "name": "Spotify",
        "cost": 69,
        "active": True,
    }


def test_find_subscription_by_name_missing():
    assert find_subscription_by_name([], "Netflix") is None


def test_is_valid_subscription_accepts_valid_record():
    assert is_valid_subscription({"name": "Canva", "cost": 120}) is True


def test_is_valid_subscription_rejects_missing_name():
    assert is_valid_subscription({"name": "", "cost": 120}) is False


def test_is_valid_subscription_rejects_zero_cost():
    assert is_valid_subscription({"name": "Canva", "cost": 0}) is False



# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
Dictionary records often come from user input or API requests.

Questions:
1. Why should missing keys not crash the app?
2. Why should cost be validated before saving?
3. What could go wrong if users can submit any category or vendor value?
"""



# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task: only do this if the main tasks felt comfortable without help.
"""

# Stretch:
# Return a validation result like:
# {"valid": False, "errors": ["Name is required"]}
# instead of only True or False.




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

