Voting System Project 

This project demonstrates a simple voting system built using the Django framework. Users can browse polls, cast votes, and view results, while admins can manage poll questions and choices. It's an excellent introduction to Django’s Model-View-Template (MVT) architecture.


---

Features

User Features:

View available polls.

Vote on a poll.

View voting results.


Admin Features:

Create, edit, and delete poll questions and choices.

View detailed poll results.




---

Installation

Follow the steps below to set up and run the project locally:

Prerequisites

Python 3.11 or higher

pip for package management


Steps

1. Clone the repository:

git clone <repository-url>
cd voting_system


2. Install Django:

pip install django


3. Create and configure the Django project:

django-admin startproject voting_system
cd voting_system
python manage.py startapp polls


4. Apply migrations:

python manage.py makemigrations
python manage.py migrate


5. Create a superuser for admin access:

python manage.py createsuperuser


6. Run the server:

python manage.py runserver


7. Access the application in your browser at http://127.0.0.1:8000/.




---

Code Overview

Models (polls/models.py)

Question: Represents a poll question.

Choice: Represents the options for a question and tracks votes.


Views (polls/views.py)

homepage: Displays a welcome message.

index: Lists available polls.

detail: Shows poll details and voting options.

results: Displays voting results.

vote: Handles vote submission.


Templates

Base Template: Includes navigation and layout structure.

Index Page: Displays the list of available polls.

Detail Page: Allows users to cast votes.

Results Page: Shows poll results.



---

File Structure

voting_system/
├── polls/
│   ├── migrations/
│   ├── templates/
│   │   ├── polls/
│   │   │   ├── base.html
│   │   │   ├── index.html
│   │   │   ├── detail.html
│   │   │   ├── results.html
│   ├── static/
│   │   ├── polls/
│   │   │   ├── styles.css
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── voting_system/
│   ├── settings.py
│   ├── urls.py


---

Admin Interface

The admin interface allows you to:

1. Add or delete questions.


2. Add or update choices.


3. View detailed voting statistics.




---

Example Usage

1. Start the development server:

python manage.py runserver


2. Open the browser and navigate to http://127.0.0.1:8000/.


3. Admins can access the admin interface at http://127.0.0.1:8000/admin/.

