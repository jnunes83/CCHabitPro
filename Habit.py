"""
The Habit Class.
It imports sqlite3.
"""
import sqlite3
from datetime import datetime

# THE HABIT CLASS.
class HabitClass:
    """
    A class used to represent a habit.

    Attributes
    ----------
    habit_name: str
        the name of the habit
    owner: str
        the owner aka the user who the habit belongs to
    category: str
        the category the habit belongs to, which can be 'Health', 'Diet', or 'Exercise'
    periodicity: str
        the periodicity of the habit which can be 'weekly' or 'daily'
    datetime_of_creation: datetime
        the date and time of when the habit was first created
    """

    def __init__(self, habit_name, owner, category, periodicity, datetime_of_creation):
        """
        Parameters
        ----------
        :param habit_name: str
            the name of the habit
        :param owner: str
            the owner aka the user who the habit belongs to
        :param category: str
            the category the habit belongs to, which can be 'Health', 'Diet', or 'Exercise'
        :param periodicity: str
            the periodicity of the habit which can be 'weekly' or 'daily'
        :param datetime_of_creation: datetime
            the date and time of when the habit was first created
        """
        self.habit_name = habit_name
        self.owner = owner
        self.category = category
        self.periodicity = periodicity
        self.datetime_of_creation = datetime_of_creation
        
        from os.path import join, dirname, abspath
        db_path = join(dirname(abspath(__file__)), 'main_db.db')

        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def mark_completed(self):
        """
        Marks the habit as completed for the current period.
        """
        datetime_of_completion = datetime.now()
        self.cur.execute("INSERT INTO progress VALUES(?, ?, ?, ?)",
                         (self.habit_name, self.periodicity, self.owner, datetime_of_completion))
        self.conn.commit()