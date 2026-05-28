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
# LESSON 1 — Classes and Attributes
# Bug: describe() uses bare `name` instead of `self.name` → NameError
# Fixed output: 'Creature: Dragon'
# ---------------------------------------------------------------------------
L1 = BASE + r"\unit_7\lesson_1.yaml"

BROKEN_L1 = (
    "class Creature:\n"
    "    def __init__(self, name):\n"
    "        self.name = name\n"
    "    def describe(self):\n"
    "        print(\"Creature: \" + name)\n"
    "\n"
    "c = Creature(\"Dragon\")\n"
    "c.describe()"
)

apply_break_fix(L1, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara finishes writing her Creature class and proudly calls describe() on her Dragon — "
        "but instead of the creature's name, a NameError erupts from the workshop cauldron."
    ),
    'story_after': "Elara adds self. before name in describe(), and the Dragon announces itself correctly.",
    'prompt': (
        "Elara's Creature class stores the name correctly in __init__, but describe() crashes with a NameError. "
        "Find the missing prefix and fix it so the creature can introduce itself."
    ),
    'broken_code': BROKEN_L1,
    'hint': "Inside a method, instance attributes must be accessed through self, not as bare variable names.",
    'explanation': (
        "The describe() method uses the bare name name, which does not exist as a local variable. "
        "Changing it to self.name tells Python to look up the attribute stored on the instance."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Creature: Dragon'",
            'message': "describe() should print 'Creature: Dragon'",
        }
    ],
})

apply_break_fix(L1, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara writes a SystemModule class for the Helix's diagnostics panel, but calling describe() "
        "triggers a NameError that shuts down the entire readout."
    ),
    'story_after': "Yara prefixes name with self. and the system name prints cleanly to the diagnostic feed.",
    'prompt': (
        "Yara's SystemModule stores the name in __init__, but describe() fails with a NameError. "
        "Fix the attribute reference so the module can report its own name."
    ),
    'broken_code': BROKEN_L1,
    'hint': "Inside a method, instance attributes must be accessed through self, not as bare variable names.",
    'explanation': (
        "The describe() method refers to name as a bare variable, but name is stored as self.name. "
        "Replacing name with self.name gives Python the correct reference to the instance attribute."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Creature: Dragon'",
            'message': "describe() should print 'Creature: Dragon'",
        }
    ],
})

apply_break_fix(L1, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole programs a Suspect profile class so each person of interest can state their own name, "
        "but the first test call throws a NameError straight back at him."
    ),
    'story_after': "Cole fixes the attribute reference with self.name and the suspect profile prints without error.",
    'prompt': (
        "Cole's Creature class sets up name in __init__ correctly, but describe() crashes. "
        "Spot where self. is missing and add it so the profile can announce itself."
    ),
    'broken_code': BROKEN_L1,
    'hint': "Inside a method, instance attributes must be accessed through self, not as bare variable names.",
    'explanation': (
        "describe() writes name instead of self.name. "
        "Because name is not a local variable inside the method, Python raises a NameError. "
        "Prefixing it with self. resolves the lookup to the instance attribute set in __init__."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Creature: Dragon'",
            'message': "describe() should print 'Creature: Dragon'",
        }
    ],
})

# ---------------------------------------------------------------------------
# LESSON 2 — Methods
# Bug: cast() defined without `self` as first parameter → TypeError on call
# Fixed output: 'Casting!'
# ---------------------------------------------------------------------------
L2 = BASE + r"\unit_7\lesson_2.yaml"

BROKEN_L2 = (
    "class Spell:\n"
    "    def __init__(self, name):\n"
    "        self.name = name\n"
    "    def cast():\n"
    "        print(\"Casting!\")\n"
    "\n"
    "s = Spell(\"Fireball\")\n"
    "s.cast()"
)

apply_break_fix(L2, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara adds a cast() method to her Spell class, but the moment she tries to use it on a Fireball instance "
        "Python throws a TypeError and the spell fizzles."
    ),
    'story_after': "Elara adds self as the first parameter to cast() and the Fireball blazes into life.",
    'prompt': (
        "Elara's Spell class has a cast() method that crashes with a TypeError when called on an instance. "
        "Find the missing parameter and fix the method signature."
    ),
    'broken_code': BROKEN_L2,
    'hint': "Every instance method must have self as its first parameter so Python can pass the object automatically.",
    'explanation': (
        "When you call s.cast(), Python automatically passes the instance as the first argument. "
        "Without self in the definition, Python sees too many arguments and raises a TypeError. "
        "Adding self as the first parameter fixes the signature."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Casting!'",
            'message': "cast() should print 'Casting!'",
        }
    ],
})

apply_break_fix(L2, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara writes a diagnostic() method for the Helix's Spell module, but invoking it on a live instance "
        "immediately raises a TypeError and halts the diagnostic run."
    ),
    'story_after': "Yara inserts self into the method signature and the diagnostic completes successfully.",
    'prompt': (
        "Yara's Spell class defines cast() without the required first parameter and crashes on call. "
        "Fix the method definition so it can be called on an instance."
    ),
    'broken_code': BROKEN_L2,
    'hint': "Every instance method must have self as its first parameter so Python can pass the object automatically.",
    'explanation': (
        "Python passes the calling instance as the first argument automatically. "
        "cast() declares no parameters, so Python sees one unexpected argument and raises a TypeError. "
        "Declaring def cast(self): gives Python the slot it needs."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Casting!'",
            'message': "cast() should print 'Casting!'",
        }
    ],
})

apply_break_fix(L2, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole builds an investigate() method on his Spell class so suspects can be questioned through the object, "
        "but calling it on an instance raises a TypeError that closes the interrogation room."
    ),
    'story_after': "Cole adds self to the method definition and the interrogation method runs without complaint.",
    'prompt': (
        "Cole's Spell class has a cast() method that fails with a TypeError the moment it is called on an instance. "
        "Add the missing parameter to the method signature to fix it."
    ),
    'broken_code': BROKEN_L2,
    'hint': "Every instance method must have self as its first parameter so Python can pass the object automatically.",
    'explanation': (
        "Calling s.cast() makes Python inject the instance as the first argument. "
        "Because cast() has no parameters, Python sees an unexpected extra argument and raises a TypeError. "
        "Writing def cast(self): provides the required slot."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Casting!'",
            'message': "cast() should print 'Casting!'",
        }
    ],
})

# ---------------------------------------------------------------------------
# LESSON 3 — Methods That Change State
# Bug: level_up() assigns to local `level` instead of `self.level` → attribute unchanged
# Fixed output: '4'
# ---------------------------------------------------------------------------
L3 = BASE + r"\unit_7\lesson_3.yaml"

BROKEN_L3 = (
    "class Hero:\n"
    "    def __init__(self, level):\n"
    "        self.level = level\n"
    "    def level_up(self):\n"
    "        level = self.level + 1\n"
    "\n"
    "h = Hero(3)\n"
    "h.level_up()\n"
    "print(h.level)"
)

apply_break_fix(L3, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara writes a level_up() spell on her Hero class to advance its power, "
        "but after calling it the hero's level refuses to budge — it still reads 3."
    ),
    'story_after': "Elara assigns the result to self.level instead of a bare local variable and the hero advances to level 4.",
    'prompt': (
        "Elara's level_up() method calculates the new level but the hero's attribute never changes. "
        "Find where the result is being lost and fix it so the attribute is actually updated."
    ),
    'broken_code': BROKEN_L3,
    'hint': "Assigning to a bare variable inside a method creates a local variable — use self.attribute to update the instance.",
    'explanation': (
        "level = self.level + 1 stores the new value in a temporary local variable that disappears when the method returns. "
        "Writing self.level = self.level + 1 saves the updated value back onto the instance."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '4'",
            'message': "h.level should be 4 after calling level_up()",
        }
    ],
})

apply_break_fix(L3, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara programs an upgrade() method to raise a module's operational level on the Helix, "
        "but the console still shows level 3 after the upgrade completes."
    ),
    'story_after': "Yara routes the result to self.level and the module's level ticks up to 4 as expected.",
    'prompt': (
        "Yara's Hero module has a level_up() method that computes the new level but never saves it. "
        "Fix the assignment so the updated level persists on the instance."
    ),
    'broken_code': BROKEN_L3,
    'hint': "Assigning to a bare variable inside a method creates a local variable — use self.attribute to update the instance.",
    'explanation': (
        "level = self.level + 1 creates a local variable inside the method; when the method exits, that value is discarded. "
        "Replacing it with self.level = self.level + 1 writes the new value directly onto the object."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '4'",
            'message': "h.level should be 4 after calling level_up()",
        }
    ],
})

apply_break_fix(L3, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole writes a rank_up() method to promote a suspect's threat ranking in the case file, "
        "but after calling it the rank still shows 3 — the update vanished without a trace."
    ),
    'story_after': "Cole writes the result to self.level and the ranking correctly advances to 4.",
    'prompt': (
        "Cole's Hero class has a level_up() method that silently discards the new level. "
        "Fix the single assignment line so the change is stored on the instance."
    ),
    'broken_code': BROKEN_L3,
    'hint': "Assigning to a bare variable inside a method creates a local variable — use self.attribute to update the instance.",
    'explanation': (
        "The line level = self.level + 1 stores the result in a local variable that Python throws away at the end of the method. "
        "Using self.level = self.level + 1 persists the value on the instance so it is visible after the call."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == '4'",
            'message': "h.level should be 4 after calling level_up()",
        }
    ],
})

# ---------------------------------------------------------------------------
# LESSON 4 — Multiple Instances
# Bug: second print uses a.name instead of b.name → first name printed twice
# Fixed output: 'Luna\nRex'
# ---------------------------------------------------------------------------
L4 = BASE + r"\unit_7\lesson_4.yaml"

BROKEN_L4 = (
    "class Pet:\n"
    "    def __init__(self, name):\n"
    "        self.name = name\n"
    "\n"
    "a = Pet(\"Luna\")\n"
    "b = Pet(\"Rex\")\n"
    "print(a.name)\n"
    "print(a.name)"
)

apply_break_fix(L4, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara summons two familiars — Luna and Rex — and tries to announce both of them, "
        "but the enchantment recites Luna's name twice and Rex is never introduced."
    ),
    'story_after': "Elara changes the second print to b.name and both familiars are announced in order.",
    'prompt': (
        "Elara's code creates two Pet familiars but prints the first one's name twice. "
        "Fix the second print statement so each familiar is announced correctly."
    ),
    'broken_code': BROKEN_L4,
    'hint': "Check which instance variable is used in each print call — the second print should reference the second instance.",
    'explanation': (
        "Both print statements use a.name, so Luna appears twice and Rex is never printed. "
        "Changing the second print to b.name points it at the Rex instance and produces the correct output."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Luna\\nRex'",
            'message': "Should print 'Luna' then 'Rex' on separate lines",
        }
    ],
})

apply_break_fix(L4, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara deploys two drone units — Luna and Rex — and attempts to log both unit IDs to the mission console, "
        "but the log shows Luna's identifier for both entries."
    ),
    'story_after': "Yara corrects the second log line to b.name and both drone IDs appear on the manifest.",
    'prompt': (
        "Yara's code registers two Pet drones but reads the first unit's name for both print calls. "
        "Fix the second print so each drone's ID is logged correctly."
    ),
    'broken_code': BROKEN_L4,
    'hint': "Check which instance variable is used in each print call — the second print should reference the second instance.",
    'explanation': (
        "The second print(a.name) reads from the first instance again instead of the second. "
        "Replacing a.name with b.name in the second print outputs Rex as intended."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Luna\\nRex'",
            'message': "Should print 'Luna' then 'Rex' on separate lines",
        }
    ],
})

apply_break_fix(L4, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole logs two witnesses — Luna and Rex — into the case system and asks it to print both names, "
        "but the report lists Luna twice and Rex's entry is completely missing."
    ),
    'story_after': "Cole updates the second print to b.name and the witness log correctly lists both names.",
    'prompt': (
        "Cole's code creates two Pet witnesses but the second print statement names the wrong instance. "
        "Correct it so the report prints each witness's name once."
    ),
    'broken_code': BROKEN_L4,
    'hint': "Check which instance variable is used in each print call — the second print should reference the second instance.",
    'explanation': (
        "print(a.name) is called twice, so 'Luna' appears twice and 'Rex' is never printed. "
        "Changing the second call to print(b.name) directs it to the Rex instance and fixes the report."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Luna\\nRex'",
            'message': "Should print 'Luna' then 'Rex' on separate lines",
        }
    ],
})

# ---------------------------------------------------------------------------
# LESSON 5 — Inheritance
# Bug: describe() accesses self.bread (typo) instead of self.breed → AttributeError
# Fixed output: 'Rex is a Labrador'
# ---------------------------------------------------------------------------
L5 = BASE + r"\unit_7\lesson_5.yaml"

BROKEN_L5 = (
    "class Animal:\n"
    "    def __init__(self, name):\n"
    "        self.name = name\n"
    "\n"
    "class Dog(Animal):\n"
    "    def __init__(self, name, breed):\n"
    "        super().__init__(name)\n"
    "        self.breed = breed\n"
    "    def describe(self):\n"
    "        print(self.name + \" is a \" + self.bread)\n"
    "\n"
    "d = Dog(\"Rex\", \"Labrador\")\n"
    "d.describe()"
)

apply_break_fix(L5, "fantasy", {
    'type': 'break_fix',
    'story_before': (
        "Elara crafts a Dog spell bloodline that inherits from Animal, but when she calls describe() "
        "on her Labrador familiar an AttributeError erupts — the lineage cannot read its own kind."
    ),
    'story_after': "Elara corrects the typo to self.breed and the familiar proudly announces 'Rex is a Labrador'.",
    'prompt': (
        "Elara's Dog subclass stores the breed correctly but describe() crashes with an AttributeError. "
        "Find the misspelled attribute name and fix it."
    ),
    'broken_code': BROKEN_L5,
    'hint': "Read the attribute name used in describe() very carefully and compare it to the name set in __init__.",
    'explanation': (
        "self.bread is a typo — the attribute is stored as self.breed in __init__. "
        "Correcting the spelling to self.breed in describe() resolves the AttributeError."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Rex is a Labrador'",
            'message': "describe() should print 'Rex is a Labrador'",
        }
    ],
})

apply_break_fix(L5, "scifi", {
    'type': 'break_fix',
    'story_before': (
        "Yara builds a Dog submodule that inherits from Animal and adds a specialisation type, "
        "but calling describe() on the Labrador unit crashes the subsystem with an AttributeError."
    ),
    'story_after': "Yara corrects self.bread to self.breed and the unit's identification string prints correctly.",
    'prompt': (
        "Yara's Dog class sets self.breed in __init__ but describe() refers to a differently spelled attribute. "
        "Fix the typo so the method can access the correct attribute."
    ),
    'broken_code': BROKEN_L5,
    'hint': "Read the attribute name used in describe() very carefully and compare it to the name set in __init__.",
    'explanation': (
        "The method accesses self.bread, but the attribute was stored under self.breed. "
        "Python raises an AttributeError because self.bread does not exist. Fixing the spelling resolves it."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Rex is a Labrador'",
            'message': "describe() should print 'Rex is a Labrador'",
        }
    ],
})

apply_break_fix(L5, "mystery", {
    'type': 'break_fix',
    'story_before': (
        "Cole builds a Dog subclass to extend the Animal profile with a breed field, "
        "but describe() throws an AttributeError when Cole tries to print the suspect's background."
    ),
    'story_after': "Cole spots the typo, fixes self.bread to self.breed, and the profile reads 'Rex is a Labrador'.",
    'prompt': (
        "Cole's Dog class inherits from Animal and stores breed in __init__, but describe() cannot find the attribute. "
        "Spot the misspelling and correct it."
    ),
    'broken_code': BROKEN_L5,
    'hint': "Read the attribute name used in describe() very carefully and compare it to the name set in __init__.",
    'explanation': (
        "self.bread in describe() does not match self.breed set in __init__. "
        "The one-letter typo ('a' instead of 'e') causes an AttributeError. Correcting the spelling fixes the access."
    ),
    'tests': [
        {
            'code': "assert _stdout.strip() == 'Rex is a Labrador'",
            'message': "describe() should print 'Rex is a Labrador'",
        }
    ],
})

print("\nAll Unit 7 break-and-fix exercises applied.")
