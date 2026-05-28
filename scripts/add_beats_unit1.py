"""
add_beats_unit1.py
Adds story_before and story_after fields to every exercise in every world
for Unit 1 lessons 1–5.
"""

import yaml


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


# ---------------------------------------------------------------------------
# LESSON 1 — Variables
# ---------------------------------------------------------------------------

L1 = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units\unit_1\lesson_1.yaml"

apply_beats(L1, 'fantasy', [
    # 0 concept: ingredient = "moonpetal"
    (
        "Elara's master has left a chaotic workshop full of unlabelled ingredient jars — she must label each one so she can brew the right potion.",
        "The first jar is labelled and ready; now Elara needs to read those labels back to make sure they match the recipe.",
    ),
    # 1 mcq: potion = "Starfire Brew"
    (
        "Elara holds up a cauldron with the name 'Starfire Brew' scratched on it — she needs to read what the label actually says.",
        "The label reads correctly; she can trust the variable names to hold exactly what she wrote.",
    ),
    # 2 arrange: store "moonpetal"
    (
        "The 'moonpetal' jar is empty of its name tag — Elara must write the ingredient name onto it before anything else.",
        "The jar is labelled 'moonpetal'; she sets it on the shelf and reaches for the next ingredient.",
    ),
    # 3 fill_blank: score = 100 (potion_strength)
    (
        "Elara needs to record the potion strength value in her notes using the right operator — one wrong symbol and the whole record is useless.",
        "Potion strength is logged at 100; she underlines it and moves on to reading the value back.",
    ),
    # 4 mcq: heat reassigned 10 -> 20
    (
        "The cauldron temperature was set too low; Elara corrects it and needs to know which reading the cauldron will show now.",
        "The cauldron now shows the updated heat value — she confirms variables store the most recent assignment.",
    ),
    # 5 arrange: print potion_strength
    (
        "Elara wrote the potion strength down but now needs to display it on the workshop notice board.",
        "The strength is displayed; the apprentices can now read it from across the room.",
    ),
    # 6 mcq: which line stores correctly
    (
        "A junior apprentice wrote four different lines trying to label an ingredient — Elara must spot the only correct one.",
        "Elara circles the correct line and explains to the apprentice that = stores, it doesn't compare.",
    ),
    # 7 fill_blank: choose valid variable name for "hello"
    (
        "Elara needs to pick a proper label name for a new spell word — only plain words work as label names.",
        "The spell word is safely stored under a sensible label; the workshop ledger is growing.",
    ),
    # 8 mcq: two variables a b printed
    (
        "Elara lines up two ingredient jars labelled differently and reads each one aloud to the apprentices.",
        "Both values appear on separate lines — each print() call reads exactly one jar.",
    ),
    # 9 mini_code: score = 42
    (
        "The master's formula requires a variable called score set to exactly 42 — Elara must write it herself.",
        "score is set and printed; the formula's first requirement is satisfied.",
    ),
    # 10 mini_code: language + year
    (
        "The workshop registry needs both the scripting language name and the year it was created stored and displayed.",
        "Both values are in the registry — the workshop is fully catalogued and ready for the next lesson.",
    ),
])

apply_beats(L1, 'scifi', [
    # 0 concept: system = "life_support"
    (
        "The Helix just lost its index after a power surge — Engineer Yara must re-register each system into a data register before anything can restart.",
        "The life_support register is online; Yara reads it back to the console to confirm it holds the right value.",
    ),
    # 1 mcq: sector = "Alpha-7"
    (
        "Yara stores the damaged sector name in a register — she needs to verify the console will display what she stored, not the register's label.",
        "The console confirms 'Alpha-7' — the register holds the value, not its own name.",
    ),
    # 2 arrange: store "life_support"
    (
        "The life_support register is blank after the surge — Yara must write the system name into it before the restart sequence can begin.",
        "Register written; she moves on to confirming its value is readable from the display panel.",
    ),
    # 3 fill_blank: hull_rating = 100
    (
        "Hull integrity must be logged at 100 before the repair drones are cleared to launch — Yara needs the correct assignment operator.",
        "Hull rating recorded; the drone bay doors are cleared for the repair mission.",
    ),
    # 4 mcq: fuel overwritten 10 -> 20
    (
        "Yara sees two fuel readings in the log — only the latest one matters for the jump calculation.",
        "She confirms the register shows the updated fuel level; overwriting an old reading is by design.",
    ),
    # 5 arrange: print hull_rating
    (
        "The repair drones need to see the hull_rating value on their status screen before they deploy.",
        "The rating is broadcast; the drones acknowledge and head for the hull breach.",
    ),
    # 6 mcq: which stores correctly
    (
        "A trainee engineer submitted four code snippets to store a system name — only one is valid syntax.",
        "Yara flags the correct line and marks the others as logical errors in the training log.",
    ),
    # 7 fill_blank: valid variable name for "hello"
    (
        "The new status-code register needs a proper identifier name — reserved words and numbers won't work.",
        "Register named and populated; it's ready to receive real status codes from the sensors.",
    ),
    # 8 mcq: two variables printed
    (
        "Yara logs two system statuses back-to-back and checks the console output order.",
        "Both statuses appear on separate lines — each print() transmits exactly one register value.",
    ),
    # 9 mini_code: score = 42
    (
        "The calibration protocol requires a register called score initialised to 42 and confirmed on screen.",
        "Calibration register verified; the protocol advances to the next system check.",
    ),
    # 10 mini_code: language + year
    (
        "The ship's historical databank needs two entries — the programming language used on-board and the year it was first deployed.",
        "Both entries are saved and displayed; the databank is updated and the core boot sequence is complete.",
    ),
])

apply_beats(L1, 'mystery', [
    # 0 concept: suspect = "Victor Crane"
    (
        "Detective Cole's evidence board is blank after the break-in at the precinct — he must re-log every suspect and detail from scratch.",
        "Victor Crane is back in the file; Cole reads the name aloud to confirm the entry is correct.",
    ),
    # 1 mcq: location = "Dockside Warehouse"
    (
        "Cole logs the crime scene location — he needs to check the file will display the place name, not the field label.",
        "The file reads 'Dockside Warehouse' — the variable holds the value, not its own tag.",
    ),
    # 2 arrange: store "Victor Crane"
    (
        "The suspect field in Cole's notebook is empty — he has to write Victor Crane's name in before the interview can start.",
        "Name recorded; Cole clips the page and turns to the evidence tally.",
    ),
    # 3 fill_blank: evidence_count = 100
    (
        "Cole must log exactly 100 pieces of evidence using the right operator — using == here would be a rookie mistake.",
        "Evidence count locked in at 100; the tally sheet is signed and filed.",
    ),
    # 4 mcq: suspect_id overwritten 10 -> 20
    (
        "Cole crossed out an old suspect ID and wrote a new one — he needs to confirm which number the file now holds.",
        "The file shows the updated ID — Cole notes that the old value is gone the moment you overwrite it.",
    ),
    # 5 arrange: print evidence_count
    (
        "The lieutenant wants the evidence count read out in the briefing — Cole needs to display it from his notes.",
        "The tally is read aloud; the room goes quiet as the number sinks in.",
    ),
    # 6 mcq: which stores correctly
    (
        "A rookie handed Cole four attempts at logging a clue — only one actually stores the value.",
        "Cole marks the correct line and reminds the rookie that a single equals sign records, a double compares.",
    ),
    # 7 fill_blank: valid variable name for "hello"
    (
        "Cole needs to name a new evidence field — the field name has to be a plain word, no quotes or numbers first.",
        "Field named and filled; the clue is filed under a proper label in the evidence log.",
    ),
    # 8 mcq: two suspects printed
    (
        "Cole reads two suspect entries from the file at the morning briefing — both must appear on separate lines.",
        "Both names are read out in order — each print() statement surfaces exactly one record.",
    ),
    # 9 mini_code: score = 42
    (
        "The case numbering system requires Cole to store an evidence score of 42 and confirm it on the printout.",
        "Score recorded and confirmed; the evidence log is numbered and ready.",
    ),
    # 10 mini_code: language + year
    (
        "The precinct archive needs two entries: the coding language used in the forensic tools and the year those tools were introduced.",
        "Both entries are filed — the archive is updated and the investigation has its digital foundation.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 2 — Numbers and Maths
# ---------------------------------------------------------------------------

L2 = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units\unit_1\lesson_2.yaml"

apply_beats(L2, 'fantasy', [
    # 0 concept: petals + roots = total
    (
        "Elara's recipe calls for precise quantities — she must add the petal count to the root count to know how many ingredients to gather.",
        "The total ingredient count is calculated; she scribbles it at the top of the recipe scroll.",
    ),
    # 1 mcq: petals - spoiled
    (
        "Three moonpetals turned black overnight — Elara needs to subtract the spoiled ones from her total.",
        "Seven good petals remain; she sets the spoiled ones aside and updates her count.",
    ),
    # 2 fill_blank: 4 * 5 (multiply)
    (
        "The master wants double the usual batch — Elara must scale the petal count by the batch multiplier.",
        "The scaled quantity is ready; she measures out twenty petals for the full batch.",
    ),
    # 3 mcq: vial_cost * vials = 48
    (
        "Elara needs to buy four vials from the market — she must calculate the total gold required before she leaves.",
        "Forty-eight gold coins accounted for; she counts them into her purse.",
    ),
    # 4 arrange: 20 / 4
    (
        "Twenty drops of moonwater essence must be divided evenly across four flasks for the ritual.",
        "Five drops per flask confirmed; she fills each one carefully and lines them up.",
    ),
    # 5 mcq: 7 / 2 = 3.5
    (
        "Seven measures of moonwater must be split between two cauldrons — division always gives a decimal here.",
        "Each cauldron gets 3.5 measures; the decimal result is expected when splitting an odd amount.",
    ),
    # 6 fill_blank: total = price + tax
    (
        "Elara needs to add the ingredient tax on top of the base cost to find what she'll actually pay.",
        "Total potion cost calculated; she writes it on the invoice and seals the order.",
    ),
    # 7 mcq: petals = petals + 1 -> 6
    (
        "One extra moonpetal was found at the bottom of the sack — Elara adds it to the running count.",
        "The count updates to six; she tucks the petal into the recipe pile.",
    ),
    # 8 arrange: remaining = 100 - 37
    (
        "The workshop started with 100 doses of potion supply — 37 have been used and Elara needs the remainder.",
        "Sixty-three doses remain; she marks the level on the supply barrel.",
    ),
    # 9 mcq: amplifier * amplifier = 9
    (
        "The magic amplifier grows stronger when multiplied by itself — Elara squares it to find the true potency.",
        "Potency confirmed at 9; she inscribes the value on the amplifier's base.",
    ),
    # 10 mini_code: 3 cauldrons * 8 petals
    (
        "Three cauldrons each need eight moonpetals — Elara must compute the total petal requirement before heading to the herb store.",
        "Twenty-four petals logged; the herb store order is written and ready to send.",
    ),
    # 11 mini_code: budget - spent = remaining
    (
        "The workshop budget is 100 gold and 35 have already been spent — Elara must calculate what's left before ordering more supplies.",
        "Sixty-five gold remaining; the budget is balanced and the supply order is approved.",
    ),
])

apply_beats(L2, 'scifi', [
    # 0 concept: fuel_cells + reserve_cells
    (
        "The Helix lost its fuel tally in the power surge — Yara must add active fuel cells to reserve cells to know total power available.",
        "Total fuel computed and logged to the dashboard; the jump drive pre-check can begin.",
    ),
    # 1 mcq: hull_rating - damage = 7
    (
        "An asteroid collision just knocked three points off hull integrity — Yara subtracts the damage to get the current rating.",
        "Hull integrity reads 7; she flags a repair alert and keeps monitoring.",
    ),
    # 2 fill_blank: 4 * 5 (engine thrust * boost)
    (
        "The engine boost factor must multiply the base thrust to calculate total output before the evasive manoeuvre.",
        "Output calculated at 20 units; the helm is cleared to begin the manoeuvre.",
    ),
    # 3 mcq: shield_draw * shields = 48
    (
        "Four shields are running — Yara must calculate the total power draw to see if the reactor can handle it.",
        "Forty-eight watts total; the reactor is at capacity but holding.",
    ),
    # 4 arrange: 20 / 4
    (
        "Twenty power units must be distributed equally across four decks before the emergency shutdown ends.",
        "Five units per deck confirmed; the distribution relays are set.",
    ),
    # 5 mcq: oxygen / compartments = 3.5
    (
        "Seven oxygen units must be split between two compartments — the result will be a decimal.",
        "Each compartment receives 3.5 units; Yara notes the float result and moves on.",
    ),
    # 6 fill_blank: total = base_power + backup_power
    (
        "Yara needs to combine base power and backup reserves to know total available power for the jump.",
        "Total power calculated; the jump drive is authorised to spin up.",
    ),
    # 7 mcq: crew = crew + 1 -> 6
    (
        "Another survivor was found in the cargo bay — Yara increments the crew count on the life-support manifest.",
        "Crew count updated to 6; the life-support allocation is recalculated.",
    ),
    # 8 arrange: fuel_remaining = 100 - 37
    (
        "The fuel reserves started at 100 units and 37 have been consumed — Yara must log what remains.",
        "Sixty-three units logged as fuel_remaining; the navigation computer updates the jump range estimate.",
    ),
    # 9 mcq: gain * gain = 9
    (
        "The sensor gain squared gives the amplified signal strength — Yara needs that value for the deep-space scan.",
        "Amplified gain confirmed at 9; the deep-space scanner is locked on target.",
    ),
    # 10 mini_code: 3 reactors * 8 power
    (
        "Three reactor cores each produce 8 power units — Yara needs the total output before authorising the weapons array.",
        "Total power output of 24 units confirmed; the weapons array is authorised.",
    ),
    # 11 mini_code: budget - spent
    (
        "The repair budget is 100 credits and 35 have already been spent — Yara must calculate remaining funds before ordering parts.",
        "Sixty-five credits remaining; the parts requisition is approved and the repair crew is dispatched.",
    ),
])

apply_beats(L2, 'mystery', [
    # 0 concept: clues_found + clues_dismissed
    (
        "Cole's evidence tally was wiped when the precinct server crashed — he must recalculate totals from his paper notes.",
        "Valid clue count restored; he writes the total on the top of the case folder.",
    ),
    # 1 mcq: witnesses - discredited = 7
    (
        "Three witnesses have been discredited — Cole strikes them from the list to see how many credible ones remain.",
        "Seven credible witnesses left; Cole circles their names and schedules the interviews.",
    ),
    # 2 fill_blank: 4 * 5 (clues * suspects)
    (
        "Cole must cross-reference every clue against every suspect — he multiplies to find the total number of cross-checks needed.",
        "Twenty cross-references required; he assigns them to his team and starts the clock.",
    ),
    # 3 mcq: ransom_per * suspects = 48
    (
        "Four suspects each demanded the same ransom — Cole calculates the total demand to include in the warrant.",
        "Forty-eight thousand total; the figure goes into the warrant application.",
    ),
    # 4 arrange: 20 / 4
    (
        "Twenty evidence items must be sorted evenly into four case folders before the court deadline.",
        "Five items per folder; the folders are sealed and couriered to the courthouse.",
    ),
    # 5 mcq: coded_pages / analysts = 3.5
    (
        "Seven coded pages must be split between two analysts — the division will yield a decimal result.",
        "Each analyst gets 3.5 pages; the half-page overlap means they'll need to compare notes.",
    ),
    # 6 fill_blank: total = primary_clues + tip_offs
    (
        "Cole needs to add the primary clues to the tip-offs to know how many total leads he's working with.",
        "Total leads tallied; he pins the number to the board and assigns priorities.",
    ),
    # 7 mcq: evidence_count = evidence_count + 1 -> 6
    (
        "Cole finds another piece of evidence while searching the room — he increments the count in his notes.",
        "Evidence count rises to 6; he bags and tags the new item.",
    ),
    # 8 arrange: leads_remaining = 100 - 37
    (
        "Cole started with 100 leads and has eliminated 37 — he needs to record how many are still open.",
        "Sixty-three leads remaining; he highlights the most promising ones for tomorrow's work.",
    ),
    # 9 mcq: cipher_key * cipher_key = 9
    (
        "Squaring the cipher key is the first step in breaking the suspect's code — Cole runs the calculation.",
        "Decoded value is 9; the cipher is cracked and the hidden message can now be read.",
    ),
    # 10 mini_code: 3 suspects * 8 evidence
    (
        "Three suspects are each linked to 8 pieces of evidence — Cole multiplies to get the total evidence count for the case summary.",
        "Twenty-four pieces of evidence logged; the case summary is complete.",
    ),
    # 11 mini_code: budget - spent
    (
        "The investigation budget is 100 and 35 has already been spent — Cole must calculate what's left for the surveillance operation.",
        "Sixty-five remains for surveillance; Cole authorises the stakeout and briefs his team.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 3 — Strings
# ---------------------------------------------------------------------------

L3 = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units\unit_1\lesson_3.yaml"

apply_beats(L3, 'fantasy', [
    # 0 concept: len + upper on incantation
    (
        "Elara discovers an ancient spell scroll but can't cast it until she measures its incantation and shouts it at full power.",
        "The incantation's length is known and its shouted form is ready; the scroll's first secret is unlocked.",
    ),
    # 1 mcq: len("potion") = 6
    (
        "The cauldron recipe requires the ingredient name to be exactly six letters — Elara must count the characters to be sure.",
        "Six characters confirmed; the ingredient name passes the recipe check.",
    ),
    # 2 fill_blank: ingredient.upper()
    (
        "The cauldron log must be written in capital letters so the enchantment can read it — Elara converts the ingredient name.",
        "MOONPETAL is entered in the log; the enchantment flares to confirm the entry.",
    ),
    # 3 mcq: potion.lower() = "starfire"
    (
        "The whisper-spell needs the potion name in lowercase or it will ring too loud in the tower — Elara converts it.",
        "The name is whispered correctly; the sleeping master doesn't stir.",
    ),
    # 4 arrange: len("cat") / len("ash")
    (
        "Elara needs to know the exact character count of the ingredient name 'ash' before she can index the recipe book.",
        "Length confirmed at 3; she opens the recipe book to page three.",
    ),
    # 5 mcq: prefix + " " + suffix = "hello world"
    (
        "Elara must fuse a spell prefix and suffix into one combined word, with a space woven between them.",
        "The fused spell word is ready; the combination has a satisfying resonance.",
    ),
    # 6 fill_blank: "hello" + "world"
    (
        "Two separate potion name fragments must be joined into one label before the jar can be sealed.",
        "The combined label is complete; she presses the seal onto the jar.",
    ),
    # 7 mcq: spell[0] = "P"
    (
        "An ancient index system classifies spells by their first rune — Elara reads the opening character of 'Phoenix'.",
        "First rune is 'P'; the spell is filed under the correct section of the arcane library.",
    ),
    # 8 arrange: print("hello".upper())
    (
        "The ritual requires the spell word 'ember' to be shouted in capital letters — Elara prepares the uppercase call.",
        "EMBER rings through the workshop; the ritual flame responds.",
    ),
    # 9 mcq: ingredient.strip() = "moonpetal"
    (
        "A scanned ingredient name came back with extra parchment-dust spaces on both sides — Elara strips them away.",
        "Clean name recovered; the ingredient is added to the recipe without errors.",
    ),
    # 10 mini_code: name.upper()
    (
        "Elara must store her own ingredient name and shout it in capital letters to activate the workshop's voice-recognition lock.",
        "The lock recognises the uppercase name and clicks open; she steps inside.",
    ),
    # 11 mini_code: greeting + " " + target
    (
        "The greeting scroll must combine 'Hello' and 'World' with a space between them — it's the first charm Elara has to cast herself.",
        "The greeting is cast; 'Hello World' hangs in shimmering letters and the scroll rolls shut.",
    ),
])

apply_beats(L3, 'scifi', [
    # 0 concept: len + upper on transmission
    (
        "An emergency transmission arrived but the comm system needs its exact character count and an all-caps version before routing it.",
        "Length measured and alert-mode version prepared; the transmission is ready to broadcast to all decks.",
    ),
    # 1 mcq: len("online") = 6
    (
        "The diagnostics router checks status codes by length — Yara must confirm 'online' is exactly 6 characters.",
        "Six characters confirmed; the router accepts the code and marks the system green.",
    ),
    # 2 fill_blank: status.upper()
    (
        "An emergency alert must be broadcast in all capitals so it triggers the alarm system correctly.",
        "CRITICAL transmitted; the alarm klaxons sound across the ship.",
    ),
    # 3 mcq: signal.lower() = "warning"
    (
        "The ship has entered quiet-running mode — all alerts must be converted to lowercase to avoid detection.",
        "Signal set to 'warning' in quiet mode; the ship slips past the patrol without triggering sensors.",
    ),
    # 4 arrange: len("err") = 3
    (
        "The error-routing protocol only accepts codes of exactly 3 characters — Yara counts the length of 'err'.",
        "Length confirmed at 3; the error code is accepted and logged.",
    ),
    # 5 mcq: prefix + " " + sector = "hello world"
    (
        "Yara must concatenate the ship prefix and sector name with a space to build the full location identifier.",
        "Full identifier assembled; it's entered into the navigation chart.",
    ),
    # 6 fill_blank: ship + " " + mission
    (
        "The mission identifier must join the ship name and mission code into one string before transmission.",
        "Full mission identifier transmitted; command acknowledges receipt.",
    ),
    # 7 mcq: system_code[0] = "P"
    (
        "The indexing protocol reads the first character of each system code to classify it — Yara checks 'Propulsion'.",
        "First character 'P' confirms propulsion classification; it's filed correctly in the system index.",
    ),
    # 8 arrange: print("mayday".upper())
    (
        "The distress beacon must broadcast 'MAYDAY' in uppercase — Yara constructs the uppercase call.",
        "MAYDAY broadcast on all frequencies; a rescue vessel acknowledges within seconds.",
    ),
    # 9 mcq: reading.strip() = "online"
    (
        "A padded sensor reading came in with extra spaces — Yara strips them before the value can be compared.",
        "Clean reading confirmed as 'online'; the sensor check passes.",
    ),
    # 10 mini_code: name.upper()
    (
        "Yara must store a crew member's name and display it in uppercase for the emergency roll call.",
        "Name appears in uppercase on the roll call board; the crew member is accounted for.",
    ),
    # 11 mini_code: "Hello" + " " + "World"
    (
        "The comms handshake protocol requires a 'Hello World' message joined from two variables to confirm the link.",
        "'Hello World' transmitted; the comms link is verified and the channel is open.",
    ),
])

apply_beats(L3, 'mystery', [
    # 0 concept: len + upper on cipher_note
    (
        "Cole intercepts a cipher note — he must measure its length and convert it to uppercase before he can cross-reference the code book.",
        "Length counted and uppercase version in hand; he opens the code book to the matching page.",
    ),
    # 1 mcq: len("shadow") = 6
    (
        "The alias 'shadow' must be exactly 6 characters to match a pattern in the criminal database — Cole counts to check.",
        "Six characters — it matches the database pattern; the alias is flagged as a known alias.",
    ),
    # 2 fill_blank: alias.upper()
    (
        "The wanted poster printer requires all names in capital letters — Cole converts the alias before submitting.",
        "SHADOW is printed on the wanted poster and circulated to all precincts.",
    ),
    # 3 mcq: cipher_word.lower() = "dagger"
    (
        "The cipher comparison algorithm is case-sensitive — Cole must normalise 'DAGGER' to lowercase before matching.",
        "'dagger' matched in the cipher table; Cole circles the result and moves to the next word.",
    ),
    # 4 arrange: len("key") = 3
    (
        "The code word 'key' is the header for a secret section — Cole counts its characters to find the right page index.",
        "Three characters — Cole flips to page three of the codebook and finds the hidden section.",
    ),
    # 5 mcq: first + " " + last = "hello world"
    (
        "Cole must join a suspect's first and last name with a space for the arrest warrant.",
        "Full name assembled; he writes it on the warrant and sends it to the magistrate.",
    ),
    # 6 fill_blank: location + timestamp
    (
        "Cole must concatenate the crime scene location and the time stamp into one evidence string for the report.",
        "Combined entry filed; the exact time and place of the incident are locked into the record.",
    ),
    # 7 mcq: clue_word[0] = "P"
    (
        "The filing system indexes coded words by their first letter — Cole reads the opening character of 'Phantom'.",
        "Filed under 'P'; the clue joins the growing stack in the Phantom section.",
    ),
    # 8 arrange: print("clue".upper())
    (
        "The forensics printer requires cipher words in uppercase before it will stamp them as verified evidence.",
        "CLUE stamped and verified; the evidence log is updated.",
    ),
    # 9 mcq: note.strip() = "alibi"
    (
        "A scanned note came back with whitespace padding on both sides — Cole strips it before comparing the alibi.",
        "'alibi' recovered cleanly; Cole matches it against the timeline and finds a contradiction.",
    ),
    # 10 mini_code: suspect name .upper()
    (
        "Cole must store the prime suspect's name and print it in uppercase for the evidence board heading.",
        "The name blazes in capitals on the board; the whole team can see who they're after.",
    ),
    # 11 mini_code: "Hello" + " " + "World"
    (
        "The forensic software handshake needs 'Hello World' assembled from two separate variables to prove the system is working.",
        "'Hello World' confirmed on screen; the forensic system is online and ready for analysis.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 4 — f-strings
# ---------------------------------------------------------------------------

L4 = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units\unit_1\lesson_4.yaml"

apply_beats(L4, 'fantasy', [
    # 0 concept: f"Ingredient {ingredient} adds {potion_strength} potency!"
    (
        "Elara needs to inscribe potion labels that include both the ingredient name and its potency — plain strings won't do.",
        "The label reads perfectly with both values woven in; she attaches it to the first vial.",
    ),
    # 1 mcq: f"I am {age} years old"
    (
        "Elara is filling out the apprentice registry scroll and must embed her age directly in the text.",
        "The scroll reads '12 years old' — the number is inscribed exactly where the placeholder was.",
    ),
    # 2 fill_blank: f prefix
    (
        "The greeting scroll has a name placeholder but is missing the magic prefix that brings it to life.",
        "With the 'f' prefix added, the apprentice's name appears on the scroll in shimmering ink.",
    ),
    # 3 mcq: f"{amplifier} times 2 is {amplifier * 2}"
    (
        "The potion label must show both the amplifier value and its doubled output in one inscribed line.",
        "The label reads '7 times 2 is 14' — the expression inside the braces was calculated before inscribing.",
    ),
    # 4 arrange: points = 100; f"Score: {points}"
    (
        "Elara needs to display the potency score of 100 inside the label text using an f-string.",
        "The label reads 'Score: 100' — the value is embedded exactly where the placeholder stood.",
    ),
    # 5 mcq: f"{petals} + {roots} = {petals + roots}"
    (
        "The recipe note must show both ingredient quantities and their combined total in one line.",
        "'3 + 4 = 7' appears on the note — all three placeholders resolved to their correct values.",
    ),
    # 6 fill_blank: f"Welcome to {city}!"
    (
        "The workshop welcome banner needs the location name embedded — only a {placeholder} in an f-string will do.",
        "The banner now reads the workshop name; visitors know exactly where they've arrived.",
    ),
    # 7 mcq: which f-string syntax is correct
    (
        "Four apprentices each wrote a greeting spell — only one used the right f-string syntax.",
        "Elara circles the correct line; the others are crossed out with a note explaining the required braces.",
    ),
    # 8 mcq: f"The {ingredient} costs {cost} gold"
    (
        "The market receipt must name the ingredient and its gold cost in one printed line.",
        "The receipt reads correctly — both the ingredient and the cost are embedded in the message.",
    ),
    # 9 fill_blank: f"HP: {hp} / 100"
    (
        "The health potion display must show the current HP value inside a fixed template string.",
        "'HP: 80 / 100' glows on the display — the potion is labelled and ready to use.",
    ),
    # 10 mini_code: f"Python was created in 1991"
    (
        "The workshop chronicles need a line that names the scripting language and the year it was discovered — all in one f-string.",
        "The chronicle entry is complete; future apprentices will know exactly when Python came to the craft.",
    ),
    # 11 mini_code: f"Hero {hero} is level {level}"
    (
        "Elara must inscribe her hero name and current level on the adventurer's guild board using an f-string.",
        "The inscription is complete — her name and level are recorded for all to see, and the lesson is done.",
    ),
])

apply_beats(L4, 'scifi', [
    # 0 concept: f"System {system} integrity is at {hull_rating} percent!"
    (
        "The status board must display each system's name and integrity reading in a single formatted message.",
        "The status message is composed and broadcast; the crew can read both the system name and its rating at a glance.",
    ),
    # 1 mcq: f"I am {age} years old"
    (
        "Yara is adding a crew member's age to the personnel file using a formatted string.",
        "The file now reads '12 years old' — the integer value was substituted cleanly into the message.",
    ),
    # 2 fill_blank: f prefix
    (
        "The crew greeting template is ready but missing the 'f' prefix that enables variable substitution.",
        "Prefix added; the crew member's name now appears in the greeting transmission.",
    ),
    # 3 mcq: f"{gain} times 2 is {gain * 2}"
    (
        "The diagnostics log must record the sensor gain and its doubled value in one line.",
        "Log reads '7 times 2 is 14' — the expression was evaluated before the message was written.",
    ),
    # 4 arrange: points = 100; f"Score: {points}"
    (
        "The power readout display needs the value 100 embedded inside a formatted status string.",
        "Display reads 'Score: 100' — the power level is visible on the bridge screen.",
    ),
    # 5 mcq: f"{shields} + {engines} = {shields + engines}"
    (
        "The power budget note must show shield draw, engine draw, and their total in one formatted line.",
        "'3 + 4 = 7' confirmed in the log — all three values resolved correctly.",
    ),
    # 6 fill_blank: f"Welcome to {city}!"
    (
        "The navigation briefing message needs the destination sector name embedded with a {placeholder}.",
        "Sector name inserted; the crew reads the destination and plots the course.",
    ),
    # 7 mcq: which f-string syntax is correct
    (
        "Four trainees submitted code to address a crew member by name — only one used correct f-string syntax.",
        "Yara flags the correct snippet and marks the others as malformed format strings in the training record.",
    ),
    # 8 mcq: f"The {component} costs {cost} gold"
    (
        "The parts requisition must log the component name and its cost in one formatted entry.",
        "Requisition entry filed — component and cost are both visible in the record.",
    ),
    # 9 fill_blank: f"HP: {hp} / 100"
    (
        "The ship status display must embed the current hull rating inside a fixed template string.",
        "'HP: 80 / 100' on the status panel — hull integrity is clearly displayed for the bridge crew.",
    ),
    # 10 mini_code: f"Python was created in 1991"
    (
        "The ship's historical databank entry needs the programming language and its creation year formatted in one string.",
        "Databank entry written — the Helix's software history is officially recorded.",
    ),
    # 11 mini_code: f"Hero {hero} is level {level}"
    (
        "The crew skills board needs each member's callsign and rank level formatted into one string.",
        "Callsign and rank recorded on the board; the mission roster is complete and the lesson is done.",
    ),
])

apply_beats(L4, 'mystery', [
    # 0 concept: f"Suspect {suspect} linked to {evidence_count} pieces of evidence!"
    (
        "Cole's case notes need suspect names and evidence counts formatted into one readable line for the court report.",
        "The report line is written — suspect and evidence count appear together exactly as the court requires.",
    ),
    # 1 mcq: f"I am {age} years old"
    (
        "Cole is recording a witness's age in the formatted case file.",
        "The file now reads '12 years old' — the integer dropped cleanly into the statement.",
    ),
    # 2 fill_blank: f prefix
    (
        "The informant's name needs to appear in the report but the format string is missing its activating prefix.",
        "Prefix inserted; the informant's name now shows up in the case note exactly as typed.",
    ),
    # 3 mcq: f"{shift} times 2 is {shift * 2}"
    (
        "Cole must record the cipher shift and its doubled offset in one line of his notes.",
        "'7 times 2 is 14' written in the notebook — the expression evaluated before Cole's pen touched the page.",
    ),
    # 4 arrange: points = 100; f"Score: {points}"
    (
        "The case tally board must display the clue count of 100 inside a formatted summary line.",
        "Tally line reads 'Score: 100' — the clue count is visible on the board.",
    ),
    # 5 mcq: f"{batch_a} + {batch_b} = {batch_a + batch_b}"
    (
        "Cole's notebook must show two clue batches and their combined total in one formatted entry.",
        "'3 + 4 = 7' in the notebook — all three values resolved, the tally is confirmed.",
    ),
    # 6 fill_blank: f"Welcome to {city}!"
    (
        "The incident report header must embed the crime scene location inside the opening line.",
        "Location name appears in the header — the report is properly addressed.",
    ),
    # 7 mcq: which f-string syntax is correct
    (
        "Four rookie officers wrote code to name a suspect in a report — Cole must find the one with correct syntax.",
        "Cole circles the correct line; the rookies learn that {braces} are required inside f-strings.",
    ),
    # 8 mcq: f"The {item} costs {cost} gold"
    (
        "The evidence log must record each stolen item and its monetary value in one formatted line.",
        "Item and value logged — the evidence entry is complete and admissible.",
    ),
    # 9 fill_blank: f"HP: {hp} / 100"
    (
        "The investigation progress display must embed the current clue count inside a fixed-format progress string.",
        "'HP: 80 / 100' on the progress tracker — the investigation's health is clearly visible.",
    ),
    # 10 mini_code: f"Python was created in 1991"
    (
        "The precinct's forensic tool registry needs the language name and creation year in one formatted entry.",
        "Registry entry complete — the forensic tools are officially documented in the case file.",
    ),
    # 11 mini_code: f"Hero {hero} is level {level}"
    (
        "Cole must log his detective name and current rank in the guild of investigators using a formatted string.",
        "Name and rank recorded — Cole's credentials are on file and the lesson is closed.",
    ),
])

# ---------------------------------------------------------------------------
# LESSON 5 — input() and Types
# ---------------------------------------------------------------------------

L5 = r"C:\Users\pyrot\Documents\Coding\python-learner\content\units\unit_1\lesson_5.yaml"

apply_beats(L5, 'fantasy', [
    # 0 concept: ingredient = input(...)
    (
        "Elara's enchanted cauldron can now ask the apprentice directly which ingredient to add — she must make it wait for their answer.",
        "The cauldron pauses, the apprentice types an ingredient name, and the workshop springs to life with the right item.",
    ),
    # 1 mcq: input() always returns str
    (
        "An apprentice typed a number into the potion strength prompt — Elara must know what type she gets back before using it.",
        "It's a string, not a number; Elara knows she'll have to cast it before any arithmetic can happen.",
    ),
    # 2 concept: quantity = int(input(...))
    (
        "The cauldron needs a whole-number quantity of petals — Elara must convert the apprentice's typed text into an integer.",
        "The quantity is now a proper integer; the cauldron can calculate the batch size without error.",
    ),
    # 3 fill_blank: int(text)
    (
        "The batch-size calculator received the quantity as text — Elara must wrap it in int() to make it usable.",
        "Converted successfully; the calculator produces the correct batch total.",
    ),
    # 4 mcq: int("42") + 8 = 50
    (
        "A potion strength of '42' arrived as a string — Elara converts it and adds an 8-point bonus.",
        "Fifty potency points confirmed; the bonus is applied and the potion is upgraded.",
    ),
    # 5 arrange: n = int("15")
    (
        "The dose counter shows '15' as text — Elara must convert it to an integer to store in potion_doses.",
        "Fifteen doses stored as an integer; the batch planner can now divide them across vials.",
    ),
    # 6 mcq: int("7") * 3 = 21
    (
        "A spell intensity string of '7' must be tripled — Elara converts and multiplies.",
        "Twenty-one intensity units calculated; the triple-strength spell is ready to cast.",
    ),
    # 7 fill_blank: float(input(...))
    (
        "Ingredient prices involve copper coins and fractions — Elara needs a decimal conversion for precise cost calculations.",
        "The price is now a float; the cost calculation is precise to the last coin.",
    ),
    # 8 mcq: int(input()) then * 2
    (
        "Elara writes a recipe doubler — it must read a quantity, convert it, then double it for the large-batch potion.",
        "The quantity doubles correctly; the large-batch recipe is calculated without error.",
    ),
    # 9 mcq: str(42) -> len = 2
    (
        "The batch code 42 must be converted to text so Elara can count how many digit characters it contains.",
        "Two digit characters confirmed; the batch code format is validated.",
    ),
    # 10 mini_code: int('25') + 1 = 26
    (
        "The apprentice age string '25' must be converted to an integer and incremented to calculate their age next year.",
        "Twenty-six printed; the registry is updated with the apprentice's upcoming age.",
    ),
    # 11 mini_code: float price, tax
    (
        "The ingredient price '9.99' must be converted to a float so Elara can calculate and print the exact 10% import tax.",
        "Tax of 1.0 calculated and printed; the invoice is complete and the workshop accounts are balanced.",
    ),
])

apply_beats(L5, 'scifi', [
    # 0 concept: crew_name = input(...)
    (
        "The Helix's crew logging terminal needs to accept a name typed by the operator — Yara hooks up input() to the prompt.",
        "The terminal accepts the typed name and welcomes the crew member; the roster updates in real time.",
    ),
    # 1 mcq: input() always returns str
    (
        "A hull integrity reading was entered via keyboard — Yara needs to know what type the system received before doing calculations.",
        "It's a string; Yara knows she must cast it before the repair algorithm can use it.",
    ),
    # 2 concept: crew_count = int(input(...))
    (
        "The life-support system needs a whole-number crew count — Yara must convert the typed text to an integer.",
        "Crew count is now an integer; the life-support allocation formula runs without a type error.",
    ),
    # 3 fill_blank: int(text)
    (
        "The crew count came in as a string from the keyboard — Yara wraps it in int() to make it usable in calculations.",
        "Converted; the life-support requirements are calculated correctly.",
    ),
    # 4 mcq: int("42") + 8 = 50
    (
        "Hull integrity '42' arrived as a string — Yara converts it and adds an 8-point repair bonus.",
        "Fifty integrity units confirmed; the repair bonus is logged and the hull status is updated.",
    ),
    # 5 arrange: n = int("15")
    (
        "The crew roster shows '15' as text — Yara converts it to an integer to store in crew_count.",
        "Fifteen crew members logged as an integer; the headcount is official.",
    ),
    # 6 mcq: int("7") * 3 = 21
    (
        "A thruster power string of '7' must be tripled for the boost calculation — Yara converts and multiplies.",
        "Twenty-one power units for the boost confirmed; the manoeuvre is authorised.",
    ),
    # 7 fill_blank: float(input(...))
    (
        "Fuel costs involve decimal credits — Yara needs float() to capture the precise price before calculating the budget.",
        "Fuel cost stored as a float; the budget calculation is accurate to two decimal places.",
    ),
    # 8 mcq: int(input()) then * 2
    (
        "The power boost subroutine must read a level from the console, convert it, and double it for output.",
        "Doubled power level output correctly; the boost subroutine is cleared for use.",
    ),
    # 9 mcq: str(42) -> len = 2
    (
        "The ship registration code 42 must be converted to a string so Yara can count its digit characters for validation.",
        "Two characters confirmed; the registration code passes format validation.",
    ),
    # 10 mini_code: int('25') + 1 = 26
    (
        "The crew age string '25' must be converted to an integer and incremented to project next year's age for the medical log.",
        "Twenty-six printed; the medical log is updated with the projected age.",
    ),
    # 11 mini_code: float price, tax
    (
        "The fuel price string '9.99' must be converted to a float so Yara can calculate and display the exact 10% fuel tax.",
        "Tax of 1.0 calculated and displayed; the fuel budget is finalised and the jump is approved.",
    ),
])

apply_beats(L5, 'mystery', [
    # 0 concept: witness_name = input(...)
    (
        "Cole needs his interview terminal to pause and accept a witness name from the keyboard before logging it.",
        "The terminal records the name; the witness statement is officially opened.",
    ),
    # 1 mcq: input() always returns str
    (
        "Cole enters a case number via keyboard — he must know what type the system returns before doing any arithmetic on it.",
        "It's a string; Cole knows he'll need to cast it before calculating case reference totals.",
    ),
    # 2 concept: suspect_count = int(input(...))
    (
        "Cole must convert the typed suspect count from text to an integer before the interview schedule can be calculated.",
        "Suspect count is now an integer; the interview planner assigns time slots without error.",
    ),
    # 3 fill_blank: int(text)
    (
        "The suspect count came back as a string from the input — Cole wraps it in int() so the investigation calculator can use it.",
        "Converted; the total interview count is computed correctly.",
    ),
    # 4 mcq: int("42") + 8 = 50
    (
        "A cipher key string of '42' must be converted and offset by 8 to find the decoded value.",
        "Decoded value of 50 confirmed; Cole writes it in the cipher notebook.",
    ),
    # 5 arrange: n = int("15")
    (
        "The clue number '15' is stored as text — Cole must convert it to an integer for the evidence log.",
        "Clue number 15 stored as an integer; it's entered into the evidence tracking system.",
    ),
    # 6 mcq: int("7") * 3 = 21
    (
        "A cipher frequency string of '7' must be tripled to find the decoded transmission frequency.",
        "Twenty-one decoded units; the frequency is matched and the transmission source is identified.",
    ),
    # 7 fill_blank: float(input(...))
    (
        "The ransom amount involves decimal figures — Cole needs float() to capture the precise value for the financial report.",
        "Ransom amount stored as a float; the financial report is accurate to the last cent.",
    ),
    # 8 mcq: int(input()) then * 2
    (
        "The search-team dispatch tool must read a suspect count, convert it, and double it to assign two officers per suspect.",
        "Team count doubled correctly; the dispatch order is sent.",
    ),
    # 9 mcq: str(42) -> len = 2
    (
        "The case reference number 42 must be converted to a string so Cole can count how many digit characters it contains.",
        "Two digit characters confirmed; the reference code format is valid and filed.",
    ),
    # 10 mini_code: int('25') + 1 = 26
    (
        "A witness age of '25' is stored as text — Cole must convert it to an integer and add one to calculate next year's age for the record.",
        "Twenty-six printed; the witness profile is updated in the case file.",
    ),
    # 11 mini_code: float price, tax
    (
        "The ransom string '9.99' thousand must be converted to a float so Cole can calculate and print the exact 10% fee for the recovery agency.",
        "Fee of 1.0 thousand calculated and printed; the recovery agency is briefed and the case is ready for court.",
    ),
])

print("\nAll beats applied successfully.")
