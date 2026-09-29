python_intro_questions = [
    {
        "question": "When was the Python programming language first introduced?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "1985", "correct": False, "feedback": "Not quite - Python came a bit later."},
            {"answer": "1991", "correct": True, "feedback": "Correct! Python was first introduced in 1991."},
            {"answer": "1995", "correct": False, "feedback": "Close, but Python was introduced a few years earlier."},
            {"answer": "2000", "correct": False, "feedback": "Python is older than that."}
        ]
    },
    {
        "question": "What does it mean that Python is 'free and open-source'?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Anyone can download, install, and use Python and it does not cost money", "correct": True, "feedback": "Correct! The paragraph explains that free and open-source means 'anyone can download, install, and use Python.'"},
            {"answer": "Python programs run faster than other languages", "correct": False, "feedback": "No, free and open-source refers to cost and accessibility, not speed."},
            {"answer": "Python is only available to students", "correct": False, "feedback": "No, the opposite - it's available to anyone, not just students."},
            {"answer": "You need a license to use Python", "correct": False, "feedback": "No, free and open-source means you don't need to pay for a license."}
        ]
    }
]


variables_quiz = [
    {
        "question": "What is the correct syntax for assigning a variable in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "variable_name == variable_value", "correct": False, "feedback": "No, == is used for comparison, not assignment."},
            {"answer": "variable_name = variable_value", "correct": True, "feedback": "Correct! The equals sign (=) is used to assign values to variables."},
            {"answer": "variable_value = variable_name", "correct": False, "feedback": "This is backwards - the variable name goes on the left, the value on the right."},
            {"answer": "assign variable_name variable_value", "correct": False, "feedback": "Python doesn't use an 'assign' keyword."}
        ]
    },
    {
        "question": "Which of the following are valid variable names in Python? (Select all that apply)",
        "type": "many_choice",
        "answers": [
            {"answer": "temperature", "correct": True, "feedback": "Correct! This starts with a letter and contains only letters."},
            {"answer": "temp_2", "correct": True, "feedback": "Correct! This starts with a letter and contains letters, numbers, and underscores."},
            {"answer": "2temp", "correct": False, "feedback": "Invalid! Variable names cannot start with a number."},
            {"answer": "_my_var", "correct": True, "feedback": "Correct! Variable names can start with an underscore."},
            {"answer": "my-variable", "correct": False, "feedback": "Invalid! Hyphens are not allowed in variable names, only underscores."}
        ]
    },
    {
        "question": "What does assigning a variable allow you to do?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Save calculated values for later use", "correct": True, "feedback": "Correct! The text explains that variable assignment lets us 'save our calculated values for later use.'"},
            {"answer": "Make calculations run faster", "correct": False, "feedback": "No, assignment is about storing values, not speed."},
            {"answer": "Print results to the screen", "correct": False, "feedback": "No, assignment stores values but doesn't display them."},
            {"answer": "Delete old calculations", "correct": False, "feedback": "No, assignment is about saving values, not deleting them."}
        ]
    }
]

functions_quiz = [
    {
        "question": "What are functions in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Variables that store numbers", "correct": False, "feedback": "No, that describes variables, not functions."},
            {"answer": "Reusable pieces of code that perform certain tasks", "correct": True, "feedback": "Correct! The text defines functions as 'reusable pieces of code that perform certain tasks.'"},
            {"answer": "A way to write comments in code", "correct": False, "feedback": "No, comments are written with # symbols."},
            {"answer": "Special symbols used in calculations", "correct": False, "feedback": "No, functions are code, not symbols."}
        ]
    },
    {
        "question": "What is the correct syntax for calling a function with arguments?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "function_name[argument1, argument2]", "correct": False, "feedback": "No, functions use parentheses, not square brackets."},
            {"answer": "function_name(argument1, argument2)", "correct": True, "feedback": "Correct! Functions use parentheses containing arguments separated by commas."},
            {"answer": "function_name argument1 argument2", "correct": False, "feedback": "No, arguments must be enclosed in parentheses."},
            {"answer": "call function_name(argument1, argument2)", "correct": False, "feedback": "No, Python doesn't use a 'call' keyword."}
        ]
    },
    {
        "question": "According to the text, what happens when you just call a function or perform a calculation with a variable?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The result automatically overwrites the original variable", "correct": False, "feedback": "No, the text emphasizes that this does NOT happen automatically."},
            {"answer": "The result is automatically saved for later use", "correct": False, "feedback": "No, results are not automatically saved."},
            {"answer": "The result is not saved unless you assign it to a variable", "correct": True, "feedback": "Correct! The text explains that 'just calling a function or performing a calculation with a variable does not save the result.'"},
            {"answer": "Python gives you an error", "correct": False, "feedback": "No, calling functions doesn't cause errors, but the result won't be saved."}
        ]
    }
]

for_loops_quiz = [
    {
        "question": "What does the append method do?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Removes the last item from a list", "correct": False, "feedback": "No, append adds items. You're thinking of a different method."},
            {"answer": "Adds a new item to the end of an existing list", "correct": True, "feedback": "Correct! The append method adds a new item to the end of an existing list."},
            {"answer": "Sorts the items in a list", "correct": False, "feedback": "No, append doesn't sort anything, it just adds items."},
            {"answer": "Counts the number of items in a list", "correct": False, "feedback": "No, that would be the len() function, not append."}
        ]
    },
    {
        "question": "How do you create an empty list in Python?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "empty_list = ()", "correct": False, "feedback": "No, parentheses create an empty tuple, not a list."},
            {"answer": "empty_list = []", "correct": True, "feedback": "Correct! Square brackets with nothing inside create an empty list."},
            {"answer": "empty_list = {}", "correct": False, "feedback": "No, curly braces create an empty dictionary, not a list."},
            {"answer": "empty_list = null", "correct": False, "feedback": "No, 'null' isn't valid Python syntax. You might be thinking of 'None', but that's not an empty list."}
        ]
    }
]

predict_output_quiz = [
    {
        "question": "What does the code in the cell below this one print? Try to predict the answer before you run it.",
        "type": "multiple_choice",
        "answers": [
            {"answer": "slice1 is [-2.7, 5.4, 42.1]\nslice2 is [-13.4, -2.7, 5.4]", "correct": True, "feedback": "Correct! slice1 = energy_kcal[1:] takes from index 1 to the end. slice2 = energy_kcal[:3] takes from the beginning up to (but not including) index 3."},
            {"answer": "slice1 is [-13.4, -2.7, 5.4]\nslice2 is [-2.7, 5.4, 42.1]", "correct": False, "feedback": "Not quite. Remember that [1:] starts at index 1 and goes to the end, while [:3] starts at the beginning and goes up to (but not including) index 3."},
            {"answer": "slice1 is [5.4, 42.1]\nslice2 is [-13.4, -2.7]", "correct": False, "feedback": "No, [1:] means from index 1 to the end (not from index 2), and [:3] means up to but not including index 3 (so it includes 3 elements, not 2)."},
            {"answer": "slice1 is [-2.7, 5.4]\nslice2 is [-13.4, -2.7, 5.4, 42.1]", "correct": False, "feedback": "Not correct. [1:] goes from index 1 to the end (includes the last element), and [:3] stops before index 3 (doesn't include all elements)."}
        ]
    }
]