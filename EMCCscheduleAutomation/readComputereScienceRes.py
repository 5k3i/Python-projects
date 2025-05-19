import json
import textwrap

def open_json(name):
    try:
        with open(name, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("The file does not exist.")
    except json.JSONDecodeError:
        print("The file is not a valid JSON.")
        
def flatten(lst):
    # Recursively flattens a list of strings or lists
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def main():
    file_name = "C:/Users/Skyle/Python projects/EMCCscheduleAutomation/computerScience.json"

    mainData = open_json(file_name)

    print("{:<12} {:<40} {:<10}".format("Credit Type", "Course Name(s)", "Credits"))
    print("-" * 65)

    total_max_credits = 0
    total_min_credits = 0

    for semester, courses in mainData["computerscience"].items():
        print("\n{:<12}".format(semester))
        max_credits = 0
        min_credits = 0
        for key, value in courses.items():
            course_names = ", ".join(flatten(value[0]))
            credits_list = value[1]
            credits = ", ".join(str(c) for c in credits_list)
            wrapped_names = textwrap.wrap(course_names, width=40)
            # Print the first line with all columns
            print("{:<12} {:<40} {:<10}".format(key, wrapped_names[0], credits))
            # Print any additional lines for wrapped course names
            for line in wrapped_names[1:]:
                print("{:<12} {:<40} {:<10}".format("", line, ""))
            # Update max and min credits for this semester
            if credits_list:
                max_credits += max(credits_list)
                min_credits += min(credits_list)
        print("-" * 65)
        print("  {:<20} {:<10}".format("Max Credits:", max_credits))
        print("  {:<20} {:<10}".format("Min Credits:", min_credits))
        print("-" * 65)
        total_max_credits += max_credits
        total_min_credits += min_credits

    # Print overall totals
    print("\n{:<20} {:<10}".format("Total Max Credits:", total_max_credits))
    print("{:<20} {:<10}".format("Total Min Credits:", total_min_credits))

if __name__ == "__main__" :
    main()