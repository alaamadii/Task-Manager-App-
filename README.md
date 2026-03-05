# Daily Schedule Task Manager

A professional, simple, and intuitive Task Manager application built with Python, Streamlit, and SQLite.

## Overview
This daily schedule manager allows users to easily add, view, update, and delete daily tasks. It implements the "Separation of Concerns" principle by modularizing the application into different components:
- **Presentation Layer (`app.py`)**: Built with Streamlit for a clean and interactive User Interface.
- **Data Access Layer (`database.py`)**: Handles all SQLite database interactions.
- **Utility Layer (`utils.py`)**: Responsible for logic such as date validation to ensure data consistency.

## Features
- **Add Tasks:** Create new tasks with a title, description, status, and due date.
- **View Tasks:** View all your tasks in a clean tabular format. Filter tasks by their current status (To Do, In Progress, Done).
- **Update Tasks:** Modify the title, description, due date, and status of existing tasks.
- **Delete Tasks:** Remove tasks that are no longer needed.

## Demo

Here is a quick look at the application in action:

**Screenshot:**
![Task Manager Screenshot](imeges/photo.png)

**Video Walkthrough:**
You can watch the demo video of this project here: [Demo Video](https://drive.google.com/file/d/1qWHrBKAfkwG3hAOaYvQMkgbn6k5UtX_g/view?usp=drive_link)


## File Structure
```
daily schedule/
│
├── app.py             # Main Streamlit application file (UI & Routing)
├── database.py        # Database creation and CRUD operations
├── utils.py           # Helper functions (e.g., date validation)
├── requirements.txt   # Required Python libraries
├── tasks.db           # SQLite database file (auto-generated upon running)
└── imeges/            # Directory containing demo images and videos
```

## Installation and Setup

### 1. Prerequisites
Ensure you have Python 3.7 or higher installed on your machine.

### 2. Clone the Repository (or navigate to the project directory)
```bash
cd "path/to/daily schedule"
```

### 3. Install Required Libraries
Install the necessary dependencies using the provided `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Streamlit development server:
```bash
streamlit run app.py
```

This will open a new tab in your default web browser displaying the application.
