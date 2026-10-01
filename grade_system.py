"""
Student Grade System
--------------------
Asks the user for a mark (0-100) and prints the matching letter grade.

Grading scale (boundaries inclusive):
    90 - 100  -> A
    80 - 89   -> B
    70 - 79   -> C
    60 - 69   -> D
    Below 60  -> E

Pure Python - standard library only.
"""

MIN_MARK = 0
MAX_MARK = 100


def get_grade(mark: float) -> str:
    """Return the letter grade for a mark in the range 0-100."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def parse_mark(text: str):
    """
    Convert user input to a valid mark.
    Returns (mark, None) on success or (None, error_message) on failure.
    """
    text = text.strip()

    if text == "":
        return None, "No input entered. Please type a number between 0 and 100."

    try:
        mark = float(text)
    except ValueError:
        return None, f"'{text}' is not a number. Please enter a number between 0 and 100."

    # Reject nan / inf, which float() accepts but are not real marks
    if mark != mark or mark in (float("inf"), float("-inf")):
        return None, f"'{text}' is not a valid mark. Please enter a number between 0 and 100."

    if mark < MIN_MARK:
        return None, f"{text} is below {MIN_MARK}. Marks cannot be negative."

    if mark > MAX_MARK:
        return None, f"{text} is above {MAX_MARK}. The maximum mark is {MAX_MARK}."

    return mark, None


def format_mark(mark: float) -> str:
    """Show whole numbers without a trailing .0 (e.g. 85 instead of 85.0)."""
    return str(int(mark)) if mark.is_integer() else str(mark)


def main():
    print("=" * 40)
    print("        STUDENT GRADE SYSTEM")
    print("=" * 40)
    print("Enter a mark between 0 and 100 (or 'q' to quit).\n")

    while True:
        try:
            user_input = input("Enter mark: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Goodbye!")
            return

        if user_input.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            return

        mark, error = parse_mark(user_input)

        if error:
            print(f"  Invalid input: {error}\n")
            continue

        grade = get_grade(mark)
        print(f"  Mark: {format_mark(mark)}  ->  Grade: {grade}\n")


if __name__ == "__main__":
    main()
