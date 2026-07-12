# MyLibrary

![Version](https://img.shields.io/badge/version-0.5-blue)
![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Flask](https://img.shields.io/badge/flask-2.x-green)
![SQLite](https://img.shields.io/badge/sqlite-3.x-lightgrey)
![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=GitHub)

## Overview

MyLibrary is a web application built with Python and Flask that helps users organize their personal book collections.

The project is being developed as a long-term learning project focused on web development, databases, and software engineering. Future versions will introduce additional features, including artificial intelligence, as the project grows.

Its primary goal is to provide a simple and intuitive way to organize books while serving as a practical way to learn how real database-driven web applications are built.

---

## Current Version

**Version 0.5 – Library Management**

**Current Status:** ✅ Completed

---

## Features

### User Interface
- Modern dark-themed interface
- Homepage with book listings
- Add Book page with form
- Edit Book page with pre-filled data
- Responsive layout
- Navigation between pages
- Color-coded status badges

### Book Management
- Add new books with all details
- Store book title, author, publisher, and page count
- Track reading status (read, reading, waiting)
- Edit existing books with pre-filled forms
- Update all book fields including status
- Display all saved books on the homepage
- Color-coded status indicators:
  - 🟢 **Read** – Green badge
  - 🟡 **Reading** – Yellow badge
  - 🔴 **Waiting** – Red badge

### Database
- SQLite database integration
- Books table with proper schema
- Status column with default 'waiting'
- Automatic ID generation
- Persistent storage
- Read data from SQLite
- Dynamic homepage generated from database contents

---

## Technologies Used

### Backend
- Python 3.x
- Flask 2.x
- SQLite 3

### Frontend
- HTML5
- CSS3

### Tools & Version Control
- Visual Studio Code
- Git
- GitHub
- DB Browser for SQLite

---

## Project Structure

```text
MyLibrary/
├── app.py                      # Flask application
├── library.db                  # SQLite database
├── README.md                   # Project documentation
├── .gitignore                  # Git ignore file
├── templates/
│   ├── index.html              # Homepage with book list
│   ├── add_book.html           # Add book form
│   └── edit_book.html          # Edit book form
└── static/
    └── style.css               # Dark theme styling