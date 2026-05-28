import yaml

BASE = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units"


def apply_break_fix(path, world, exercise):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data['worlds'][world]['exercises'].append(exercise)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ── Lesson 1 ── Defining Functions
# Bug: function is called by the wrong name (great instead of greet), causing a NameError.
# Fixed: change great() to greet(). Output: 'hello'.

lesson1 = f"{BASE}/unit_5/lesson_1.yaml"

apply_break_fix(lesson1, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara carefully inscribes her first potion recipe as a spell named greet, "
        "but when she tries to cast it she calls it by the wrong name and the cauldron explodes with an error."
    ),
    'story_after': (
        "With the spell name corrected, the cauldron chimes 'hello' and Elara's first successful recipe is complete."
    ),
    'prompt': (
        "Fix the code so the function greet is called by its correct name and prints 'hello'."
    ),
    'broken_code': "def greet():\n    print(\"hello\")\n\ngreat()",
    'hint': "Look for the misspelled function name in the call — the function is defined as greet, not great.",
    'explanation': (
        "great() raises a NameError because no function called great exists. "
        "Changing the call to greet() matches the definition and prints 'hello'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hello'",
            'message': "Should print hello"
        }
    ]
})

apply_break_fix(lesson1, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara programs a diagnostic routine on the Helix called greet, "
        "but her launch command contains a typo and the ship's console throws a NameError."
    ),
    'story_after': (
        "The corrected command fires the routine and 'hello' confirms the diagnostic subroutine is online."
    ),
    'prompt': (
        "Fix the code so the function greet is called by its correct name and prints 'hello'."
    ),
    'broken_code': "def greet():\n    print(\"hello\")\n\ngreat()",
    'hint': "Look for the misspelled function name in the call — the function is defined as greet, not great.",
    'explanation': (
        "great() raises a NameError because no function called great exists. "
        "Changing the call to greet() matches the definition and prints 'hello'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hello'",
            'message': "Should print hello"
        }
    ]
})

apply_break_fix(lesson1, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole writes a search function called greet to kick off his investigation, "
        "but when he runs it he misspells the name and the precinct terminal crashes with a NameError."
    ),
    'story_after': (
        "The corrected call runs without error and 'hello' appears on the terminal — Cole's first tool is operational."
    ),
    'prompt': (
        "Fix the code so the function greet is called by its correct name and prints 'hello'."
    ),
    'broken_code': "def greet():\n    print(\"hello\")\n\ngreat()",
    'hint': "Look for the misspelled function name in the call — the function is defined as greet, not great.",
    'explanation': (
        "great() raises a NameError because no function called great exists. "
        "Changing the call to greet() matches the definition and prints 'hello'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hello'",
            'message': "Should print hello"
        }
    ]
})

# ── Lesson 2 ── Return Values
# Bug: function is missing the return statement, so it returns None and prints None instead of 10.
# Fixed: add `return result` (or `return n * 2`). Output: '10'.

lesson2 = f"{BASE}/unit_5/lesson_2.yaml"

apply_break_fix(lesson2, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's doubling spell computes how many flasks a doubled batch will fill, "
        "but she forgets to bottle up the result and send it back — the cauldron prints None instead of the answer."
    ),
    'story_after': (
        "With the return statement in place, 10 appears on the scroll and Elara's potion count is confirmed."
    ),
    'prompt': (
        "Fix the code so double(5) returns the computed value and prints 10."
    ),
    'broken_code': "def double(n):\n    result = n * 2\n\nprint(double(5))",
    'hint': "Look for the missing return statement — the function computes result but never sends it back.",
    'explanation': (
        "Without a return statement the function implicitly returns None, so print(double(5)) prints None. "
        "Adding return result (or return n * 2) sends the computed value back and prints 10."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '10'",
            'message': "Should print 10"
        }
    ]
})

apply_break_fix(lesson2, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's power-output function does the multiplication correctly, "
        "but the result is never transmitted back to the caller and the console reads None instead of 10."
    ),
    'story_after': (
        "10 units of power register on the console — the subroutine now sends its answer back correctly."
    ),
    'prompt': (
        "Fix the code so double(5) returns the computed value and prints 10."
    ),
    'broken_code': "def double(n):\n    result = n * 2\n\nprint(double(5))",
    'hint': "Look for the missing return statement — the function computes result but never sends it back.",
    'explanation': (
        "Without a return statement the function implicitly returns None, so print(double(5)) prints None. "
        "Adding return result (or return n * 2) sends the computed value back and prints 10."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '10'",
            'message': "Should print 10"
        }
    ]
})

apply_break_fix(lesson2, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's evidence-multiplier doubles the clue count internally, "
        "but the doubled value never leaves the function and the case file records None instead of 10."
    ),
    'story_after': (
        "10 is written to the case file and Cole's doubled clue count is properly recorded."
    ),
    'prompt': (
        "Fix the code so double(5) returns the computed value and prints 10."
    ),
    'broken_code': "def double(n):\n    result = n * 2\n\nprint(double(5))",
    'hint': "Look for the missing return statement — the function computes result but never sends it back.",
    'explanation': (
        "Without a return statement the function implicitly returns None, so print(double(5)) prints None. "
        "Adding return result (or return n * 2) sends the computed value back and prints 10."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '10'",
            'message': "Should print 10"
        }
    ]
})

# ── Lesson 3 ── Multiple Parameters
# Bug: arguments are passed in the wrong order. describe(5, "hero") passes an int as name and a str as level.
# Fixed: describe("hero", 5). Output: 'hero is level 5'.

lesson3 = f"{BASE}/unit_5/lesson_3.yaml"

apply_break_fix(lesson3, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's description spell expects an ingredient name first and its potency second, "
        "but she passes them in the wrong order and the scroll displays gibberish instead of the correct label."
    ),
    'story_after': (
        "The arguments swapped into the right order, 'hero is level 5' appears on the scroll and the brew is correctly labelled."
    ),
    'prompt': (
        "Fix the call so the name comes first and the level comes second, printing 'hero is level 5'."
    ),
    'broken_code': "def describe(name, level):\n    print(name + \" is level \" + str(level))\n\ndescribe(5, \"hero\")",
    'hint': "Look at the order of the arguments in the call — name should come before level.",
    'explanation': (
        "describe(5, \"hero\") passes 5 as name and \"hero\" as level, causing a TypeError when str(level) is concatenated. "
        "Swapping to describe(\"hero\", 5) puts name and level in the correct positions and prints 'hero is level 5'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hero is level 5'",
            'message': "Should print hero is level 5"
        }
    ]
})

apply_break_fix(lesson3, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's crew-profile subroutine takes a crew member's name first and their rank level second, "
        "but the arguments are passed in reverse and the ship's log shows an error."
    ),
    'story_after': (
        "With the arguments in the right order the log reads 'hero is level 5' and the crew profile is confirmed."
    ),
    'prompt': (
        "Fix the call so the name comes first and the level comes second, printing 'hero is level 5'."
    ),
    'broken_code': "def describe(name, level):\n    print(name + \" is level \" + str(level))\n\ndescribe(5, \"hero\")",
    'hint': "Look at the order of the arguments in the call — name should come before level.",
    'explanation': (
        "describe(5, \"hero\") passes 5 as name and \"hero\" as level, causing a TypeError when str(level) is concatenated. "
        "Swapping to describe(\"hero\", 5) puts name and level in the correct positions and prints 'hero is level 5'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hero is level 5'",
            'message': "Should print hero is level 5"
        }
    ]
})

apply_break_fix(lesson3, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's suspect-description tool expects a name first and a threat level second, "
        "but the arguments are swapped and the precinct terminal throws an error when it tries to build the profile."
    ),
    'story_after': (
        "Arguments corrected, 'hero is level 5' prints cleanly and the suspect profile is filed successfully."
    ),
    'prompt': (
        "Fix the call so the name comes first and the level comes second, printing 'hero is level 5'."
    ),
    'broken_code': "def describe(name, level):\n    print(name + \" is level \" + str(level))\n\ndescribe(5, \"hero\")",
    'hint': "Look at the order of the arguments in the call — name should come before level.",
    'explanation': (
        "describe(5, \"hero\") passes 5 as name and \"hero\" as level, causing a TypeError when str(level) is concatenated. "
        "Swapping to describe(\"hero\", 5) puts name and level in the correct positions and prints 'hero is level 5'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'hero is level 5'",
            'message': "Should print hero is level 5"
        }
    ]
})

# ── Lesson 4 ── Functions Returning Booleans
# Bug: comparison is `> 50` (strict) instead of `>= 50` (inclusive).
# is_passing(50) returns False with > 50, but True with >= 50. Output: 'True'.

lesson4 = f"{BASE}/unit_5/lesson_4.yaml"

apply_break_fix(lesson4, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's parity oracle should declare a potion that scores exactly 50 as passing, "
        "but the boundary is set incorrectly and the oracle rejects a perfectly adequate brew."
    ),
    'story_after': (
        "The oracle now returns True for a score of exactly 50 and Elara's potion earns its seal of approval."
    ),
    'prompt': (
        "Fix the comparison so that a score of exactly 50 is considered passing and prints True."
    ),
    'broken_code': "def is_passing(score):\n    return score > 50\n\nprint(is_passing(50))",
    'hint': "Look at the comparison operator — the boundary value of 50 should be included as passing.",
    'explanation': (
        "score > 50 is strictly greater than, so is_passing(50) returns False. "
        "Changing it to score >= 50 includes the boundary and returns True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (50 is a passing score)"
        }
    ]
})

apply_break_fix(lesson4, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's diagnostic checker should mark a system as passing when it reaches exactly the minimum threshold of 50, "
        "but the strict comparison incorrectly fails the system at that exact reading."
    ),
    'story_after': (
        "True prints on the diagnostic panel — the system at exactly 50 is correctly cleared as passing."
    ),
    'prompt': (
        "Fix the comparison so that a score of exactly 50 is considered passing and prints True."
    ),
    'broken_code': "def is_passing(score):\n    return score > 50\n\nprint(is_passing(50))",
    'hint': "Look at the comparison operator — the boundary value of 50 should be included as passing.",
    'explanation': (
        "score > 50 is strictly greater than, so is_passing(50) returns False. "
        "Changing it to score >= 50 includes the boundary and returns True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (50 is a passing score)"
        }
    ]
})

apply_break_fix(lesson4, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's evidence-checker should confirm that exactly 50 clues is sufficient to proceed, "
        "but the strict comparison wrongly rejects that exact count and the lead is abandoned."
    ),
    'story_after': (
        "True prints in the case file — 50 clues is now correctly recognised as sufficient evidence."
    ),
    'prompt': (
        "Fix the comparison so that a score of exactly 50 is considered passing and prints True."
    ),
    'broken_code': "def is_passing(score):\n    return score > 50\n\nprint(is_passing(50))",
    'hint': "Look at the comparison operator — the boundary value of 50 should be included as passing.",
    'explanation': (
        "score > 50 is strictly greater than, so is_passing(50) returns False. "
        "Changing it to score >= 50 includes the boundary and returns True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (50 is a passing score)"
        }
    ]
})

# ── Lesson 5 ── Functions Calling Functions
# Bug: outer function calls add_bonus(score) but discards the return value, then returns the original score.
# final_score(40) returns 40 instead of 50.
# Fixed: change `add_bonus(score)` to `return add_bonus(score)`. Output: '50'.

lesson5 = f"{BASE}/unit_5/lesson_5.yaml"

apply_break_fix(lesson5, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's outer enhancement spell calls an inner bonus spell to amplify the result, "
        "but she throws away what the inner spell returns and hands back the original unenhanced value."
    ),
    'story_after': (
        "50 glows on the rune display — the outer spell now passes through the enhanced result from the inner one."
    ),
    'prompt': (
        "Fix the outer function so it returns the value produced by add_bonus and prints 50."
    ),
    'broken_code': (
        "def add_bonus(score):\n    return score + 10\n\n"
        "def final_score(score):\n    add_bonus(score)\n    return score\n\n"
        "print(final_score(40))"
    ),
    'hint': "Look at the line that calls add_bonus — the returned value is being discarded instead of passed back.",
    'explanation': (
        "add_bonus(score) is called but its return value is ignored, so final_score returns the original score of 40. "
        "Changing the line to return add_bonus(score) passes the enhanced value of 50 back to the caller."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '50'",
            'message': "Should print 50"
        }
    ]
})

apply_break_fix(lesson5, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's outer subroutine invokes a power-boost sub to increase the score, "
        "but the boosted value is silently discarded and the caller receives the original unboosted number."
    ),
    'story_after': (
        "50 transmits to the console — the chained subroutines now pass the boosted value all the way through."
    ),
    'prompt': (
        "Fix the outer function so it returns the value produced by add_bonus and prints 50."
    ),
    'broken_code': (
        "def add_bonus(score):\n    return score + 10\n\n"
        "def final_score(score):\n    add_bonus(score)\n    return score\n\n"
        "print(final_score(40))"
    ),
    'hint': "Look at the line that calls add_bonus — the returned value is being discarded instead of passed back.",
    'explanation': (
        "add_bonus(score) is called but its return value is ignored, so final_score returns the original score of 40. "
        "Changing the line to return add_bonus(score) passes the enhanced value of 50 back to the caller."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '50'",
            'message': "Should print 50"
        }
    ]
})

apply_break_fix(lesson5, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's outer deduction function calls a clue-weighing sub to strengthen the score, "
        "but the weighted result is never used and the final deduction reports the original unweighted value."
    ),
    'story_after': (
        "50 appears in the case file — the chained deductions now carry the weighted score all the way to the output."
    ),
    'prompt': (
        "Fix the outer function so it returns the value produced by add_bonus and prints 50."
    ),
    'broken_code': (
        "def add_bonus(score):\n    return score + 10\n\n"
        "def final_score(score):\n    add_bonus(score)\n    return score\n\n"
        "print(final_score(40))"
    ),
    'hint': "Look at the line that calls add_bonus — the returned value is being discarded instead of passed back.",
    'explanation': (
        "add_bonus(score) is called but its return value is ignored, so final_score returns the original score of 40. "
        "Changing the line to return add_bonus(score) passes the enhanced value of 50 back to the caller."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '50'",
            'message': "Should print 50"
        }
    ]
})

print("\nAll Unit 5 break-and-fix exercises applied.")
