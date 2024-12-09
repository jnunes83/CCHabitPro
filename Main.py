"""
Main module for CCHabitPro application.
"""
import questionary
import initialisation
from BLEHandler import BLEHandler
from Modeling import HabitModel
import pandas as pd
from User import UserClass
from sklearn.preprocessing import LabelEncoder

# Creates the database.
initialisation.launch_database()

# Program starts with an intro message.
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

# Initialize BLE and Model Handler
ble_handler = BLEHandler()
habit_model = HabitModel()

# Scan for devices
available_devices = ble_handler.scan_devices()
print(f"Available devices: {available_devices}")

# Ask the user to login or register.
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

# Example to connect to a device (replace 'Device_Name' with actual name)
ble_handler.connect_to_device('Device_Name')

# Data Collection and Preprocessing Logic
def collect_and_preprocess_data():
    # Simulated data collection
    data = {
        'age': [25, 30, 22, 35, 40, 28, 50, 45],
        'sex': ['Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Male', 'Female'],
        'height': [175, 160, 165, 180, 170, 178, 172, 158],
        'weight': [70, 60, 55, 85, 75, 68, 80, 62],
        'habit_frequency': ['Daily', 'Daily', 'Weekly', 'Daily', 'Weekly', 'Daily', 'Daily', 'Weekly'],
        'success': [1, 0, 1, 1, 0, 1, 1, 0]  # Binary target variable
    }
    
    df = pd.DataFrame(data)
    
    # Preprocessing
    label_encoder = LabelEncoder()
    df['sex'] = label_encoder.fit_transform(df['sex'])  # Encode 'sex' as numerical
    df['habit_frequency'] = label_encoder.fit_transform(df['habit_frequency'])  # Encode habit frequency

    return df

# Collect and preprocess data
training_data = collect_and_preprocess_data()
print("Training Data:")
print(training_data)

# Train the model with the processed data
habit_model.train_model(training_data)

# Placeholder for the menu function
def menu():
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

# Executes the function defined above and starts the user guidance.
menu()