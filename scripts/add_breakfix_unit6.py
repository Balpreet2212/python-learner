import yaml

BASE = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units"


def apply_break_fix(path, world, exercise):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data['worlds'][world]['exercises'].append(exercise)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ── Lesson 1 ── Creating Lists and Indexing
# Bug: index is 3 but the list only has 3 items (indices 0-2) → IndexError. Should be items[2].

lesson1 = f"{BASE}/unit_6/lesson_1.yaml"

apply_break_fix(lesson1, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara is packing the supply crate for the expedition and needs to call out the third item — "
        "potion, scroll, key — but her index spell reaches one slot too far and the crate cracks with an error."
    ),
    'story_after': (
        "The correct index illuminates the rune and 'key' appears on the crate's label — the expedition can depart."
    ),
    'prompt': (
        "Fix the code so it prints the third item in the list without causing an IndexError."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nprint(items[3])",
    'hint': "A list with three items has valid indices 0, 1, and 2 — index 3 is out of range.",
    'explanation': (
        "Python lists are zero-indexed, so a three-item list has positions 0, 1, and 2. "
        "items[3] is one past the end and raises an IndexError; items[2] correctly retrieves the third item, 'key'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'key'",
            'message': "Should print key (items[2])"
        }
    ]
})

apply_break_fix(lesson1, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara is querying the ship manifest to read the third system status — the list holds three entries — "
        "but her query uses an out-of-range index and the console throws an error."
    ),
    'story_after': (
        "'key' appears on the status panel and Yara confirms all three systems are accounted for."
    ),
    'prompt': (
        "Fix the code so it prints the third item in the list without causing an IndexError."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nprint(items[3])",
    'hint': "A list with three items has valid indices 0, 1, and 2 — index 3 is out of range.",
    'explanation': (
        "Python lists are zero-indexed, so a three-item list has positions 0, 1, and 2. "
        "items[3] is one past the end and raises an IndexError; items[2] correctly retrieves the third entry, 'key'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'key'",
            'message': "Should print key (items[2])"
        }
    ]
})

apply_break_fix(lesson1, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole is reading the third piece of evidence from the evidence box — potion, scroll, key — "
        "but he uses index 3 instead of 2 and the program crashes before he can read it."
    ),
    'story_after': (
        "'key' prints to the terminal and Cole pins it to the board as the crucial third clue."
    ),
    'prompt': (
        "Fix the code so it prints the third item in the list without causing an IndexError."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nprint(items[3])",
    'hint': "A list with three items has valid indices 0, 1, and 2 — index 3 is out of range.",
    'explanation': (
        "Python lists are zero-indexed, so a three-item list has positions 0, 1, and 2. "
        "items[3] is one past the end and raises an IndexError; items[2] correctly retrieves the third piece of evidence, 'key'."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'key'",
            'message': "Should print key (items[2])"
        }
    ]
})


# ── Lesson 2 ── Modifying Lists
# Bug: uses .add() instead of .append(). list.add() doesn't exist → AttributeError.

lesson2 = f"{BASE}/unit_6/lesson_2.yaml"

apply_break_fix(lesson2, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara is repacking the supply crate and tries to add a key to her ingredient list using the wrong spell — "
        ".add() does not exist for lists and the workshop fills with a crackling AttributeError."
    ),
    'story_after': (
        "The list expands correctly and the crate now shows all three supplies ready for departure."
    ),
    'prompt': (
        "Fix the code so the key is added to the list and the full list is printed."
    ),
    'broken_code': "items = [\"potion\", \"scroll\"]\nitems.add(\"key\")\nprint(items)",
    'hint': "Lists do not have an .add() method — look for the correct method to add an item to the end.",
    'explanation': (
        ".add() is a set method, not a list method. "
        "To add an item to the end of a list, use .append(); items.append('key') gives ['potion', 'scroll', 'key']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['potion', 'scroll', 'key']\"",
            'message': "Should print ['potion', 'scroll', 'key']"
        }
    ]
})

apply_break_fix(lesson2, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara is updating the ship manifest and tries to add a new crew member to the list using the wrong method — "
        ".add() triggers an AttributeError and the manifest update fails."
    ),
    'story_after': (
        "The manifest updates correctly and all three entries are confirmed on the bridge display."
    ),
    'prompt': (
        "Fix the code so the key is added to the list and the full list is printed."
    ),
    'broken_code': "items = [\"potion\", \"scroll\"]\nitems.add(\"key\")\nprint(items)",
    'hint': "Lists do not have an .add() method — look for the correct method to add an item to the end.",
    'explanation': (
        ".add() is a set method, not a list method. "
        "To add an item to the end of a list, use .append(); items.append('key') gives ['potion', 'scroll', 'key']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['potion', 'scroll', 'key']\"",
            'message': "Should print ['potion', 'scroll', 'key']"
        }
    ]
})

apply_break_fix(lesson2, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole is logging a new clue to the evidence list but uses the wrong method name — "
        ".add() raises an AttributeError and the evidence board stays incomplete."
    ),
    'story_after': (
        "The clue is logged and the full evidence list prints — Cole's board is up to date."
    ),
    'prompt': (
        "Fix the code so the key is added to the list and the full list is printed."
    ),
    'broken_code': "items = [\"potion\", \"scroll\"]\nitems.add(\"key\")\nprint(items)",
    'hint': "Lists do not have an .add() method — look for the correct method to add an item to the end.",
    'explanation': (
        ".add() is a set method, not a list method. "
        "To add an item to the end of a list, use .append(); items.append('key') gives ['potion', 'scroll', 'key']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['potion', 'scroll', 'key']\"",
            'message': "Should print ['potion', 'scroll', 'key']"
        }
    ]
})


# ── Lesson 3 ── Slicing and Searching Lists
# Bug: slice [1:2] returns only one item; [1:3] is needed to get items at index 1 and 2.

lesson3 = f"{BASE}/unit_6/lesson_3.yaml"

apply_break_fix(lesson3, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's slice spell is meant to grab the second and third items from the supply crate — "
        "but her slice window ends one position too early and only a single item comes back."
    ),
    'story_after': (
        "Both 'b' and 'c' appear together and Elara's supply check is complete."
    ),
    'prompt': (
        "Fix the slice so it returns both items at index 1 and 2 and prints ['b', 'c']."
    ),
    'broken_code': "items = [\"a\", \"b\", \"c\", \"d\"]\nprint(items[1:2])",
    'hint': "A slice [start:stop] excludes the stop index — extend the stop by one to include both items.",
    'explanation': (
        "items[1:2] includes only index 1, giving ['b']. "
        "To include both index 1 and 2, the stop must be 3: items[1:3] returns ['b', 'c']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['b', 'c']\"",
            'message': "Should print ['b', 'c']"
        }
    ]
})

apply_break_fix(lesson3, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's sensor scan window is supposed to read two consecutive sectors but the slice is one position too narrow — "
        "only one sector reading comes back and the safety report is incomplete."
    ),
    'story_after': (
        "Both sectors print and Yara files the complete sensor report before the jump."
    ),
    'prompt': (
        "Fix the slice so it returns both items at index 1 and 2 and prints ['b', 'c']."
    ),
    'broken_code': "items = [\"a\", \"b\", \"c\", \"d\"]\nprint(items[1:2])",
    'hint': "A slice [start:stop] excludes the stop index — extend the stop by one to include both items.",
    'explanation': (
        "items[1:2] includes only index 1, giving ['b']. "
        "To include both index 1 and 2, the stop must be 3: items[1:3] returns ['b', 'c']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['b', 'c']\"",
            'message': "Should print ['b', 'c']"
        }
    ]
})

apply_break_fix(lesson3, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Cole's evidence slice is supposed to pull two consecutive items from the evidence log — "
        "but the range ends one position short and the last item in the range is silently missed."
    ),
    'story_after': (
        "Both pieces of evidence appear and Cole can cross-reference the full range on the board."
    ),
    'prompt': (
        "Fix the slice so it returns both items at index 1 and 2 and prints ['b', 'c']."
    ),
    'broken_code': "items = [\"a\", \"b\", \"c\", \"d\"]\nprint(items[1:2])",
    'hint': "A slice [start:stop] excludes the stop index — extend the stop by one to include both items.",
    'explanation': (
        "items[1:2] includes only index 1, giving ['b']. "
        "To include both index 1 and 2, the stop must be 3: items[1:3] returns ['b', 'c']."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == \"['b', 'c']\"",
            'message': "Should print ['b', 'c']"
        }
    ]
})


# ── Lesson 4 ── Looping Over Lists
# Bug: for i in items: iterates over item values (strings), then print(items[i]) tries to use
# a string as an integer index → TypeError. Fix: print(i) directly.

lesson4 = f"{BASE}/unit_6/lesson_4.yaml"

apply_break_fix(lesson4, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's enchanted inventory loop moves through each item correctly — "
        "but then tries to use the item name itself as a numeric index into the list, crashing with a TypeError."
    ),
    'story_after': (
        "Each item name prints on its own line and the inventory scroll is complete."
    ),
    'prompt': (
        "Fix the loop so each item in the list is printed directly, one per line."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nfor i in items:\n    print(items[i])",
    'hint': "When you loop with 'for i in items', i is already the item value — you do not need to index into the list again.",
    'explanation': (
        "for i in items: assigns each element (a string) to i, not its integer position. "
        "Using items[i] tries to use a string as an index, causing a TypeError. "
        "Replacing items[i] with just i prints each item directly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print potion, scroll, key each on its own line"
        }
    ]
})

apply_break_fix(lesson4, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's processing loop iterates through the sensor array correctly — "
        "but then uses each item value as a list index by mistake, and the console throws a TypeError."
    ),
    'story_after': (
        "Each system name scrolls across the display in order and the processing log is complete."
    ),
    'prompt': (
        "Fix the loop so each item in the list is printed directly, one per line."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nfor i in items:\n    print(items[i])",
    'hint': "When you loop with 'for i in items', i is already the item value — you do not need to index into the list again.",
    'explanation': (
        "for i in items: assigns each element (a string) to i, not its integer position. "
        "Using items[i] tries to use a string as an index, causing a TypeError. "
        "Replacing items[i] with just i prints each item directly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print potion, scroll, key each on its own line"
        }
    ]
})

apply_break_fix(lesson4, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole's clue-review loop walks the evidence list item by item — "
        "but then mistakenly uses each clue string as a list index, triggering a TypeError before a single clue is read."
    ),
    'story_after': (
        "Each clue name appears on its own line and Cole can finally review the full evidence list."
    ),
    'prompt': (
        "Fix the loop so each item in the list is printed directly, one per line."
    ),
    'broken_code': "items = [\"potion\", \"scroll\", \"key\"]\nfor i in items:\n    print(items[i])",
    'hint': "When you loop with 'for i in items', i is already the item value — you do not need to index into the list again.",
    'explanation': (
        "for i in items: assigns each element (a string) to i, not its integer position. "
        "Using items[i] tries to use a string as an index, causing a TypeError. "
        "Replacing items[i] with just i prints each item directly."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print potion, scroll, key each on its own line"
        }
    ]
})


# ── Lesson 5 ── List Comprehensions
# Bug: condition uses > 5 instead of >= 5, so the boundary value 5 is excluded.

lesson5 = f"{BASE}/unit_6/lesson_5.yaml"

apply_break_fix(lesson5, 'fantasy', {
    'type': 'break_fix',
    'story_before': (
        "Elara's filter rune is meant to keep every score that meets the minimum threshold of 5 — "
        "but the strict greater-than condition silently drops the boundary value and 5 is excluded from the result."
    ),
    'story_after': (
        "The rune glows and [5, 7, 9] appears — all three passing scores are through, including the borderline 5."
    ),
    'prompt': (
        "Fix the comprehension so scores of 5 and above are included and it prints [5, 7, 9]."
    ),
    'broken_code': "scores = [3, 5, 7, 9]\npassing = [s for s in scores if s > 5]\nprint(passing)",
    'hint': "The boundary value 5 should pass — change the condition to include values equal to the threshold.",
    'explanation': (
        "s > 5 is strictly greater than, so 5 itself is excluded, giving [7, 9]. "
        "Changing to s >= 5 includes the boundary value and correctly produces [5, 7, 9]."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '[5, 7, 9]'",
            'message': "Should print [5, 7, 9]"
        }
    ]
})

apply_break_fix(lesson5, 'scifi', {
    'type': 'break_fix',
    'story_before': (
        "Yara's data pipeline filter is supposed to pass any reading at or above 5 — "
        "but the strict greater-than condition drops the boundary reading of 5 and the report comes out short."
    ),
    'story_after': (
        "[5, 7, 9] prints on the console and Yara's pipeline passes all qualifying readings, including the borderline one."
    ),
    'prompt': (
        "Fix the comprehension so scores of 5 and above are included and it prints [5, 7, 9]."
    ),
    'broken_code': "scores = [3, 5, 7, 9]\npassing = [s for s in scores if s > 5]\nprint(passing)",
    'hint': "The boundary value 5 should pass — change the condition to include values equal to the threshold.",
    'explanation': (
        "s > 5 is strictly greater than, so 5 itself is excluded, giving [7, 9]. "
        "Changing to s >= 5 includes the boundary value and correctly produces [5, 7, 9]."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '[5, 7, 9]'",
            'message': "Should print [5, 7, 9]"
        }
    ]
})

apply_break_fix(lesson5, 'mystery', {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole is filtering witness credibility scores and needs everyone at 5 or above — "
        "but the strict greater-than drops the borderline witness with a score of exactly 5, weakening the case."
    ),
    'story_after': (
        "[5, 7, 9] appears in the case file and Cole's witness list is complete — the borderline witness is back in."
    ),
    'prompt': (
        "Fix the comprehension so scores of 5 and above are included and it prints [5, 7, 9]."
    ),
    'broken_code': "scores = [3, 5, 7, 9]\npassing = [s for s in scores if s > 5]\nprint(passing)",
    'hint': "The boundary value 5 should pass — change the condition to include values equal to the threshold.",
    'explanation': (
        "s > 5 is strictly greater than, so 5 itself is excluded, giving [7, 9]. "
        "Changing to s >= 5 includes the boundary value and correctly produces [5, 7, 9]."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '[5, 7, 9]'",
            'message': "Should print [5, 7, 9]"
        }
    ]
})

print("\nAll Unit 6 break-and-fix exercises applied.")
