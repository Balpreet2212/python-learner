import yaml
import sys
from pathlib import Path

UNIT_DIR = Path(__file__).parent.parent / "content" / "units" / "unit_7"


def apply_beats(path, world, beats):
    """beats: list of (story_before, story_after) strings, indexed by exercise position"""
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    exercises = data["worlds"][world]["exercises"]
    for i, (before, after) in enumerate(beats):
        if i < len(exercises):
            exercises[i]["story_before"] = before
            exercises[i]["story_after"] = after
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ---------------------------------------------------------------------------
# LESSON 1 — Classes and Attributes
# ---------------------------------------------------------------------------
L1 = UNIT_DIR / "lesson_1.yaml"

apply_beats(L1, "fantasy", [
    # 0 concept
    (
        "Scholar Ash has catalogued dozens of beasts, but writing out every creature by hand wastes precious parchment — a single blueprint is needed.",
        "The Creature blueprint is drawn: name and threat stored as one arcane record, ready to be copied for any beast Ash encounters.",
    ),
    # 1 mcq
    (
        "Ash spots a fire-aligned Spell in the grimoire and needs to read its element attribute.",
        "The element leaps off the page — Ash now knows how to read any single attribute from a class instance.",
    ),
    # 2 fill_blank
    (
        "The bestiary template is nearly complete, but the threat_level is not yet stored on the creature object.",
        "With self in place, the creature's danger rating is permanently bound to each individual beast record.",
    ),
    # 3 mcq
    (
        "An Orb's power is etched into the blueprint — Ash must verify what happens when that value is doubled.",
        "The doubled power rolls off the page correctly; Ash grows confident reading computed expressions from attributes.",
    ),
    # 4 arrange
    (
        "Ash wants a Tome class to catalogue magical books, complete with title and author — the blocks need assembling.",
        "The Tome blueprint snaps together perfectly; Ash can now stamp out as many book records as the library demands.",
    ),
    # 5 mcq
    (
        "A Mage entry stores both name and age — Ash needs to know what the combined string prints.",
        "The string concatenation reveals 'Alice is 30'; Ash sees how multiple attributes can be woven into a single message.",
    ),
    # 6 fill_blank
    (
        "A glowing Lantern hangs in the workshop, but its glow can only be read through the right instance variable.",
        "Reaching through the lantern variable, Ash retrieves the glow value and notes it in the compendium.",
    ),
    # 7 mcq
    (
        "Ash's apprentice asks: why does __init__ exist at all — what magic does it perform?",
        "The answer is clear: __init__ is the summoning ritual that breathes initial state into every new object.",
    ),
    # 8 mcq
    (
        "A Rune blueprint stores its own area in __init__ — Ash must trace what value emerges when the side is 6.",
        "The area 36 is confirmed; Ash now trusts that __init__ can pre-compute and store values, not just copy parameters.",
    ),
    # 9 mini_code
    (
        "Ash needs a Rectangle blueprint to map creature territories — width and height must both be stored and displayed.",
        "The Rectangle class rises from the page; Ash measures the territory and the compendium records both dimensions.",
    ),
    # 10 mini_code
    (
        "Two creatures need separate entries — Ash must build a Student-style class and produce records for both.",
        "Both creature records are written and printed; Ash's bestiary grows one blueprint at a time, ready for Lesson 2.",
    ),
])

apply_beats(L1, "scifi", [
    # 0 concept
    (
        "Engineer Rex has a fleet of ships to register, but typing each vessel's data from scratch wastes critical build time — one reusable blueprint is required.",
        "The Ship class is drafted: name and crew count locked into a schematic that can spawn any vessel in the fleet.",
    ),
    # 1 mcq
    (
        "Rex spots an Engine entry in the manifest and needs to confirm what its fuel_type attribute holds.",
        "The fuel type prints cleanly — Rex confirms that a stored attribute can be retrieved from any instance by name.",
    ),
    # 2 fill_blank
    (
        "The Ship schematic is missing its shield_level binding — Rex must anchor it to self before the vessel is spaceworthy.",
        "The shield_level is now wired to the object; every Ship spawned from this blueprint will carry its own rating.",
    ),
    # 3 mcq
    (
        "A Reactor's output reading is on the schematic — Rex needs to verify what doubling it produces.",
        "Output 14 confirmed on the console; Rex now knows how to derive computed values straight from stored attributes.",
    ),
    # 4 arrange
    (
        "Rex needs a Module class with title and author fields to organise ship documentation — the code blocks await assembly.",
        "The Module blueprint assembles without errors; ship documentation can now be stamped out as individual instances.",
    ),
    # 5 mcq
    (
        "A Pilot record holds both name and age — Rex needs to predict what the combined status string prints.",
        "The status string 'Alice is 30' transmits correctly; Rex sees how to broadcast multi-attribute data in one line.",
    ),
    # 6 fill_blank
    (
        "A Console powers up, but its power reading is locked behind the correct instance variable name.",
        "Accessing through desk, Rex reads the power value and logs it to the ship's diagnostic report.",
    ),
    # 7 mcq
    (
        "A junior engineer asks Rex what __init__ actually does when a new object is created.",
        "Rex explains: __init__ is the bootstrap sequence — it initialises every system the moment a new object is registered.",
    ),
    # 8 mcq
    (
        "A Hull schematic pre-computes its own area in __init__ — Rex needs to trace what prints for side = 6.",
        "Area 36 is correct; Rex files it away — __init__ can pre-calculate and store values, not just record inputs.",
    ),
    # 9 mini_code
    (
        "Rex needs a Rectangle blueprint to define hull panel dimensions — both width and height must be stored and reported.",
        "The Rectangle class is drafted and both dimensions print to the schematic; the hull design is on record.",
    ),
    # 10 mini_code
    (
        "Two crew members need separate entries — Rex must produce a Student-style class and log both to the manifest.",
        "Both crew records transmit to the manifest; Rex has a working blueprint pattern ready to carry into Lesson 2.",
    ),
])

apply_beats(L1, "mystery", [
    # 0 concept
    (
        "Detective Cole has a growing list of suspects but no consistent way to record them — a single profile template will fix that.",
        "The Suspect class is opened: name and motive filed together in one template Cole can replicate for every person of interest.",
    ),
    # 1 mcq
    (
        "A piece of Evidence is logged in the system — Cole needs to confirm what its item attribute actually holds.",
        "The item value reads out cleanly; Cole now knows how to pull any single attribute from a filed profile.",
    ),
    # 2 fill_blank
    (
        "The Suspect template is incomplete — the alibi_strength is not yet bound to the object, leaving the profile open.",
        "With self in place, the alibi rating is locked into every suspect record the moment it is created.",
    ),
    # 3 mcq
    (
        "A Clue's weight is on file — Cole needs to know what doubling it produces for the investigation's scoring.",
        "Weight 14 confirmed; Cole sees how arithmetic on a stored attribute produces a derived value on the spot.",
    ),
    # 4 arrange
    (
        "Cole wants a CaseFile class to organise reports by title and author — the code pieces need to be ordered correctly.",
        "The CaseFile template locks into shape; every new report can now be filed as a clean, separate instance.",
    ),
    # 5 mcq
    (
        "A Detective profile stores name and age — Cole needs to predict how the combined identification string prints.",
        "The string 'Alice is 30' prints as expected; Cole notes how two attributes can be merged into one statement.",
    ),
    # 6 fill_blank
    (
        "A Suspect is on file, but the threat_level can only be read through the correct instance variable.",
        "Reaching through desk, Cole pulls the threat level and adds it to the case dossier.",
    ),
    # 7 mcq
    (
        "A rookie detective asks Cole what __init__ actually does when a Suspect is created.",
        "Cole answers plainly: __init__ is the intake process — it stamps every new profile with its opening data the moment it is filed.",
    ),
    # 8 mcq
    (
        "A Fingerprint record pre-computes its own area in __init__ — Cole must trace what prints for side = 6.",
        "Area 36 confirmed; Cole notes that __init__ can store calculated fields alongside raw inputs.",
    ),
    # 9 mini_code
    (
        "Cole needs a Rectangle profile template to measure crime scene footprints — width and height must be stored and displayed.",
        "The Rectangle class is on file and both measurements print; Cole's scene-mapping toolkit is taking shape.",
    ),
    # 10 mini_code
    (
        "Two suspects need separate profile entries — Cole must produce a Student-style class and print both records.",
        "Both profiles print cleanly to the case file; Cole has a repeatable template ready to carry into Lesson 2.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 2 — Methods
# ---------------------------------------------------------------------------
L2 = UNIT_DIR / "lesson_2.yaml"

apply_beats(L2, "fantasy", [
    # 0 concept
    (
        "Ash's Creature blueprints now hold data, but the bestiary needs behaviours too — methods that can speak for each beast.",
        "The Creature gains is_dangerous and describe methods; Ash can now interrogate any beast through its own built-in actions.",
    ),
    # 1 mcq
    (
        "A Dragon's roar() method is defined — Ash must predict what the dragon announces when called.",
        "The roar returns 'Rex says Woof!' as written; Ash confirms that methods reach into self.name to build their output.",
    ),
    # 2 fill_blank
    (
        "A MagicCircle needs an area() method, but the correct attribute name must be supplied inside the formula.",
        "With self.radius in place, the circle's area computes correctly — the spell diagram is accurately measured.",
    ),
    # 3 mcq
    (
        "A SpellSlot tracker starts empty — Ash must follow value() to see what it returns before any spell is cast.",
        "Zero returns, as expected; Ash sees that a method simply reads back whatever state the object currently holds.",
    ),
    # 4 arrange
    (
        "Ash wants to give a Mage an introduce() method that announces its name — the pieces need arranging.",
        "The introduce method slots into the Mage blueprint; the wizard can now speak its own name without external help.",
    ),
    # 5 mcq
    (
        "An Altar's area() multiplies its two dimensions — Ash must verify the result for width 4, height 5.",
        "Area 20 is returned; Ash sees how a method can take stored attributes and combine them into a useful result.",
    ),
    # 6 fill_blank
    (
        "A FlameGauge measures dragon-fire in Celsius, but Ash needs to complete the formula that converts it to Fahrenheit.",
        "The + operator completes the conversion; 100 degrees Celsius becomes 212 Fahrenheit, and the gauge is calibrated.",
    ),
    # 7 mcq
    (
        "A Rune's is_strong() method checks whether its inscription is long enough — Ash must decide the outcome for 'abc123'.",
        "False is returned — six characters fall short of eight; Ash now knows how methods can enforce thresholds.",
    ),
    # 8 mcq
    (
        "A treasure Chest needs its volume calculated — Ash traces volume() for dimensions 2, 3, 4.",
        "Volume 24 is confirmed; Ash sees that three stored attributes can be multiplied inside a single method call.",
    ),
    # 9 mini_code
    (
        "Ash must map a triangular creature territory — a Triangle class with an area() method is required.",
        "The territory area computes perfectly; Ash's bestiary now includes methods that derive useful measurements.",
    ),
    # 10 mini_code
    (
        "A wizard's gold pouch needs an is_overdrawn() check — Ash must build a BankAccount class with that method.",
        "The pouch reports correctly whether gold is positive or spent; Ash is ready to move on to state-changing methods.",
    ),
])

apply_beats(L2, "scifi", [
    # 0 concept
    (
        "Rex's Ship blueprints store data, but the fleet needs active behaviours — methods that can query and describe each unit.",
        "The Engine gains is_powerful and describe methods; Rex can now run diagnostics on any component through its own interface.",
    ),
    # 1 mcq
    (
        "A Drone's signal() method is defined — Rex must predict what it broadcasts when called.",
        "The signal prints 'Rex says Woof!' as coded; Rex confirms methods compose output from self.name without extra input.",
    ),
    # 2 fill_blank
    (
        "A Thruster's area() method needs the correct attribute name to complete its cross-section calculation.",
        "With self.radius supplied, the thruster's cross-section computes — the engineering schematic is verified.",
    ),
    # 3 mcq
    (
        "A PowerCell tracker starts at zero — Rex must follow value() to confirm what it returns before any charge is added.",
        "Zero returns as expected; Rex notes that a method is just a query — it reports the object's current state.",
    ),
    # 4 arrange
    (
        "Rex needs a Pilot class with a transmit() method that broadcasts the pilot's name — the code needs ordering.",
        "The transmit method is wired into the Pilot blueprint; the crew member can now self-identify on the comms channel.",
    ),
    # 5 mcq
    (
        "A ShieldPanel's area() multiplies width by height — Rex traces the output for dimensions 4 and 5.",
        "Area 20 confirmed on the readout; Rex sees how methods turn raw attribute data into actionable results.",
    ),
    # 6 fill_blank
    (
        "A HeatSensor tracks reactor temperatures in Celsius, but the Fahrenheit conversion formula needs its final operator.",
        "The + closes the formula; 100 Celsius becomes 212 Fahrenheit, and the heat shield is cleared for re-entry.",
    ),
    # 7 mcq
    (
        "An AccessCode's is_strong() check determines whether 'abc123' is long enough to secure the airlock.",
        "False is returned — six characters fall below the threshold of eight; Rex upgrades the access policy.",
    ),
    # 8 mcq
    (
        "A CargoHold's volume() method is on the schematic — Rex traces the output for dimensions 2, 3, 4.",
        "Volume 24 is confirmed; Rex sees how three attributes multiply together cleanly inside a single method.",
    ),
    # 9 mini_code
    (
        "Rex needs the cross-section of a delta-wing fighter — a Triangle class with an area() method is required.",
        "The wing area calculates correctly; Rex's design suite now has methods that derive geometric results on demand.",
    ),
    # 10 mini_code
    (
        "The ship's credit reserves need an is_overdrawn() monitor — Rex must build a BankAccount class with that method.",
        "The reserve monitor reports accurately; Rex is primed to tackle methods that actively change an object's state.",
    ),
])

apply_beats(L2, "mystery", [
    # 0 concept
    (
        "Cole's Suspect profiles hold data, but the investigation needs active techniques — methods that can assess and describe each person of interest.",
        "The Suspect gains is_dangerous and describe methods; Cole can now run assessments on any profile through its own built-in logic.",
    ),
    # 1 mcq
    (
        "A Witness has a testify() method — Cole must predict what the witness says when called to the stand.",
        "The testimony prints 'Rex says Woof!' as coded; Cole sees that methods reach into self.name to form their output.",
    ),
    # 2 fill_blank
    (
        "A CrimeScene needs its area() calculated, but the correct attribute must be referenced inside the formula.",
        "With self.radius in place, the perimeter area computes — the scene is measured and logged in the case file.",
    ),
    # 3 mcq
    (
        "An EvidenceLog starts empty — Cole must follow value() to confirm what it returns before any evidence is entered.",
        "Zero returns as expected; Cole notes that a read-only method simply reports whatever state the object currently holds.",
    ),
    # 4 arrange
    (
        "Cole needs a Profiler class with an introduce() method that states its name — the code blocks need ordering.",
        "The introduce method is filed into the Profiler blueprint; the investigator can now announce its identity on record.",
    ),
    # 5 mcq
    (
        "A SafeRoom's area() multiplies its dimensions — Cole traces the output for width 4, height 5.",
        "Area 20 confirmed; Cole sees how a method converts stored measurements into a useful investigative result.",
    ),
    # 6 fill_blank
    (
        "A ForensicLab thermometer tracks sample temperatures in Celsius — Cole must complete the Fahrenheit conversion formula.",
        "The + operator closes the conversion; the sample temperature is correctly calibrated for the lab report.",
    ),
    # 7 mcq
    (
        "A SafeCode's is_strong() check assesses whether 'abc123' is long enough for the vault combination.",
        "False is returned — six characters miss the eight-character minimum; Cole flags the code as weak evidence.",
    ),
    # 8 mcq
    (
        "A Vault's volume() method is on file — Cole traces the result for dimensions 2, 3, 4.",
        "Volume 24 confirmed; Cole notes that three attributes can be multiplied cleanly inside a single method.",
    ),
    # 9 mini_code
    (
        "Cole must map a triangular crime scene footprint — a Triangle class with an area() method is required.",
        "The footprint area calculates correctly; Cole's forensic toolkit now includes geometry methods for scene analysis.",
    ),
    # 10 mini_code
    (
        "The department's evidence fund needs an is_overdrawn() check — Cole must build a BankAccount class with that method.",
        "The fund monitor works correctly; Cole is ready to move on to methods that actually change an object's state.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 3 — Methods That Change State
# ---------------------------------------------------------------------------
L3 = UNIT_DIR / "lesson_3.yaml"

apply_beats(L3, "fantasy", [
    # 0 concept
    (
        "Ash's creatures can speak and describe themselves, but the workshop needs objects whose inner state can actually change — like a magical battery that drains.",
        "The Battery drains twice and clamps at zero; Ash now understands that each method call permanently alters the object's stored value.",
    ),
    # 1 mcq
    (
        "An enchantment counter ticks twice — Ash must predict the final count.",
        "Count reaches 2; Ash sees that each increment() call builds on the previous state, not a fixed starting point.",
    ),
    # 2 fill_blank
    (
        "A wizard's mana pool needs a spend() method that deducts the cast cost — Ash must choose the right operator.",
        "With -= in place, the mana pool shrinks correctly after each spell; the pouch drains as the wizard works.",
    ),
    # 3 mcq
    (
        "Elara pushes two spell scrolls onto a stack — Ash must read what the stack looks like afterwards.",
        "Both scrolls appear in order: [1, 2]; Ash confirms that append-based methods preserve insertion order.",
    ),
    # 4 arrange
    (
        "A magical BankAccount needs a deposit method that adds to its balance — the code blocks need assembling.",
        "The deposit method is assembled; gold can now flow into the account and the balance updates with each call.",
    ),
    # 5 mcq
    (
        "A magic torch is toggled on then off — Ash must determine its final state.",
        "The torch returns to False after two toggles; Ash sees that state changes are cumulative and reversible.",
    ),
    # 6 fill_blank
    (
        "A cauldron needs a method that adds new ingredients to its queue — the right list method must be chosen.",
        "append slots the ingredient at the end; the cauldron's queue grows in the correct order.",
    ),
    # 7 mcq
    (
        "Elara refuels a mana tank then uses some — Ash must trace the final fuel level.",
        "Fuel ends at 60; Ash follows the arithmetic: 50 + 30 = 80, then 80 - 20 = 60.",
    ),
    # 8 mcq
    (
        "A spell score tracker accumulates points then resets — Ash must predict the final score.",
        "Zero is printed after reset(); Ash sees that a reset method can wipe accumulated state in a single call.",
    ),
    # 9 mini_code
    (
        "Ash needs a Timer that ticks five seconds — a seconds attribute and a tick() method that adds 1 are required.",
        "Five ticks land correctly at seconds = 5; the enchanted timer is working and ready for longer rituals.",
    ),
    # 10 mini_code
    (
        "Ash's spell inventory needs add_item and remove_item methods — the sword must be removable from the shield.",
        "The inventory updates cleanly: sword gone, shield remains; Ash's mutable collection pattern is complete and ready for Lesson 4.",
    ),
])

apply_beats(L3, "scifi", [
    # 0 concept
    (
        "The Helix's components store data and report status, but the crew needs systems that actually change state under load — starting with the ship's battery.",
        "The battery drains and clamps at zero; Voss confirms that each method call on a mutable object permanently updates its stored charge.",
    ),
    # 1 mcq
    (
        "The system event counter fires twice — Rex must predict the final count logged to the console.",
        "Count reads 2; Rex sees that increment() accumulates on live state, not a snapshot.",
    ),
    # 2 fill_blank
    (
        "The ship's fuel reserve needs a spend() method that deducts cost — Rex must pick the correct assignment operator.",
        "With -= wired in, the reserve drains correctly each time the engines fire.",
    ),
    # 3 mcq
    (
        "Voss pushes two commands onto the command stack — Rex must read the stack's final contents.",
        "The stack holds [1, 2] in order; Rex confirms that the command queue preserves insertion sequence.",
    ),
    # 4 arrange
    (
        "The ship's BankAccount needs a deposit method to add to its balance — the code blocks need ordering.",
        "The deposit method is wired up; the account balance now updates correctly with each transaction.",
    ),
    # 5 mcq
    (
        "A ship indicator light is toggled on then off — Rex must determine its final state.",
        "The indicator returns to False; Rex sees that two toggles cancel each other and restore the original state.",
    ),
    # 6 fill_blank
    (
        "The mission queue needs a method to append new tasks — Rex must choose the right list operation.",
        "append queues the task at the end; the mission stack grows in the correct priority order.",
    ),
    # 7 mcq
    (
        "Voss refuels a tank then burns some on a manoeuvre — Rex must trace the final fuel reading.",
        "Fuel settles at 60; Rex traces 50 + 30 = 80, then 80 - 20 = 60 on the gauge.",
    ),
    # 8 mcq
    (
        "A mission score tracker logs points then resets for the next sortie — Rex must predict the final value.",
        "Zero prints after reset(); Rex notes that a reset method is the cleanest way to wipe accumulated state.",
    ),
    # 9 mini_code
    (
        "Rex needs a mission Timer that counts seconds — a seconds attribute and a tick() method adding 1 are required.",
        "Five ticks produce seconds = 5; the timer is mission-ready and logging elapsed time correctly.",
    ),
    # 10 mini_code
    (
        "The ship's Inventory needs add_item and remove_item methods to manage cargo — 'sword' must be removable.",
        "The cargo list updates correctly: sword offloaded, shield retained; Rex's mutable inventory system is operational for Lesson 4.",
    ),
])

apply_beats(L3, "mystery", [
    # 0 concept
    (
        "Cole's profiles can describe suspects, but the case needs records that change as new information arrives — like a credibility score that drains under interrogation.",
        "The Battery drains and clamps at zero; Cole sees that each method call permanently alters the object's stored value, just as evidence shifts a suspect's standing.",
    ),
    # 1 mcq
    (
        "The evidence counter is updated twice as new items are logged — Cole must predict the final tally.",
        "Count reaches 2; Cole confirms that each increment() builds on the live state of the object.",
    ),
    # 2 fill_blank
    (
        "A suspect's alibi window needs a spend() method that deducts hours — Cole must choose the right operator.",
        "With -= in place, the alibi window narrows correctly as each hour is accounted for.",
    ),
    # 3 mcq
    (
        "Cole pushes two clues onto the evidence stack — the order matters, so he checks the final contents.",
        "Both clues appear in order [1, 2]; Cole confirms the stack preserves the sequence in which evidence was filed.",
    ),
    # 4 arrange
    (
        "The department fund needs a deposit method to add incoming money — the code pieces need to be ordered.",
        "The deposit method is filed; the fund balance now updates correctly each time resources are added.",
    ),
    # 5 mcq
    (
        "A case-open indicator is toggled on then off — Cole must determine its final state.",
        "The indicator returns to False after two toggles; Cole notes that reversible state changes can be tracked precisely.",
    ),
    # 6 fill_blank
    (
        "The evidence queue needs a method that appends new clues — Cole must choose the right list operation.",
        "append adds the clue to the end; the evidence queue grows in the order items were discovered.",
    ),
    # 7 mcq
    (
        "Cole adds to then draws from the informant fund — he must trace the final balance.",
        "The fund settles at 60; Cole follows 50 + 30 = 80, then 80 - 20 = 60 in the ledger.",
    ),
    # 8 mcq
    (
        "A case score tracker accumulates leads then resets when the case is closed — Cole must predict the final value.",
        "Zero prints after reset(); Cole notes that resetting a score object clears all accumulated state in one call.",
    ),
    # 9 mini_code
    (
        "Cole needs a Timer to track interrogation length — a seconds attribute and a tick() method adding 1 are required.",
        "Five ticks land at seconds = 5; the interrogation timer is calibrated and running.",
    ),
    # 10 mini_code
    (
        "The case file needs add_item and remove_item methods to manage evidence — 'sword' must be removable, leaving 'shield'.",
        "The evidence list updates cleanly: sword gone, shield on record; Cole's mutable case file is ready for Lesson 4.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 4 — Multiple Instances
# ---------------------------------------------------------------------------
L4 = UNIT_DIR / "lesson_4.yaml"

apply_beats(L4, "fantasy", [
    # 0 concept
    (
        "Elara can now craft a single Creature, but the workshop must be able to summon many separate familiars — each fully independent.",
        "Three familiars spring to life from the same blueprint, each with its own attributes; changing one leaves the others untouched.",
    ),
    # 1 mcq
    (
        "Two spell containers hold different capacities — Elara must add their sizes together.",
        "The combined capacity is 30; Elara sees that separate instances each carry their own data and can be combined freely.",
    ),
    # 2 fill_blank
    (
        "Two wizards are registered, but the spell must read the hp from Alice's instance specifically.",
        "Accessing p1.hp, Elara reads Alice's health correctly — the second wizard's data remains untouched.",
    ),
    # 3 mcq
    (
        "Two familiars share the same blueprint, but only one is renamed — Elara must verify which names print.",
        "d1 prints 'Max' and d2 stays 'Bella'; renaming one familiar never bleeds into another.",
    ),
    # 4 arrange
    (
        "Elara wants two Lantern instances with different glow levels and needs to compare which burns brighter.",
        "The brighter lantern is identified correctly; Elara can now pit two instances against each other using attribute comparisons.",
    ),
    # 5 mcq
    (
        "Two familiars each track their own mana with independent counters — Elara must predict both final values.",
        "a.n is 2, b.n is 1; the familiars prove entirely independent — one's mana changes nothing in the other.",
    ),
    # 6 fill_blank
    (
        "Two wizards' spell-point scores are on record — Elara must determine whether the first outscores the second.",
        "The > comparison returns True; Elara can now rank any two instances by their attributes.",
    ),
    # 7 mcq
    (
        "Elara loops through a list of summoned creatures and prints each one's brand attribute.",
        "Toyota, BMW, Ford print in order; Elara sees that a list of instances can be iterated just like a list of strings.",
    ),
    # 8 mcq
    (
        "Two magical jars share the same blueprint, but only one is filled — Elara must check both filled values.",
        "j1.filled is 5, j2.filled is 0; filling one jar never touches the other, confirming true independence.",
    ),
    # 9 mini_code
    (
        "Elara needs two different magical dice — a 6-sided and a 20-sided — each capable of producing its own random roll.",
        "Both dice roll within their correct ranges; Elara's randomised familiar-challenge system is ready.",
    ),
    # 10 mini_code
    (
        "Three apprentices compete for the highest score — Elara must build Student instances and find the top performer.",
        "The highest-scoring apprentice's name is announced; Elara's roster system is complete and ready for Lesson 5.",
    ),
])

apply_beats(L4, "scifi", [
    # 0 concept
    (
        "Voss has one working unit blueprint, but the mission calls for a whole fleet — each vessel must be independent of the others.",
        "Three units deploy from the same schematic, each with its own data; modifying one leaves the rest of the fleet unchanged.",
    ),
    # 1 mcq
    (
        "Two cargo containers report different capacities — Voss must add both sizes to plan total storage.",
        "Combined capacity is 30; Voss confirms that two separate instances can contribute their data to a shared calculation.",
    ),
    # 2 fill_blank
    (
        "Two crew members are registered, but the system must pull the hp reading from Alice's record specifically.",
        "p1.hp returns Alice's health correctly — p2's data stays isolated on its own record.",
    ),
    # 3 mcq
    (
        "Two units share the same class, but only one is renamed in the field — Voss checks both unit IDs.",
        "d1 prints 'Max', d2 stays 'Bella'; renaming one unit has zero effect on the other.",
    ),
    # 4 arrange
    (
        "Voss wants two Lamp units at different power levels and needs to identify the brighter one.",
        "The brighter unit is identified correctly; Voss can now compare any two instances by their attribute values.",
    ),
    # 5 mcq
    (
        "Two units each track their own mission count independently — Voss must predict both final counts.",
        "a.n is 2, b.n is 1; the units are fully independent — one's mission count never changes the other.",
    ),
    # 6 fill_blank
    (
        "Two units' performance scores are on record — Voss must determine whether unit 1 outscores unit 2.",
        "The > comparison returns True; Voss can now rank any two units by their stored scores.",
    ),
    # 7 mcq
    (
        "Voss iterates through the fleet and prints each vehicle's brand identifier.",
        "Toyota, BMW, Ford print in sequence; Voss confirms that a list of objects can be looped over just like any other list.",
    ),
    # 8 mcq
    (
        "Two fuel tanks share the same blueprint, but only one receives a fill — Voss checks both fuel readings.",
        "j1.filled is 5, j2.filled is 0; filling one tank never touches the other, confirming complete independence.",
    ),
    # 9 mini_code
    (
        "Voss needs a 6-sided and a 20-sided Dice unit, each able to return its own random roll result.",
        "Both dice produce rolls within their correct ranges; Voss's randomised mission-assignment module is operational.",
    ),
    # 10 mini_code
    (
        "Three crew candidates compete on grade — Voss must build Student instances and surface the top-scoring member.",
        "The highest-graded crew member's name prints correctly; Voss is ready to extend the class hierarchy in Lesson 5.",
    ),
])

apply_beats(L4, "mystery", [
    # 0 concept
    (
        "Cole has one Suspect profile template, but the case has multiple witnesses — each must be tracked as a fully independent object.",
        "Three separate witness profiles are created from the same class; changing one record leaves the others exactly as filed.",
    ),
    # 1 mcq
    (
        "Two evidence containers have different capacities — Cole must add both to plan total storage space.",
        "Combined capacity is 30; Cole confirms that separate instances each hold their own data without interference.",
    ),
    # 2 fill_blank
    (
        "Two witnesses are on file, but the read must pull the credibility score from Alice's record specifically.",
        "p1.hp returns Alice's score correctly — Bob's record is untouched.",
    ),
    # 3 mcq
    (
        "Two suspects are registered under the same class, but only one is renamed during the investigation — Cole checks both.",
        "d1 prints 'Max', d2 stays 'Bella'; updating one suspect's alias has no effect on any other profile.",
    ),
    # 4 arrange
    (
        "Cole wants two Lamp instances at different brightness levels and needs to determine which shines brighter.",
        "The brighter lamp is identified correctly; Cole can now compare any two instances head-to-head by attribute.",
    ),
    # 5 mcq
    (
        "Two witnesses each track their own interview count — Cole must predict both final tallies.",
        "a.n is 2, b.n is 1; the witnesses keep completely separate counts — one's interviews never affect the other.",
    ),
    # 6 fill_blank
    (
        "Two witnesses have credibility scores on file — Cole must determine whether witness 1 outranks witness 2.",
        "The > comparison returns True; Cole can now rank any two profiles by their stored scores.",
    ),
    # 7 mcq
    (
        "Cole iterates through a suspect list and prints each person's name.",
        "Toyota, BMW, Ford print in sequence; Cole confirms that a list of profile objects can be looped through like any other list.",
    ),
    # 8 mcq
    (
        "Two evidence bags share the same class, but only one receives contents — Cole checks both filled readings.",
        "j1.filled is 5, j2.filled is 0; filling one bag never touches the other, proving full independence.",
    ),
    # 9 mini_code
    (
        "Cole needs a 6-sided and a 20-sided Dice object to randomise case assignment — each must roll within its own range.",
        "Both dice roll correctly within their ranges; Cole's randomised case-selection tool is on record.",
    ),
    # 10 mini_code
    (
        "Three informants are ranked by reliability grade — Cole must build Student instances and surface the most reliable one.",
        "The top-ranked informant's name prints; Cole's multi-instance roster is complete and ready for the inheritance lesson.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 5 — Inheritance
# ---------------------------------------------------------------------------
L5 = UNIT_DIR / "lesson_5.yaml"

apply_beats(L5, "fantasy", [
    # 0 concept
    (
        "Ash's workshop holds many creature types, and writing a full blueprint for each from scratch would fill every scroll — a shared ancestry is the answer.",
        "Cat and Dog both inherit from Animal: name flows down automatically, and each child overrides speak() with its own magic word.",
    ),
    # 1 mcq
    (
        "A child spell class inherits the base spell's power attribute — Ash must verify it is accessible without redefinition.",
        "The inherited attribute prints cleanly at 120; Ash confirms that child classes own everything the parent declared.",
    ),
    # 2 fill_blank
    (
        "A Square rune inherits from Shape and overrides area() — Ash must supply the operator that squares the side.",
        "Multiply closes the formula: 5 * 5 = 25; the rune's area is correct and the override is complete.",
    ),
    # 3 mcq
    (
        "A child Mage class inherits greet() from its parent — Ash checks whether it can call the method without defining it again.",
        "'Hi, I am Alice' prints correctly; Ash sees that inherited methods work on child instances without any extra code.",
    ),
    # 4 arrange
    (
        "A Bird familiar must inherit from Animal and override speak() to return 'Tweet' — the blocks need ordering.",
        "Bird(Animal) is assembled; the familiar chirps 'Tweet' while still carrying its name from the parent's __init__.",
    ),
    # 5 mcq
    (
        "Two child spell classes: one overrides the chant, one inherits it — Ash must predict what each prints.",
        "B prints 'B' and C prints 'A'; Ash sees that overriding is optional — children that stay silent inherit the parent's voice.",
    ),
    # 6 fill_blank
    (
        "A dragon familiar class needs to inherit from Animal automatically — Ash must name the parent inside the parentheses.",
        "Animal is placed in the brackets; the dragon inherits name from __init__ without any extra setup.",
    ),
    # 7 mcq
    (
        "A child Sword class overrides the attack method to deal double damage — Ash traces the output.",
        "'Slash! 20 damage' is the result; Ash understands that overriding replaces the parent's behaviour entirely.",
    ),
    # 8 mcq
    (
        "Ash pauses to consider: what is the core benefit of giving spell classes a shared bloodline through inheritance?",
        "Reuse without repetition — child spells inherit the parent's logic and only override what makes them unique, keeping the spellbook lean.",
    ),
    # 9 mini_code
    (
        "Ash needs a Circle that inherits from Shape and overrides area() — the blueprint and the override both need writing.",
        "Circle(Shape) computes the area as ~78.5; Ash's shape hierarchy is complete and every subclass can specialise at will.",
    ),
    # 10 mini_code
    (
        "A Car must inherit make and speed from Vehicle and add its own honk() method — both the parent and the child need defining.",
        "The Car inherits cleanly and honk() returns 'Beep!'; Ash's inheritance mastery is sealed — the entire unit's arc is complete.",
    ),
])

apply_beats(L5, "scifi", [
    # 0 concept
    (
        "Voss needs specialised ship modules, but rewriting every shared attribute from scratch for each one would blow the build schedule — a base module class is the solution.",
        "Cat and Dog module variants inherit from Animal: the name registers automatically, and each child overrides its output signal independently.",
    ),
    # 1 mcq
    (
        "A sub-module inherits its speed rating from the base module — Voss must confirm the attribute is accessible without redeclaring it.",
        "Speed prints at 120 without any extra code in Car; Voss confirms inherited attributes are fully owned by child classes.",
    ),
    # 2 fill_blank
    (
        "A Square solar panel inherits from Shape and overrides area() — Voss must supply the operator that squares the side length.",
        "Multiply locks in: 5 * 5 = 25; the panel's area is verified and the override is complete.",
    ),
    # 3 mcq
    (
        "A sub-module inherits the greet broadcast from its parent — Voss checks whether it transmits without being redefined.",
        "'Hi, I am Alice' transmits correctly; Voss sees that inherited methods fire on child instances with zero additional code.",
    ),
    # 4 arrange
    (
        "A Bird drone unit must inherit from Animal and override speak() to broadcast 'Tweet' — the code needs assembling.",
        "Bird(Animal) is wired up; the drone broadcasts 'Tweet' while still registering its name from the parent's __init__.",
    ),
    # 5 mcq
    (
        "Two sub-modules: one overrides the hello signal, one inherits it — Voss must predict each module's output.",
        "B outputs 'B', C outputs 'A'; Voss sees that silence in a child class means inheriting the parent's default signal.",
    ),
    # 6 fill_blank
    (
        "A drone sub-class needs to inherit from Animal — Voss must specify the parent module inside the parentheses.",
        "Animal is placed in the brackets; the drone inherits the name attribute automatically from the base module's __init__.",
    ),
    # 7 mcq
    (
        "A specialised Sword weapon module overrides attack() to deal double the base damage — Voss traces the output.",
        "'Slash! 20 damage' is confirmed; overriding replaces the parent's output entirely with the child's specialised behaviour.",
    ),
    # 8 mcq
    (
        "Voss pauses to consider: what is the primary engineering benefit of building child modules from a parent class?",
        "Code reuse without duplication — child modules share the parent's logic and override only their unique behaviour, keeping the codebase lean.",
    ),
    # 9 mini_code
    (
        "Voss needs a Circle module that inherits from Shape and overrides area() to compute the cross-section.",
        "Circle(Shape) returns ~78.5; the module hierarchy is complete and any future shape can be slotted in as a child.",
    ),
    # 10 mini_code
    (
        "A Car class must inherit make and speed from Vehicle and add a honk() method — both the parent and child need defining.",
        "The Car inherits cleanly and honk() returns 'Beep!'; Voss's inheritance module is fully operational — Unit 7 complete.",
    ),
])

apply_beats(L5, "mystery", [
    # 0 concept
    (
        "Cole's investigation reveals categories of criminal that share common traits — rewriting a full profile for each type would bury the department in paperwork.",
        "Cat and Dog criminal types inherit from Animal: the name is logged automatically, and each type overrides its own motive method.",
    ),
    # 1 mcq
    (
        "A sub-suspect inherits the base suspect's speed attribute — Cole must verify it is available without redeclaring it.",
        "Speed reads at 120 from the child class alone; Cole confirms that inherited data is fully accessible to every child profile.",
    ),
    # 2 fill_blank
    (
        "A Square crime scene area is computed by a child class overriding the base — Cole must supply the correct operator.",
        "Multiply is the answer: 5 * 5 = 25; the scene's area is on file and the override is verified.",
    ),
    # 3 mcq
    (
        "A sub-suspect profile inherits the greeting method — Cole checks whether it can be called without redefining it.",
        "'Hi, I am Alice' is returned; Cole sees that inherited methods work on child instances without any extra code.",
    ),
    # 4 arrange
    (
        "An accomplice profile must inherit from Animal and override speak() to return 'Tweet' — the blocks need ordering.",
        "Bird(Animal) is assembled; the accomplice profile inherits its name automatically and announces its own call sign.",
    ),
    # 5 mcq
    (
        "Two criminal sub-types: one overrides the motive, one inherits it — Cole must predict what each returns.",
        "B returns 'B', C returns 'A'; Cole understands that a child class that stays silent inherits the parent's default motive.",
    ),
    # 6 fill_blank
    (
        "An accomplice class needs to inherit from Animal — Cole must name the parent class inside the parentheses.",
        "Animal is entered; the accomplice profile inherits its name attribute automatically from the base class's __init__.",
    ),
    # 7 mcq
    (
        "A specialised criminal class overrides the attack method for greater impact — Cole traces the output.",
        "'Slash! 20 damage' is the result; Cole sees that overriding replaces the parent's behaviour with the child's own logic.",
    ),
    # 8 mcq
    (
        "Cole reflects: what is the core investigative value of building criminal profiles through inheritance?",
        "Shared logic, specialised details — child profiles reuse the parent's foundation and only define what makes each type distinct.",
    ),
    # 9 mini_code
    (
        "Cole needs a Circle scene-boundary class that inherits from Shape and overrides area() for circular perimeters.",
        "Circle(Shape) computes ~78.5; the scene-boundary hierarchy is complete and any shape can now be profiled as a child class.",
    ),
    # 10 mini_code
    (
        "A Car class must inherit make and speed from Vehicle and add a honk() method — both parent and child need writing.",
        "The Car inherits cleanly and honk() returns 'Beep!'; Cole's case is closed — Unit 7's class hierarchy stands complete.",
    ),
])

print("\nAll beats applied successfully.")
