# This module save informations about transcations
import datetime

def two_weeks_ahead():
    # This function calculate the due date to return the book. Takes no argument returns due date in date format
    today = datetime.date.today()
    due_time = today + datetime.timedelta(20)
    return due_time
