"""
The user class contains all the important functions of the CCHabitoPro app.
"""
import questionary
import sqlite3
from datetime import datetime
import Habit

# THE USER CLASS.
class UserClass:
    """
    A class used to represent a user.

    Attributes
    ----------
    username: str
        the username defined by the user
    password: str
        the password used by the user
    age: str
        the age of the user
    sex: str
        the sex of the user
    height: float
        the height of the user in cm
    weight: float
        the weight of the user in kg
    race: str
        the race of the user
    occupation: str
        the occupation of the user
    geographical_area: str
        the geographical area of residence
    history_of_illnesses: str
        history of illnesses or allergies
    conn:
        Establishing a connection to the database
    """
    
    def __init__(self, username, password, age, sex, height, weight, race, occupation, geographical_area, history_of_illnesses):
        """
        Parameters
        ----------
        :param username: str
            the username defined by the user
        :param password: str
            the password used by the user
        :param age: str
            age of the user
        :param sex: str
            sex of the user
        :param height: float
            height of the user in cm
        :param weight: float
            weight of the user in kg
        :param race: str
            race of the user
        :param occupation: str
            occupation of the user
        :param geographical_area: str
            geographical area of residence
        :param history_of_illnesses: str
            history of illnesses or allergies
        """
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.race = race
        self.occupation = occupation
        self.geographical_area = geographical_area
        self.history_of_illnesses = history_of_illnesses

        from os.path import join, dirname, abspath
        db_path = join(dirname(abspath(__file__)), 'main_db.db')

        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def store_in_db(self):
        """Stores the user data into the database."""
        self.cur.execute("INSERT INTO users (username, password, age, sex, height, weight, race, occupation, geographical_area, history_of_illnesses) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (self.username, self.password, self.age, self.sex, self.height, self.weight, self.race, self.occupation, self.geographical_area, self.history_of_illnesses))
        self.conn.commit()

    def create_habit(self):
        """Lets the user create a new habit."""
        habit_name = questionary.text("Type in the name of the habit: ").ask()
        task_description = questionary.text("Enter a description for the task: ").ask()
        periodicity = questionary.select("Is this a daily or weekly habit?", choices=["Daily", "Weekly"]).ask()
        datetime_of_creation = datetime.now()

        new_habit = Habit.HabitClass(habit_name, self.username, task_description, periodicity, datetime_of_creation)
        new_habit.mark_completed()  # Example of marking the habit as completed for demonstration