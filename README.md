# AI Health Analyst (BMI Calculator)

A console-based Python application that calculates Body Mass Index (BMI) according to World Health Organization (WHO) standards, performs real-time data analysis for groups, and tracks session history.

## Features
* **Robust Input Validation:** Utilizes `try-except` blocks to handle `ValueError` and prevents logical errors by checking against negative or zero values for weight and height.
* **Dynamic Session History:** Stores computed BMI records in a dynamic list throughout the active session.
* **Group Data Analytics:** On exit, the program calculates and displays group statistics, including total profiles analyzed and the average BMI of the group.
* **Interactive Control Flow:** Employs a structured `while` loop controlled by boolean flags and interactive user prompts (`Y/N`) to manage session flow.

## Technical Stack
* **Language:** Python 3.15.2
* **Core Concepts:** Loops (`while`), exception handling (`try-except`), conditional branching (`if-elif-else`), type casting, math functions (`round`), list operations (`append`, `sum`, `len`).

## How It Works
1. The program prompts the user for weight (kg) and height (m).
2. It validates the inputs to ensure they are numeric and positive.
3. It computes the BMI using the formula: $BMI = \frac{weight}{height^2}$, rounded to 3 decimal places.
4. It categorizes the BMI into Underweight, Normal, or Overweight, offering health recommendations.
5. Upon session termination, it aggregates all data to output the final group analytics report.
