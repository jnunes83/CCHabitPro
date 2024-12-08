"""
This document regulates our user guidance. It represents the menu or the main navigation.
It imports the library 'questionary' as the Command Line Interface (CLI) that guides the user through the program.
It also imports the initialisation.py doc which launches the core functionalities of the program.
"""
import questionary
import initialisation

# CREATES THE DATABASE.
initialisation.launch_database()

# PROGRAM STARTS AND INTRO MESSAGE INTRODUCES THE APP.
intro_message = "\n******************************\n" \
                "Welcome to CCHabitPro! The Habit Tracker for Chronic Diseases\n" \
                "You can use this app to track your habits for a healthier life.\n" \
                "******************************\n"
print(intro_message)

# Predefined habits
predefined_habits = {
    'hypertension': [
        {'name': 'Blood Pressure Check', 'periodicity': 'daily'},
        {'name': 'Take BP Medication', 'periodicity': 'daily'},
        {'name': 'Low Sodium Diet', 'periodicity': 'daily'},
        {'name': '30min Walking', 'periodicity': 'daily'},
        {'name': 'Stress Management', 'periodicity': 'daily'}
    ],
    'diabetes': [
        {'name': 'Blood Sugar Check', 'periodicity': 'daily'},
        {'name': 'Take Diabetes Medication', 'periodicity': 'daily'},
        {'name': 'Foot Check', 'periodicity': 'daily'},
        {'name': 'Carb Counting', 'periodicity': 'daily'},
        {'name': 'Exercise', 'periodicity': 'daily'}
    ],
    'obesity': [
        {'name': 'Weight Check', 'periodicity': 'weekly'},
        {'name': 'Calorie Tracking', 'periodicity': 'daily'},
        {'name': 'Exercise', 'periodicity': 'daily'},
        {'name': 'Water Intake', 'periodicity': 'daily'},
        {'name': 'Sleep Tracking', 'periodicity': 'daily'}
    ]
}

# ASKS THE USER TO LOGIN OR REGISTER.
first_question = questionary.select(
    "Is this your first time here or have you been here before? ", choices=[
        "Register",
        "Login"
    ]).ask()

if first_question == "Login":
    # Call a login function here (not implemented in this scope)
    pass

elif first_question == "Register":
    print("\nLooks like you're new here! Let's set up your profile.\n")
    
    username = questionary.text("Choose a username:").ask()
    password = questionary.password("Choose a password:").ask()
    age = questionary.text("Enter your date of birth (YYYY-MM-DD):").ask()
    sex = questionary.select("Select your sex:", choices=["Male", "Female", "Other"]).ask()
    height = questionary.text("Enter your height (cm):").ask()
    weight = questionary.text("Enter your weight (kg):").ask()
    race = questionary.text("Enter your race:").ask()
    occupation = questionary.select("Select your occupation:", choices=["Working", "Student", "Unemployed"]).ask()
    geographical_area = questionary.text("Enter your geographical area:").ask()
    medical_history = questionary.text("Enter your medical history:").ask()

    new_user = UserClass(username, password, age, sex, height, weight, race, occupation, geographical_area, medical_history)
    new_user.store_in_db()

    print("\nProfile created successfully! Let's set up your habits.\n")
    
    # Adding predefined habits to the database for the user
    for category, habits in predefined_habits.items():
        for habit in habits:
            new_user.create_habit(habit['name'], category, habit['periodicity'])

# Placeholder for the menu function, which will allow users to create habits
def menu():
    """
    This is the main menu of our program.
    It asks and prompts the user what they want to do and guides them through the functionalities.
    """
    second_question = questionary.select("What do you want to do? ",
                                         choices=[
                                             "View my habits",
                                             "Analyze my habits",
                                             "Exit Program"
                                         ]).ask()
    if second_question == "View my habits":
        # Call view habits function (not implemented in this scope)
        pass
    
    elif second_question == "Analyze my habits":
        # Call analyze habits function (not implemented in this scope)
        pass
    
    elif second_question == "Exit Program":
        print("\nSee you soon!\n")

# EXECUTES THE FUNCTION DEFINED ABOVE AND STARTS THE USER GUIDANCE.
menu()