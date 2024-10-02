# LibraryManagementSystem
The library management system to allow a librarian to track books and their quantity, books issued to members, book fees.

## Setup Instructions

### Requirements:
- Python 3.x
- MySQL
- Virtual Environment

### Steps to Run:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/LibraryManagementSystem.git
   cd LibraryManagementSystem

2. Run the setup script: 
For Linux or MacOS:
	bash
	./setup.sh
For Windows:
	bash
	python -m venv LibraryManagementSystem
	LibraryManagementSystem\Scripts\activate
	pip install -r requirements.txt

3. Create the MySQL database: After the script runs, log into MySQL:
	bash
	mysql -u root -p
	CREATE DATABASE LMS;

4. Configure the database in your Flask app: Update the db_storage.py file or configuration file with your MySQL credentials:
	Python
	'mysql+mysqldb://username:password@localhost/LMS'

5. Run the Flask application:
	bash
	flask run