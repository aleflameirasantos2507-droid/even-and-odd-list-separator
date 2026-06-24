# Even and Odd List Separator

A beginner-friendly Python project that stores user-entered numbers in a main list and separates them into even and odd lists.

## Features

- Stores all entered numbers in a main list
- Creates a list of even numbers
- Creates a list of odd numbers
- Allows continuous input until the user chooses to stop
- Displays all three lists at the end

## Technologies Used

- Python 3

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/even-and-odd-list-separator.git
```

2. Navigate to the project folder:

```bash
cd even-and-odd-list-separator
```

3. Run the script:

```bash
python main.py
```

## Example

### Input

```text
Enter a value: 10
Would you like to continue? [Y/N] Y

Enter a value: 7
Would you like to continue? [Y/N] Y

Enter a value: 4
Would you like to continue? [Y/N] N
```

### Output

```text
Main list: [10, 7, 4]
Even numbers: [10, 4]
Odd numbers: [7]
```

## Learning Objectives

This project demonstrates:

- Lists
- Conditional statements
- Loops (`while`)
- Modulus operator (`%`)
- Input validation
- Data classification

## Key Concepts

### Checking for Even Numbers

```python
number % 2 == 0
```

If the remainder is zero, the number is even.

### Checking for Odd Numbers

```python
number % 2 != 0
```

If the remainder is not zero, the number is odd.

### Storing Values in Different Lists

```python
even_numbers.append(number)
```

and

```python
odd_numbers.append(number)
```

allow the program to organize data automatically.
