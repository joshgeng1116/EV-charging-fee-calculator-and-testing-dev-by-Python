def time_to_minutes(time_input):
    ar = time_input.split(":")
    hour = int(ar[0])
    minute = int(ar[1])
    final_minute = hour*60+minute
    return final_minute