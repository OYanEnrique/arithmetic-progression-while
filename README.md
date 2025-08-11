# arithmetic-progression-while
An interactive command-line tool written in Python to generate and display terms of an arithmetic progression. Users can specify a starting term and ratio, view more terms on demand, and see the final sum of the progression.

# Interactive Arithmetic Progression Generator

This Python script provides an interactive way to explore arithmetic progressions. A user starts by providing an initial term and a common difference (called a "ratio" in the script). The program then generates the first 10 terms.

From there, the user can choose to display more terms in increments until they decide to stop. At the end, the script calculates and displays the sum of all terms that were shown.

## Features

-   Initializes with a user-defined starting term and ratio.
-   Displays the first 10 terms of the progression by default.
-   Interactively prompts the user to display additional terms.
-   Visually shows the calculation for each new term.
-   Calculates and displays the sum of all generated terms upon completion.

## How to Run

1.  Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2.  Save the code as `arithmetic_progression_while.py`.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where the file is saved.
5.  Run the script using the command:
    ```bash
    python arithmetic_progression_while.py
    ```

## Usage Example

The following example shows a user starting with a term of `2` and a ratio of `3`. After the first 10 terms are displayed, they ask for 2 more before finishing the program by entering `0`.

```
Enter the term:
2
Enter the ratio:
3
Term: 2, Ratio: 3

2=2
2 + 3=5
5 + 3=8
8 + 3=11
11 + 3=14
14 + 3=17
17 + 3=20
20 + 3=23
23 + 3=26
26 + 3=29
how many more terms do you want to show?
2
29 + 3=32
32 + 3=35
how many more terms do you want to show?
0
The sum of the terms is: 222
```
