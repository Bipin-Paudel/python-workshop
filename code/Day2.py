age = 17

# Check condition
# if age >= 18:
#     # Indented block that runs if condition is met
#     print("You can vote")



# else:
#     print("you can't vote")

# for number in range(1, 6):
#     print(number)

# count = 1

# # Loop while count is less or equal to 5
# while count <= 5:
#     print(count)
    
#     # CRITICAL: increment counter to eventually stop the loop!
#     count += 1


# number = int(input("Enter number: "))

# # Variable to accumulate product
# factorial = 1

# # Multiply numbers sequentially from 1 to number
# for i in range(1, number + 1):
#     factorial *= i

# print("Factorial is:", factorial)



# # multiplication table 

# number = int(input("Enter number: "))

# # Loop from 1 to 10
# for i in range(1, 11):
#     # Calculate product and display inline
#     print(f"{number} x {i} = {number * i}")


# def add(a, b):
#     return a + b

# # Call function and store return value in a variable
# result = add(5, 3)
# print("Result of function calculation:", result)

# student = {
#     "name": "Sita",
#     "marks": 90
# }

# # Update existing value
# student["marks"] = 95

# # Add a completely new key-value pair
# student["city"] = "Kathmandu"

# print("Updated student record:", student)


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "❌ Error: Cannot divide by zero!"
#     return a / b

# while True:
#     print("\n--- MODULAR CALCULATOR MENU ---")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")
    
#     choice = input("Enter choice (1-5): ")
    
#     if choice == "5":
#         print("👋 Exiting Calculator. Goodbye!")
#         break
        
#     if choice in ["1", "2", "3", "4"]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
        
#         if choice == "1":
#             print("Result:", add(num1, num2))
#         elif choice == "2":
#             print("Result:", subtract(num1, num2))
#         elif choice == "3":
#             print("Result:", multiply(num1, num2))
#         elif choice == "4":
#             print("Result:", divide(num1, num2))
#     else:
#         print("❌ Invalid Option selected!")




# Empty database storage list
students = []

while True:
    print("\n--- STUDENT RECORDS MENU ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")
        
        # Package details into a structured dictionary
        student = {
            "name": name,
            "age": age,
            "marks": marks
        }
        
        # Save record to list database
        students.append(student)
        print(f"🎉 Student {name} Added successfully!")
        
    elif choice == "2":
        if not students:
            print("📂 Database is currently empty.")
        else:
            print(f"\nTotal Records: {len(students)}")
            for idx, student in enumerate(students, 1):
                print(f"{idx}. Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")
                
    elif choice == "3":
        print("👋 Exiting database system. Goodbye!")
        break
        
    else:
        print("❌ Invalid option selected. Try again!")