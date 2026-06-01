# ============================================================
# Day 118: Final build part 3
# App: In-house Subscription Tracker
# End Goal: High-intermediate Python developer level
# Difficulty Mode: Ground-up but adaptive
# Main Focus: reports and imports
# App Feature: Assemble reporting/import logic
# ============================================================

"""
How to use this file in VS Code:

1. Read the teaching section.
2. Read the code and answer the questions in comments or in your own notes.
3. Try the bug spotting section before looking anything up.
4. Complete or modify the writing tasks.
5. Run the file with:
   python Day_118.py

6. Later, run pytest with:
   pytest Day_118.py

Adaptive rule:
- If this feels easy without help, complete the stretch task.
- If this feels hard, write down exactly where you got stuck.
- When you paste your completed work for marking, the next lesson can be adjusted.
"""


# ============================================================
# 1. TEACHING SECTION
# ============================================================

"""
Today works at high-intermediate backend-prep level.

Main idea:
- reports and imports
- App feature: Assemble reporting/import logic

You are now combining validation, permissions, service flow, reporting, and tests.
This is the kind of thinking used before moving into FastAPI routes and real databases.
"""


# ============================================================
# 2. CODE READING SECTION
# ============================================================

class InMemorySubscriptionRepository:
    def __init__(self):
        self.subscriptions = []
        self.next_id = 1

    def create(self, payload):
        record = payload.copy()
        record["id"] = self.next_id
        self.next_id += 1
        self.subscriptions.append(record)
        return record

    def list_all(self):
        return self.subscriptions.copy()


def create_subscription_service(repository, payload, current_user):
    if not payload.get("name"):
        return {"success": False, "error": "Name is required", "data": None}

    if payload.get("cost", 0) <= 0:
        return {"success": False, "error": "Cost must be greater than 0", "data": None}

    record = {
        "name": payload["name"],
        "cost": payload["cost"],
        "active": True,
        "user_id": current_user["id"],
    }

    created = repository.create(record)
    return {"success": True, "error": None, "data": created}


# Questions:
# 1. What responsibility does the repository have?
# 2. What responsibility does the service function have?
# 3. Why is this easier to test than mixing everything together?



# ============================================================
# 3. BUG SPOTTING SECTION
# ============================================================

def update_subscription_service(repository, subscription_id, payload, current_user):
    subscription = repository.get_by_id(subscription_id)

    subscription["name"] = payload["name"]
    subscription["cost"] = payload["cost"]

    return {"success": True, "data": subscription, "error": None}

# Bug questions:
# 1. What happens if get_by_id returns None?
# 2. What validation is missing?
# 3. What permission check is missing?
# 4. What audit logging might be useful here?



# ============================================================
# 4. WRITING / CODING PRACTICE
# ============================================================

# Task 1:
# Complete this high-intermediate service flow.

def validate_subscription_payload(payload):
    errors = []

    if not payload.get("name"):
        errors.append("Name is required")

    if payload.get("cost", 0) <= 0:
        errors.append("Cost must be greater than 0")

    return errors


def user_can_create_subscription(current_user):
    return current_user.get("role") in ["user", "admin"]


def create_subscription_record(payload, current_user):
    return {
        "name": payload["name"],
        "cost": payload["cost"],
        "active": True,
        "category": payload.get("category", "General"),
        "user_id": current_user["id"],
    }


def create_subscription_service(repository, payload, current_user):
    if not user_can_create_subscription(current_user):
        return {"success": False, "data": None, "error": "Not allowed"}

    errors = validate_subscription_payload(payload)
    if errors:
        return {"success": False, "data": None, "error": errors}

    record = create_subscription_record(payload, current_user)
    created = repository.create(record)

    return {"success": True, "data": created, "error": None}


class FakeRepository:
    def __init__(self):
        self.records = []
        self.next_id = 1

    def create(self, record):
        saved = record.copy()
        saved["id"] = self.next_id
        self.next_id += 1
        self.records.append(saved)
        return saved


repo = FakeRepository()
result = create_subscription_service(
    repo,
    {"name": "Canva", "cost": 120, "category": "Design"},
    {"id": 10, "role": "user"},
)
print(result)
# Expected output: success response with saved Canva subscription



# ============================================================
# 5. PYTEST SECTION
# ============================================================

def test_create_subscription_service_creates_valid_subscription():
    repo = FakeRepository()
    payload = {"name": "Canva", "cost": 120, "category": "Design"}
    current_user = {"id": 10, "role": "user"}

    result = create_subscription_service(repo, payload, current_user)

    assert result["success"] is True
    assert result["data"]["id"] == 1
    assert result["data"]["name"] == "Canva"
    assert result["data"]["user_id"] == 10


def test_create_subscription_service_rejects_missing_name():
    repo = FakeRepository()
    payload = {"name": "", "cost": 120}
    current_user = {"id": 10, "role": "user"}

    result = create_subscription_service(repo, payload, current_user)

    assert result["success"] is False
    assert "Name is required" in result["error"]


def test_create_subscription_service_rejects_negative_cost():
    repo = FakeRepository()
    payload = {"name": "Canva", "cost": -1}
    current_user = {"id": 10, "role": "user"}

    result = create_subscription_service(repo, payload, current_user)

    assert result["success"] is False
    assert "Cost must be greater than 0" in result["error"]


def test_create_subscription_service_rejects_unknown_role():
    repo = FakeRepository()
    payload = {"name": "Canva", "cost": 120}
    current_user = {"id": 10, "role": "guest"}

    result = create_subscription_service(repo, payload, current_user)

    assert result == {"success": False, "data": None, "error": "Not allowed"}



# ============================================================
# 6. WHITE-HAT / SECURITY THINKING SECTION
# ============================================================

"""
Security thinking:
At this level, security is part of the service flow.

Questions:
1. Does this function validate before saving?
2. Does it check permission before saving?
3. Does it avoid trusting user_id from the payload?
4. Does it return controlled errors?
5. What would you log in an audit log?
"""



# ============================================================
# 7. STRETCH TASK
# ============================================================

"""
Stretch task: only do this if the main tasks felt comfortable without help.
"""

# Stretch:
# Add an audit_log list to the repository.
# After creating a subscription, save:
# {"action": "subscription_created", "user_id": current_user["id"], "subscription_id": created["id"]}
#
# Then add a pytest test that proves the audit log entry was created.




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

