# Assignment Part 3: File I/O, APIs & Exception Handling

Total Marks: 25
Batch: BITSoM_BA_2511392

## Overview

This assignment demonstrates file operations, REST API integration, and exception handling.

## Tasks

Task 1: File Read & Write Basics (6 marks)
- Create python_notes.txt with 5 topics using UTF-8 encoding
- Add 2 additional topics using append mode
- Read file and print numbered lines
- Search file by keyword (case-insensitive)
- File handling with context managers
- String manipulation (strip, lower)
- User input validation

Task 2: API Integration (8 marks)
- Fetch 20 products from DummyJSON API, display in formatted table
- Filter products (rating 2.5 or higher), sort by price descending
- Fetch laptops by category, list name and price
- POST request to create new product, display server response
- GET and POST requests using requests library
- JSON parsing and manipulation
- Data filtering and sorting

Task 3: Exception Handling (7 marks)
- Guarded Calculator: Function safe_divide handles normal division, ZeroDivisionError, and TypeError
- Guarded File Reader: Function read_file_safe handles FileNotFoundError with descriptive error messages
- Demonstrates proper error handling patterns

Task 4: Logging to File (4 marks)
- Logs all errors to error_log.txt with timestamps
- Creates error_log.txt automatically during execution
- Tracks errors from file operations and API requests
- Proper error message formatting with date and time

## Running the Code

python part3_api_files.py

Output includes successful operations, errors, and logged information.

Generated files:
- python_notes.txt: Created by the script with sample topics
- error_log.txt: Created by the script with error logs

## Total Marks: 25
