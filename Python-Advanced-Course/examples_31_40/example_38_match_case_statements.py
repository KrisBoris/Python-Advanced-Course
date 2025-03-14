# Example 38 - Match-case statements

day = input("Enter week's day: ")

match day:
    case "Saturday" | "Sunday":
        print("Today is weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Today is not weekend")
    case _:
        print("Invalid day")