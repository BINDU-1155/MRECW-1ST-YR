def is_leap(year):
    leap = False
    
    # Check if year is divisible by 4
    if year % 4 == 0:
        # If divisible by 100, it should also be divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap
year = int(input())