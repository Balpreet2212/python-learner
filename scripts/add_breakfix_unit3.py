import yaml

BASE = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units"

def apply_break_fix(path, world, exercise):
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    data['worlds'][world]['exercises'].append(exercise)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ---------------------------------------------------------------------------
# Lesson 1 — if Statements: missing colon at end of if line
# ---------------------------------------------------------------------------
L1 = BASE + r"\unit_3\lesson_1.yaml"

apply_break_fix(L1, "fantasy", {
    "type": "break_fix",
    "story_before": "Elara's spell detector is almost ready, but the enchantment refuses to activate. She realises the incantation line is missing the colon that seals the condition.",
    "story_after": "With the colon restored, the detector flares to life and correctly reports the creature's vitality.",
    "prompt": "The code should print 'alive' when hp is greater than 0. Fix the syntax error on the if line so the spell can compile.",
    "broken_code": "hp = 10\nif hp > 0\n    print(\"alive\")",
    "hint": "Check the end of the if line — Python needs a specific punctuation mark there.",
    "explanation": "The if statement was missing its colon. Python requires a colon at the end of every if line: `if hp > 0:`.",
    "tests": [
        {"code": "assert _stdout.strip() == 'alive'", "message": "Should print 'alive' when hp is 10"}
    ]
})

apply_break_fix(L1, "scifi", {
    "type": "break_fix",
    "story_before": "Yara's hull-status diagnostic script refuses to run, throwing a compile error before a single sensor reading appears. She traces the fault to the condition line.",
    "story_after": "After adding the missing colon, the diagnostic runs cleanly and reports the hull is intact.",
    "prompt": "The code should print 'alive' when hp is greater than 0. Fix the syntax error on the if line so the diagnostic can execute.",
    "broken_code": "hp = 10\nif hp > 0\n    print(\"alive\")",
    "hint": "Check the end of the if line — Python needs a specific punctuation mark there.",
    "explanation": "The if statement was missing its colon. Python requires a colon at the end of every if line: `if hp > 0:`.",
    "tests": [
        {"code": "assert _stdout.strip() == 'alive'", "message": "Should print 'alive' when hp is 10"}
    ]
})

apply_break_fix(L1, "mystery", {
    "type": "break_fix",
    "story_before": "Detective Cole's witness-filter script crashes before it can process a single name, leaving the case board empty. He spots a syntax error right on the condition line.",
    "story_after": "With the colon in place, the script runs and correctly flags the witness as present.",
    "prompt": "The code should print 'alive' when hp is greater than 0. Fix the syntax error on the if line so the filter can run.",
    "broken_code": "hp = 10\nif hp > 0\n    print(\"alive\")",
    "hint": "Check the end of the if line — Python needs a specific punctuation mark there.",
    "explanation": "The if statement was missing its colon. Python requires a colon at the end of every if line: `if hp > 0:`.",
    "tests": [
        {"code": "assert _stdout.strip() == 'alive'", "message": "Should print 'alive' when hp is 10"}
    ]
})


# ---------------------------------------------------------------------------
# Lesson 2 — if / else: messages are swapped in the branches
# ---------------------------------------------------------------------------
L2 = BASE + r"\unit_3\lesson_2.yaml"

apply_break_fix(L2, "fantasy", {
    "type": "break_fix",
    "story_before": "Elara's path-chooser spell is supposed to guide travellers who score 50 or higher down the safe road, but adventurers are being sent the wrong way entirely. The messages in the two branches have been swapped.",
    "story_after": "Once the messages are corrected, the spell sends high-scorers down the right path and the forest is safe again.",
    "prompt": "The code should print 'Pass' when score is 75 (>= 50) and 'Fail' otherwise. Swap the print strings so each branch shows the correct message.",
    "broken_code": "score = 75\nif score >= 50:\n    print(\"Fail\")\nelse:\n    print(\"Pass\")",
    "hint": "Look at what each branch prints — are 'Pass' and 'Fail' in the right branches?",
    "explanation": "The print strings were swapped. When score >= 50 the code should print 'Pass', and the else branch should print 'Fail'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Pass'", "message": "Should print 'Pass' when score is 75"}
    ]
})

apply_break_fix(L2, "scifi", {
    "type": "break_fix",
    "story_before": "Yara's launch-readiness checker is displaying the wrong status: a perfectly safe score of 75 is triggering a 'Fail' alarm while an actual failure would show 'Pass'. The branch messages are reversed.",
    "story_after": "With the messages corrected, the launch checker gives the crew accurate go/no-go readings.",
    "prompt": "The code should print 'Pass' when score is 75 (>= 50) and 'Fail' otherwise. Swap the print strings so each branch shows the correct message.",
    "broken_code": "score = 75\nif score >= 50:\n    print(\"Fail\")\nelse:\n    print(\"Pass\")",
    "hint": "Look at what each branch prints — are 'Pass' and 'Fail' in the right branches?",
    "explanation": "The print strings were swapped. When score >= 50 the code should print 'Pass', and the else branch should print 'Fail'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Pass'", "message": "Should print 'Pass' when score is 75"}
    ]
})

apply_break_fix(L2, "mystery", {
    "type": "break_fix",
    "story_before": "Detective Cole's verdict printer is embarrassing the precinct — a suspect with plenty of evidence against them is being printed as 'Pass' while the innocent are labelled 'Fail'. Someone swapped the branch messages.",
    "story_after": "After fixing the messages, the verdict printer correctly labels each outcome and Cole can proceed with confidence.",
    "prompt": "The code should print 'Pass' when score is 75 (>= 50) and 'Fail' otherwise. Swap the print strings so each branch shows the correct message.",
    "broken_code": "score = 75\nif score >= 50:\n    print(\"Fail\")\nelse:\n    print(\"Pass\")",
    "hint": "Look at what each branch prints — are 'Pass' and 'Fail' in the right branches?",
    "explanation": "The print strings were swapped. When score >= 50 the code should print 'Pass', and the else branch should print 'Fail'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Pass'", "message": "Should print 'Pass' when score is 75"}
    ]
})


# ---------------------------------------------------------------------------
# Lesson 3 — elif Chains: = instead of == in elif condition
# ---------------------------------------------------------------------------
L3 = BASE + r"\unit_3\lesson_3.yaml"

apply_break_fix(L3, "fantasy", {
    "type": "break_fix",
    "story_before": "Elara's rank-display spell crashes the moment it tries to evaluate the second crystal tier. She discovers a faulty elif that uses a single equals sign instead of the comparison operator.",
    "story_after": "With the comparison corrected, the crystal glows Silver for rank 2 just as the ancient texts describe.",
    "prompt": "The code should print 'Silver' when rank is 2. Fix the elif condition so it compares rank to 2 instead of assigning it.",
    "broken_code": "rank = 2\nif rank == 1:\n    print(\"Bronze\")\nelif rank = 2:\n    print(\"Silver\")\nelse:\n    print(\"Gold\")",
    "hint": "Check the elif line — is it using the right operator to compare rank to 2?",
    "explanation": "The elif used `=` (assignment) instead of `==` (equality check). The fix is `elif rank == 2:` so Python compares rather than assigns.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Silver'", "message": "Should print 'Silver' when rank is 2"}
    ]
})

apply_break_fix(L3, "scifi", {
    "type": "break_fix",
    "story_before": "Yara's crew-rank display script throws a SyntaxError when the Helix tries to categorise a rank-2 engineer. The second branch of the rating system is broken by a mistyped operator.",
    "story_after": "Once the operator is corrected, the display correctly shows 'Silver' for rank-2 crew members.",
    "prompt": "The code should print 'Silver' when rank is 2. Fix the elif condition so it compares rank to 2 instead of assigning it.",
    "broken_code": "rank = 2\nif rank == 1:\n    print(\"Bronze\")\nelif rank = 2:\n    print(\"Silver\")\nelse:\n    print(\"Gold\")",
    "hint": "Check the elif line — is it using the right operator to compare rank to 2?",
    "explanation": "The elif used `=` (assignment) instead of `==` (equality check). The fix is `elif rank == 2:` so Python compares rather than assigns.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Silver'", "message": "Should print 'Silver' when rank is 2"}
    ]
})

apply_break_fix(L3, "mystery", {
    "type": "break_fix",
    "story_before": "Detective Cole's suspect-tier classifier crashes on the second tier, leaving mid-level suspects unclassified. A single character error in the elif condition is to blame.",
    "story_after": "After fixing the comparison operator, the classifier correctly identifies rank-2 suspects as 'Silver' tier.",
    "prompt": "The code should print 'Silver' when rank is 2. Fix the elif condition so it compares rank to 2 instead of assigning it.",
    "broken_code": "rank = 2\nif rank == 1:\n    print(\"Bronze\")\nelif rank = 2:\n    print(\"Silver\")\nelse:\n    print(\"Gold\")",
    "hint": "Check the elif line — is it using the right operator to compare rank to 2?",
    "explanation": "The elif used `=` (assignment) instead of `==` (equality check). The fix is `elif rank == 2:` so Python compares rather than assigns.",
    "tests": [
        {"code": "assert _stdout.strip() == 'Silver'", "message": "Should print 'Silver' when rank is 2"}
    ]
})


# ---------------------------------------------------------------------------
# Lesson 4 — Conditions with and / or: or instead of and
# ---------------------------------------------------------------------------
L4 = BASE + r"\unit_3\lesson_4.yaml"

apply_break_fix(L4, "fantasy", {
    "type": "break_fix",
    "story_before": "Elara's vault requires BOTH a key AND the password to open, but her guardian spell is letting in anyone who has only one of the two. The spell is using OR instead of AND.",
    "story_after": "With the logical operator corrected, the vault stays sealed unless the visitor possesses both the key and the password.",
    "prompt": "The code should print 'denied' when has_key is True but knows_password is False. Fix the condition so BOTH requirements must be met.",
    "broken_code": "has_key = True\nknows_password = False\nif has_key or knows_password:\n    print(\"enter\")\nelse:\n    print(\"denied\")",
    "hint": "Check the logical operator in the if condition — should it be 'and' or 'or'?",
    "explanation": "Using `or` allows entry when either condition is true. Changing it to `and` ensures both has_key and knows_password must be True before entry is granted.",
    "tests": [
        {"code": "assert _stdout.strip() == 'denied'", "message": "Should print 'denied' when only one condition is met"}
    ]
})

apply_break_fix(L4, "scifi", {
    "type": "break_fix",
    "story_before": "Yara's airlock safety protocol demands BOTH a keycard AND an authorisation code, but the script is cycling open for anyone who swipes a keycard alone. The logical operator is wrong.",
    "story_after": "After changing the operator, the airlock correctly stays sealed until both credentials are presented.",
    "prompt": "The code should print 'denied' when has_key is True but knows_password is False. Fix the condition so BOTH requirements must be met.",
    "broken_code": "has_key = True\nknows_password = False\nif has_key or knows_password:\n    print(\"enter\")\nelse:\n    print(\"denied\")",
    "hint": "Check the logical operator in the if condition — should it be 'and' or 'or'?",
    "explanation": "Using `or` allows entry when either condition is true. Changing it to `and` ensures both has_key and knows_password must be True before entry is granted.",
    "tests": [
        {"code": "assert _stdout.strip() == 'denied'", "message": "Should print 'denied' when only one condition is met"}
    ]
})

apply_break_fix(L4, "mystery", {
    "type": "break_fix",
    "story_before": "Cole's restricted archive should only open for someone with BOTH a badge AND a PIN, but the access script is granting entry to badge holders who don't know the PIN. The gate logic is using OR.",
    "story_after": "With the operator fixed, the archive correctly turns away anyone who cannot provide both credentials.",
    "prompt": "The code should print 'denied' when has_key is True but knows_password is False. Fix the condition so BOTH requirements must be met.",
    "broken_code": "has_key = True\nknows_password = False\nif has_key or knows_password:\n    print(\"enter\")\nelse:\n    print(\"denied\")",
    "hint": "Check the logical operator in the if condition — should it be 'and' or 'or'?",
    "explanation": "Using `or` allows entry when either condition is true. Changing it to `and` ensures both has_key and knows_password must be True before entry is granted.",
    "tests": [
        {"code": "assert _stdout.strip() == 'denied'", "message": "Should print 'denied' when only one condition is met"}
    ]
})


# ---------------------------------------------------------------------------
# Lesson 5 — Nested if: inner condition uses < instead of >
# ---------------------------------------------------------------------------
L5 = BASE + r"\unit_3\lesson_5.yaml"

apply_break_fix(L5, "fantasy", {
    "type": "break_fix",
    "story_before": "Elara's battle-strategy spell is supposed to order an attack when a warrior is armed AND has strength above 5, but it keeps retreating even from powerful fighters. The inner strength check has the comparison backwards.",
    "story_after": "Once the comparison is corrected, the spell correctly commands an attack for armed warriors whose strength exceeds 5.",
    "prompt": "The code should print 'attack' when armed is True and strength is 8. Fix the inner if condition so it attacks when strength is greater than 5.",
    "broken_code": "armed = True\nstrength = 8\nif armed:\n    if strength < 5:\n        print(\"attack\")\n    else:\n        print(\"retreat\")",
    "hint": "Check the inner if condition — is the comparison operator pointing in the right direction?",
    "explanation": "The inner condition `strength < 5` was backwards. With strength = 8, this is False so the code printed 'retreat'. Changing it to `strength > 5` makes the condition True and prints 'attack'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'attack'", "message": "Should print 'attack' when armed and strength is 8"}
    ]
})

apply_break_fix(L5, "scifi", {
    "type": "break_fix",
    "story_before": "Yara's nested weapons-authorisation script should fire the cannons when the ship is armed AND power exceeds 5, but the Helix keeps standing down even at full power. The power threshold comparison is inverted.",
    "story_after": "After flipping the comparison, the authorisation system correctly clears weapons fire when power is high enough.",
    "prompt": "The code should print 'attack' when armed is True and strength is 8. Fix the inner if condition so it attacks when strength is greater than 5.",
    "broken_code": "armed = True\nstrength = 8\nif armed:\n    if strength < 5:\n        print(\"attack\")\n    else:\n        print(\"retreat\")",
    "hint": "Check the inner if condition — is the comparison operator pointing in the right direction?",
    "explanation": "The inner condition `strength < 5` was backwards. With strength = 8, this is False so the code printed 'retreat'. Changing it to `strength > 5` makes the condition True and prints 'attack'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'attack'", "message": "Should print 'attack' when armed and strength is 8"}
    ]
})

apply_break_fix(L5, "mystery", {
    "type": "break_fix",
    "story_before": "Cole's interrogation-decision script should press the suspect hard when they are present AND their resistance score is above 5, but a resistance of 8 is somehow triggering a retreat. The inner comparison is backwards.",
    "story_after": "With the corrected comparison, the script correctly decides to press the interrogation when resistance is high.",
    "prompt": "The code should print 'attack' when armed is True and strength is 8. Fix the inner if condition so it attacks when strength is greater than 5.",
    "broken_code": "armed = True\nstrength = 8\nif armed:\n    if strength < 5:\n        print(\"attack\")\n    else:\n        print(\"retreat\")",
    "hint": "Check the inner if condition — is the comparison operator pointing in the right direction?",
    "explanation": "The inner condition `strength < 5` was backwards. With strength = 8, this is False so the code printed 'retreat'. Changing it to `strength > 5` makes the condition True and prints 'attack'.",
    "tests": [
        {"code": "assert _stdout.strip() == 'attack'", "message": "Should print 'attack' when armed and strength is 8"}
    ]
})


print("\nAll Unit 3 break-and-fix exercises applied.")
