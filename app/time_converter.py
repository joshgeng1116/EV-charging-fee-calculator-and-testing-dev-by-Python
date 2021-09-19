def time_to_minutes(time_input):
    ar = time_input.split(":")

    # Check there are the required number of inputs 
    if not(len(ar) == 2):
        raise ValueError("The input string is not in the correct format")
    
    hour = int(ar[0])
    minute = int(ar[1])

    # Check time within boundaries 
    if not(minute >= 0 and minute < 60):
        raise ValueError("Minutes must be in the range 0 - 59")
    if not(hour >= 0 and hour < 24):
        raise ValueError("Hours must be in the range 0 - 24")
    # Prepare Return 
    final_minutes = hour * 60 + minute
    return final_minutes