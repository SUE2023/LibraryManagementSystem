#!/bin/bash

# Create a virtual environment
python3 -m venv LibraryManagementSystem

# Activate the virtual environment
source LibraryManagementSystem/bin/activate

# Install necessary Python packages
pip install -r requirements.txt

# Install MySQL server (for Linux)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    sudo apt update
    sudo apt install mysql-server
    sudo mysql_secure_installation
    sudo service mysql start
fi

# Install MySQL server (for MacOS using Homebrew)
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew update
    brew install mysql
    brew services start mysql
    mysql_secure_installation
fi

# Prompt to set up the MySQL database
echo "Please log in to MySQL and create the LMS database."
echo "Run the following command in MySQL:"
echo "CREATE DATABASE LMS;"
echo "Don't forget to update the MySQL user and password in your app configuration."

# Inform the user to activate the virtual environment manually if running on Windows
if [[ "$OSTYPE" == "msys" ]]; then
    echo "For Windows: Activate the virtual environment by running 'LibraryManagementSystem\\Scripts\\activate' in cmd"
fi
