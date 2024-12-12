import time


def hour_minute_second_program():
    total_seconds = int(input("Enter the number of seconds for the timer: "))

    while total_seconds > 0:
        # Calculate hours, minutes, and seconds
        hour = total_seconds // 3600
        minute = (total_seconds % 3600) // 60
        second = total_seconds % 60

        # Print the timer in a "HH:MM:SS" format
        print(f"Timer: {hour:02}:{minute:02}:{second:02}")

        # Sleep for 1 second and decrease the timer
        time.sleep(1)
        total_seconds -= 1

    print("Time's up!")


# Call the program
hour_minute_second_program()
