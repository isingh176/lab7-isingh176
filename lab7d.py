#!/usr/bin/env python3
# Student ID: isingh176

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second
    Function attributes: __init__, __str__, __repr__,
                         time_to_sec, format_time,
                         change_time, sum_times
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """String representation for easy printing"""
        return self.format_time()

    def __repr__(self):
        """Representation of the object"""
        return f"Time({self.hour:02d}, {self.minute:02d}, {self.second:02d})"

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add another Time object to this one and return a new Time object as the sum."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Modify the current time object by adding/subtracting seconds."""
        total_seconds = self.time_to_sec() + seconds
        updated_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = updated_time.hour, updated_time.minute, updated_time.second
        return None

    def time_to_sec(self):
        """Convert a time object to a single integer representing seconds from midnight."""
        minutes = self.hour * 60 + self.minute
        return minutes * 60 + self.second

    def valid_time(self):
        """Check for the validity of the time object attributes."""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True

def sec_to_time(seconds):
    """Convert a given number of seconds to a Time object in hour, minute, second format."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

