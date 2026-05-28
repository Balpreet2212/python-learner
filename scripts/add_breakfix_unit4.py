import yaml

BASE = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units"


def apply_break_fix(path, world, exercise):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data['worlds'][world]['exercises'].append(exercise)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1 — for Loops with range()
# Bug: range(1, 5) should be range(1, 6) to include 5 (off-by-one)
# ─────────────────────────────────────────────────────────────────────────────
L1 = BASE + r"\unit_4\lesson_1.yaml"

apply_break_fix(L1, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara's enchanted herb picker is supposed to harvest every row from 1 to 5, "
        "but the master's basket keeps coming back with only four bundles — row 5 is always bare."
    ),
    'story_after': (
        "With the range corrected to include row 5, all five bundles fill the basket and the master nods with satisfaction."
    ),
    'prompt': (
        "Elara's harvesting spell loops through herb rows 1 to 5, but it stops one row too early. "
        "Fix the range so that row 5 is included and all five row numbers are printed."
    ),
    'broken_code': "for i in range(1, 5):\n    print(i)",
    'hint': "Check the stop value of range() — Python stops before it, so you may need to go one higher.",
    'explanation': (
        "range(1, 5) produces 1, 2, 3, 4 — it stops before 5. "
        "Changing it to range(1, 6) includes 5, printing all five row numbers."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '1\\n2\\n3\\n4\\n5'",
            'message': "Should print 1 through 5, one number per line"
        }
    ]
})

apply_break_fix(L1, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara's sector scanner is programmed to sweep sectors 1 through 5, "
        "but the mission log shows only four sectors scanned — the final sector is never reached."
    ),
    'story_after': (
        "With the range fixed to stop after sector 5, all five sector IDs appear in the log and the sweep is complete."
    ),
    'prompt': (
        "Yara's scanner loop is supposed to log sectors 1 to 5, but it misses the last one. "
        "Fix the range so sector 5 is included and all five sector numbers are printed."
    ),
    'broken_code': "for i in range(1, 5):\n    print(i)",
    'hint': "Python's range() stops before its second argument — raise the stop value by 1.",
    'explanation': (
        "range(1, 5) yields 1, 2, 3, 4 because Python stops before the end value. "
        "Changing it to range(1, 6) adds sector 5 to the sequence."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '1\\n2\\n3\\n4\\n5'",
            'message': "Should print 1 through 5, one number per line"
        }
    ]
})

apply_break_fix(L1, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole's file-review program is meant to open case files numbered 1 through 5, "
        "but file 5 is never opened — the loop quits one number too soon."
    ),
    'story_after': (
        "Correcting the range to include 5 ensures all five files are reviewed and no evidence is overlooked."
    ),
    'prompt': (
        "Cole's loop should review file numbers 1 to 5, but it stops at 4. "
        "Fix the range so file 5 is included and all five file numbers are printed."
    ),
    'broken_code': "for i in range(1, 5):\n    print(i)",
    'hint': "The stop value in range() is exclusive — increment it by 1 to include the last file.",
    'explanation': (
        "range(1, 5) generates 1, 2, 3, 4 only. "
        "Using range(1, 6) extends the sequence to include 5, so all five file numbers are printed."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '1\\n2\\n3\\n4\\n5'",
            'message': "Should print 1 through 5, one number per line"
        }
    ]
})


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2 — for Loops with Lists
# Bug: loop variable is `item` but code prints `items` (the whole list)
# ─────────────────────────────────────────────────────────────────────────────
L2 = BASE + r"\unit_4\lesson_2.yaml"

apply_break_fix(L2, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara's inventory spell is supposed to announce each item in her satchel one at a time, "
        "but every incantation recites the entire satchel instead of a single item."
    ),
    'story_after': (
        "Switching from the list name to the loop variable fixes the spell — each item is announced on its own line."
    ),
    'prompt': (
        "Elara's loop should print each item from her satchel individually, "
        "but it prints the whole list every time. Fix the print statement to use the loop variable."
    ),
    'broken_code': 'items = ["potion", "scroll", "key"]\nfor item in items:\n    print(items)',
    'hint': "Check what you are passing to print — it should be the single loop variable, not the whole list.",
    'explanation': (
        "print(items) outputs the entire list object on every iteration. "
        "Changing it to print(item) uses the loop variable, which holds one element at a time."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print each item on its own line: potion, scroll, key"
        }
    ]
})

apply_break_fix(L2, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara's crew-manifest printer is meant to display each crew member's name in turn, "
        "but every line of output shows the full crew list instead of one name."
    ),
    'story_after': (
        "Using the loop variable instead of the list name fixes the manifest — each crew member is listed separately."
    ),
    'prompt': (
        "Yara's loop should print one crew member per line, "
        "but it prints the entire list on every iteration. Fix the print statement."
    ),
    'broken_code': 'items = ["potion", "scroll", "key"]\nfor item in items:\n    print(items)',
    'hint': "The print call should reference the loop variable that holds one item, not the list itself.",
    'explanation': (
        "print(items) dumps the whole list each iteration. "
        "Replacing it with print(item) correctly prints the current crew member's name."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print each item on its own line: potion, scroll, key"
        }
    ]
})

apply_break_fix(L2, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Detective Cole's evidence logger should record each piece of evidence separately, "
        "but the log shows the complete evidence list printed over and over instead."
    ),
    'story_after': (
        "Fixing the print to use the loop variable logs each piece of evidence on its own line, as required."
    ),
    'prompt': (
        "Cole's loop should print each evidence item individually, "
        "but it prints the full list every time. Fix the print statement to use the loop variable."
    ),
    'broken_code': 'items = ["potion", "scroll", "key"]\nfor item in items:\n    print(items)',
    'hint': "Look at the variable name inside the for statement — that is what print should receive.",
    'explanation': (
        "print(items) outputs the list object on every pass. "
        "Changing it to print(item) prints the individual element the loop variable currently holds."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'potion\\nscroll\\nkey'",
            'message': "Should print each item on its own line: potion, scroll, key"
        }
    ]
})


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3 — range() with Start, Stop, Step
# Bug: step is 1 instead of 2, so it prints every number instead of every other
# ─────────────────────────────────────────────────────────────────────────────
L3 = BASE + r"\unit_4\lesson_3.yaml"

apply_break_fix(L3, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara's path-tracer is supposed to mark every other stepping stone through the forest, "
        "but it is stamping every single stone — the trail looks nothing like the pattern on the map."
    ),
    'story_after': (
        "Changing the step from 1 to 2 makes the tracer skip alternate stones, matching the map's dotted path exactly."
    ),
    'prompt': (
        "Elara's loop should print every other number from 0 to 8 (0, 2, 4, 6, 8), "
        "but the step value is wrong so it prints every number. Fix the step in range()."
    ),
    'broken_code': "for i in range(0, 10, 1):\n    print(i)",
    'hint': "The third argument to range() is the step — change it so the loop skips every other value.",
    'explanation': (
        "range(0, 10, 1) steps by 1, producing 0 through 9. "
        "Changing the step to 2 gives range(0, 10, 2), which yields 0, 2, 4, 6, 8."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n2\\n4\\n6\\n8'",
            'message': "Should print 0, 2, 4, 6, 8 — every other number"
        }
    ]
})

apply_break_fix(L3, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara's scanner is configured to sample every other sector to conserve power, "
        "but the diagnostic log shows every sector being scanned — the power budget is blown."
    ),
    'story_after': (
        "Setting the step to 2 makes the scanner skip alternate sectors, restoring the efficient alternating pattern."
    ),
    'prompt': (
        "Yara's scan loop should hit sectors 0, 2, 4, 6, 8 only, "
        "but it is scanning every sector because the step is wrong. Fix the step in range()."
    ),
    'broken_code': "for i in range(0, 10, 1):\n    print(i)",
    'hint': "Increase the step argument in range() so the probe jumps two sectors at a time.",
    'explanation': (
        "A step of 1 visits every value from 0 to 9. "
        "Changing it to 2 produces range(0, 10, 2), sampling only the even-numbered sectors."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n2\\n4\\n6\\n8'",
            'message': "Should print 0, 2, 4, 6, 8 — every other sector"
        }
    ]
})

apply_break_fix(L3, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole's pattern checker is meant to flag every other file for a targeted review, "
        "but it is opening every single file — the pattern the captain described is completely ignored."
    ),
    'story_after': (
        "With the step corrected to 2, the checker flags files 0, 2, 4, 6, 8 — exactly the alternating pattern Cole needs."
    ),
    'prompt': (
        "Cole's loop should check every other file, printing 0, 2, 4, 6, 8, "
        "but it checks every file because the step is set to 1. Fix the step in range()."
    ),
    'broken_code': "for i in range(0, 10, 1):\n    print(i)",
    'hint': "The third argument to range() controls how many values are skipped — set it to skip one file each time.",
    'explanation': (
        "range(0, 10, 1) produces every integer from 0 to 9. "
        "Using a step of 2 changes it to range(0, 10, 2), giving only the even-indexed files."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n2\\n4\\n6\\n8'",
            'message': "Should print 0, 2, 4, 6, 8 — every other file"
        }
    ]
})


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 4 — while Loops
# Bug: condition is `count > 0` but count starts at 0, so loop never runs.
# Fix: change to `count < 3`
# ─────────────────────────────────────────────────────────────────────────────
L4 = BASE + r"\unit_4\lesson_4.yaml"

apply_break_fix(L4, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara's training counter is supposed to put the hero through three rounds of drills before declaring them done, "
        "but the champion never trains at all — the counter sits idle and only 'done' appears."
    ),
    'story_after': (
        "Flipping the condition to count < 3 lets the loop run three rounds, "
        "printing 0, 1, and 2 before the champion declares 'done'."
    ),
    'prompt': (
        "The training loop should print 0, 1, 2 then print 'done', "
        "but the while condition is wrong so the loop never executes. Fix the condition."
    ),
    'broken_code': "count = 0\nwhile count > 0:\n    print(count)\n    count += 1\nprint(\"done\")",
    'hint': "Think about whether the condition is True when count starts at 0 — you may need to flip the comparison.",
    'explanation': (
        "count starts at 0, so count > 0 is immediately False and the loop body never runs. "
        "Changing the condition to count < 3 makes it True at the start and runs the loop for counts 0, 1, and 2."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n1\\n2\\ndone'",
            'message': "Should print 0, 1, 2 then done"
        }
    ]
})

apply_break_fix(L4, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara's boot-cycle sequence is supposed to tick through three initialisation stages before the ship comes online, "
        "but the reactor console skips straight to the 'done' message — no cycles ever run."
    ),
    'story_after': (
        "Correcting the condition to count < 3 triggers all three boot cycles, "
        "logging 0, 1, and 2 before the system prints 'done'."
    ),
    'prompt': (
        "The boot-cycle loop should print 0, 1, 2 then print 'done', "
        "but the while condition prevents the loop from ever starting. Fix the condition."
    ),
    'broken_code': "count = 0\nwhile count > 0:\n    print(count)\n    count += 1\nprint(\"done\")",
    'hint': "Check the direction of the comparison — with count at 0, is count > 0 ever True at the start?",
    'explanation': (
        "Because count is initialised to 0, the condition count > 0 is False immediately and the loop is skipped. "
        "Using count < 3 makes the condition True at launch, running the loop for values 0, 1, and 2."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n1\\n2\\ndone'",
            'message': "Should print 0, 1, 2 then done"
        }
    ]
})

apply_break_fix(L4, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole's evidence-review loop should cycle through three passes before closing the file, "
        "but the review never starts — the program jumps straight to 'done' without examining anything."
    ),
    'story_after': (
        "Changing the condition to count < 3 allows the loop to run three review passes, "
        "printing 0, 1, and 2 before Cole writes 'done' in the case log."
    ),
    'prompt': (
        "Cole's review loop should print 0, 1, 2 then print 'done', "
        "but the while condition is wrong so the loop never runs. Fix the condition."
    ),
    'broken_code': "count = 0\nwhile count > 0:\n    print(count)\n    count += 1\nprint(\"done\")",
    'hint': "count starts at 0 — evaluate whether count > 0 is True or False at that point.",
    'explanation': (
        "count > 0 evaluates to False when count is 0, so the loop body is skipped entirely. "
        "The fix is to use count < 3, which is True for 0, 1, and 2 before becoming False at 3."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '0\\n1\\n2\\ndone'",
            'message': "Should print 0, 1, 2 then done"
        }
    ]
})


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 5 — break and continue
# Bug: `continue` is used where `break` is needed.
# With `continue`: skips gem, prints rock and dirt.
# With `break`: stops at gem, prints only rock.
# ─────────────────────────────────────────────────────────────────────────────
L5 = BASE + r"\unit_4\lesson_5.yaml"

apply_break_fix(L5, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara's gem-finder is enchanted to stop the moment it touches a gem and keep everything before it, "
        "but the spell skips right past the gem and keeps printing — 'rock' and 'dirt' both appear in the output."
    ),
    'story_after': (
        "Replacing continue with break makes the loop halt the instant it finds the gem, so only 'rock' is printed."
    ),
    'prompt': (
        "The loop should print every item before the gem and then stop when it finds 'gem'. "
        "Right now it skips 'gem' with continue and keeps going. Replace continue with break."
    ),
    'broken_code': 'items = ["rock", "gem", "dirt"]\nfor item in items:\n    if item == "gem":\n        continue\n    print(item)',
    'hint': "continue skips to the next iteration; to stop the whole loop you need the other keyword.",
    'explanation': (
        "continue skips only the current iteration, so 'dirt' still gets printed after 'gem' is skipped. "
        "break exits the loop immediately when 'gem' is found, leaving 'rock' as the only printed value."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'rock'",
            'message': "Should print only 'rock' — the loop must stop when it hits 'gem'"
        }
    ]
})

apply_break_fix(L5, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara's emergency-stop protocol is supposed to halt the scan the moment the target reading is detected, "
        "but the scanner skips past it with continue and keeps logging — the halt never happens."
    ),
    'story_after': (
        "Swapping continue for break triggers an immediate halt when 'gem' is detected, leaving only 'rock' in the log."
    ),
    'prompt': (
        "The scan loop should log everything before 'gem' and then stop. "
        "It currently uses continue, which skips 'gem' but keeps scanning. Replace continue with break."
    ),
    'broken_code': 'items = ["rock", "gem", "dirt"]\nfor item in items:\n    if item == "gem":\n        continue\n    print(item)',
    'hint': "You need the keyword that exits the loop entirely, not the one that skips a single iteration.",
    'explanation': (
        "continue causes the loop to move on to 'dirt' after skipping 'gem', so both 'rock' and 'dirt' are printed. "
        "Using break instead stops the loop at 'gem', so only 'rock' is logged."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'rock'",
            'message': "Should print only 'rock' — the scan must halt when 'gem' is reached"
        }
    ]
})

apply_break_fix(L5, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole's search is meant to stop the moment it hits the key clue — everything before it is noted and then the case closes, "
        "but the loop skips the clue with continue and logs 'dirt' as well, contaminating the findings."
    ),
    'story_after': (
        "Using break instead of continue stops the search at the key clue, so only 'rock' appears in Cole's notes."
    ),
    'prompt': (
        "Cole's loop should print items before 'gem' and stop when it finds 'gem'. "
        "It currently uses continue, which skips 'gem' but keeps going. Replace continue with break."
    ),
    'broken_code': 'items = ["rock", "gem", "dirt"]\nfor item in items:\n    if item == "gem":\n        continue\n    print(item)',
    'hint': "One keyword skips the rest of this iteration; the other ends the entire loop — pick the one that ends it.",
    'explanation': (
        "With continue, the loop skips 'gem' but proceeds to print 'dirt', giving two lines of output. "
        "Replacing continue with break exits the loop when 'gem' is found, so only 'rock' is printed."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'rock'",
            'message': "Should print only 'rock' — the loop must stop at 'gem'"
        }
    ]
})


print("\nAll Unit 4 break-and-fix exercises applied.")
