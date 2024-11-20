import random

# Define the quiz questions and answers
Python = {
    1: ["What is the output of print(10/3)?", "3.33", "3", "3.0", "None of the above", "3.33"],
    2: ["What is the purpose of the 'len()' function?", "To find the length of a string",
        "To count the number of elements in a list", "To calculate the area of a shape", "Both A and B",
        "Both A and B"],
    3: ["What is the difference between '==' and 'is'?", "'==' compares values, 'is' compares identities",
        "'is' compares values, '==' compares identities", "Both compare values", "Both compare identities",
        "'==' compares values, 'is' compares identities"],
    4: ["What is the output of print(list(range(5))?", "[0, 1, 2, 3, 4]", "[1, 2, 3, 4, 5]", "[0, 1, 2, 3]",
        "[1, 2, 3, 4]", "[0, 1, 2, 3, 4]"],
    5: ["What is the purpose of a 'try-except' block?", "To handle exceptions and prevent program crashes",
        "To create a loop", "To define a function", "None of the above",
        "To handle exceptions and prevent program crashes"]
}

DBMS = {
    1: ["What is a DBMS?", "Database Management Software", "Data Backup Management System",
        "Disk Block Management System", "None of the above", "Database Management Software"],
    2: ["Which command is used to create a table?", "CREATE TABLE", "MAKE TABLE",
        "INSERT TABLE", "DEFINE TABLE", "CREATE TABLE"],
    3: ["What does SQL stand for?", "Structured Query Language",
        "Statistical Query Language", "Simple Query Language", "None of the above", "Structured Query Language"],
    4: ["What is a primary key?", "Unique identifier for a record",
        "Foreign key in another table", "Data type", "None of the above", "Unique identifier for a record"],
    5: ["What is a foreign key?", "Links two tables together",
        "Primary key of another table", "Data type", "Both A and B", "Both A and B"]
}

DSA = {
    1: ["Which data structure uses LIFO?", "Stack", "Queue", "Linked List", "Tree", "Stack"],
    2: ["What is a graph?", "Collection of nodes and edges", "Linear data structure",
        "Hierarchical data structure", "None", "Collection of nodes and edges"],
    3: ["What is recursion?", "Function calling itself", "Iterative process",
        "Sorting algorithm", "None", "Function calling itself"],
    4: ["What is the base case in recursion?", "Condition to stop recursion",
        "Start of recursion", "Recursive call", "None", "Condition to stop recursion"],
    5: ["Which algorithm has best time complexity for searching in a sorted array?",
        "Binary Search", "Linear Search", "Bubble Sort", "None", "Binary Search"],
}

# Function to display the banner
def display_banner():
    print("*******************************")
    print("**  Welcome to Quiz App  **")
    print("*******************************")


# Function to register a new user
def register_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Registration successful!")


# Function to login an existing user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("Login successful!")


# Function to display the quiz options
def display_quiz_options():
    print("Choose a quiz category:")
    print("1. DSA")
    print("2. DBMS")
    print("3. Python")


# Function to conduct the quiz
def conduct_quiz(category):
    quiz_data = {
        'DSA': DSA,
        'DBMS': DBMS,
        'Python': Python
    }
    # Select 5 random questions from the chosen category
    print(f"\n** Category: {category} **\n")
    questions = random.sample(list(quiz_data[category].keys()), 5)
    score = 0

    print("\n** Starting Quiz **\n")

    for q_id in questions:
        ques, op1, op2, op3, op4, correct_answer = quiz_data[category][q_id]
        print(f"{ques}\n")
        print(f"1. {op1}\n2. {op2}\n3. {op3}\n4. {op4}\n")

        user_answer = input("Enter your choice (1-4): ")
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {correct_answer}\n")

    print(f"\n** Quiz completed! Your score: {score}/5 **")

    # Store results in a dictionary
    results = {
        'username': 'User',
        'category': category,
        'score': score
    }
    return results

# Function to show the results of the quiz
def show_result():
    # Load results from a file or a database (you'll need to implement the storage mechanism)
    results_data = {}  # Load your results data here

    if results_data:
        # Display the results based on the user's choice
        print("Choose the result you want to see:")
        for i, result in enumerate(results_data):
            print(f"{i+1}. {result['category']} - Score: {result['score']}")
        choice = int(input("Enter your choice: "))
        selected_result = results_data[choice - 1]
        print(f"\nUsername: {selected_result['username']}\nCategory: {selected_result['category']}\nScore: {selected_result['score']}\n")
    # else:
    #     print("No results found.")


# Function to store results
def store_results(results):
    results_data.append(results)


# Main loop of the quiz app
results_data = []
while True:
    display_banner()
    print("1. Registration")
    print("2. Login")
    print("3. Attempt Quiz")
    print("4. Show Result")
    print("5. Exit Quiz")

    choice = input("Enter your choice: ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        display_quiz_options()
        category_choice = input("Enter your choice (1-3): ")
        if category_choice == '1':
            results = conduct_quiz('DSA')
            store_results(results)
        elif category_choice == '2':
            results = conduct_quiz('DBMS')
            store_results(results)
        elif category_choice == '3':
            results = conduct_quiz('Python')
            store_results(results)
        else:
            print("Invalid category choice!")
    elif choice == '4':
        show_result()
    elif choice == '5':
        print("Exiting the quiz app...")
        break
    else:
        print("Invalid choice! Please try again.")
