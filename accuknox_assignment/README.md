# AccuKnox Django Trainee Assignment

## Candidate

**Name:** Prabhavati Sagar

## Introduction

This project is my solution for the AccuKnox Django Trainee assignment. In this assignment, I implemented the required Django Signals examples and a custom Python Rectangle class.

---

# Technologies Used

* Python 3.8
* Django 4.2
* SQLite
* PyCharm

---

# How to Run the Project

1. Install Django.

```bash
pip install django
```

2. Apply migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Start the Django server.

```bash
python manage.py runserver
```

4. Open the following URLs in your browser:

* `http://127.0.0.1:8000/sync/`
* `http://127.0.0.1:8000/thread/`
* `http://127.0.0.1:8000/transaction/`

---

# Question 1

### Are Django signals synchronous or asynchronous by default?

From my implementation and testing, I observed that Django signals execute **synchronously** by default.

To verify this, I added a 5-second delay inside the signal using `time.sleep(5)`. When I created an Employee object, the browser waited for the signal to complete before showing the response.

**Output**

```
Execution Time: 5.03 seconds
```

**Conclusion**

The response was returned only after the signal finished executing. This shows that Django signals are synchronous by default.

---

# Question 2

### Do Django signals run in the same thread as the caller?

To verify this, I printed the thread ID in both the view and the signal.

The thread IDs were the same.

**Conclusion**

Based on the output, I concluded that Django signals run in the same thread as the caller by default.

---

# Question 3

### Do Django signals run in the same database transaction as the caller?

To test this, I used `transaction.atomic()` and intentionally raised an exception after creating an Employee object.

The transaction rolled back successfully, and the record count remained unchanged.

**Output**

```
Before: 2
After: 2
```

**Conclusion**

Since the new record was not saved after the rollback, I concluded that Django signals run within the same database transaction as the caller.

---

# Rectangle Class

I created a custom `Rectangle` class that accepts `length` and `width` during initialization.

I implemented the `__iter__()` method so that the object can be iterated.

When iterated, it returns:

```
{'length': 10}
{'width': 5}
```

This satisfies the requirements given in the assignment.

---

# Final Note

I completed all four tasks mentioned in the assignment and tested each implementation before submission.
