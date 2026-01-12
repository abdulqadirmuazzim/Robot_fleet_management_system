# Employee data collector - stores name, age, job as tuples in a list

employees = []  # List to store employee tuples (name, age, job)

print("Enter employee details (press Enter on name to quit):")

while True:
    # Get name input - check if empty to quit
    name = input("Enter name: ").strip()

    # If name is empty (just Enter pressed), exit the loop
    if not name:
        break

    # Get age input
    age = input("Enter age: ").strip()

    # Get job input
    job = input("Enter job: ").strip()

    # Validate age is a number (optional but good practice)
    try:
        age = int(age)
    except ValueError:
        print("Age must be a number. Skipping this entry.")
        continue

    # Create tuple and add to list
    employee = (name, age, job)
    employees.append(employee)

    print(f"Added: {employee}\n")

# Display all collected data
print("\n--- All Employees ---")
if employees:
    for i, emp in enumerate(employees, 1):
        print(f"{i}. Name: {emp[0]}, Age: {emp[1]}, Job: {emp[2]}")
else:
    print("No employees added.")

print(f"\nTotal employees stored: {len(employees)}")
