import yaml

BASE = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units"


def apply_break_fix(path, world, exercise):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data['worlds'][world]['exercises'].append(exercise)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ── Lesson 1 ── Floor Division, Modulo, Exponents
# Bug: ^ (bitwise XOR) used instead of ** (exponentiation). 2 ^ 8 == 10, not 256.

lesson1 = f"{BASE}/unit_2/lesson_1.yaml"

apply_break_fix(lesson1, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara needs to calculate how many potion flasks a batch formula will produce — "
        "the recipe calls for 2 to the power of 8, but she has used the wrong operator."
    ),
    'story_after': (
        "The corrected formula blazes 256 on the cauldron's rune display, and Elara's mentor nods with approval."
    ),
    'prompt': (
        "Fix the code so it correctly calculates 2 to the power of 8 and prints 256."
    ),
    'broken_code': "result = 2 ^ 8\nprint(result)",
    'hint': "Look for the wrong operator — Python uses ** for exponentiation, not ^.",
    'explanation': (
        "^ is bitwise XOR in Python, not exponentiation. "
        "2 ^ 8 evaluates to 10, but 2 ** 8 correctly gives 256."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '256'",
            'message': "Should print 256 (2 ** 8)"
        }
    ]
})

apply_break_fix(lesson1, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Zara is calculating the Helix's power output for a jump sequence — "
        "the formula requires 2 to the power of 8, but the wrong operator has crept into the code."
    ),
    'story_after': (
        "256 units of power flood the display and the jump drive spools up correctly."
    ),
    'prompt': (
        "Fix the code so it correctly calculates 2 to the power of 8 and prints 256."
    ),
    'broken_code': "result = 2 ^ 8\nprint(result)",
    'hint': "Look for the wrong operator — Python uses ** for exponentiation, not ^.",
    'explanation': (
        "^ is bitwise XOR in Python, not exponentiation. "
        "2 ^ 8 evaluates to 10, but 2 ** 8 correctly gives 256."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '256'",
            'message': "Should print 256 (2 ** 8)"
        }
    ]
})

apply_break_fix(lesson1, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole is computing the cipher key strength for a coded message — "
        "the formula needs 2 to the power of 8, but a wrong operator is producing a garbage result."
    ),
    'story_after': (
        "256 prints cleanly and Cole confirms the cipher key strength, unlocking the next stage of the investigation."
    ),
    'prompt': (
        "Fix the code so it correctly calculates 2 to the power of 8 and prints 256."
    ),
    'broken_code': "result = 2 ^ 8\nprint(result)",
    'hint': "Look for the wrong operator — Python uses ** for exponentiation, not ^.",
    'explanation': (
        "^ is bitwise XOR in Python, not exponentiation. "
        "2 ^ 8 evaluates to 10, but 2 ** 8 correctly gives 256."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '256'",
            'message': "Should print 256 (2 ** 8)"
        }
    ]
})

# ── Lesson 2 ── Order of Operations
# Bug: missing parentheses. 2 + 3 * 4 == 14, but (2 + 3) * 4 == 20.

lesson2 = f"{BASE}/unit_2/lesson_2.yaml"

apply_break_fix(lesson2, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's spell formula should add two ingredient counts together first, then multiply by the batch size — "
        "but without parentheses the multiplication runs first and the result is wrong."
    ),
    'story_after': (
        "With the brackets in place the spell formula returns 20, and the batch size is correct."
    ),
    'prompt': (
        "Fix the code so the addition happens before the multiplication and it prints 20."
    ),
    'broken_code': "result = 2 + 3 * 4\nprint(result)",
    'hint': "Look for missing parentheses — addition needs to happen before multiplication here.",
    'explanation': (
        "Without parentheses Python evaluates 3 * 4 = 12 first, then adds 2, giving 14. "
        "Wrapping the addition in brackets, (2 + 3) * 4, forces it to run first and gives 20."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '20'",
            'message': "Should print 20 ((2 + 3) * 4)"
        }
    ]
})

apply_break_fix(lesson2, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Zara's power formula adds two energy sources and then multiplies by the boost factor — "
        "but the missing parentheses mean the multiplication runs first and the output is wrong."
    ),
    'story_after': (
        "The corrected formula prints 20 and the Helix's boost calculation is accurate."
    ),
    'prompt': (
        "Fix the code so the addition happens before the multiplication and it prints 20."
    ),
    'broken_code': "result = 2 + 3 * 4\nprint(result)",
    'hint': "Look for missing parentheses — addition needs to happen before multiplication here.",
    'explanation': (
        "Without parentheses Python evaluates 3 * 4 = 12 first, then adds 2, giving 14. "
        "Wrapping the addition in brackets, (2 + 3) * 4, forces it to run first and gives 20."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '20'",
            'message': "Should print 20 ((2 + 3) * 4)"
        }
    ]
})

apply_break_fix(lesson2, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's scoring formula combines two clue groups and scales them by the case weight — "
        "but without parentheses the multiplication runs first and the score comes out wrong."
    ),
    'story_after': (
        "The corrected formula prints 20 and Cole's evidence weight is properly calculated."
    ),
    'prompt': (
        "Fix the code so the addition happens before the multiplication and it prints 20."
    ),
    'broken_code': "result = 2 + 3 * 4\nprint(result)",
    'hint': "Look for missing parentheses — addition needs to happen before multiplication here.",
    'explanation': (
        "Without parentheses Python evaluates 3 * 4 = 12 first, then adds 2, giving 14. "
        "Wrapping the addition in brackets, (2 + 3) * 4, forces it to run first and gives 20."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '20'",
            'message': "Should print 20 ((2 + 3) * 4)"
        }
    ]
})

# ── Lesson 3 ── Comparison Operators
# Bug: > used instead of >=. print(5 > 5) prints False, but print(5 >= 5) prints True.

lesson3 = f"{BASE}/unit_2/lesson_3.yaml"

apply_break_fix(lesson3, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's Truth Rune should confirm that a potion strength of exactly 5 meets the minimum threshold of 5 — "
        "but the wrong comparison operator means the rune returns False instead of True."
    ),
    'story_after': (
        "The rune glows True and Elara's mentor confirms the potion passes the threshold check."
    ),
    'prompt': (
        "Fix the code so that a strength of 5 compared to a minimum of 5 prints True."
    ),
    'broken_code': "strength = 5\nprint(strength > 5)",
    'hint': "Look for the wrong comparison operator — the boundary value should be included.",
    'explanation': (
        "> means strictly greater than, so 5 > 5 is False. "
        "Changing it to >= (greater than or equal to) makes 5 >= 5 evaluate to True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (5 >= 5)"
        }
    ]
})

apply_break_fix(lesson3, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Zara's hull integrity sensor should confirm that a reading of exactly 5 meets the safe minimum of 5 — "
        "but the wrong operator makes the check return False and trigger a false alarm."
    ),
    'story_after': (
        "True prints and the false alarm clears — hull integrity is confirmed at the safe minimum."
    ),
    'prompt': (
        "Fix the code so that a hull integrity of 5 compared to a minimum of 5 prints True."
    ),
    'broken_code': "hull_integrity = 5\nprint(hull_integrity > 5)",
    'hint': "Look for the wrong comparison operator — the boundary value should be included.",
    'explanation': (
        "> means strictly greater than, so 5 > 5 is False. "
        "Changing it to >= (greater than or equal to) makes 5 >= 5 evaluate to True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (5 >= 5)"
        }
    ]
})

apply_break_fix(lesson3, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's analysis script should flag that a clue count of exactly 5 meets the required threshold of 5 — "
        "but the wrong comparison operator causes it to return False and the lead gets dropped."
    ),
    'story_after': (
        "True prints and the lead is correctly flagged — the clue count meets the threshold."
    ),
    'prompt': (
        "Fix the code so that a clue count of 5 compared to a threshold of 5 prints True."
    ),
    'broken_code': "clue_count = 5\nprint(clue_count > 5)",
    'hint': "Look for the wrong comparison operator — the boundary value should be included.",
    'explanation': (
        "> means strictly greater than, so 5 > 5 is False. "
        "Changing it to >= (greater than or equal to) makes 5 >= 5 evaluate to True."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (5 >= 5)"
        }
    ]
})

# ── Lesson 4 ── Booleans and bool()
# Bug: `and` used instead of `or`.
# score = 80, bonus = 5. (score >= 50) and (bonus >= 10) → True and False → False.
# Fixed: (score >= 50) or (bonus >= 10) → True or False → True.

lesson4 = f"{BASE}/unit_2/lesson_4.yaml"

apply_break_fix(lesson4, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's Truth Stone should light up when a score is high enough OR a bonus meets its target — "
        "but the code uses and instead of or, so the stone stays dark even when one condition is true."
    ),
    'story_after': (
        "The Truth Stone glows True and Elara's mentor confirms the logical gate is now correct."
    ),
    'prompt': (
        "Fix the code so is_valid is True when score >= 50 OR bonus >= 10, and print it. "
        "With score = 80 and bonus = 5 the result should be True."
    ),
    'broken_code': "score = 80\nbonus = 5\nis_valid = (score >= 50) and (bonus >= 10)\nprint(is_valid)",
    'hint': "Look for the wrong logical operator — only one condition needs to be true here.",
    'explanation': (
        "and requires both conditions to be True, so True and False gives False. "
        "Changing and to or means True or False gives True, which is the intended behaviour."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (score >= 50 OR bonus >= 10)"
        }
    ]
})

apply_break_fix(lesson4, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Zara's status flag should read True when power is sufficient OR the bonus reserve meets its minimum — "
        "but the code uses and instead of or, so the flag stays False even when power is fine."
    ),
    'story_after': (
        "True prints on the status panel and Zara clears the ship for the next manoeuvre."
    ),
    'prompt': (
        "Fix the code so is_valid is True when score >= 50 OR bonus >= 10, and print it. "
        "With score = 80 and bonus = 5 the result should be True."
    ),
    'broken_code': "score = 80\nbonus = 5\nis_valid = (score >= 50) and (bonus >= 10)\nprint(is_valid)",
    'hint': "Look for the wrong logical operator — only one condition needs to be true here.",
    'explanation': (
        "and requires both conditions to be True, so True and False gives False. "
        "Changing and to or means True or False gives True, which is the intended behaviour."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (score >= 50 OR bonus >= 10)"
        }
    ]
})

apply_break_fix(lesson4, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's profile flag should be set True when a suspect score is high enough OR a bonus indicator meets its bar — "
        "but the code uses and instead of or, and the flag returns False even when the score alone qualifies."
    ),
    'story_after': (
        "True prints in the case file and Cole adds the suspect to the active list."
    ),
    'prompt': (
        "Fix the code so is_valid is True when score >= 50 OR bonus >= 10, and print it. "
        "With score = 80 and bonus = 5 the result should be True."
    ),
    'broken_code': "score = 80\nbonus = 5\nis_valid = (score >= 50) and (bonus >= 10)\nprint(is_valid)",
    'hint': "Look for the wrong logical operator — only one condition needs to be true here.",
    'explanation': (
        "and requires both conditions to be True, so True and False gives False. "
        "Changing and to or means True or False gives True, which is the intended behaviour."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'True'",
            'message': "Should print True (score >= 50 OR bonus >= 10)"
        }
    ]
})

# ── Lesson 5 ── Logical Operators: and, or, not
# Bug: condition is `if locked:` instead of `if not locked:`.
# locked = False, so `if locked:` takes the else branch and prints "Locked".
# Fix: change to `if not locked:` to print "Open".

lesson5 = f"{BASE}/unit_2/lesson_5.yaml"

apply_break_fix(lesson5, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's gate spell should open the door when it is NOT locked — "
        "but the condition checks the wrong direction and the gate stays shut even though it is unlocked."
    ),
    'story_after': (
        "Open prints and the gate swings wide — Elara's mentor smiles as the not operator does its job."
    ),
    'prompt': (
        "Fix the code so the gate prints 'Open' when locked is False."
    ),
    'broken_code': "locked = False\nif locked:\n    print(\"Open\")\nelse:\n    print(\"Locked\")",
    'hint': "Look for the missing not — the gate should open when it is NOT locked.",
    'explanation': (
        "if locked: is True only when locked is True, so with locked = False the else branch runs and prints 'Locked'. "
        "Changing the condition to if not locked: flips the logic so the gate opens correctly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Open'",
            'message': "Should print Open (gate is not locked)"
        }
    ]
})

apply_break_fix(lesson5, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Zara's airlock should open when it is NOT sealed — "
        "but the check is inverted and the airlock reports itself as locked even though the seal is disengaged."
    ),
    'story_after': (
        "Open prints on the airlock panel and Zara steps through without delay."
    ),
    'prompt': (
        "Fix the code so the airlock prints 'Open' when locked is False."
    ),
    'broken_code': "locked = False\nif locked:\n    print(\"Open\")\nelse:\n    print(\"Locked\")",
    'hint': "Look for the missing not — the airlock should open when it is NOT sealed.",
    'explanation': (
        "if locked: is True only when locked is True, so with locked = False the else branch runs and prints 'Locked'. "
        "Changing the condition to if not locked: flips the logic so the airlock opens correctly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Open'",
            'message': "Should print Open (airlock is not sealed)"
        }
    ]
})

apply_break_fix(lesson5, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's evidence safe should open when it is NOT secured — "
        "but the condition is backwards and the safe reports itself as locked even though it has been disarmed."
    ),
    'story_after': (
        "Open prints and Cole retrieves the key evidence, finally getting the break the case needed."
    ),
    'prompt': (
        "Fix the code so the safe prints 'Open' when locked is False."
    ),
    'broken_code': "locked = False\nif locked:\n    print(\"Open\")\nelse:\n    print(\"Locked\")",
    'hint': "Look for the missing not — the safe should open when it is NOT secured.",
    'explanation': (
        "if locked: is True only when locked is True, so with locked = False the else branch runs and prints 'Locked'. "
        "Changing the condition to if not locked: flips the logic so the safe opens correctly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Open'",
            'message': "Should print Open (safe is not secured)"
        }
    ]
})

print("\nAll Unit 2 break-and-fix exercises applied.")
