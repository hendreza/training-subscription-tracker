# ============================================================
# Day 85: Rate-limit thinking
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: basic abuse prevention
# App Feature: Count repeated actions
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code and answer the questions in comments or in your own notes.
3. Try the bug spotting section before looking anything up.
4. Complete or modify the writing tasks.
5. Run the file with:
   python Day_85.py

6. Later, run pytest with:
   pytest Day_85.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today introduces stronger app architecture thinking.

Main idea:
- basic abuse prevention
- App feature: Count repeated actions

The Subscription Tracker now has users, permissions, reports, and safer service-style functions.
The goal is not just code that works, but code that is testable and secure.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

def user_can_view_subscription(current_user, subscription):
    if current_user.get("role") == "admin":
        return True

    return subscription.get("user_id") == current_user.get("id")


current_user = {"id": 10, "role": "user"}
subscription = {"id": 1, "name": "Netflix", "user_id": 10}

print(user_can_view_subscription(current_user, subscription))

# Questions:
# 1. Why can an admin view all subscriptions?
# 2. Why do normal users need matching user_id?
# 3. What security bug happens if we forget this check?



# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

def get_subscription_for_user(subscriptions, subscription_id, current_user):
    for subscription in subscriptions:
        if subscription["id"] == subscription_id:
            return subscription

    return None

# Bug questions:
# 1. What access control check is missing?
# 2. How could this leak another user's data?
# 3. What should happen if the user does not own the subscription?



# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Return only the subscriptions that the current user is allowed to view.

def user_can_view_subscription(current_user, subscription):
    if current_user.get("role") == "admin":
        return True

    return subscription.get("user_id") == current_user.get("id")


def filter_visible_subscriptions(subscriptions, current_user):
    visible = []

    for subscription in subscriptions:
        if user_can_view_subscription(current_user, subscription):
            visible.append(subscription)

    return visible


sample_subscriptions = [
    {"id": 1, "name": "Netflix", "user_id": 10, "cost": 199},
    {"id": 2, "name": "Spotify", "user_id": 20, "cost": 69},
]

result = filter_visible_subscriptions(sample_subscriptions, {"id": 10, "role": "user"})
print(result)
# Expected output: [{"id": 1, "name": "Netflix", "user_id": 10, "cost": 199}]


# Task 2:
# Build a safe response shape.

def success_response(data):
    return {"success": True, "data": data, "error": None}


def error_response(message):
    return {"success": False, "data": None, "error": message}



# ============================================================
# 5. PYTEST SECTION
# ============================================================

def test_user_can_view_own_subscription():
    user = {"id": 10, "role": "user"}
    subscription = {"id": 1, "user_id": 10}

    assert user_can_view_subscription(user, subscription) is True


def test_user_cannot_view_other_users_subscription():
    user = {"id": 10, "role": "user"}
    subscription = {"id": 1, "user_id": 20}

    assert user_can_view_subscription(user, subscription) is False


def test_admin_can_view_any_subscription():
    admin = {"id": 99, "role": "admin"}
    subscription = {"id": 1, "user_id": 20}

    assert user_can_view_subscription(admin, subscription) is True


def test_filter_visible_subscriptions_for_normal_user():
    subscriptions = [
        {"id": 1, "name": "Netflix", "user_id": 10, "cost": 199},
        {"id": 2, "name": "Spotify", "user_id": 20, "cost": 69},
    ]

    result = filter_visible_subscriptions(subscriptions, {"id": 10, "role": "user"})

    assert result == [{"id": 1, "name": "Netflix", "user_id": 10, "cost": 199}]



# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
This is one of the most important backend skills.

Questions:
1. What is the risk of trusting subscription_id alone?
2. Why must we check ownership on read, update, and archive?
3. Why should error messages not reveal whether another user's record exists?
"""



# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task: only do this if the main tasks felt comfortable without help.
"""

# Stretch:
# Write get_visible_subscription_by_id().
# It should return:
# - success_response(subscription) if found and allowed
# - error_response("Subscription not found") otherwise
#
# Do not reveal whether a forbidden subscription exists.




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

