from random import choice

# Constants
AMOUNT_OF_ALARMS = 4

# Variables - 24H
today_availability = ["07:15 pm", "07:30 pm", "07:45 pm", "08:00 pm", "08:15 pm", "08:30 pm", "08:45 pm", "09:00 pm", "09:15 pm", "09:30 pm", "09:45 pm", "10:00 pm", "11:15 pm", "11:30 pm"]
random_times = []

# Functionality
def main():
    for _ in range(AMOUNT_OF_ALARMS):
        random_times.append(choice(today_availability))

    print("Your four random times are as follows:")
    random_times.sort()
    for time in random_times:
        print(time)

if __name__ == "__main__":
    main()