#  Teemo is not really excited about the new year's eve, 
#  but he has to celebrate it with his friends anyway.

#  He has a really big passion about programming and he wants to be productive till midnight. 
#  He wants to know how many minutes he has left to work on his new project.
#  He doesn't want to look on the clock all the time, so he thought about a function, 
#  which returns him the number of minutes.

#  The function minutesToMidnight(d) will take a date object as parameter. Return the number of minutes in the following format:
#  "x minute(s)"

#  You will always get a date object with of today with a random timestamp.
#  You have to round the number of minutes. Milliseconds doesn't matter!



def minutes_to_midnight(d):

    date, time = str(d).split(' ')
    hours, minutes, seconds = time.split(':')
    
    if int(seconds) >= 30:
        remaining_seconds_in_minutes = 1
    else:
        remaining_seconds_in_minutes = 0
    
    remaining_hours_in_minutes = (23 - int(hours)) * 60
        
    remaining_minutes = 60 - int(minutes) - remaining_seconds_in_minutes
    
    total = remaining_hours_in_minutes + remaining_minutes
    ans = str(total) + ' minutes'
    return ans


