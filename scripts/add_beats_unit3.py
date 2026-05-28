import yaml
import sys
from pathlib import Path

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


# ── LESSON 1 ── if Statements ─────────────────────────────────────────────────

L1 = str(Path(__file__).parent.parent / "content/units/unit_3/lesson_1.yaml")

L1_FANTASY = [
    # 0 concept – threat_level >= 60 → "Draw your sword!"
    (
        "Ranger Kira's bestiary scroll lights up as a creature prowls the tree-line — she must decide whether its threat level warrants drawing steel.",
        "The scroll's rune flares gold: the if block runs and Kira's blade is already in hand as the creature steps into the clearing.",
    ),
    # 1 mcq – creature_age < 13 → "child"
    (
        "Kira spots a small, wide-eyed beast and wonders whether it is young enough to be harmless — only one condition will tell her.",
        "The creature blinks back at her, barely a yearling; the if fires and Kira lowers her bow.",
    ),
    # 2 fill_blank – hp == 0 → "game over"
    (
        "The battle is fierce — Kira needs her alarm rune to trigger the instant her hit points reach exactly zero, not a moment before.",
        "She inscribes the == symbol and the rune locks in place, ready to sound the moment her last point of health drains away.",
    ),
    # 3 arrange – score > 100 → "win"
    (
        "After the skirmish Kira tallies her combat score; the enchanted ledger should only cry 'win' when she has truly surpassed a hundred points.",
        "The ledger's ink rearranges itself into a perfect if statement, and Kira watches the word 'win' shimmer into view above the threshold.",
    ),
    # 4 mcq – beast_size 5, > 10 is False, "done" always runs
    (
        "A compact beast trots past — Kira checks whether it exceeds her 'big' threshold, knowing the patrol log will always note 'done' regardless.",
        "The beast is smaller than the threshold; the if skips, but 'done' appears in her log — the patrol continues undisturbed.",
    ),
    # 5 mcq – creature_name == "Alice" → "Hello, Alice!"
    (
        "A voice from the shadows matches a name in Kira's wanted list — the scroll will greet the creature only if the name matches exactly.",
        "The name checks out; the scroll unfurls a greeting, and Kira steps forward to meet the surprisingly polite creature.",
    ),
    # 6 fill_blank – if rank >= 5 → "unlocked"
    (
        "An enchanted gate bars the way into the ancient zone — Kira needs to start the rank check that will swing it open for her.",
        "She writes the if keyword and the gate shudders, ready to swing open the moment her rank clears the threshold.",
    ),
    # 7 mcq – n % 2 == 0 → "even"
    (
        "Kira counts four pairs of tracks in the mud and suspects the beasts travel in groups — she checks whether the number is even to confirm.",
        "Four divides cleanly by two; 'even' echoes through the forest, and Kira notes the creatures hunt in pairs.",
    ),
    # 8 arrange – health == 0 → "dead"
    (
        "After landing the final blow, Kira needs her combat script to confirm the creature has truly fallen — only health at exactly zero should mark it dead.",
        "The script clicks together and prints 'dead' the instant the creature's health hits zero; Kira can finally catch her breath.",
    ),
    # 9 mcq – if n > 0 checks positivity
    (
        "Kira has learned that only a genuinely positive threat reading calls for action — she must choose the correct condition to test for that.",
        "She picks if n > 0 and marks the lesson in her bestiary: zero or below means no threat worth pursuing.",
    ),
    # 10 mini_code – temperature > 36.5 → "fever"
    (
        "Kira presses her sensor to a captured creature to see whether its body heat signals sickness — she must write the check herself.",
        "The sensor script is ready; any reading above 36.5 will flash 'fever' and Kira will know to keep her distance.",
    ),
    # 11 mini_code – len(password) >= 8 → "strong password"
    (
        "Before making camp, Kira must secure the perimeter with a password long enough to keep intruders out — only eight or more characters will do.",
        "The camp ward hums to life, rejecting short passwords and accepting strong ones; Kira's party can rest safely tonight.",
    ),
]

L1_SCIFI = [
    # 0 concept – hull_integrity >= 60 → "Systems nominal."
    (
        "Engineer Yara pulls up the hull-integrity readout — the ship's alert system needs an if check before it can report status to the bridge.",
        "Hull at 85 clears the threshold; the if block fires and 'Systems nominal.' scrolls across every panel on deck.",
    ),
    # 1 mcq – crew_age < 13 → "child"
    (
        "The passenger manifest flags an unusual entry — Yara needs to verify whether the age value triggers the under-13 condition.",
        "The check confirms it: the passenger is a child, and the system prints the correct flag for the cabin assignment algorithm.",
    ),
    # 2 fill_blank – hull_integrity == 0 → "game over"
    (
        "Yara programs the evacuation alarm to fire only when hull integrity drops to exactly zero — no false triggers, no missed warnings.",
        "The == operator locks in the condition; the alarm will stay silent right up to the last possible moment, then scream.",
    ),
    # 3 arrange – score > 100 → "win"
    (
        "After a successful asteroid-dodge manoeuvre, Voss needs the mission log to record 'win' only when the score genuinely tops 100.",
        "The if block snaps into place; the log will stamp 'win' the moment the score crosses the line.",
    ),
    # 4 mcq – reactor_output 5, > 10 is False, "done" always runs
    (
        "The reactor output is low but the checklist must keep running — Yara traces what prints when the if condition fails.",
        "The if skips the 'big' warning, but 'done' rolls on regardless; the checklist never stalls, even on a quiet reactor day.",
    ),
    # 5 mcq – pilot_name == "Alice" → "Hello, Alice!"
    (
        "The cockpit door scanner matches the pilot's name before granting access — Yara traces what the system prints when it finds a match.",
        "Name verified; the system greets the pilot and the door hisses open, exactly as the if block intended.",
    ),
    # 6 fill_blank – if clearance_level >= 5 → "unlocked"
    (
        "The launch bay is sealed until the crew member's clearance level meets the minimum — Yara needs to open the conditional that will check it.",
        "The if keyword is in place; the bay doors will slide apart the moment clearance_level reaches five.",
    ),
    # 7 mcq – n % 2 == 0 → "even"
    (
        "The symmetry check on the thruster array needs to confirm the thruster count is even before the balancing routine can run.",
        "'even' prints and the balancing routine kicks in — four thrusters aligned, the ship steadies on its heading.",
    ),
    # 8 arrange – health == 0 → "dead"
    (
        "Yara's bio-monitor must flag a crew member's life signs the instant they drop to zero — she assembles the condition now.",
        "The monitor script is assembled; it will trigger the medical alert the moment any reading hits zero.",
    ),
    # 9 mcq – if n > 0 checks positivity
    (
        "A sensor only counts as live when it returns a strictly positive reading — Yara must pick the right condition for the diagnostic.",
        "if n > 0 is confirmed; the diagnostic will skip any dead sensor returning zero or below.",
    ),
    # 10 mini_code – temperature > 36.5 → "fever"
    (
        "Yara's bio-scanner sweeps the crew roster — she must write the check that flags elevated temperatures before the next shift.",
        "The scanner is armed; any crew member above 36.5 will be flagged 'fever' and redirected to the med bay.",
    ),
    # 11 mini_code – len(password) >= 8 → "strong password"
    (
        "The security door to the engine room demands a strong access code — Yara's script must enforce the eight-character minimum.",
        "The door's logic is locked in; short codes bounce off, strong codes slide it open, and the engine room stays secure.",
    ),
]

L1_MYSTERY = [
    # 0 concept – alibi_strength >= 60 → "Alibi holds."
    (
        "Detective Cole has a suspect's alibi on his desk — he needs an if check to decide whether the score is high enough to hold.",
        "Score at 85 clears the bar; the if block runs and Cole marks the alibi credible, moving the suspect to the witness column.",
    ),
    # 1 mcq – suspect_age < 13 → "child"
    (
        "A witness on the list looks suspiciously young — Cole checks whether the age value will trigger the under-13 condition in his notes.",
        "The condition fires; Cole notes the witness is a child and adjusts his interview approach accordingly.",
    ),
    # 2 fill_blank – evidence_count == 0 → "game over"
    (
        "Cole wants his case file to close only when every shred of evidence has been catalogued — the alarm should fire at exactly zero, not before.",
        "The == operator is inked in; the file will stay open until the last piece of evidence is logged.",
    ),
    # 3 arrange – score > 100 → "win"
    (
        "Cole's confidence meter should only flash 'win' when he's gathered enough to close the case definitively — over a hundred points.",
        "The if block is assembled; once his confidence cracks 100 the meter will finally declare the case solved.",
    ),
    # 4 mcq – clue_count 5, > 10 is False, "done" always runs
    (
        "Cole has five clues — not enough to trigger the major-haul alert, but the log still needs to confirm the sweep is 'done'.",
        "The if skips the alert, but 'done' stamps the log; Cole pockets his notebook and moves to the next room.",
    ),
    # 5 mcq – witness_name == "Alice" → "Hello, Alice!"
    (
        "Cole is looking for a specific witness by name — he needs to see what his script prints when the name matches exactly.",
        "The match fires and Cole greets Alice at the door; he knows exactly who he's dealing with.",
    ),
    # 6 fill_blank – if evidence_level >= 5 → "unlocked"
    (
        "The study door will only open once Cole's evidence level is strong enough — he needs to write the check that decides.",
        "The if is in place; once evidence_level hits five the lock yields and Cole steps into the study.",
    ),
    # 7 mcq – n % 2 == 0 → "even"
    (
        "Four fingerprints on the windowsill — Cole suspects they come in pairs, and needs the parity check to confirm.",
        "'even' confirms it: the prints come in pairs, and Cole adds 'two-person entry' to his working theory.",
    ),
    # 8 arrange – health == 0 → "dead"
    (
        "Cole's alibi-health tracker must flag the moment a suspect's alibi crumbles completely to zero — he assembles the condition.",
        "The condition is set; the instant alibi health hits zero, the tracker flags the suspect for arrest.",
    ),
    # 9 mcq – if n > 0 checks positivity
    (
        "Cole only pursues a lead when it shows a positive count — he needs the right condition to filter out dead ends.",
        "if n > 0 is confirmed; Cole will only follow leads that show real, positive weight.",
    ),
    # 10 mini_code – temperature > 36.5 → "fever"
    (
        "A piece of evidence was recently handled — Cole uses a thermometer to check whether the surface temperature indicates recent human contact.",
        "The script is ready; any reading above 36.5 will print 'fever' and Cole will know the evidence was touched recently.",
    ),
    # 11 mini_code – len(password) >= 8 → "strong password"
    (
        "The locked cabinet in the study needs a combination — Cole must write the check that decides whether it's strong enough to have kept the killer out.",
        "The combination check is written; short codes get rejected, and Cole now knows whether the killer had inside knowledge.",
    ),
]

# ── LESSON 2 ── if / else ─────────────────────────────────────────────────────

L2 = str(Path(__file__).parent.parent / "content/units/unit_3/lesson_2.yaml")

L2_FANTASY = [
    # 0 concept – threat_level 45, < 60 → "Hold your ground."
    (
        "Kira faces a new creature and must choose: cast the fire spell or hold her ground — exactly one action is right, never both.",
        "Threat too low for fire; the else branch runs and Kira stands firm, saving her mana for the real fight ahead.",
    ),
    # 1 mcq – beast_size 3, > 5 is False → "small"
    (
        "A tiny creature scurries across the path — Kira traces the if/else to see which label it earns.",
        "3 is not greater than 5; the else fires and the bestiary stamps it 'small' — nothing to worry about.",
    ),
    # 2 arrange – n % 2 == 0 → "even", else "odd"
    (
        "Kira counts the creatures filing out of the burrow — she needs an if/else that decides whether the number is even or odd.",
        "The if/else is assembled; Kira will always get a clear even-or-odd count no matter how many beasts emerge.",
    ),
    # 3 fill_blank – else when bonded is False
    (
        "Kira's familiar-bond spell has two outcomes: welcome her spirit companion if bonded, or ask her to seek one out — she needs the else.",
        "The else branch is in place; unbonded rangers now see the prompt to find their familiar.",
    ),
    # 4 mcq – dragon_heat 100, > 50 → "hot"
    (
        "A dragon looms overhead, heat radiating from its scales — Kira checks which branch fires when the heat reading exceeds 50.",
        "100 is well over 50; the if branch blazes 'hot' and Kira raises her heat-ward before approaching.",
    ),
    # 5 mcq – name == "" → "No name"
    (
        "The bestiary returns an empty name field for an unidentified creature — Kira must trace what the if/else prints in that case.",
        "An empty string is falsy; the else branch runs and the bestiary logs 'No name' until the creature can be identified.",
    ),
    # 6 fill_blank – else → status = "minor"
    (
        "Young rangers below the age of 18 must earn the squire rank before advancing — Kira adds the else branch that assigns it.",
        "The else is written; any ranger under the threshold is now correctly labelled 'minor' in the guild register.",
    ),
    # 7 mcq – n = 0 is falsy → "falsy"
    (
        "Kira's potion count is zero — she traces the if/else on a falsy value to confirm which branch will run.",
        "0 is falsy; the else fires and Kira gets the low-supply warning — time to visit the alchemist.",
    ),
    # 8 arrange – hp > 0 → "alive", else "dead"
    (
        "After a long battle, Kira's script must declare whether the creature still breathes — she assembles the alive/dead if/else.",
        "The if/else is complete; the script will always deliver a verdict, alive or dead, the moment the fight ends.",
    ),
    # 9 mcq – exactly one branch runs
    (
        "A forest crossroads: the trail or the mountain pass — Kira recalls the rule about how many branches an if/else ever takes.",
        "Exactly one; Kira strides confidently down the chosen path, knowing the other route is closed off entirely.",
    ),
    # 10 mini_code – odd/even
    (
        "The ancient crystal hums with a number that will open one of two hidden doors — Kira must write the code that reads it and picks the right door.",
        "The odd/even check is ready; the crystal will always direct Kira to the correct door, never leaving her guessing.",
    ),
    # 11 mini_code – speeding vs ok
    (
        "A creature charges toward camp at alarming speed — Kira writes the script that tells her whether it's exceeding the safe approach limit.",
        "The check is in place; any charge beyond the limit will flag 'speeding' and give Kira time to raise the alarm.",
    ),
]

L2_SCIFI = [
    # 0 concept – hull_integrity 45 → "Abort launch."
    (
        "Voss is at the launch console — hull integrity must clear 60 or the mission is scrubbed; exactly one outcome is possible.",
        "Hull at 45 fails the check; the else branch fires and 'Abort launch.' flashes across every screen on the bridge.",
    ),
    # 1 mcq – crew_count 3, > 5 is False → "small"
    (
        "The head count comes in short — Voss traces the if/else to confirm whether it triggers the small-crew protocol.",
        "3 is less than 5; the else runs and the small-crew alert lights up the mission board.",
    ),
    # 2 arrange – n % 2 == 0 → "even", else "odd"
    (
        "Voss pairs the thrusters for the burn sequence — he builds the if/else that classifies any thruster count as even or odd.",
        "The if/else is assembled; the pairing algorithm can now safely route power no matter what count comes in.",
    ),
    # 3 fill_blank – else when verified is False
    (
        "The airlock only greets verified crew — Voss adds the else that redirects anyone whose badge hasn't been scanned.",
        "The else branch is live; unverified crew now see the re-scan prompt instead of slipping through unchecked.",
    ),
    # 4 mcq – reactor_temp 100, > 50 → "hot"
    (
        "The reactor core temperature spikes — Voss traces the if/else to see which alert fires when the reading hits 100.",
        "100 clears 50 by a wide margin; the if branch triggers 'hot' and Voss calls for a controlled shutdown.",
    ),
    # 5 mcq – name == "" → "No name"
    (
        "The crew registry returns a blank name field for an unregistered access attempt — Voss traces what the if/else prints.",
        "Empty string is falsy; the else runs and 'No name' is logged as a security incident for review.",
    ),
    # 6 fill_blank – else → status = "minor" (cadet)
    (
        "Crew members below the experience threshold need the cadet rank — Voss adds the else that assigns it automatically.",
        "The else is in place; junior crew are now correctly ranked and assigned to the training rotation.",
    ),
    # 7 mcq – n = 0 is falsy → "falsy"
    (
        "Zero fuel cells remain in the reserve tank — Voss traces the if/else on a zero value to confirm the warning fires.",
        "0 is falsy; the else branch triggers and the fuel-critical alert reaches the captain's console.",
    ),
    # 8 arrange – hp > 0 → "alive", else "dead"
    (
        "The bio-monitor must report whether a crew member's life signs are still active — Voss assembles the alive/dead if/else.",
        "The if/else is live; medical will now receive an instant, unambiguous reading the moment any life sign changes.",
    ),
    # 9 mcq – exactly one branch runs
    (
        "The ship faces a fork in the flight corridor — Voss recalls why if/else always commits to exactly one route.",
        "Exactly one; the Helix locks onto the chosen corridor and the other path is sealed off by the flight computer.",
    ),
    # 10 mini_code – odd/even
    (
        "The navigation ping arrives with a sector code — Voss must write the check that classifies it as even or odd for the routing table.",
        "The classifier is ready; every incoming sector code will now be correctly routed without ambiguity.",
    ),
    # 11 mini_code – speeding vs ok
    (
        "An asteroid is closing on the ship — Voss needs the script that tells him whether its speed breaches the safe approach limit.",
        "The check is live; any object exceeding the limit will trigger 'speeding' and auto-engage the deflector array.",
    ),
]

L2_MYSTERY = [
    # 0 concept – alibi_strength 45 → "Alibi rejected."
    (
        "Cole scores the alibi at 45 — it needs to hit 60 to hold, and he knows only one branch of the if/else will run.",
        "45 falls short; the else fires and 'Alibi rejected.' goes into the casebook — the suspect moves up the list.",
    ),
    # 1 mcq – clue_count 3, > 5 is False → "small"
    (
        "Cole counts only three clues from the scene — he traces the if/else to see whether that's enough to trigger the major-haul label.",
        "3 is less than 5; the else runs and Cole notes a slim evidence haul — he'll need to dig deeper.",
    ),
    # 2 arrange – n % 2 == 0 → "even", else "odd"
    (
        "Cole counts the fingerprints on the glass — he builds the if/else that will tell him whether the count is even or odd.",
        "The if/else is assembled; Cole will always get a clean even-or-odd tally from the print scanner.",
    ),
    # 3 fill_blank – else when cleared is False
    (
        "Cleared witnesses get a pass; those still under scrutiny need to answer more questions — Cole adds the else branch.",
        "The else is written; uncleared witnesses now receive the follow-up question prompt automatically.",
    ),
    # 4 mcq – tension_level 100, > 50 → "hot"
    (
        "The interrogation room tension spikes to 100 — Cole traces the if/else to see which label the atmosphere earns.",
        "100 clears 50 by a mile; the if branch prints 'hot' and Cole knows the suspect is close to cracking.",
    ),
    # 5 mcq – name == "" → "No name"
    (
        "An anonymous tip came in with no name attached — Cole traces the if/else to see what the system logs for an empty string.",
        "Empty string is falsy; the else runs and 'No name' is flagged in the tip log — the source remains unknown.",
    ),
    # 6 fill_blank – else → status = "minor"
    (
        "Anyone under 18 in the case file must be tagged as a minor — Cole adds the else branch that sets the status automatically.",
        "The else is in place; minors in the case file are now correctly flagged and routed to the appropriate officer.",
    ),
    # 7 mcq – n = 0 is falsy → "falsy"
    (
        "Zero solid leads left — Cole traces the if/else on a zero value to confirm the dead-end warning will fire.",
        "0 is falsy; the else fires and Cole's instinct is confirmed — time to revisit the first scene.",
    ),
    # 8 arrange – hp > 0 → "alive", else "dead"
    (
        "Cole's alibi tracker must deliver a clear verdict on each suspect — he assembles the alive/dead if/else now.",
        "The if/else is complete; every alibi will receive an unambiguous verdict the moment Cole runs the check.",
    ),
    # 9 mcq – exactly one branch runs
    (
        "The corridor splits: suspect room or witness room — Cole confirms the rule that if/else always takes exactly one path.",
        "Exactly one; Cole strides down the correct corridor, the other door locked behind him by the logic of the if/else.",
    ),
    # 10 mini_code – odd/even
    (
        "A number is scratched into the desk — Cole must write the script that classifies it as odd or even to crack the next clue.",
        "The classifier is ready; the number's parity will unlock the next step of Cole's investigation.",
    ),
    # 11 mini_code – speeding vs ok
    (
        "Cole clocks a fleeing car — he writes the script that decides whether its speed exceeds the legal limit, making it a lead worth chasing.",
        "The check is live; any vehicle over the limit prints 'speeding' and Cole has grounds to call in the pursuit.",
    ),
]

# ── LESSON 3 ── elif Chains ────────────────────────────────────────────────────

L3 = str(Path(__file__).parent.parent / "content/units/unit_3/lesson_3.yaml")

L3_FANTASY = [
    # 0 concept – threat 82 → "Dangerous creature."
    (
        "Kira holds up the Rank Crystal and it pulses with a score of 82 — she needs the elif chain to translate that number into a threat tier.",
        "82 skips 'Legendary' but catches 'Dangerous'; the crystal settles on amber and Kira readies her mid-level defences.",
    ),
    # 1 mcq – beast_size 50, > 25 → "medium"
    (
        "A creature of middling bulk lumbers into view — Kira traces the elif chain to see which size label it earns.",
        "50 clears the 25-threshold but not 100; 'medium' is stamped in the bestiary and Kira adjusts her approach.",
    ),
    # 2 fill_blank – elif creature_speed > 60
    (
        "Kira's speed-response chart has two tiers and needs the keyword that links them — the second check only runs if the first failed.",
        "elif slots in perfectly; Kira's chart now classifies every creature speed without overlapping conditions.",
    ),
    # 3 mcq – dragon_heat 100, == 100 → "at boiling point"
    (
        "The dragon's heat reads exactly 100 — Kira walks through the chain to find which branch that triggers.",
        "> 100 is False, == 100 is True; 'at boiling point' prints and Kira knows the dragon is primed but hasn't unleashed yet.",
    ),
    # 4 arrange – high / mid / low chain
    (
        "Kira needs a three-tier threat scale from high to low — she arranges the full if/elif/else chain herself.",
        "The chain is in place; every threat level will now route to exactly one tier, giving Kira a clear response plan.",
    ),
    # 5 mcq – score 90, first elif is also 90 but first wins
    (
        "The crystal reads 90 twice in the chain — Kira must remember that only the first True branch matters.",
        "First branch wins; 'A' prints once and the elif is skipped — Kira trusts the earliest reading.",
    ),
    # 6 fill_blank – else → status = "critical"
    (
        "Kira's health chain needs a final catch for the most dire cases — she adds the else that marks her as critically wounded.",
        "The else seals the chain; any hp at 25 or below now routes straight to 'critical' status.",
    ),
    # 7 mcq – n = 5, > 5 False, > 3 True → "B"
    (
        "Kira's rank-scale has three labels — she traces what score 5 earns when only the B-tier condition is True.",
        "n > 5 is False, n > 3 is True; 'B' prints and Kira records a solid mid-rank encounter.",
    ),
    # 8 mcq – how many elif branches?
    (
        "Kira wants to add more creature tiers to her bestiary — she checks whether there's a hard limit on elif branches.",
        "As many as she needs; Kira adds three more tiers to the crystal's scale, confident each will be evaluated in order.",
    ),
    # 9 mini_code – grade A/B/C/F
    (
        "The Rank Crystal needs Kira to program its grading logic — she reads a beast score and must print the correct letter grade.",
        "The grading chain is live; every score the crystal reads will now map to exactly one grade and Kira can track her progress.",
    ),
    # 10 mini_code – BMI / mass index
    (
        "Kira's bestiary also classifies creatures by mass index — she builds the elif chain that converts a float reading into a weight category.",
        "The mass-index chain is complete; Kira can now classify any creature with a single scan, from underweight waif to heavy-set brute.",
    ),
]

L3_SCIFI = [
    # 0 concept – hull 82 → "Hull stable."
    (
        "Voss runs the hull status chain — integrity at 82 needs to route to the right tier before he can file the maintenance report.",
        "82 misses 'optimal' but hits 'stable'; 'Hull stable.' prints and Voss schedules a routine patch rather than an emergency repair.",
    ),
    # 1 mcq – reactor_output 50, > 25 → "medium"
    (
        "The reactor readout shows 50 — Voss traces the elif chain to see which output tier that triggers.",
        "50 clears 25 but not 100; 'medium' prints and Voss keeps the reactor on its current setting.",
    ),
    # 2 fill_blank – elif thruster_speed > 60
    (
        "The thruster classification system has two speed tiers — Voss fills in the keyword that connects them in the chain.",
        "elif locks in; the thruster chart now handles any speed input without ambiguity.",
    ),
    # 3 mcq – core_temp 100, == 100 → "at boiling point"
    (
        "The reactor core reads exactly 100 — Voss walks through the chain to find which branch catches that precise value.",
        "> 100 is False, == 100 is True; 'at boiling point' triggers and Voss initiates the controlled cool-down protocol.",
    ),
    # 4 arrange – high / mid / low chain
    (
        "Voss needs a three-level alert system — he assembles the if/elif/else chain that maps any reading to high, mid, or low.",
        "The chain is assembled; every incoming alert will now land in exactly one tier, giving the bridge a clear priority.",
    ),
    # 5 mcq – score 90, first elif also 90 but first wins
    (
        "Two branches in the chain both match score 90 — Voss confirms which one takes priority.",
        "The first True branch wins; 'A' prints once and Voss notes that sensor order matters in the diagnostic chain.",
    ),
    # 6 fill_blank – else → status = "critical"
    (
        "The hull chain needs a final catch for the worst-case scenario — Voss adds the else that labels it 'critical'.",
        "The else is in place; any integrity at 25 or below now triggers the critical-damage protocol automatically.",
    ),
    # 7 mcq – n = 5, > 5 False, > 3 True → "B"
    (
        "The sector alert scale has three tiers — Voss traces which tier a value of 5 earns when the top condition is False.",
        "n > 3 is True; 'B' prints and the sector gets a mid-level alert — not critical, but worth monitoring.",
    ),
    # 8 mcq – how many elif branches?
    (
        "Voss wants to extend the alert chain with more tiers — he checks whether the language imposes a limit on elif.",
        "No limit; Voss adds two more alert tiers to the chain, knowing only the first match will ever fire.",
    ),
    # 9 mini_code – grade A/B/C/F
    (
        "The performance log needs grading logic — Voss programs the elif chain that converts a system-check score into a letter grade.",
        "The grading chain is live; every system-check score will now resolve to a single grade on the mission report.",
    ),
    # 10 mini_code – BMI / med-bay
    (
        "The med-bay scanner needs a body-mass classifier — Voss builds the elif chain that maps a float reading to a health category.",
        "The classifier is deployed; every crew member scanned will now receive an instant, unambiguous health category.",
    ),
]

L3_MYSTERY = [
    # 0 concept – suspicion 82 → "Strong lead."
    (
        "Cole runs his suspicion-scoring chain on the next name in the file — 82 points needs to land in the right tier.",
        "82 misses 'Prime suspect' but hits 'Strong lead'; Cole circles the name and moves it to the active-investigation pile.",
    ),
    # 1 mcq – clue_weight 50, > 25 → "medium"
    (
        "A clue weighs in at 50 on Cole's importance scale — he traces the chain to see which tier it earns.",
        "50 clears 25 but not 100; 'medium' prints and Cole files the clue as supporting evidence, not the smoking gun.",
    ),
    # 2 fill_blank – elif urgency_level > 60
    (
        "Cole's urgency scale has two tiers — he fills in the keyword that chains them so the second only checks when the first fails.",
        "elif is in; Cole's urgency chart now correctly prioritises actions without skipping or double-counting.",
    ),
    # 3 mcq – tension_level 100, == 100 → "at boiling point"
    (
        "The interrogation tension reads exactly 100 — Cole traces the chain to find which branch catches that peak value.",
        "> 100 is False, == 100 is True; 'at boiling point' prints and Cole leans forward — the suspect is about to talk.",
    ),
    # 4 arrange – high / mid / low chain
    (
        "Cole needs a three-tier threat-level scale for his field notes — he assembles the if/elif/else chain from scratch.",
        "The chain is assembled; Cole's field notes will now auto-classify every situation from high to low without ambiguity.",
    ),
    # 5 mcq – score 90, first elif also 90 but first wins
    (
        "Two branches both match score 90 in the evidence chain — Cole confirms which one takes priority in Python.",
        "The first True branch wins; 'A' prints once and Cole learns to always put his strongest criteria first.",
    ),
    # 6 fill_blank – else → status = "critical"
    (
        "Cole's alibi-health chain needs a final net for the most suspicious cases — he adds the else that marks them 'critical'.",
        "The else is sealed in; any alibi at 25 points or below now flags the suspect as critically suspicious.",
    ),
    # 7 mcq – n = 5, > 5 False, > 3 True → "B"
    (
        "Cole's evidence-importance scale has three tiers — he traces which tier a value of 5 earns when the top condition fails.",
        "n > 3 is True; 'B' prints and Cole tags the clue as moderately important — worth keeping, not worth leading with.",
    ),
    # 8 mcq – how many elif branches?
    (
        "Cole wants to add more suspect tiers to his ranking chain — he checks whether elif has a limit.",
        "No limit; Cole adds two more tiers and confidently knows only the first match will direct his next move.",
    ),
    # 9 mini_code – grade A/B/C/F
    (
        "Cole needs his evidence grader to assign a letter tier to each piece — he builds the elif chain that reads a score and prints the grade.",
        "The grader is live; every piece of evidence will now receive a clear A-through-F rating in the casebook.",
    ),
    # 10 mini_code – density index
    (
        "The forensic scanner needs a density-index classifier — Cole programs the elif chain that maps a float reading to a physical category.",
        "The classifier is deployed; every sample the scanner reads will now snap into one of four density categories instantly.",
    ),
]

# ── LESSON 4 ── Conditions with and / or ──────────────────────────────────────

L4 = str(Path(__file__).parent.parent / "content/units/unit_3/lesson_4.yaml")

L4_FANTASY = [
    # 0 concept – threat >= 7 AND has_shield → "Brace for impact!"
    (
        "Kira faces a high-threat creature while her shield is raised — she needs both conditions true at once to decide her stance.",
        "Threat 9 and shield both True; the if fires and Kira braces, combining two pieces of information into one decisive moment.",
    ),
    # 1 mcq – x > 0 AND x < 10 → "in range"
    (
        "A creature is somewhere in the clearing — Kira checks whether it falls within striking range using two boundary conditions joined by and.",
        "Both conditions hold; 'in range' prints and Kira nocks her arrow, confident of the creature's position.",
    ),
    # 2 fill_blank – size >= 13 AND size <= 19 → "juvenile"
    (
        "Kira needs to classify a creature as juvenile only when its size falls within both the lower and upper bounds — she must choose the right connector.",
        "and is chosen; the juvenile tag now requires both boundaries to be satisfied before it appears in the bestiary.",
    ),
    # 3 mcq – threat 45, < 0 or > 100 both False → "valid"
    (
        "Kira checks whether a threat reading of 45 is out of the safe range using an or condition — she traces the result.",
        "Neither branch of the or is True; 'valid' prints and Kira trusts the reading is within normal bounds.",
    ),
    # 4 arrange – name and score >= 50 → "qualified"
    (
        "Kira's combat-registry check must confirm a creature has both a recorded name and a score of at least 50 before marking it qualified.",
        "The if with and is assembled; only creatures meeting both requirements will earn the qualified stamp.",
    ),
    # 5 mcq – storming and no shelter → "stay inside"
    (
        "A storm rages and Kira has no shelter — she evaluates the nested not/and logic to decide whether to venture out.",
        "The compound condition resolves to False; the else fires and Kira stays inside, warm and dry until the storm passes.",
    ),
    # 6 fill_blank – scroll_name AND mana_cost → "cast"
    (
        "The Fireball spell demands both the correct scroll name and exact mana cost — Kira fills in the connector that enforces both.",
        "and is in place; the spell will only cast when both the name and the mana reading match exactly.",
    ),
    # 7 mcq – outside range 1..100 uses or
    (
        "Kira needs the condition that flags a threat level as outside the valid 1-to-100 range — she picks the right logical operator.",
        "n < 1 or n > 100 is correct; Kira now has a reliable out-of-range detector for any reading she receives.",
    ),
    # 8 mcq – hp > 20 AND shield → "safe"
    (
        "Kira checks her hp and shield status simultaneously — she traces the and condition to see whether 'safe' or 'danger' prints.",
        "Both conditions are True; 'safe' prints and Kira pushes forward, confident her combined defences are holding.",
    ),
    # 9 mini_code – score >= 50 AND passed_exam
    (
        "Kira must advance to the next zone only when her combat score and her trial result both confirm she's ready — she writes the combined check.",
        "The and condition is live; Kira will only pass through when both the score and the trial outcome are in her favour.",
    ),
    # 10 mini_code – hour between 9 and 17
    (
        "The enchanted hunting ground is only open during daylight hours — Kira writes the and condition that checks whether the hour falls within the window.",
        "The window check is in place; the gate will stay closed before dawn and after dusk, opening only during the permitted hours.",
    ),
]

L4_SCIFI = [
    # 0 concept – fuel >= 18 AND shields_up → "Launch ready!" / "Abort"
    (
        "Voss needs both fuel and shields in the green before the launch window opens — a single and condition will make or break the countdown.",
        "Fuel is 17, one short; and fails and 'Abort' flashes — Voss calls a hold while the tanks are topped up.",
    ),
    # 1 mcq – x > 0 AND x < 10 → "in range"
    (
        "The fuel gauge reads 5 — Voss checks whether that value falls inside the launch-window range using two boundary conditions.",
        "Both bounds are satisfied; 'in range' confirms the reading is valid and Voss marks the tank as mission-ready.",
    ),
    # 2 fill_blank – age >= 13 AND age <= 19 → "cadet"
    (
        "A crew member must meet both the lower and upper age limits to be classified as a junior cadet — Voss selects the right connector.",
        "and is chosen; the cadet flag now requires both age boundaries to be True before it appears on the crew manifest.",
    ),
    # 3 mcq – hull 45, < 0 or > 100 both False → "valid"
    (
        "Voss checks a hull reading of 45 against the out-of-range or condition — he traces which branch fires.",
        "Neither side of the or is True; 'valid' prints and Voss confirms the sensor data is within acceptable bounds.",
    ),
    # 4 arrange – name and score >= 50 → "qualified"
    (
        "A crew member must have both an ID on file and a readiness score of at least 50 to qualify for the launch team — Voss assembles the check.",
        "The and condition is in place; only crew members meeting both criteria will make the final launch roster.",
    ),
    # 5 mcq – storm and no shelter → "stay inside"
    (
        "A solar storm is raging and the shielding is down — Voss evaluates the compound logic to decide whether to dispatch crew outside.",
        "The compound condition resolves to False; the else fires and Voss keeps all crew inside until the storm passes.",
    ),
    # 6 fill_blank – crew_id AND launch_code → "access"
    (
        "The escape pod requires both a valid crew ID and the correct launch code — Voss fills in the connector that enforces both.",
        "and is in; the pod will only unlock when both the ID and the code match the registry.",
    ),
    # 7 mcq – outside range 1..100 uses or
    (
        "Voss needs the condition that flags a fuel reading as out of the valid range — he selects the right logical operator.",
        "n < 1 or n > 100 is correct; Voss now has a reliable out-of-range guard for every fuel sensor on the ship.",
    ),
    # 8 mcq – hp > 20 AND shield → "safe"
    (
        "Voss checks hull integrity and shield status together — he traces the and condition to see whether 'safe' or 'danger' appears.",
        "Both conditions are True; 'safe' prints and Voss logs the section as structurally sound.",
    ),
    # 9 mini_code – score >= 50 AND passed_exam
    (
        "A crew member must hit both the fitness threshold and pass the clearance check to board the ship — Voss writes the combined condition.",
        "The and condition is armed; only personnel who clear both gates will receive a boarding pass.",
    ),
    # 10 mini_code – hour between 9 and 17
    (
        "The launch window is restricted to specific hours — Voss writes the and condition that confirms the current hour is inside the window.",
        "The window check is live; any launch attempt outside the hours will be blocked automatically by the new condition.",
    ),
]

L4_MYSTERY = [
    # 0 concept – age >= 18 AND has_badge → "Access granted" / "Access denied"
    (
        "Cole needs both age and badge to clear a witness for access — one condition alone isn't enough; both must be true.",
        "Age is 17, just short; the and fails and 'Access denied' prints — Cole sends the witness back for proper clearance.",
    ),
    # 1 mcq – x > 0 AND x < 10 → "in range"
    (
        "A suspect's credibility score is 5 — Cole checks whether it falls within the valid investigation range using two boundary conditions.",
        "Both bounds hold; 'in range' confirms the score is meaningful and Cole adds the suspect to the active list.",
    ),
    # 2 fill_blank – age >= 13 AND age <= 19 → "young adult"
    (
        "Cole must flag a suspect as a young adult only when the age falls within both limits — he picks the connector that enforces both.",
        "and is chosen; the young-adult tag now requires both age conditions to be True before it appears in the case file.",
    ),
    # 3 mcq – score 45, < 0 or > 100 both False → "valid"
    (
        "Cole checks a credibility score of 45 against the out-of-range or condition — he traces which branch fires.",
        "Neither side of the or is True; 'valid' prints and Cole accepts the score as a legitimate data point.",
    ),
    # 4 arrange – name and score >= 50 → "qualified"
    (
        "A suspect qualifies for deeper investigation only when they have an ID and a suspicion score of at least 50 — Cole assembles the check.",
        "The and condition is assembled; only suspects meeting both requirements will be escalated to the formal inquiry.",
    ),
    # 5 mcq – raining and no umbrella → "stay inside"
    (
        "It's raining and Cole has no umbrella — he evaluates the compound not/and logic to decide whether the outdoor stakeout can proceed.",
        "The compound condition resolves to False; the else fires and Cole decides the stakeout waits for dry weather.",
    ),
    # 6 fill_blank – suspect_name AND access_code → "access"
    (
        "The locked room requires both the right name and the correct code — Cole fills in the connector that enforces both at once.",
        "and is in; the room will only open when both the name and the code are a match.",
    ),
    # 7 mcq – outside range 1..100 uses or
    (
        "Cole needs the condition that flags a credibility score as outside the valid range — he selects the right logical operator.",
        "n < 1 or n > 100 is correct; Cole now has a reliable filter for any score that falls outside what the case can use.",
    ),
    # 8 mcq – hp > 20 AND shield → "safe"
    (
        "Cole checks alibi strength and witness support together — he traces the and condition to confirm whether the suspect reads as 'safe' or 'danger'.",
        "Both conditions are True; 'safe' prints and Cole marks the suspect as currently low-priority.",
    ),
    # 9 mini_code – score >= 50 AND passed_exam
    (
        "Cole will only formally charge a suspect when both the evidence score clears 50 and the alibi has been broken — he writes the combined check.",
        "The and condition is ready; only cases where both gates are cleared will generate an arrest warrant.",
    ),
    # 10 mini_code – hour between 9 and 17
    (
        "The interview office is open only between certain hours — Cole writes the and condition that confirms whether he can still get in.",
        "The window check is live; any visit outside the hours will print 'closed' and Cole will have to come back tomorrow.",
    ),
]

# ── LESSON 5 ── Nested if ──────────────────────────────────────────────────────

L5 = str(Path(__file__).parent.parent / "content/units/unit_3/lesson_5.yaml")

L5_FANTASY = [
    # 0 concept – dragon + breath_weapon → "Dodge and roll!"
    (
        "Kira spots a dragon and needs to know two things in sequence: is it a dragon, and does it have its breath weapon ready?",
        "Both layers pass; 'Dodge and roll!' echoes through the glade — nested checks let Kira react to exactly the right combination of facts.",
    ),
    # 1 mcq – x 10, > 5 True, > 8 True → "big"
    (
        "Kira measures a creature in two stages — she traces the nested if to see what label prints when both thresholds are cleared.",
        "Both ifs are True; 'big' prints and Kira gives the creature a wide berth.",
    ),
    # 2 fill_blank – nested if is_hostile inside if in_sight
    (
        "Kira only needs to check hostility once she can actually see the creature — she adds the inner if that runs inside the outer sight check.",
        "The nested if is in place; hostility is now only tested when the creature is visible, avoiding false alarms in the dark.",
    ),
    # 3 mcq – a 3 < 5 True, b 7 > 5 True → "both"
    (
        "Kira reads two creature stats at once — she traces the nested if to confirm what prints when both inner and outer conditions are True.",
        "Both are True; 'both' prints and Kira knows the creature meets the dual threshold for her rarest bestiary entry.",
    ),
    # 4 arrange – nested active → level > 5 → "veteran"
    (
        "Kira needs a veteran label that only appears when the ranger is active and their level clears five — she assembles the nested structure.",
        "The nested if is assembled; 'veteran' will now only print for active rangers who have truly earned the rank.",
    ),
    # 5 mcq – score 70, >= 60 True, >= 90 False → "pass"
    (
        "A creature score of 70 enters the nested check — Kira traces which inner branch fires when the outer passes but the inner top-tier fails.",
        "Outer True, inner False; the inner else runs and 'pass' prints — a solid showing, not an elite one.",
    ),
    # 6 fill_blank – inner else when bow drawn but no arrows
    (
        "Kira has her bow drawn but her quiver is empty — she adds the inner else that handles the no-arrows case inside the outer bow check.",
        "The inner else is in; Kira's script now covers both fire and no-ammo outcomes whenever the bow is drawn.",
    ),
    # 7 mcq – x 3, > 1 True, > 2 True, > 3 False → "mid"
    (
        "Three layers of creature threat — Kira traces the triple-nested if to find which branch ultimately fires for a value of 3.",
        "x > 1 and x > 2 are True, x > 3 is False; the innermost else runs and 'mid' marks the creature at a middle danger level.",
    ),
    # 8 mcq – when to replace nested if with and
    (
        "Kira wonders whether she can simplify a nested if into a single and condition — she recalls the rule for when that's valid.",
        "When both conditions lead to the same action with no inner else; Kira rewrites the simpler cases and keeps nested for the complex ones.",
    ),
    # 9 mini_code – nested role + active
    (
        "Kira must grant camp access only when the ranger's role is 'admin' and they are marked active — she uses nested if to enforce both gates in order.",
        "The nested check is live; only active admins will see 'admin active', keeping the camp roster properly gated.",
    ),
    # 10 mini_code – nested score + bonus → A+ / A / nothing
    (
        "The Rank Crystal awards A+ for an elite score with a rare relic, plain A for elite without it, and nothing for lower scores — Kira programs the nested logic.",
        "The nested if is complete; the crystal now awards precisely the right rating for every combination of score and relic status.",
    ),
]

L5_SCIFI = [
    # 0 concept – captain + verified → "Full launch authority"
    (
        "Voss must clear two gates in sequence: confirm captain rank, then verify identity — only then can the launch authority be granted.",
        "Both layers pass; 'Full launch authority' lights up the console and the countdown can begin.",
    ),
    # 1 mcq – x 10, > 5 True, > 8 True → "big"
    (
        "The hull diagnostic runs two threshold checks in sequence — Voss traces the nested if to see which output a reading of 10 produces.",
        "Both ifs are True; 'big' prints and Voss logs the reading as well above nominal.",
    ),
    # 2 fill_blank – nested if systems_ready inside if crew_aboard
    (
        "Systems should only be checked for readiness once the crew is confirmed aboard — Voss adds the inner if that enforces that order.",
        "The nested if is in place; systems readiness is now only checked after crew presence is confirmed, preventing premature ignition.",
    ),
    # 3 mcq – a 3 < 5 True, b 7 > 5 True → "both"
    (
        "Voss evaluates two flight parameters in a nested check — he traces what prints when both the outer and inner conditions are True.",
        "Both are True; 'both' prints and Voss logs the dual-parameter pass in the pre-flight checklist.",
    ),
    # 4 arrange – nested active → level > 5 → "veteran"
    (
        "The crew ranking system gives the veteran label only to active members whose level exceeds five — Voss assembles the nested condition.",
        "The nested if is assembled; the veteran tag will now only appear for the right combination of active status and experience level.",
    ),
    # 5 mcq – score 70, >= 60 True, >= 90 False → "pass"
    (
        "A hull integrity score of 70 enters the nested rating chain — Voss traces which inner branch fires when the outer passes but the elite tier doesn't.",
        "Outer True, inner False; the inner else runs and 'pass' prints — the hull is acceptable, not outstanding.",
    ),
    # 6 fill_blank – inner else when engines armed but no fuel
    (
        "The engines are armed but the fuel tank is empty — Voss adds the inner else that handles the no-fuel case inside the armed-engines check.",
        "The inner else is in; the script now outputs the correct message whether fuel is present or not, whenever engines are armed.",
    ),
    # 7 mcq – x 3, > 1 True, > 2 True, > 3 False → "mid"
    (
        "Three layers of launch-readiness checks run in sequence — Voss traces the triple-nested if to find which branch fires for a value of 3.",
        "First two ifs pass, the third fails; the innermost else runs and 'mid' marks the system at a moderate readiness level.",
    ),
    # 8 mcq – when to replace nested if with and
    (
        "Voss considers collapsing a nested if into a single and — he recalls the rule that governs when that refactor is safe.",
        "When both conditions must be True for the same action with no inner else; Voss simplifies the checklist entries that qualify.",
    ),
    # 9 mini_code – nested role + active
    (
        "Voss gates the command console: captain rank must be confirmed first, then active status checked inside — he writes the nested if now.",
        "The nested check is live; only active captains will see 'admin active' on the console, keeping the bridge secure.",
    ),
    # 10 mini_code – nested score + bonus → A+ / A / nothing
    (
        "The performance log gives elite crew an A+ with a turbo boost flag, plain A without it, and nothing below the threshold — Voss programs the nested logic.",
        "The nested if is complete; every crew evaluation will now receive exactly the right rating based on both score and boost status.",
    ),
]

L5_MYSTERY = [
    # 0 concept – inspector + cleared → "Full access"
    (
        "Cole must pass two checkpoints in order: confirm inspector rank, then verify clearance — only then does the evidence room open.",
        "Both layers clear; 'Full access' is granted and Cole steps into the evidence room, the nested if keeping lesser ranks out.",
    ),
    # 1 mcq – x 10, > 5 True, > 8 True → "big"
    (
        "Cole runs two layers of suspect-data checks in sequence — he traces the nested if to see which label a value of 10 earns.",
        "Both ifs are True; 'big' prints and Cole marks the data point as high-significance in his notes.",
    ),
    # 2 fill_blank – nested if key_matches inside if drawer_unlocked
    (
        "Cole can only check whether the key matches once the drawer is confirmed unlocked — he adds the inner if that enforces that sequence.",
        "The nested if is in; the key-match test now only runs after the drawer-unlocked check passes, preventing wasted effort.",
    ),
    # 3 mcq – a 3 < 5 True, b 7 > 5 True → "both"
    (
        "Cole examines two pieces of evidence with a nested check — he traces what prints when both the outer and inner conditions are True.",
        "Both are True; 'both' prints and Cole notes that two independent clues point to the same conclusion.",
    ),
    # 4 arrange – nested active → level > 5 → "veteran"
    (
        "Cole's informant database tags veterans only when an informant is active and their reliability level exceeds five — he assembles the nested check.",
        "The nested if is assembled; the veteran tag will only appear for informants who are both active and proven reliable.",
    ),
    # 5 mcq – score 70, >= 60 True, >= 90 False → "pass"
    (
        "A suspect credibility score of 70 enters the nested rating chain — Cole traces which inner branch fires when the outer passes but the elite tier doesn't.",
        "Outer True, inner False; 'pass' prints and Cole marks the suspect as credible enough to keep on the list, not enough to lead it.",
    ),
    # 6 fill_blank – inner else when safe open but documents gone
    (
        "The safe is open but the documents may already be gone — Cole adds the inner else that handles the empty-safe case inside the open-safe check.",
        "The inner else is in; Cole's script now distinguishes between finding evidence and finding an empty safe, both with the safe open.",
    ),
    # 7 mcq – x 3, > 1 True, > 2 True, > 3 False → "mid"
    (
        "Three layers of evidence-quality checks — Cole traces the triple-nested if to find which branch fires for a quality value of 3.",
        "First two ifs pass, the third fails; the innermost else runs and 'mid' grades the evidence at a moderate quality level.",
    ),
    # 8 mcq – when to replace nested if with and
    (
        "Cole wonders when he can simplify a nested if into a single and condition — he recalls the rule that makes the refactor valid.",
        "When both conditions lead to the same single action with no inner else; Cole rewrites the simple cases and keeps nested for the branching ones.",
    ),
    # 9 mini_code – nested role + active
    (
        "Cole gates the case file: inspector rank must be confirmed first, then active clearance checked inside — he writes the nested if now.",
        "The nested check is live; only active inspectors will see 'admin active' in the file, keeping sensitive case data protected.",
    ),
    # 10 mini_code – nested score + bonus → A+ / A / nothing
    (
        "Cole grades evidence: top-tier with a key witness earns A+, top-tier without earns A, and anything below the threshold earns nothing — he programs the nested logic.",
        "The nested if is complete; every piece of evidence will now receive exactly the right grade based on both its score and its witness backing.",
    ),
]

# ── Apply all beats ────────────────────────────────────────────────────────────

apply_beats(L1, 'fantasy', L1_FANTASY)
apply_beats(L1, 'scifi',   L1_SCIFI)
apply_beats(L1, 'mystery', L1_MYSTERY)

apply_beats(L2, 'fantasy', L2_FANTASY)
apply_beats(L2, 'scifi',   L2_SCIFI)
apply_beats(L2, 'mystery', L2_MYSTERY)

apply_beats(L3, 'fantasy', L3_FANTASY)
apply_beats(L3, 'scifi',   L3_SCIFI)
apply_beats(L3, 'mystery', L3_MYSTERY)

apply_beats(L4, 'fantasy', L4_FANTASY)
apply_beats(L4, 'scifi',   L4_SCIFI)
apply_beats(L4, 'mystery', L4_MYSTERY)

apply_beats(L5, 'fantasy', L5_FANTASY)
apply_beats(L5, 'scifi',   L5_SCIFI)
apply_beats(L5, 'mystery', L5_MYSTERY)

print("Done — all Unit 3 story beats applied.")
