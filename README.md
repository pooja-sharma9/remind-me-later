# Remind Me Later

This project is a Django-based API that allows users to create reminders with a date, time, message, and method (SMS or Email). It does not handle actual message delivery. It only saves the reminder data to the database.


### How to Run This Project

Follow the steps below to clone and run the project.

### 1. Clone the Repository
#
### 2. Create and Activate Virtual Environment
#

If you don't have `venv` created:

python -m venv venv

#### Activate the virtual environment:
##### On Windows:
venv\scripts\activate

### 3. Install Dependencies
#
Install the required packages:

pip install -r requirements.txt

### 4. Run Migrations
#
python manage.py makemigrations
python manage.py migrate

### 5. Run the Development Server
#
Start the server:

python manage.py runserver

### 6. Access the API
#
Once the server is running, you can access the POST API at:

### For Creating
#
http://127.0.0.1:8000/api/reminders/

### JSON:
{
  "date": "2025-05-15",
  "time": "10:30:00",
  "message": "Meeting with team",
  "reminder_method": "Email"
}

#### For Viewing
#
http://127.0.0.1:8000/api/reminders/all/

### 7. Viewing and Interacting with SQLite Database
#
#### Step 1: Open the SQLite Shell
sqlite3 db.sqlite3
#
#### Step 2: List tables
.tables
#
#### Step 3: View the schema of their custom table (`reminders_reminder`)
.schema reminders_reminder
#
#### Step 4: See all the data in the `reminders_reminder` table
SELECT * FROM reminders_reminder;
#
#### Step 5: To exit the SQLite shell
.quit
#

