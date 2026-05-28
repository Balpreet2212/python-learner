import yaml
import os

def apply_beats(path, world, beats):
    """beats: list of (story_before, story_after) strings, indexed by exercise position"""
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f)
    exercises = data['worlds'][world]['exercises']
    for i, (before, after) in enumerate(beats):
        if i < len(exercises):
            exercises[i]['story_before'] = before
            exercises[i]['story_after'] = after
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)
    print(f"Updated {path} / {world}")


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1: Floor Division, Modulo, Exponents
# ─────────────────────────────────────────────────────────────────────────────

L1 = os.path.join(os.path.dirname(__file__), '..', 'content', 'units', 'unit_2', 'lesson_1.yaml')

# FANTASY – Finn rationing supplies on Frostpeak
l1_fantasy = [
    # 0 concept
    ("Finn must split 43 ration bars into pouches and calculate the power of a frost crystal — he needs three new operators to do it.",
     "Finn now understands floor division, modulo, and exponents — the tools that will carry him through every supply calculation on the mountain."),
    # 1 mcq – 7 // 2
    ("Finn has 7 food packs and wants to fill pouches that each hold 2 — he needs to know how many complete pouches he can make.",
     "Three full pouches packed and ready; the leftover half-pack stays behind at camp."),
    # 2 mcq – 10 % 3
    ("Finn counts 10 torches and wants to group them in threes — he needs to know how many will be left over.",
     "One stray torch remains after the groups are formed, and Finn tucks it into his belt."),
    # 3 arrange – 15 // 4
    ("Finn has 15 stamina potions to pack into crates of 4 — he needs to build the expression that tells him how many full crates he gets.",
     "Three full crates are loaded onto the sled; the remaining potions go into Finn's pack."),
    # 4 fill_blank – 17 % 5
    ("Finn wants to find out how many stamina points remain after distributing them into groups of 5 — he needs the right operator.",
     "Two points left over — just enough for one last burst up the icy slope."),
    # 5 mcq – 2 ** 10
    ("Each altitude checkpoint doubles the frost intensity, and Finn needs to know how fierce it gets after 10 doublings.",
     "1024 frost units — Finn layers on every warming rune he has before pushing higher."),
    # 6 arrange – 3 ** 4
    ("The storm triples in strength each stage, and Finn must build the expression that calculates its final intensity after 4 stages.",
     "81 — Finn braces himself and pulls his hood tight against the howling wind."),
    # 7 mcq – 100 % 7
    ("Finn has 100 metres of rope to cut into 7-metre sections — he needs to find out how many metres will be left over at the end.",
     "2 metres of rope left — not enough for another section, but Finn coils it up anyway."),
    # 8 fill_blank – defence ** 2
    ("Finn's frost shield strength is his defence stat squared — he needs the right operator to calculate it.",
     "The shield crackles to life, its power locked in by the exponent Finn just applied."),
    # 9 mcq – n % 2 == 0
    ("Finn wants to check whether he can pair up his supply bundles evenly before distributing them — he needs to know which expression tests for that.",
     "Modulo by 2 — the simplest test on the mountain, and now Finn's bundles sort themselves in seconds."),
    # 10 mini_code – 50 // 8 and 50 % 8
    ("Finn has 50 ration bars and pouches that hold 8 each — he needs to print both how many full pouches he can fill and how many bars are left over.",
     "6 full pouches packed, 2 bars tucked aside — Finn shoulders the load and heads for the next checkpoint."),
    # 11 mini_code – 2 ** 16
    ("The frost doubles every level of the summit; Finn needs to calculate exactly how powerful it becomes after 16 doublings and print it.",
     "65536 — the number blazes on the rune stone, and Finn knows he will need every spell in the book to survive the peak."),
]

# SCIFI – Zara distributing fuel cells aboard the Helix
l1_scifi = [
    # 0 concept
    ("Zara needs to split 43 fuel cells across thruster banks and calculate exponential sensor range — three new operators will handle it all.",
     "Floor division, modulo, and exponentiation are now in Zara's engineering toolkit, ready for every allocation problem the Helix throws at her."),
    # 1 mcq – 7 // 2
    ("Zara has 7 fuel rods to distribute equally between 2 thruster pods — she needs to know how many complete rods each pod gets.",
     "Three rods per pod loaded; the partial rod is logged as waste and vented."),
    # 2 mcq – 10 % 3
    ("10 scan pulses are being grouped into bursts of 3 — Zara needs to know how many pulses remain after the last full burst.",
     "One pulse left over; Zara queues it for the next burst cycle."),
    # 3 arrange – 15 // 4
    ("Zara has 15 cargo units to load across 4 storage bays using floor division — she needs to build that expression now.",
     "Three units per bay loaded and sealed; Zara marks the manifest and moves on."),
    # 4 fill_blank – 17 % 5
    ("After filling thruster tanks in batches of 5, Zara needs the right operator to find how many fuel units remain.",
     "2 units remain — Zara logs them as reserve and sets the batch timer for the next refuel cycle."),
    # 5 mcq – 2 ** 10
    ("Each relay booster doubles the signal strength; Zara needs to know the total reach after 10 doublings.",
     "1024 units — strong enough to punch through the asteroid field, and Zara opens the comms channel."),
    # 6 arrange – 3 ** 4
    ("Asteroid density triples every sector, and Zara needs to build the code that calculates the density after 4 sectors.",
     "81 — shields to maximum; Zara punches the thruster and threads through the debris."),
    # 7 mcq – 100 % 7
    ("Zara has 100 metres of cable to cut into 7-metre segments — she needs to know how many metres will be left over.",
     "2 metres of cable left; Zara labels the offcut and stows it in the emergency kit."),
    # 8 fill_blank – hull_rating ** 2
    ("Shield strength is the hull rating squared — Zara needs the right operator to compute it.",
     "The shield matrix locks in at full output, its power calculated and confirmed."),
    # 9 mcq – n % 2 == 0
    ("Zara needs to check whether she can pair thrusters evenly before a symmetric burn — she needs to know which expression tests for that.",
     "Modulo 2 returns the answer instantly; Zara pairs the thrusters and initiates the burn sequence."),
    # 10 mini_code – 50 // 8 and 50 % 8
    ("Zara has 50 fuel cells to load into thruster banks of 8 — she needs to print both how many full banks she fills and how many cells are left over.",
     "6 banks filled, 2 cells reserved — Zara seals the bays and reports ready for departure."),
    # 11 mini_code – 2 ** 16
    ("Each jump doubles the ship's speed multiplier; Zara needs to calculate and print the multiplier after 16 jumps.",
     "65536 — the Helix shudders as Zara punches the number into the nav computer and initiates the jump sequence."),
]

# MYSTERY – Cole filing and counting evidence
l1_mystery = [
    # 0 concept
    ("Cole has 43 evidence photos to file and needs to count branches of a case tree — three operators will handle the math.",
     "Floor division, modulo, and exponents — Cole adds them to his analytical toolkit and starts sorting the evidence room."),
    # 1 mcq – 7 // 2
    ("Cole is splitting 7 witness statements between 2 detectives and needs to know how many complete statements each gets.",
     "Three statements per detective assigned; the remaining statement is held for a joint review."),
    # 2 mcq – 10 % 3
    ("Cole groups 10 alibi entries into batches of 3 for review and needs to find out how many entries are left unchecked.",
     "One entry left over — Cole circles it in red and flags it for a second look."),
    # 3 arrange – 15 // 4
    ("Cole needs to distribute 15 case files across 4 detectives using floor division — he builds the expression now.",
     "Three files each; the remaining files land on Cole's own desk, as usual."),
    # 4 fill_blank – 17 % 5
    ("Cole has 17 suspect leads to group in fives and needs the right operator to find how many are left unassigned.",
     "2 leads left without a detective — Cole pins them to the board and makes a note to follow up personally."),
    # 5 mcq – 2 ** 10
    ("Each new witness doubles the possible alibi combinations; Cole needs to know the total after 10 witnesses.",
     "1024 combinations — Cole mutters under his breath and pours another coffee."),
    # 6 arrange – 3 ** 4
    ("Each lead branches into 3 sub-leads; Cole must build the expression to count how many trails exist after 4 levels.",
     "81 trails — Cole draws the tree on the whiteboard and circles the ones that point back to the same suspect."),
    # 7 mcq – 100 % 7
    ("Cole has 100 minutes of surveillance footage divided into 7-minute review slots — he needs to find out how many minutes remain after the last full slot.",
     "2 minutes of footage left unreviewed — Cole rewinds the tape and watches it one more time."),
    # 8 fill_blank – witness_rating ** 2
    ("A witness's credibility score is their rating squared — Cole needs the right operator to compute it.",
     "The credibility score is locked in; Cole logs it next to the witness's name in the casebook."),
    # 9 mcq – n % 2 == 0
    ("Cole wants to check whether a case number splits evenly between two detectives — he needs to know which expression tests for that.",
     "Modulo 2 — Cole pairs the cases in seconds and hands out the assignments."),
    # 10 mini_code – 50 // 8 and 50 % 8
    ("Cole has 50 evidence photos to file in folders of 8 — he needs to print both how many full folders are complete and how many photos are left over.",
     "6 full folders filed, 2 photos left on the desk — Cole slips them into a new folder marked 'overflow'."),
    # 11 mini_code – 2 ** 16
    ("Each branch of the case doubles the number of leads; Cole needs to calculate and print the total leads after 16 branches.",
     "65536 leads — Cole stares at the number, then pins a single name at the centre of the board."),
]

apply_beats(L1, 'fantasy', l1_fantasy)
apply_beats(L1, 'scifi',   l1_scifi)
apply_beats(L1, 'mystery', l1_mystery)


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2: Order of Operations
# ─────────────────────────────────────────────────────────────────────────────

L2 = os.path.join(os.path.dirname(__file__), '..', 'content', 'units', 'unit_2', 'lesson_2.yaml')

# FANTASY – Finn computing spell formulas on Frostpeak
l2_fantasy = [
    # 0 concept
    ("Finn's spell formulas depend on the order calculations happen — getting it wrong could send his magic wildly off target.",
     "With brackets controlling the order, Finn's spells land exactly where he aims them."),
    # 1 mcq – 2 + 3 * 4
    ("Finn casts a frost bolt: 3 ice shards boosted by power 4, plus 2 base damage — but which operation runs first?",
     "14 damage — the multiplication happened first, just as the spell scroll says it should."),
    # 2 fill_blank – (2 + 3) * 4
    ("Finn wants to add his stamina boost before multiplying by the power factor — he needs to wrap the right part in brackets.",
     "20 total spell power — the brackets force the addition first and the spell surges correctly."),
    # 3 mcq – 10 - 2 * 3
    ("The mountain drops Finn's altitude by 2 metres per storm across 3 storms — Finn needs to know where he ends up.",
     "Altitude 4 — Finn plants his ice-axe and checks the distance still to go."),
    # 4 arrange – (6 + 8 + 10) / 3
    ("Finn records stamina readings at three checkpoints and needs to build the code that correctly averages them.",
     "The average prints cleanly — brackets grouped the sum before division, just as the spell formula requires."),
    # 5 mcq – (10 - 3) ** 2
    ("Finn calculates frost pressure by subtracting safe zones from the altitude and squaring the result — brackets matter here.",
     "49 pressure units — Finn tightens his frost ward and keeps climbing."),
    # 6 fill_blank – (a + b + c) / 3
    ("Finn has three camp stamina readings and needs to divide their sum by 3 — he just needs the right operator after the brackets.",
     "Mean stamina calculated; Finn knows exactly how much energy he has left for the final push."),
    # 7 mcq – x * 2 + 1
    ("Finn doubles his speed boost then adds a rune bonus — but in what order does Python evaluate this?",
     "11 — multiplication first, then the bonus added on top, exactly as Finn planned."),
    # 8 mcq – 8 / 2 + 6 / 3
    ("Finn shares rations and torches across zones — two separate divisions happen before the final sum.",
     "6.0 total per zone — Finn ticks off the supply list and heads for the next camp."),
    # 9 arrange – (a + b) / 2
    ("Two altitude readings need averaging — Finn must build the expression that adds them first, then halves the result.",
     "The midpoint altitude is found; Finn marks it on his map and plots a safe path between the two camps."),
    # 10 mini_code – average of 70, 85, 91
    ("Finn's stamina at three checkpoints is 70, 85, and 91 — he needs to calculate and print the average.",
     "82.0 — a solid score; Finn nods and prepares for the steepest section of the climb."),
    # 11 mini_code – (12 + 8) * (5 - 3)
    ("Finn's final spell formula is (12 + 8) * (5 - 3) — he needs to print the correct result using parentheses.",
     "40 — the spell formula checks out, and Finn commits it to memory for the summit battle."),
]

# SCIFI – Zara computing trajectory corrections aboard the Helix
l2_scifi = [
    # 0 concept
    ("Zara's trajectory calculations depend on the exact order of arithmetic — a single wrong precedence and the Helix misses its window.",
     "With the order of operations confirmed, Zara locks in the corrected course and the ship steadies."),
    # 1 mcq – 2 + 3 * 4
    ("Zara's thruster model adds 3 burst units multiplied by power factor 4, then adds baseline thrust — she needs to know which runs first.",
     "14 — multiplication before addition, exactly as the flight computer expects."),
    # 2 fill_blank – (2 + 3) * 4
    ("Zara needs the sensor sum computed before the range factor is applied — she adds a bracket to control the order.",
     "20 scan units — the sensor array locks on correctly with the brackets in place."),
    # 3 mcq – 10 - 2 * 3
    ("Zara's fuel drops 2 units per asteroid collision across 3 collisions — she needs to know what remains.",
     "4 units remaining — Zara reroutes power from non-essential systems to stretch the fuel supply."),
    # 4 arrange – (6 + 8 + 10) / 3
    ("Zara needs to average velocity readings from three sensor buoys — she must build the correct bracketed expression.",
     "The average velocity prints correctly; Zara enters it into the nav system and confirms the heading."),
    # 5 mcq – (10 - 3) ** 2
    ("Zara computes collision impact force: distance minus safe zones, squared — brackets determine the result.",
     "49 impact units — Zara boosts the shield emitters and adjusts the approach vector."),
    # 6 fill_blank – (a + b + c) / 3
    ("Three waypoint fuel readings are already summed in brackets — Zara just needs the right operator to find the mean.",
     "Mean fuel level confirmed; Zara updates the mission log and sets the next waypoint."),
    # 7 mcq – x * 2 + 1
    ("Zara doubles her thruster output then adds one emergency boost unit — Python's precedence rules decide the order.",
     "11 — thrusters at maximum, one boost in reserve; Zara clears the debris field."),
    # 8 mcq – 8 / 2 + 6 / 3
    ("Zara distributes oxygen and power cells across sections of the ship — two independent divisions happen before the total is summed.",
     "6.0 resources per zone — Zara logs the allocation and seals the bulkhead doors."),
    # 9 arrange – (a + b) / 2
    ("Two thrust readings need to be averaged — Zara builds the expression that sums them first, then halves the result.",
     "Midpoint velocity confirmed; Zara feeds it to the autopilot and watches the nav line stabilise."),
    # 10 mini_code – average of 70, 85, 91
    ("Zara's fuel readings at three waypoints are 70, 85, and 91 — she needs to calculate and print the average.",
     "82.0 — well above the safety threshold; Zara marks the route clear and accelerates."),
    # 11 mini_code – (12 + 8) * (5 - 3)
    ("Zara's trajectory formula is (12 + 8) * (5 - 3) — she must print the correct result using parentheses.",
     "40 — the formula checks out; Zara fires the manoeuvring thrusters and the Helix slides onto the correct course."),
]

# MYSTERY – Cole cross-referencing timestamps and evidence weights
l2_mystery = [
    # 0 concept
    ("Cole is cross-referencing timestamps and the order of arithmetic matters — one wrong calculation could let a suspect slip away.",
     "With the correct order established, Cole's timeline holds up and the evidence begins to point in one direction."),
    # 1 mcq – 2 + 3 * 4
    ("Cole scores three witness sightings against a credibility factor of 4, then adds 2 confirmed clues — which operation runs first?",
     "14 evidence points — the multiplication ran first, and the total lines up with Cole's notes."),
    # 2 fill_blank – (2 + 3) * 4
    ("Cole wants to combine two clue scores before scaling them by a reliability factor — he wraps the addition in brackets.",
     "20 — the combined score is weighted correctly, and Cole circles the figure in his casebook."),
    # 3 mcq – 10 - 2 * 3
    ("Three false alibis each cost Cole 2 credibility points — he needs to know how many certainty points he has left.",
     "4 remaining — enough to keep the case open, but Cole knows he needs more solid evidence."),
    # 4 arrange – (6 + 8 + 10) / 3
    ("Cole needs to average credibility scores from three witnesses — he builds the correctly bracketed expression.",
     "The mean score prints; Cole notes whether it clears his reliability threshold and moves on."),
    # 5 mcq – (10 - 3) ** 2
    ("Cole calculates the alibi discrepancy: reported minutes minus verified, then squared — brackets determine the order.",
     "49 inconsistency points — Cole highlights the figure and adds it to the suspect file."),
    # 6 fill_blank – (a + b + c) / 3
    ("Three witness credibility scores are already summed in brackets — Cole just needs the right operator to find the mean.",
     "Mean trustworthiness calculated; Cole ranks the witnesses and decides which testimony to lead with."),
    # 7 mcq – x * 2 + 1
    ("Cole doubles the number of suspect sightings then adds one confirmed lead — precedence rules determine the result.",
     "11 total clues — Cole staples them together and adds the stack to the active investigation file."),
    # 8 mcq – 8 / 2 + 6 / 3
    ("Cole splits footage hours between detectives and case files between officers — two divisions before the total workload is summed.",
     "6.0 per person — Cole signs the assignment sheets and hands them out before the morning briefing."),
    # 9 arrange – (a + b) / 2
    ("Two alibi timestamps need to be averaged — Cole builds the expression that adds them first, then halves the result.",
     "The midpoint time is found; Cole marks it on the timeline and checks whether the suspect could have been at the scene."),
    # 10 mini_code – average of 70, 85, 91
    ("Cole's credibility scores for three witnesses are 70, 85, and 91 — he needs to calculate and print the average.",
     "82.0 — above the reliability threshold; Cole marks all three as credible and schedules formal interviews."),
    # 11 mini_code – (12 + 8) * (5 - 3)
    ("Cole's evidence formula is (12 + 8) * (5 - 3) — he must print the correct result using parentheses.",
     "40 — the formula confirms the suspect's opportunity window, and Cole closes the casebook with quiet certainty."),
]

apply_beats(L2, 'fantasy', l2_fantasy)
apply_beats(L2, 'scifi',   l2_scifi)
apply_beats(L2, 'mystery', l2_mystery)


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3: Comparison Operators
# ─────────────────────────────────────────────────────────────────────────────

L3 = os.path.join(os.path.dirname(__file__), '..', 'content', 'units', 'unit_2', 'lesson_3.yaml')

# FANTASY – Finn using Truth Runes on Frostpeak
l3_fantasy = [
    # 0 concept
    ("Finn discovers Truth Runes etched into a waystone — ancient glyphs that answer yes or no questions about the mountain's conditions.",
     "The three runes glow True in sequence; Finn now trusts them to guide every decision he makes on the climb."),
    # 1 mcq – 7 > 3
    ("Finn's first rune test: is he above the storm threshold of altitude 3?",
     "True — Finn is well clear of the storm line and the rune pulses green."),
    # 2 fill_blank – altitude == 10
    ("Finn needs to check whether he has reached the exact summit altitude of 10 — only one operator can test for equality without changing the value.",
     "The rune confirms it: altitude is exactly 10, and the summit marker lights up."),
    # 3 mcq – score >= 60
    ("Finn's stamina score is 60 — he needs to know whether he meets the minimum threshold of 60 to keep climbing.",
     "True — 60 meets 60, and the path ahead remains open."),
    # 4 arrange – altitude != 5
    ("Finn must build a rune that glows True only when he is NOT at the cursed altitude of 5.",
     "The != rune flares True — Finn is not at the cursed marker and presses on with relief."),
    # 5 mcq – 5 < 10
    ("Finn's stamina is 5 and the required minimum is 10 — the rune needs to tell him whether he falls short.",
     "True — he does fall short; Finn drinks a stamina potion before attempting the next ledge."),
    # 6 fill_blank – stamina >= 50
    ("Finn wants to know if his stamina meets or exceeds the 50 required to cross the glacier — he needs the right comparison.",
     "The rune answers True or False instantly; Finn either steps onto the glacier or waits at camp."),
    # 7 mcq – x == 5 and x != 5
    ("A rune checkpoint asks two questions at once: is altitude 5, and is it not 5?",
     "True then False — the rune pair confirms Finn's exact position, no ambiguity."),
    # 8 mcq – 'Alice' == 'alice'
    ("Finn checks a rune inscription against the scroll — the names look the same but the capitalisation differs.",
     "False — rune matching is case-sensitive, and Finn corrects the inscription before the seal accepts him."),
    # 9 arrange – stamina <= 0
    ("Finn needs a rune that signals True the moment his stamina hits zero — he builds the expression now.",
     "The rune stands ready to flash True if Finn's stamina ever bottoms out, keeping him safe on the mountain."),
    # 10 mini_code – score >= 60
    ("Finn reads his stamina from a sensor and needs to print True if it is 60 or above, False if it is below.",
     "The result prints correctly — Finn now has a reusable stamina check he can apply at every camp."),
    # 11 mini_code – a != b
    ("Finn takes two altitude readings and needs to print True if they differ, False if they match.",
     "With both comparison tools in hand, Finn can verify any condition on the mountain — his Truth Rune toolkit is complete."),
]

# SCIFI – Zara running sensor threshold checks aboard the Helix
l3_scifi = [
    # 0 concept
    ("Zara's ship sensors need calibrating against critical thresholds — she configures them to return simple True or False signals.",
     "All three sensor comparisons return True and the diagnostic board lights up green across the board."),
    # 1 mcq – 7 > 3
    ("Zara checks whether 7 remaining fuel pods exceed the minimum of 3 for safe navigation.",
     "True — fuel pods are above the critical threshold; Zara clears the navigation lock."),
    # 2 fill_blank – shield_level == 10
    ("Zara needs to confirm the shield is at exactly full charge — only one operator tests for equality without overwriting the value.",
     "The sensor confirms full charge; Zara logs it and moves to the next pre-flight check."),
    # 3 mcq – score >= 60
    ("Zara's fuel efficiency score is 60 — she checks whether it meets the minimum safe threshold of 60.",
     "True — efficiency is exactly at threshold; Zara clears the asteroid navigation mode."),
    # 4 arrange – fuel_level != 5
    ("Zara builds a sensor alert that fires True whenever fuel is NOT at the critical warning level of 5.",
     "The alert is armed — it will fire the moment fuel drops to 5, giving Zara time to react."),
    # 5 mcq – 5 < 10
    ("Zara's shield power is 5 and the dense asteroid cluster requires 10 — she checks whether she falls short.",
     "True — she does fall short; Zara diverts power from life support to the shield emitters."),
    # 6 fill_blank – fuel_reading >= 50
    ("Zara needs to verify that her fuel reading meets or exceeds the minimum safe level of 50 before continuing.",
     "The sensor reads True or False immediately; Zara either accelerates or holds position to conserve fuel."),
    # 7 mcq – x == 5 and x != 5
    ("The ship's dual sensor logs the shield reading twice — once checking equality, once checking inequality.",
     "True then False — both readings agree, confirming no sensor drift."),
    # 8 mcq – 'Alice' == 'alice'
    ("Zara verifies a pilot ID code but notices the capitalisation differs between two records.",
     "False — the ID system is case-sensitive; Zara flags the discrepancy for the security officer."),
    # 9 arrange – hull_integrity <= 0
    ("Zara builds a critical alert that fires True when hull integrity reaches zero or below.",
     "The alert is set; if the hull takes enough damage, the alarm will trigger automatically."),
    # 10 mini_code – fuel >= 60
    ("Zara reads a fuel value and must print True if it is 60 or above, False if it is below.",
     "The check runs cleanly — Zara integrates it into the automated pre-launch sequence."),
    # 11 mini_code – a != b
    ("Two sensor readings come in and Zara must print True if they differ, False if they match.",
     "Sensor comparison complete — Zara has a full set of threshold checks and the Helix is ready for the next mission."),
]

# MYSTERY – Cole comparing evidence values to thresholds
l3_mystery = [
    # 0 concept
    ("Cole sets up comparison checks in his analysis system to cross-reference the suspect's timeline against verified facts.",
     "Three comparisons, three True results — Cole leans back and starts building his case with confidence."),
    # 1 mcq – 7 > 3
    ("Cole checks whether 7 corroborating witnesses exceed the 3 needed to confirm a sighting.",
     "True — seven witnesses more than clears the bar; Cole marks the sighting as confirmed."),
    # 2 fill_blank – arrival_time == 10
    ("Cole needs to check whether the suspect's reported arrival matches the 10pm sighting — one operator does this without overwriting the data.",
     "The match is confirmed; Cole circles 10pm on the timeline and draws a line to the suspect's name."),
    # 3 mcq – score >= 60
    ("A credibility score of 60 — Cole checks whether it meets the minimum threshold of 60 for reliable testimony.",
     "True — the witness clears the bar; Cole schedules a formal interview."),
    # 4 arrange – suspect_time != 5
    ("Cole builds a check that returns True whenever the suspect's time does NOT match the 5pm alibi.",
     "The check is set — any deviation from the 5pm claim will be flagged immediately."),
    # 5 mcq – 5 < 10
    ("The suspect's alibi window is 5 minutes but the crime took 10 — Cole checks whether the alibi falls short.",
     "True — the alibi cannot cover the full crime window; Cole notes it as a critical inconsistency."),
    # 6 fill_blank – credibility >= 50
    ("Cole checks whether a witness's credibility score meets or exceeds the reliability threshold of 50.",
     "The system flags reliable witnesses instantly; Cole can now filter testimony in seconds."),
    # 7 mcq – x == 5 and x != 5
    ("Cole's system checks the suspect's timestamp twice — once for equality, once for inequality.",
     "True then False — both comparisons agree; the timestamp is solid and Cole logs it as confirmed."),
    # 8 mcq – 'Alice' == 'alice'
    ("Cole notices two files spell the suspect's name differently — he checks whether they actually match.",
     "False — the case system is case-sensitive; Cole flags it as a possible alias and opens a new lead."),
    # 9 arrange – credibility <= 0
    ("Cole builds a check that fires True when a witness's credibility drops to zero or below.",
     "Zero or below means the testimony is dismissed automatically — Cole's filter is now fully configured."),
    # 10 mini_code – score >= 60
    ("Cole reads a witness credibility score and must print True if it is 60 or above, False if it is below.",
     "The reliability filter runs correctly — Cole feeds it into the evidence-sorting pipeline."),
    # 11 mini_code – a != b
    ("Cole reads two suspect timestamps and must print True if they conflict, False if they match.",
     "Conflict detection is live — Cole's comparison toolkit is complete and the case is finally taking shape."),
]

apply_beats(L3, 'fantasy', l3_fantasy)
apply_beats(L3, 'scifi',   l3_scifi)
apply_beats(L3, 'mystery', l3_mystery)


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 4: Booleans and bool()
# ─────────────────────────────────────────────────────────────────────────────

L4 = os.path.join(os.path.dirname(__file__), '..', 'content', 'units', 'unit_2', 'lesson_4.yaml')

# FANTASY – Finn using the Truth Stone on Frostpeak
l4_fantasy = [
    # 0 concept
    ("Finn finds a Truth Stone at the mountain's base — a crystal that converts any value into a clear True or False signal.",
     "Empty means False, anything real means True — the stone never wavers, and Finn trusts it completely."),
    # 1 mcq – bool(0)
    ("Finn holds the stone against a stamina reading of 0 — he needs to know what it returns.",
     "False — the stone dims; Finn rests at camp before the next attempt."),
    # 2 mcq – bool('hello')
    ("Finn tests a rune tablet with an inscription — will the Truth Stone glow for a non-empty string?",
     "True — the stone pulses; the inscription is real and worth reading."),
    # 3 fill_blank – bool(stamina)
    ("Finn wants to convert his stamina value directly into a True or False signal — he needs the right function.",
     "bool(stamina) returns the answer; Finn now knows at a glance whether he can keep moving."),
    # 4 mcq – bool([])
    ("Finn holds the stone over an empty supply pack — what does it return for an empty list?",
     "False — nothing in the pack; Finn returns to base camp to restock before continuing."),
    # 5 arrange – print(bool(5))
    ("Finn wants to test a potion count of 5 through the Truth Stone — he builds the code to do it.",
     "True — five potions is plenty; the stone glows and Finn heads for the next ledge."),
    # 6 mcq – falsy values
    ("Finn needs to memorise which values the Truth Stone calls False — the stone's rules are strict.",
     "0, empty string, empty list, None — Finn carves the list into his waystone so he never forgets."),
    # 7 fill_blank – bool(torch_count > 0)
    ("Finn wants an explicit True or False signal for whether he has any torches — he wraps the comparison in the right function.",
     "The stone returns True or False cleanly; Finn always knows whether he can light the path ahead."),
    # 8 mcq – bool(0) then bool(-5)
    ("The stone tests two readings: first 0, then -5 — Finn needs to predict both results.",
     "False then True — even negative values are truthy; the stone glows on anything non-zero."),
    # 9 mcq – bool('')
    ("Finn finds a blank rune tablet — what does the Truth Stone say about an empty string?",
     "False — nothing written; Finn sets the blank tablet aside and searches for an inscribed one."),
    # 10 mini_code – bool(n) from input
    ("Finn reads his stamina from a sensor and needs to print its boolean value using bool().",
     "The result prints correctly — Finn's stamina check is now a single line of reliable code."),
    # 11 mini_code – bool(s) from input
    ("Finn reads a rune inscription and needs to print True if it is non-empty, False if the tablet is blank.",
     "The Truth Stone's logic is now encoded in Finn's spellbook — he can test any value on the mountain."),
]

# SCIFI – Zara reading binary sensor signals aboard the Helix
l4_scifi = [
    # 0 concept
    ("Zara reconfigures her ship's sensors to output binary True or False signals — no more ambiguous readings mid-flight.",
     "Zero and empty return False; everything else returns True — the sensors are now unambiguous."),
    # 1 mcq – bool(0)
    ("A fuel reading of 0 comes in — Zara needs to know what bool() returns for it.",
     "False — tanks empty; Zara hits the emergency reserve switch and diverts to the nearest depot."),
    # 2 mcq – bool('hello')
    ("A non-empty transmission arrives — Zara checks whether bool() returns True for a non-empty string.",
     "True — data received; Zara opens the message and reads the incoming coordinates."),
    # 3 fill_blank – bool(shield_level)
    ("Zara wants to convert her shield level directly into a True or False status signal.",
     "The shield status reads True or False instantly — Zara wires it into the bridge display."),
    # 4 mcq – bool([])
    ("The asteroid detection list comes back empty — Zara checks what bool() returns for an empty list.",
     "False — nothing detected; Zara confirms the path ahead is clear and increases speed."),
    # 5 arrange – print(bool(5))
    ("Zara tests a thruster power reading of 5 through the boolean converter — she builds the code.",
     "True — thrusters are live; Zara fires the manoeuvring burn and adjusts heading."),
    # 6 mcq – falsy values
    ("Zara needs to know which values her sensor system treats as offline — she checks the full list of falsy values.",
     "0, empty string, empty list, None — Zara adds all four to the sensor calibration checklist."),
    # 7 fill_blank – bool(ammo_count > 0)
    ("Zara wants an explicit True or False for whether she has any ammo loaded — she wraps the comparison in bool().",
     "The weapons system now outputs a clear status signal; Zara patches it into the combat readiness panel."),
    # 8 mcq – bool(0) then bool(-5)
    ("Two readings come through the sensor — first 0, then -5 — Zara predicts what bool() returns for each.",
     "False then True — a pressure differential of -5 is non-zero and truthy; the sensor flags it."),
    # 9 mcq – bool('')
    ("An empty transmission string arrives — Zara checks what bool() returns for it.",
     "False — no data in the signal; Zara requests a retransmission from the relay buoy."),
    # 10 mini_code – bool(n) from input
    ("Zara reads a shield level and needs to print its boolean value using bool().",
     "The shield status prints correctly — Zara integrates the check into the automated pre-jump checklist."),
    # 11 mini_code – bool(s) from input
    ("Zara reads a transmission signal and needs to print True if it contains data, False if it is empty.",
     "Binary sensor logic is fully operational — the Helix now processes every reading as a clean True or False."),
]

# MYSTERY – Cole classifying evidence as valid or worthless
l4_mystery = [
    # 0 concept
    ("Cole sets up a classification system: every piece of evidence gets converted to True (worth following) or False (dead end).",
     "Zero and blank entries are False, everything else is True — Cole's system is ruthlessly efficient."),
    # 1 mcq – bool(0)
    ("A witness reports 0 sightings — Cole checks what bool() returns for a zero count.",
     "False — nothing to work with; Cole crosses the witness off the list and moves on."),
    # 2 mcq – bool('hello')
    ("A non-empty witness statement comes in — Cole checks whether bool() returns True for it.",
     "True — something was said; Cole logs it and schedules a follow-up interview."),
    # 3 fill_blank – bool(motive_strength)
    ("Cole wants to convert a suspect's motive strength directly into a True or False signal.",
     "The motive classification prints instantly — Cole files it under 'confirmed' or 'none' accordingly."),
    # 4 mcq – bool([])
    ("Cole's evidence list comes back empty from the scene — he checks what bool() returns for an empty list.",
     "False — nothing found; Cole widens the search radius and sends the forensics team back in."),
    # 5 arrange – print(bool(5))
    ("Cole has 5 corroborating witnesses — he runs the count through bool() to confirm it is solid.",
     "True — five witnesses is solid; Cole adds the testimony block to the prosecution file."),
    # 6 mcq – falsy values
    ("Cole needs to know which values his classification system treats as dead ends — the full list of falsy values.",
     "0, empty string, empty list, None — Cole writes them in red at the top of his evidence-review checklist."),
    # 7 fill_blank – bool(alibi_time > 0)
    ("Cole wants an explicit True or False for whether the suspect has any recorded alibi time.",
     "The alibi status is classified immediately — Cole either pursues the lead or marks it closed."),
    # 8 mcq – bool(0) then bool(-5)
    ("Two entries are checked: 0 confirmed sightings, then a -5 minute timeline discrepancy.",
     "False then True — even a negative discrepancy is truthy and worth investigating; Cole flags it."),
    # 9 mcq – bool('')
    ("A witness report arrives with a blank name field — Cole checks what bool() returns for an empty string.",
     "False — anonymous and inadmissible; Cole sets it aside and looks for a signed version."),
    # 10 mini_code – bool(n) from input
    ("Cole reads a suspect's motive score and needs to print True if they have any motive, False if there is none.",
     "The motive check runs cleanly — Cole feeds it into the automated suspect-ranking pipeline."),
    # 11 mini_code – bool(s) from input
    ("Cole reads a witness statement and needs to print True if it is non-empty, False if it is blank.",
     "Every piece of evidence is now classified True or False — Cole's investigation engine is fully operational."),
]

apply_beats(L4, 'fantasy', l4_fantasy)
apply_beats(L4, 'scifi',   l4_scifi)
apply_beats(L4, 'mystery', l4_mystery)


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 5: Logical Operators (and, or, not)
# ─────────────────────────────────────────────────────────────────────────────

L5 = os.path.join(os.path.dirname(__file__), '..', 'content', 'units', 'unit_2', 'lesson_5.yaml')

# FANTASY – Finn using logical conditions to navigate Frostpeak's weather logic
l5_fantasy = [
    # 0 concept
    ("Finn reaches a junction where two conditions must be evaluated together — he needs logical operators to combine Truth Rune checks.",
     "and, or, and not give Finn the power to make complex climb decisions with a single expression."),
    # 1 mcq – True and False
    ("Finn reads two storm flags — both must be clear before he can proceed safely.",
     "False — one flag is set; the route is blocked and Finn waits for the storm to pass."),
    # 2 mcq – True or False
    ("Two trail conditions are checked — the path is safe if either one holds.",
     "True — at least one condition is met; Finn picks the safer trail and continues."),
    # 3 fill_blank – stamina >= 50 and has_rope
    ("Finn can only attempt the summit when both his stamina is high enough AND he has a rope — he needs the right operator.",
     "Both conditions locked in with and; Finn checks his gear and starts the final ascent."),
    # 4 mcq – stamina >= 60 or stamina < 50
    ("Finn checks whether his stamina is outside the healthy range — either too high to be realistic or worryingly low.",
     "True — stamina is below 50; Finn stops at the nearest waystone and drinks a restorative potion."),
    # 5 arrange – altitude > 0 and altitude < 100
    ("Finn builds a condition that confirms he is in the valid climbing window: altitude above zero AND below 100.",
     "Both bounds check out; the safe climbing window is confirmed and Finn's route is clear."),
    # 6 mcq – not (altitude > 10)
    ("Finn flips a danger flag — he wants to know when he is NOT above the storm threshold.",
     "False — he is above 10; the flag stays clear and Finn keeps his pace."),
    # 7 fill_blank – not (altitude >= 0)
    ("Finn marks the trail as unsafe when altitude is NOT in the valid range — he needs the right operator to flip the result.",
     "not flips the flag cleanly; the unsafe marker activates the moment altitude goes out of range."),
    # 8 mcq – True and False / True or False
    ("Finn logs two trail flags and needs to predict what and and or return for each combination.",
     "False then True — and is strict, or is flexible; Finn now knows exactly which gate to use for each decision."),
    # 9 mcq – x >= 1 and x <= 10
    ("Finn needs a single expression that is True only when altitude is between 1 and 10 inclusive.",
     "and is the answer — both bounds must hold; Finn's safe-zone check is now one clean line."),
    # 10 mini_code – hp > 50 and shield == True
    ("Finn reads his hp and shield status and must print True only when both conditions are met.",
     "The combined check works perfectly — Finn's summit gate now requires both stamina and equipment to be in order."),
    # 11 mini_code – age < 13 or age >= 18
    ("Finn reads an age value and must print True if it falls outside the mid-range, False if it is in between.",
     "or captures both extremes in one expression — Finn's logical toolkit is complete and the summit is within reach."),
]

# SCIFI – Zara applying proximity and fuel logic aboard the Helix
l5_scifi = [
    # 0 concept
    ("Zara needs to combine multiple sensor conditions into single go/no-go signals — logical operators will link them together.",
     "and, or, and not give Zara precise control over every flight-safety decision on the Helix."),
    # 1 mcq – True and False
    ("Zara reads two collision flags — both must be clear before she can accelerate.",
     "False — one flag is still set; Zara holds position and waits for the debris to clear."),
    # 2 mcq – True or False
    ("Two navigation sensors are checked — a safe route exists if either one clears.",
     "True — one sensor confirms a clear path; Zara threads the ship through the gap."),
    # 3 fill_blank – fuel >= 20 and clearance
    ("Launch requires both sufficient fuel AND air traffic clearance — Zara links the conditions with the right operator.",
     "Both conditions met with and; Zara fires the main engines and the Helix lifts off."),
    # 4 mcq – fuel >= 60 or fuel < 50
    ("Zara checks whether fuel is outside the normal operating range — either suspiciously full or dangerously low.",
     "True — fuel is below 50; Zara reroutes to the nearest refuelling depot."),
    # 5 arrange – distance > 0 and distance < 100
    ("Zara builds a condition that confirms the target is within the safe flight corridor: distance above zero AND below 100.",
     "Corridor confirmed — Zara locks in the heading and engages the autopilot."),
    # 6 mcq – not (distance > 10)
    ("Zara flips a proximity alert — she wants to know when the target is NOT farther than 10 units away.",
     "False — it is farther than 10; no proximity alert, and Zara relaxes her grip on the controls."),
    # 7 fill_blank – not (distance >= 0)
    ("Zara marks a sector as unsafe when distance is NOT in the valid range — she flips the condition with the right operator.",
     "not reverses the flag; the sector is marked unsafe the instant distance goes out of bounds."),
    # 8 mcq – True and False / True or False
    ("Zara logs two sensor flags and needs to predict what and and or return for each combination.",
     "False then True — and demands both, or accepts either; Zara now wires the correct gate into each system."),
    # 9 mcq – x >= 1 and x <= 10
    ("Zara needs a single expression that returns True only when a sensor reading is between 1 and 10 inclusive.",
     "and enforces both bounds simultaneously — Zara's range checker is now one tight line of code."),
    # 10 mini_code – hp > 50 and shield == True
    ("Zara reads hull integrity and shield status and must print True only when both are within safe limits.",
     "The combined go/no-go check is live — the Helix will only proceed when both systems are green."),
    # 11 mini_code – age < 13 or age >= 18
    ("Zara reads a crew age value and must print True if it falls outside the mid-range, False if it is in the middle.",
     "or captures both ends of the range in one expression — Zara's logical sensor suite is fully operational."),
]

# MYSTERY – Cole evaluating combined conditions in the investigation
l5_mystery = [
    # 0 concept
    ("Cole needs to combine multiple evidence conditions into single verdicts — logical operators will link his comparisons together.",
     "and, or, and not give Cole the precision to evaluate complex alibi and motive combinations in one expression."),
    # 1 mcq – True and False
    ("Cole tests an alibi flag against a motive flag — both must hold for the alibi to stick.",
     "False — one condition fails; the alibi collapses and Cole moves the suspect up the list."),
    # 2 mcq – True or False
    ("Two witness statements are evaluated — the sighting is confirmed if either one checks out.",
     "True — at least one statement holds; Cole marks the sighting as corroborated."),
    # 3 fill_blank – motive_confirmed and alibi_broken
    ("Cole can name a suspect only when motive is confirmed AND the alibi is broken — he links both with the right operator.",
     "Both conditions locked in with and; Cole writes the suspect's name at the top of the board."),
    # 4 mcq – evidence >= 60 or evidence < 50
    ("Cole checks whether an evidence count is outside the expected range — either surprisingly high or suspiciously low.",
     "True — it is below 50; Cole flags the shortage and requests a second sweep of the scene."),
    # 5 arrange – evidence > 0 and evidence < 100
    ("Cole builds a condition that confirms evidence is within a credible range: above zero AND below 100.",
     "Both bounds hold — the evidence count is plausible and Cole logs it as valid."),
    # 6 mcq – not (alibis > 10)
    ("Cole flips an alibi status — he wants to know when the suspect does NOT have more than 10 alibis.",
     "False — they do have more than 10; Cole notes the unusually high alibi count as suspicious in itself."),
    # 7 fill_blank – not (evidence >= 0)
    ("Cole flags a statement as unreliable when it is NOT within the valid evidence range — he flips the condition.",
     "not inverts the flag; any out-of-range entry is automatically marked unreliable."),
    # 8 mcq – True and False / True or False
    ("Cole logs two investigation flags and needs to predict what and and or return for each pair.",
     "False then True — and is strict, or is lenient; Cole knows exactly which gate to apply to each piece of evidence."),
    # 9 mcq – x >= 1 and x <= 10
    ("Cole needs a single expression that returns True only when a suspect score is between 1 and 10 inclusive.",
     "and captures both bounds — Cole's in-range check is now a single clean expression."),
    # 10 mini_code – hp > 50 and shield == True
    ("Cole reads an evidence score and an alibi-broken flag and must print True only when both conditions are met.",
     "The confirmation check runs correctly — Cole only names a suspect when the evidence and the broken alibi both clear the bar."),
    # 11 mini_code – age < 13 or age >= 18
    ("Cole reads a value and must print True if it falls outside the mid-range, False if it is in between.",
     "or handles both extremes in one expression — Cole's logical evidence engine is fully built, and the case is ready for court."),
]

apply_beats(L5, 'fantasy', l5_fantasy)
apply_beats(L5, 'scifi',   l5_scifi)
apply_beats(L5, 'mystery', l5_mystery)

print("\nAll story beats applied for Unit 2.")
