task = input("Enter task decription: ")
priority = input("What's the task priority? (High/Medium/Low) ").lower()
time_bound = input("Is the task time-bound? (Yes/No) ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task} is a high priority task that isn't time-bound. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task} is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task} is a medium priority task that isn't time-bound. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task} is a low priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"'{task} is a low priority task that isn't time-bound. Consider completing it when you have free time.")