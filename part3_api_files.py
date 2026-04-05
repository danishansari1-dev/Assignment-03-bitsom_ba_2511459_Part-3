

import requests
from datetime import datetime
import json

# =====================================================================
# TASK 1: FILE READ & WRITE BASICS (6 marks)
# =====================================================================

print("\n" + "="*70)
print("TASK 1: FILE READ & WRITE BASICS")
print("="*70)

# Part A: Write data to file
print("\n--- PART A: Writing to File ---")
student_notes = [
    "Topic 1: Variables store data. Python is dynamically typed.",
    "Topic 2: Lists are ordered and mutable.",
    "Topic 3: Dictionaries store key-value pairs.",
    "Topic 4: Loops automate repetitive tasks.",
    "Topic 5: Exception handling prevents crashes."
]

# Write initial 5 lines with write mode
try:
    with open("python_notes.txt", "w", encoding="utf-8") as file:
        for note in student_notes:
            file.write(note + "\n")
    print("[OK] Wrote 5 lines to python_notes.txt")
except Exception as e:
    print(f"[ERROR] Error writing to file: {e}")

# Append two more lines with append mode
additional_notes = [
    "Topic 6: Python is fun.",
    "Topic 7: Python can declare results."
]

try:
    with open("python_notes.txt", "a", encoding="utf-8") as file:
        for note in additional_notes:
            file.write(note + "\n")
    print("[OK] Appended 2 additional lines to python_notes.txt")
except Exception as e:
    print(f"[ERROR] Error appending to file: {e}")

# Part B: Read file and process
print("\n--- PART B: Reading from File ---")

try:
    with open("python_notes.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    print(f"\n[OK] Read file. Total lines: {len(lines)}")
    print("\nFile contents (numbered):")
    print("-" * 60)
    
    for idx, line in enumerate(lines, 1):
        cleaned_line = line.rstrip("\n")  # Strip trailing newline
        print(f"  {idx}. {cleaned_line}")
    
    print("\n[OK] Total number of lines in file:", len(lines))
    
    # Keyword search
    keyword = input("\nEnter a keyword to search in file: ").strip().lower()
    matching_lines = [line.rstrip("\n") for line in lines if keyword in line.lower()]
    
    if matching_lines:
        print(f"\n[OK] Found {len(matching_lines)} line(s) containing '{keyword}':")
        for line in matching_lines:
            print(f"  → {line}")
    else:
        print(f"\n[ERROR] No lines found containing keyword '{keyword}'. Try another search.")

except FileNotFoundError:
    print("[ERROR] Error: File python_notes.txt not found.")
except Exception as e:
    print(f"[ERROR] Error reading file: {e}")


# =====================================================================
# TASK 2: API INTEGRATION (8 marks)
# =====================================================================

print("\n\n" + "="*70)
print("TASK 2: API INTEGRATION")
print("="*70)

BASE_URL = "https://dummyjson.com"

# Step 1: Fetch and Display Products
print("\n--- STEP 1: Fetch and Display Products ---")

try:
    response = requests.get(f"{BASE_URL}/products?limit=20", timeout=5)
    response.raise_for_status()
    products = response.json().get("products", [])
    
    print(f"[OK] Fetched {len(products)} products\n")
    print("Formatted Product Table:")
    print("-" * 80)
    print(f"{'ID':<5} | {'Title':<25} | {'Category':<15} | {'Price':<10} | {'Rating':<6}")
    print("-" * 80)
    
    for product in products[:10]:  # Display first 10 for readability
        product_id = product.get("id", "N/A")
        title = product.get("title", "N/A")[:23]
        category = product.get("category", "N/A")[:13]
        price = f"${product.get('price', 0):.2f}"
        rating = f"{product.get('rating', 0):.2f}"
        
        print(f"{product_id:<5} | {title:<25} | {category:<15} | {price:<10} | {rating:<6}")
    
    print("-" * 80)

except requests.exceptions.RequestException as e:
    print(f"[ERROR] Error fetching products: {e}")
    products = []

# Step 2: Filter and Sort
print("\n--- STEP 2: Filter (Rating ≥ 2.5) and Sort by Price (Descending) ---")

try:
    if products:
        filtered_products = [p for p in products if p.get("rating", 0) >= 2.5]
        sorted_products = sorted(filtered_products, key=lambda x: x.get("price", 0), reverse=True)
        
        print(f"[OK] Filtered {len(sorted_products)} products with rating ≥ 2.5\n")
        print("Filtered & Sorted Product List:")
        print("-" * 80)
        print(f"{'Rank':<5} | {'Title':<25} | {'Price':<10} | {'Rating':<6}")
        print("-" * 80)
        
        for idx, product in enumerate(sorted_products[:10], 1):
            title = product.get("title", "N/A")[:23]
            price = f"${product.get('price', 0):.2f}"
            rating = f"{product.get('rating', 0):.2f}"
            print(f"{idx:<5} | {title:<25} | {price:<10} | {rating:<6}")
        
        print("-" * 80)
    else:
        print("[ERROR] No products available to filter.")

except Exception as e:
    print(f"[ERROR] Error filtering products: {e}")

# Step 3: Search by Category (Laptops)
print("\n--- STEP 3: Search by Category (Laptops) ---")

try:
    response = requests.get(f"{BASE_URL}/products/category/laptops", timeout=5)
    response.raise_for_status()
    laptops = response.json().get("products", [])
    
    print(f"[OK] Found {len(laptops)} laptops in database\n")
    print("Laptops Available:")
    print("-" * 60)
    
    for idx, laptop in enumerate(laptops, 1):
        name = laptop.get("title", "N/A")
        price = f"${laptop.get('price', 0):.2f}"
        print(f"  {idx}. {name:<45} - {price}")
    
    print("-" * 60)

except requests.exceptions.RequestException as e:
    print(f"[ERROR] Error fetching laptops: {e}")

# Step 4: POST Request (Simulated)
print("\n--- STEP 4: POST Request (Create New Product) ---")

custom_product = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

try:
    response = requests.post(f"{BASE_URL}/products/add", json=custom_product, timeout=5)
    response.raise_for_status()
    result = response.json()
    
    print("[OK] Sent POST request\n")
    print("Server Response:")
    print("-" * 60)
    print(json.dumps(result, indent=2))
    print("-" * 60)

except requests.exceptions.RequestException as e:
    print(f"[ERROR] Error sending POST request: {e}")


# =====================================================================
# TASK 3: EXCEPTION HANDLING (7 marks)
# =====================================================================

print("\n\n" + "="*70)
print("TASK 3: EXCEPTION HANDLING")
print("="*70)

# Part A: Guarded Calculator
print("\n--- PART A: Guarded Calculator ---")

def safe_divide(a, b):
    """
    Safely divide two numbers with exception handling.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Result of division or error message string
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"

# Test cases
test_cases = [
    (10, 2, "Normal division"),
    (10, 0, "Division by zero"),
    ("ten", 2, "Invalid input type")
]

print("Testing safe_divide() function:")
print("-" * 60)

for a, b, description in test_cases:
    result = safe_divide(a, b)
    print(f"[OK] safe_divide({a}, {b}) [{description}]")
    print(f"  → Result: {result}")

# Part B: Guarded File Reader
print("\n--- PART B: Guarded File Reader ---")

def read_file_safe(filename):
    """
    Safely read a file with comprehensive exception handling.
    
    Args:
        filename: Path to file to read
    
    Returns:
        File contents or None if error
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()
        return contents
    except FileNotFoundError:
        print(f"[ERROR] Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"[ERROR] Error: Permission denied for file '{filename}'.")
        return None
    finally:
        print(f"ℹ File operation attempt complete for '{filename}'.")

# Test file reading
print("\nTesting read_file_safe() function:")
print("-" * 60)

print("\n→ Attempting to read 'python_notes.txt':")
content1 = read_file_safe("python_notes.txt")
if content1:
    print(f"[OK] Read {len(content1)} characters\n")

print("\n→ Attempting to read non-existent 'ghost_file.txt':")
content2 = read_file_safe("ghost_file.txt")

# Part C: Robust API Calls (Enhanced Task 2 with exception handling)
print("\n--- PART C: Robust API Calls ---")

def fetch_product_safe(product_id):
    """
    Safely fetch product from API with comprehensive error handling.
    
    Args:
        product_id: ID of product to fetch
    
    Returns:
        Product data or None if error
    """
    try:
        response = requests.get(f"{BASE_URL}/products/{product_id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("[ERROR] Connection failed. Please check your internet.")
        return None
    except requests.exceptions.Timeout:
        print("[ERROR] Request timed out. Try again later.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"[ERROR] HTTP Error: {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")
        return None

print("Safely fetching product details:")
print("-" * 60)

# Test with valid product
product = fetch_product_safe(1)
if product:
    print(f"[OK] Product found: {product.get('title')} - ${product.get('price')}")

# Test with invalid product
print("\nAttempting to fetch non-existent product (ID: 999):")
product = fetch_product_safe(999)

# Part D: Input Validation Loop
print("\n--- PART D: Input Validation Loop ---")
print("Product lookup with input validation:")
print("-" * 60)

loop_count = 0
while loop_count < 3:  # Limit to 3 iterations for demo
    try:
        user_input = input(f"\nIteration {loop_count + 1}: Enter a product ID to look up (1-50), or 'quit' to exit: ").strip()
        
        if user_input.lower() == 'quit':
            print("[OK] Exiting product lookup.")
            break
        
        # Validate input is integer
        try:
            product_id = int(user_input)
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number between 1 and 100.")
            continue
        
        # Validate range
        if not (1 <= product_id <= 100):
            print("[ERROR] Product ID must be between 1 and 100. Please try again.")
            continue
        
        # Fetch product
        try:
            response = requests.get(f"{BASE_URL}/products/{product_id}", timeout=5)
            
            if response.status_code == 404:
                print(f"[ERROR] Product not found (ID: {product_id})")
            elif response.status_code == 200:
                product = response.json()
                title = product.get('title', 'N/A')
                price = product.get('price', 'N/A')
                print(f"[OK] Product found: {title} - ${price}")
            else:
                print(f"[ERROR] Unexpected response code: {response.status_code}")
        
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Error fetching product: {e}")
        
        loop_count += 1
    
    except KeyboardInterrupt:
        print("\n[OK] Lookup interrupted by user.")
        break
    except Exception as e:
        print(f"[ERROR] Unexpected error: {e}")


# =====================================================================
# TASK 4: LOGGING TO FILE (4 marks)
# =====================================================================

print("\n\n" + "="*70)
print("TASK 4: LOGGING TO FILE")
print("="*70)

def log_error(function_name, error_message):
    """
    Log an error to error_log.txt with timestamp.
    
    Args:
        function_name: Name of function where error occurred
        error_message: Description of error
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] ERROR in {function_name}: {error_message}\n"
    
    try:
        with open("error_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(log_entry)
        print(f"[OK] Logged error to error_log.txt: {error_message}")
    except Exception as e:
        print(f"[ERROR] Error writing to log file: {e}")

print("\nLogging Demonstration:")
print("-" * 60)

# Trigger and log error 1: Connection Error
print("\n→ Simulating Connection Error (unreachable URL):")
try:
    response = requests.get("http://this-host-does-not-exist-xyz.com/api", timeout=2)
except requests.exceptions.ConnectionError as e:
    log_error("fetch_products", f"ConnectionError - {str(e)[:50]}")

# Trigger and log error 2: HTTP Error (invalid product ID)
print("\n→ Simulating HTTP Error (Product not found - ID: 999):")
try:
    response = requests.get(f"{BASE_URL}/products/999", timeout=5)
    if response.status_code != 200:
        log_error("fetch_product", f"HTTPError - Product ID 999 not found (Status: {response.status_code})")
except Exception as e:
    log_error("fetch_product", str(e))

# Read and display error log
print("\n--- Error Log Contents ---")
print("-" * 60)

try:
    with open("error_log.txt", "r", encoding="utf-8") as log_file:
        log_contents = log_file.read()
    
    if log_contents:
        print("Error Log File (error_log.txt):\n")
        print(log_contents)
        print("-" * 60)
        print("[OK] Error log created and populated.")
    else:
        print("[ERROR] Error log is empty.")

except FileNotFoundError:
    print("[ERROR] Error log file not found.")
except Exception as e:
    print(f"[ERROR] Error reading log file: {e}")


# =====================================================================
# FINAL SUMMARY
# =====================================================================

print("\n" + "="*70)
