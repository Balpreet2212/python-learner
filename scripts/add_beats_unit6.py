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


# ─────────────────────────────────────────────
# LESSON 1  –  Creating Lists and Indexing
# ─────────────────────────────────────────────
L1 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_6\\lesson_1.yaml"

apply_beats(L1, 'fantasy', [
    # 0 concept
    (
        "Brin's supply crate is a jumbled mess — the wizard insists every expedition item be organised into a proper list before dawn.",
        "Brin marvels at how the crate's contents line up neatly in order, each item reachable by its position.",
    ),
    # 1 mcq
    (
        "The enchanted inventory scroll numbers every slot starting from zero — Brin must learn to read the right position.",
        "Good — Brin knows that the second slot hides at index one, not two.",
    ),
    # 2 fill_blank
    (
        "The wizard needs the very first provision from the crate right away.",
        "Brin hands over the first item without hesitation, knowing index zero always points to the front.",
    ),
    # 3 mcq
    (
        "Before setting off, Brin must count how many supplies have been packed.",
        "The tally is confirmed — Brin's pack holds exactly four items and not one more.",
    ),
    # 4 arrange
    (
        "The expedition roster needs to be written out and the lead hero's name called first.",
        "The heroes list is assembled and the first name rings out — the guild is ready to march.",
    ),
    # 5 mcq
    (
        "Brin must check the weight of the third bundle in the gear list.",
        "The third weight is located — Brin updates the load chart and shoulders the pack.",
    ),
    # 6 fill_blank
    (
        "The wizard asks how many items remain in the supply list before the final count.",
        "Brin recites the total — three supplies accounted for, the crate sealed tight.",
    ),
    # 7 mcq
    (
        "Some essentials are flagged as 'ready' with a True or False mark — Brin checks the first flag.",
        "The first essential reads True, and Brin breathes a sigh of relief — it is packed.",
    ),
    # 8 arrange
    (
        "The treasurer wants a count of how many priced items are in the budget list.",
        "The count is printed — Brin can now tell the guild exactly how many cost entries exist.",
    ),
    # 9 mcq
    (
        "The wizard's apprentice needs a blank container before filling it with new supplies.",
        "An empty crate stands ready — Brin knows square brackets conjure a list from thin air.",
    ),
    # 10 mini_code
    (
        "Brin is charting a star route and must list three planet names, then call out the second stop.",
        "The second planet echoes through the workshop — the route scroll is officially drafted.",
    ),
    # 11 mini_code
    (
        "The final task: pack four expedition supplies into a list, then report the full contents and the total count to the wizard.",
        "The crate is inventoried and sealed — Brin's list is complete and the expedition can begin.",
    ),
])

apply_beats(L1, 'scifi', [
    # 0 concept
    (
        "Navigator Zev's sensor log is overflowing with raw data — Command needs every asteroid ID stored in an ordered list before the next jump.",
        "Zev watches the asteroid IDs slot neatly into position, each one addressable by its index on the scanner grid.",
    ),
    # 1 mcq
    (
        "The onboard computer indexes all sensor readings from zero — Zev needs to pull the correct slot.",
        "Index one confirmed — Zev records the second reading and relays it to the bridge.",
    ),
    # 2 fill_blank
    (
        "Command is requesting the first item in the scan list immediately.",
        "Slot zero retrieved — Zev transmits the lead entry and the bridge logs it instantly.",
    ),
    # 3 mcq
    (
        "Before the next manoeuvre Zev needs a full count of hazard entries on the list.",
        "Four hazards confirmed — Zev files the count and updates the threat assessment.",
    ),
    # 4 arrange
    (
        "The crew roster must be compiled and the first crew member's name broadcast over comms.",
        "The crew list is live and the first name announced — all stations acknowledge.",
    ),
    # 5 mcq
    (
        "A specific hazard rating deep in the list needs to be checked before altering course.",
        "The third rating is retrieved — Zev adjusts the navigation path accordingly.",
    ),
    # 6 fill_blank
    (
        "Command wants to know exactly how many asteroids are currently tracked in the log.",
        "Three asteroids confirmed in the log — Zev's count report is transmitted successfully.",
    ),
    # 7 mcq
    (
        "The sensor status array uses True and False flags — Zev checks whether the first sensor is online.",
        "First sensor reads True — it is active and streaming data to the navigation console.",
    ),
    # 8 arrange
    (
        "Engineering needs a count of fuel cost entries stored in the budget list.",
        "The entry count is printed — Zev passes the fuel summary to the chief engineer.",
    ),
    # 9 mcq
    (
        "Zev needs a fresh, empty list to start a new scan log for the next sector.",
        "An empty log is initialised with square brackets — ready to receive incoming asteroid data.",
    ),
    # 10 mini_code
    (
        "Zev is charting three planets on the star map and must display the second destination.",
        "The second planet is on screen — Zev plots the jump coordinates and awaits confirmation.",
    ),
    # 11 mini_code
    (
        "Final system check: log four asteroid IDs in a list and report both the full list and its length to Command.",
        "Four asteroids logged and count verified — the sensor array is fully operational for the mission.",
    ),
])

apply_beats(L1, 'mystery', [
    # 0 concept
    (
        "Cole's corkboard is chaos — before questioning anyone, every suspect name must be pinned into an ordered list.",
        "Three names line up on the board, each reachable by position — Cole can now navigate the suspect file with precision.",
    ),
    # 1 mcq
    (
        "The case file numbers every entry starting at zero — Cole needs to pull the right index.",
        "Case ID at index one located — Cole underlines it and adds it to the active file.",
    ),
    # 2 fill_blank
    (
        "Cole needs the first clue logged in the evidence list — the one that started this whole case.",
        "The first piece of evidence is in hand — Cole pins it front-and-centre on the board.",
    ),
    # 3 mcq
    (
        "Before the morning briefing, Cole needs a precise count of clues currently pinned.",
        "Four clues counted — Cole updates the whiteboard tally before the chief arrives.",
    ),
    # 4 arrange
    (
        "Cole compiles the suspect list and announces the lead name to the precinct.",
        "The list is assembled and the prime suspect's name is spoken aloud — the investigation has a focus.",
    ),
    # 5 mcq
    (
        "A relevance score buried third in the list may crack the alibi wide open.",
        "Score at index two retrieved — Cole marks it as a key data point in the case notes.",
    ),
    # 6 fill_blank
    (
        "The lieutenant wants a headcount of everyone currently on the suspect board.",
        "Three suspects confirmed — Cole reads the number to the lieutenant without hesitation.",
    ),
    # 7 mcq
    (
        "The alibi log uses True and False — Cole checks whether the first suspect's alibi holds.",
        "Alibi at position zero is True — Cole circles the name and moves to the next lead.",
    ),
    # 8 arrange
    (
        "The evidence locker has ransom amounts logged — Cole needs a count of entries for the DA.",
        "The count is printed — Cole passes the tally to the DA's office for the court filing.",
    ),
    # 9 mcq
    (
        "Cole needs a fresh, empty list to start logging a new round of clues from the witness interview.",
        "An empty evidence list stands ready — Cole picks up the pen and prepares to record.",
    ),
    # 10 mini_code
    (
        "Cole is cross-referencing planets in a smuggling route and needs to display the second stop.",
        "The second planet on the route is identified — Cole marks it on the map and calls for backup.",
    ),
    # 11 mini_code
    (
        "Final board update: record four suspect names in a list and report the full list and count to the chief.",
        "The suspect list is filed and the count confirmed — Cole's board is organised and the case can proceed.",
    ),
])


# ─────────────────────────────────────────────
# LESSON 2  –  Modifying Lists
# ─────────────────────────────────────────────
L2 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_6\\lesson_2.yaml"

apply_beats(L2, 'fantasy', [
    # 0 concept
    (
        "The expedition plan keeps changing — Brin must learn to add, remove, and pull items from the supply list on the fly.",
        "Brin has the three core techniques down: append for loading, remove for discarding, pop for grabbing the last item.",
    ),
    # 1 mcq
    (
        "A new piece of gear just arrived — Brin needs to check how many items the pack holds after adding it.",
        "Four items confirmed after the addition — Brin tightens the straps and heads toward the gate.",
    ),
    # 2 fill_blank
    (
        "One supply on the list turned out to be a duplicate — Brin must drop it by name.",
        "The unwanted item is gone — the list is clean and every remaining supply is needed.",
    ),
    # 3 mcq
    (
        "Brin reaches into the pack and pulls out the last item, checking what it was.",
        "The last supply is retrieved and identified — Brin tucks it aside and notes the pack is shorter by one.",
    ),
    # 4 arrange
    (
        "A potion arrived last minute and must be slipped into the inventory before departure.",
        "The potion is appended and the updated inventory printed — Brin is relieved nothing was forgotten.",
    ),
    # 5 mcq
    (
        "A damaged item needs to be struck from the gear list by name.",
        "The damaged gear is removed — the pack is lighter and every remaining item is serviceable.",
    ),
    # 6 fill_blank
    (
        "Brin wants to pull the last supply from the crate and inspect it before the wizard arrives.",
        "The last item is popped and examined — Brin sets it on the table and awaits the wizard's verdict.",
    ),
    # 7 mcq
    (
        "After loading a new supply and dropping an old one, Brin needs to confirm the final item count.",
        "Three items remain — Brin knows the pack is manageable and the weight balanced.",
    ),
    # 8 mcq
    (
        "The wizard tests Brin with a tricky pop-then-append puzzle to see if the pack truly changes.",
        "Brin sees through the trick — popping then re-appending the same item leaves the pack unchanged.",
    ),
    # 9 mini_code
    (
        "Brin practises a full restock: start with three supplies, add a fourth, drop the first, and show the final pack.",
        "The pack is restocked correctly — Brin presents it to the wizard and earns an approving nod.",
    ),
    # 10 mini_code
    (
        "The wizard sets a final challenge: reduce a five-item stack down to just two by popping, then display what remains.",
        "Only two items remain in the crate — Brin has mastered adding and removing supplies, and the expedition roster is locked in.",
    ),
])

apply_beats(L2, 'scifi', [
    # 0 concept
    (
        "The cargo manifest is never static — Zev must learn to load new units, offload specific items, and retrieve the last cargo in the bay.",
        "Zev now has three essential cargo operations: append to load, remove to offload by ID, pop to unload the last unit.",
    ),
    # 1 mcq
    (
        "A new module just docked — Zev needs to verify the updated item count in the cargo bay.",
        "Four modules confirmed in the bay — Zev clears the docking clamps and updates the manifest.",
    ),
    # 2 fill_blank
    (
        "One cargo item in the manifest is flagged for offloading by ID.",
        "The flagged item is removed — the manifest is clean and the remaining cargo is mission-ready.",
    ),
    # 3 mcq
    (
        "Zev runs an unloading sequence on the last unit in the bay to log what it was.",
        "The last unit is retrieved and logged — the bay shrinks by one and the manifest is updated.",
    ),
    # 4 arrange
    (
        "A last-minute supply needs to be loaded into the inventory before departure clearance.",
        "The supply is appended and the updated manifest confirmed — Zev signals ready for launch.",
    ),
    # 5 mcq
    (
        "One cargo item in the manifest has been recalled — Zev must offload it by name.",
        "The recalled item is removed — the bay is clear of problematic cargo and the mission proceeds.",
    ),
    # 6 fill_blank
    (
        "Zev needs to unload the last cargo unit and record exactly what was retrieved.",
        "The last unit is popped and logged — Zev files the retrieval report with the cargo officer.",
    ),
    # 7 mcq
    (
        "After loading a drill and offloading a probe, Zev checks the bay's final item count.",
        "Three units remain in the bay — Zev confirms the count with the cargo officer and seals the hatch.",
    ),
    # 8 mcq
    (
        "Command tests Zev with a pop-then-reload cycle to see whether the manifest actually changes.",
        "Zev reports back: unloading and immediately reloading the same unit leaves the manifest identical.",
    ),
    # 9 mini_code
    (
        "Zev runs a live manifest update: start with three cargo items, load a fourth, offload the first, and print the result.",
        "The manifest is updated and verified — Zev transmits the final cargo list to Command.",
    ),
    # 10 mini_code
    (
        "Final drill: reduce a five-unit stack to two by popping, then display what remains in the bay.",
        "Two units remain — Zev has mastered cargo operations and the Helix is cleared for departure.",
    ),
])

apply_beats(L2, 'mystery', [
    # 0 concept
    (
        "Fresh leads keep arriving and old ones keep getting debunked — Cole must learn to add new clues, remove dead ends, and retrieve the latest piece of evidence.",
        "Cole has the three board operations locked in: append to log new evidence, remove to clear irrelevant items, pop to pull the last entry.",
    ),
    # 1 mcq
    (
        "A new clue just came in — Cole needs to check the updated evidence count after logging it.",
        "Four clues now on the board — Cole marks the addition and briefs the sergeant.",
    ),
    # 2 fill_blank
    (
        "One entry on the board has been ruled irrelevant — Cole must clear it by name.",
        "The dead-end clue is gone — the board is sharper and every remaining item points toward the truth.",
    ),
    # 3 mcq
    (
        "Cole retrieves the last piece of evidence from the locker to examine it under the lamp.",
        "The last item is pulled and identified — Cole notes it in the case file and the locker holds one less entry.",
    ),
    # 4 arrange
    (
        "A new piece of evidence must be added to the board before the detective's morning briefing.",
        "The evidence is logged and the updated board printed — Cole is ready to present the case.",
    ),
    # 5 mcq
    (
        "A clue that turned out to be planted needs to be struck from the evidence list.",
        "The planted clue is removed — the investigation refocuses on the genuine leads.",
    ),
    # 6 fill_blank
    (
        "Cole reaches into the evidence locker for the last item and records what it is.",
        "The last clue is popped and examined — Cole adds a note to the file and prepares to follow up.",
    ),
    # 7 mcq
    (
        "After logging a witness account and discarding a bad receipt, Cole checks how many items remain.",
        "Three items on the board — Cole knows the case is tightening and the suspect pool is narrowing.",
    ),
    # 8 mcq
    (
        "Cole tests a theory: remove the last clue and immediately re-pin it — does the board change?",
        "The board is unchanged — Cole nods, understanding that pop then append is a net-zero operation.",
    ),
    # 9 mini_code
    (
        "Cole drills the full evidence cycle: start with three items, add a fourth clue, remove the first, and display the board.",
        "The board is updated correctly — Cole photographs it and sends the image to the DA.",
    ),
    # 10 mini_code
    (
        "Final test: whittle a five-item evidence stack down to two by popping, then show what remains.",
        "Two core clues remain — Cole has mastered the evidence locker, and the case file is airtight.",
    ),
])


# ─────────────────────────────────────────────
# LESSON 3  –  Slicing and Searching Lists
# ─────────────────────────────────────────────
L3 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_6\\lesson_3.yaml"

apply_beats(L3, 'fantasy', [
    # 0 concept
    (
        "The supply crate is fully packed — now Brin needs to inspect only certain sections and check whether a specific item is already included.",
        "Brin can now slice any portion of the crate and confirm membership in an instant — no more rummaging through the whole pack.",
    ),
    # 1 mcq
    (
        "The wizard wants to see only the middle section of the gear list, not the whole thing.",
        "The middle slice is revealed — Brin reads out the three items and the wizard makes notes.",
    ),
    # 2 fill_blank
    (
        "Before the first rest stop, Brin inspects only the first three supplies to confirm they are secure.",
        "The leading three items check out — Brin reseals that section and moves on.",
    ),
    # 3 mcq
    (
        "The lantern is supposedly packed — Brin uses the 'in' keyword to verify before leaving the workshop.",
        "True — the lantern is confirmed in the pack, and Brin stops searching by hand.",
    ),
    # 4 arrange
    (
        "The wizard requests the last two supply weights from the load list.",
        "The tail slice is printed — the wizard notes the heaviest items are at the rear of the crate.",
    ),
    # 5 mcq
    (
        "Brin needs to inspect supply weights stored in the middle two slots of the list.",
        "Indices two and three are extracted — Brin checks whether those weights are within the carry limit.",
    ),
    # 6 fill_blank
    (
        "Brin must confirm whether a torch has already been packed before adding another one.",
        "False — no torch is present, so Brin safely adds one without creating a duplicate.",
    ),
    # 7 mcq
    (
        "The wizard asks for the first three entries of the supply count list for a quick audit.",
        "The first three entries are sliced and handed over — the audit begins immediately.",
    ),
    # 8 mcq
    (
        "Brin checks whether two expedition heroes are on the team roster using 'in'.",
        "Bob is on the list and Dave is not — Brin updates the attendance scroll accordingly.",
    ),
    # 9 mini_code
    (
        "Brin packs five supply weights and must slice out only the middle three for the load report.",
        "The middle slice is extracted and handed to the quartermaster — the load report is complete.",
    ),
    # 10 mini_code
    (
        "Final check: build a four-item menu list, verify if 'pizza' is packed, then display the first two items for the cook.",
        "The membership check is done and the first two items noted — Brin's supply search skills are fully forged.",
    ),
])

apply_beats(L3, 'scifi', [
    # 0 concept
    (
        "The asteroid field log is complete — now Zev must scan specific sectors and verify whether a particular rock is already on the map.",
        "Zev can now slice any range of the sensor log and confirm membership in one operation — the navigation console is far more efficient.",
    ),
    # 1 mcq
    (
        "Command wants a mid-range sector report, not the full asteroid log.",
        "The middle sector slice is transmitted — Command acknowledges and marks the region on the chart.",
    ),
    # 2 fill_blank
    (
        "Before the thruster burn, Zev pulls only the first three readings to confirm the path is clear.",
        "The first three readings are clear — Zev authorises the burn and the Helix accelerates.",
    ),
    # 3 mcq
    (
        "Zev needs to verify whether sector 'beta' is already in the mapped field before tasking a probe.",
        "True — beta is confirmed on the map, and Zev redirects the probe to an uncharted sector.",
    ),
    # 4 arrange
    (
        "Navigation needs the last two hazard readings at the tail of the sensor list.",
        "The tail slice is sent — navigation updates the route to avoid the highest-hazard zones.",
    ),
    # 5 mcq
    (
        "Two specific hazard ratings deep in the log need to be pulled for the safety report.",
        "Ratings at indices two and three are extracted — the safety officer files them in the mission log.",
    ),
    # 6 fill_blank
    (
        "Zev must confirm whether asteroid 'X-99' has already been logged before dispatching a new probe.",
        "False — X-99 is not in the log, so Zev queues the probe and adds it to the tracking list.",
    ),
    # 7 mcq
    (
        "The lead scientist requests the first three hazard readings for the pre-mission briefing.",
        "Three readings sliced and transmitted — the briefing starts on schedule.",
    ),
    # 8 mcq
    (
        "Zev checks the crew roster to confirm which team members are aboard and which are not.",
        "Bob is on the roster and Dave is not — Zev updates the manifest and locks the airlock.",
    ),
    # 9 mini_code
    (
        "Zev logs five hazard ratings and must extract only the middle three for the sector report.",
        "The middle-sector slice is filed — the sector report is transmitted and Command approves the flight path.",
    ),
    # 10 mini_code
    (
        "Final drill: build a four-item menu list, check for 'pizza', then display the first two items for the galley log.",
        "The membership check is done and the galley slice is recorded — Zev's search and slice skills are mission-ready.",
    ),
])

apply_beats(L3, 'mystery', [
    # 0 concept
    (
        "The evidence board is full — Cole now needs to narrow in on specific sections of the clue log and confirm whether a particular lead has been recorded.",
        "Cole can slice any portion of the evidence log and check membership instantly — the investigation moves with surgical precision.",
    ),
    # 1 mcq
    (
        "The lieutenant wants only a mid-section overview of the suspect list, not the whole board.",
        "The middle three suspects are extracted and briefed — the lieutenant circles the most likely name.",
    ),
    # 2 fill_blank
    (
        "Cole reviews only the first three pieces of evidence before the morning press conference.",
        "The leading three clues are confirmed solid — Cole presents them to the press with confidence.",
    ),
    # 3 mcq
    (
        "Cole needs to verify whether 'receipt' is already pinned to the board before logging another copy.",
        "True — the receipt is already there, so Cole avoids duplicating it and moves on.",
    ),
    # 4 arrange
    (
        "The DA wants the last two clue scores from the relevance log for the court filing.",
        "The tail slice is handed to the DA — the filing is complete and the case moves to trial.",
    ),
    # 5 mcq
    (
        "Cole extracts two specific relevance scores from the middle of the evidence log.",
        "Scores at indices two and three retrieved — Cole highlights them as the strongest leads in the file.",
    ),
    # 6 fill_blank
    (
        "Cole checks whether the word 'alibi' has already been logged before adding a new entry.",
        "False — it is not in the log, so Cole adds the alibi note and cross-references the timeline.",
    ),
    # 7 mcq
    (
        "The sergeant asks for the first three clue entries in the case file for a quick review.",
        "Three clues sliced and handed over — the sergeant reads them and nods in agreement.",
    ),
    # 8 mcq
    (
        "Cole checks whether two suspects are already on the board using the 'in' operator.",
        "Bob is on the board and Dave is not — Cole updates the suspect registry and closes the gap.",
    ),
    # 9 mini_code
    (
        "Cole records five relevance scores and must pull the middle three for the court summary.",
        "The middle slice is extracted and submitted — the court summary is watertight.",
    ),
    # 10 mini_code
    (
        "Final exercise: build a four-item menu list, check if 'pizza' is present, and display the first two items for the alibi log.",
        "The check is done and the slice is recorded — Cole's slicing and searching skills are case-ready.",
    ),
])


# ─────────────────────────────────────────────
# LESSON 4  –  Looping Over Lists
# ─────────────────────────────────────────────
L4 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_6\\lesson_4.yaml"

apply_beats(L4, 'fantasy', [
    # 0 concept
    (
        "The supply list is organised — but Brin must now walk through every item one by one to calculate the total expedition load.",
        "The running total is complete — Brin knows the exact weight and average load for the journey ahead.",
    ),
    # 1 mcq
    (
        "Elara reads each ingredient aloud from the list so the wizard can record them in the spell tome.",
        "Every ingredient is spoken in turn — the wizard's quill catches them all and the tome is updated.",
    ),
    # 2 fill_blank
    (
        "Elara must add each potion strength value to a running total inside the loop.",
        "The total is accumulated correctly — Elara presents the final strength figure to the master alchemist.",
    ),
    # 3 mcq
    (
        "Elara measures the length of each spell word to ensure none exceed the chant limit.",
        "The character counts are printed in order — Elara marks the overlong words for revision.",
    ),
    # 4 arrange
    (
        "The guild treasurer wants each supply cost printed at double rate for the insurance ledger.",
        "Each doubled price is printed — the treasurer copies them into the ledger without complaint.",
    ),
    # 5 mcq
    (
        "Elara counts how many ingredient weights exceed the threshold of two to filter heavy components.",
        "Three heavy ingredients identified — Elara sets them aside for the high-potency batch.",
    ),
    # 6 fill_blank
    (
        "Elara loops through a roster and must print each adventurer's name in uppercase for the proclamation scroll.",
        "Every name blazes in capitals across the scroll — the proclamation is ready to be read at the gates.",
    ),
    # 7 mcq
    (
        "Elara doubles each potion value and collects the results into a new list for the shop display.",
        "The doubled list is built — Elara pins it to the shop board and the customers take notice.",
    ),
    # 8 mcq
    (
        "Elara stitches together the spell letters one by one to form the incantation word.",
        "The letters are joined — the full incantation is ready and Elara whispers it with confidence.",
    ),
    # 9 mini_code
    (
        "Elara needs to loop through five enchanted numbers and print only those greater than ten.",
        "Only the qualifying values are printed — the spell filter works and the potion is correctly dosed.",
    ),
    # 10 mini_code
    (
        "Final task: loop through four temperature readings and find the highest without using max() — the furnace calibration depends on it.",
        "The peak temperature is found manually — Elara calibrates the furnace and the workshop is ready for the next brew.",
    ),
])

apply_beats(L4, 'scifi', [
    # 0 concept
    (
        "The sensor array has a full list of readings — Zara must now loop through every value to compute the total signal strength.",
        "The total is tallied and the average calculated — Zara files the report and the navigation crew adjusts course.",
    ),
    # 1 mcq
    (
        "Zara transmits each asteroid sector name from the log one by one so they appear on the bridge display.",
        "Every sector name scrolls across the display in sequence — the bridge crew notes them all.",
    ),
    # 2 fill_blank
    (
        "Zara accumulates each sensor reading into a running total inside the loop.",
        "The total is correct — Zara submits the aggregate signal strength to the science officer.",
    ),
    # 3 mcq
    (
        "Zara measures the length of each sector code to verify they all fit the transmission format.",
        "Character counts logged — Zara flags any overlong codes for the comms team to shorten.",
    ),
    # 4 arrange
    (
        "Engineering needs each fuel cost doubled and printed to model emergency rationing.",
        "Every doubled cost is printed — engineering uses the figures to plan the contingency reserves.",
    ),
    # 5 mcq
    (
        "Zara counts how many asteroids have a signal strength above two to prioritise further scanning.",
        "Three high-signal asteroids identified — Zara queues probes toward those targets immediately.",
    ),
    # 6 fill_blank
    (
        "Zara loops through the crew roster and prints each name in uppercase for the official mission log.",
        "Every name is capitalised and logged — the mission roster is formatted and ready for Command.",
    ),
    # 7 mcq
    (
        "Zara doubles each sensor signal and appends the result to a new list for the amplified readings report.",
        "The amplified readings list is ready — Zara transmits it to the science station for analysis.",
    ),
    # 8 mcq
    (
        "Zara concatenates sector codes into a single string for the compressed transmission packet.",
        "The codes are joined into one string — the compressed packet is queued for the next data burst.",
    ),
    # 9 mini_code
    (
        "Zara loops through five signal values and prints only those above ten — weak signals are noise and must be filtered.",
        "Only the strong signals are printed — the noise is gone and the map is cleaner.",
    ),
    # 10 mini_code
    (
        "Final calibration: loop through four temperature readings from the reactor and find the peak value without using max().",
        "The peak reactor temperature is found — Zara adjusts the cooling system and the Helix is fully operational.",
    ),
])

apply_beats(L4, 'mystery', [
    # 0 concept
    (
        "The suspect board is set — Cole must now go through every credibility score one by one to compute the average and identify the strongest leads.",
        "The total and average are in hand — Cole highlights the top-scoring suspects and prepares for interrogation.",
    ),
    # 1 mcq
    (
        "Cole reads each suspect name aloud from the board so the court stenographer can record them.",
        "Every name is spoken in turn — the stenographer types them up and the official record is complete.",
    ),
    # 2 fill_blank
    (
        "Cole adds each clue weight to a running total inside the loop to gauge the overall case strength.",
        "The total clue weight is tallied — Cole knows the case is solid enough to proceed.",
    ),
    # 3 mcq
    (
        "Cole measures the length of each clue phrase to identify verbose statements that may be fabricated.",
        "Character counts logged for each phrase — Cole flags the unusually long ones for closer scrutiny.",
    ),
    # 4 arrange
    (
        "The accountant needs each financial figure doubled and printed to model the laundering amounts.",
        "Every doubled figure is on paper — the accountant forwards them to the financial crimes unit.",
    ),
    # 5 mcq
    (
        "Cole counts how many suspects have a credibility score above two to narrow the active lead pool.",
        "Three high-credibility suspects identified — Cole updates the board and schedules their interviews.",
    ),
    # 6 fill_blank
    (
        "Cole loops through the suspect list and prints each name in uppercase for the formal arrest warrant.",
        "Every name is in capitals on the warrant — the judge signs it and the arrests are authorised.",
    ),
    # 7 mcq
    (
        "Cole doubles each evidence weight and records the adjusted values in a new list for the forensics report.",
        "The doubled weights are compiled — Cole attaches the list to the forensics report and closes the envelope.",
    ),
    # 8 mcq
    (
        "Cole joins each initial from the alibi list into a single string to create a coded identifier.",
        "The initials are stitched together — the identifier matches the monogram on the suspect's briefcase.",
    ),
    # 9 mini_code
    (
        "Cole loops through five clue values and prints only those above ten — low-weight clues are circumstantial and not worth pursuing.",
        "Only the substantial clues are printed — Cole focuses the investigation on the strongest evidence.",
    ),
    # 10 mini_code
    (
        "Final drill: loop through four credibility readings and find the highest without using max() — the top suspect must be identified manually.",
        "The highest score is found — Cole circles the suspect's name and the case moves to its final chapter.",
    ),
])


# ─────────────────────────────────────────────
# LESSON 5  –  List Comprehensions
# ─────────────────────────────────────────────
L5 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_6\\lesson_5.yaml"

apply_beats(L5, 'fantasy', [
    # 0 concept
    (
        "Elara discovers a powerful one-line enchantment that can transform and filter an entire ingredient list in a single incantation.",
        "Squares and even-numbered counts conjured in a breath — Elara realises comprehensions are the most elegant magic she has learned.",
    ),
    # 1 mcq
    (
        "Elara needs every potion strength value doubled in a single spell — no long loops allowed.",
        "All four values are doubled in one line — the master alchemist raises an eyebrow in approval.",
    ),
    # 2 fill_blank
    (
        "Elara must measure the length of each spell word in the grimoire using a comprehension.",
        "The character counts are conjured in a single expression — the grimoire page is annotated in moments.",
    ),
    # 3 mcq
    (
        "The recipe calls for only the odd-numbered ingredient quantities — Elara filters them with a comprehension.",
        "Only the odd counts remain — Elara mixes the correct batch and the cauldron glows the right colour.",
    ),
    # 4 arrange
    (
        "Elara must compute the square of each number from one to five to calibrate the enchantment matrix.",
        "The squares are computed and printed — the enchantment matrix aligns and the chamber hums with power.",
    ),
    # 5 mcq
    (
        "Elara capitalises every ingredient name for the formal spell catalogue in one sweeping enchantment.",
        "Every name blazes in uppercase — the catalogue is formatted and ready for the Grand Archivist.",
    ),
    # 6 fill_blank
    (
        "Only ingredients with a value greater than five are potent enough — Elara filters the list with a comprehension.",
        "The weak ingredients are sifted out — only the potent ones remain and the brew is strengthened.",
    ),
    # 7 mcq
    (
        "Elara counts how many potions in the shop cost less than twenty gold to plan the discount sale.",
        "Three affordable potions identified — Elara marks them for the sale shelf and adjusts the price tags.",
    ),
    # 8 mcq
    (
        "Elara must recognise the long-form loop that is equivalent to a list comprehension — understanding the magic behind the shorthand.",
        "The loop equivalent is matched — Elara understands that the comprehension is simply elegant shorthand for the same spell.",
    ),
    # 9 mini_code
    (
        "Elara needs a list of every multiple of three from one to thirty, conjured in a single comprehension.",
        "All ten multiples appear at once — the ritual circle is complete and the enchantment holds.",
    ),
    # 10 mini_code
    (
        "Final challenge: filter the temperature readings above twenty-five using a comprehension — only the hottest values should fuel the forge.",
        "The high temperatures are extracted in one line — the forge is stoked to perfect intensity and Elara's list mastery is complete.",
    ),
])

apply_beats(L5, 'scifi', [
    # 0 concept
    (
        "Zara discovers that the sensor pipeline can transform and filter entire data arrays in a single line of code — no verbose loops required.",
        "Squared values and even readings produced in one expression — Zara realises comprehensions are the most efficient tool in the data pipeline.",
    ),
    # 1 mcq
    (
        "Zara needs every sensor signal doubled in one compact operation for the amplified scan.",
        "All four signals are doubled in a single line — Command confirms the amplified scan is live.",
    ),
    # 2 fill_blank
    (
        "Zara must compute the length of each sector code in a single pipeline expression.",
        "The code lengths are computed instantly — Zara flags any that exceed the transmission limit.",
    ),
    # 3 mcq
    (
        "Only odd-indexed sensor readings are relevant to the interference filter — Zara extracts them with a comprehension.",
        "The odd readings are isolated — the interference analysis can now proceed with clean data.",
    ),
    # 4 arrange
    (
        "Zara must generate the squared values for numbers one through five to calibrate the sensor gain.",
        "The gain calibration values are printed — the sensor array is tuned and ready for deep-space operation.",
    ),
    # 5 mcq
    (
        "Zara capitalises all sector names in one pass for inclusion in the official mission log.",
        "Every name is uppercased and logged — the mission report is formatted and transmitted to Command.",
    ),
    # 6 fill_blank
    (
        "Only sensor readings above five are strong enough to be meaningful — Zara filters them with a comprehension.",
        "Weak readings are dropped — only high-fidelity data remains and the analysis is far more reliable.",
    ),
    # 7 mcq
    (
        "Zara counts how many asteroids have a mass below twenty to prioritise retrieval missions.",
        "Three lightweight asteroids identified — Zara queues the retrieval drones and updates the mission plan.",
    ),
    # 8 mcq
    (
        "Zara must identify the equivalent for-loop for a comprehension — understanding the underlying engine.",
        "The loop equivalent is matched — Zara confirms the comprehension is just a streamlined version of the same operation.",
    ),
    # 9 mini_code
    (
        "Zara needs a list of all multiples of three from one to thirty generated in a single comprehension for the frequency scan.",
        "All ten multiples are produced at once — the frequency scan completes and the data pipeline is operational.",
    ),
    # 10 mini_code
    (
        "Final mission check: filter the temperature readings above twenty-five with a comprehension — only critical heat signatures matter for the reactor alert.",
        "Critical temperatures extracted in one line — the reactor alert is calibrated and the Helix's data systems are fully mission-ready.",
    ),
])

apply_beats(L5, 'mystery', [
    # 0 concept
    (
        "Cole discovers a one-line technique that can transform and filter an entire witness list in a single statement — far faster than combing through them manually.",
        "Squared scores and even IDs produced in one sweep — Cole realises comprehensions are the sharpest analytical tool he has encountered.",
    ),
    # 1 mcq
    (
        "Cole needs every witness credibility score doubled in one concise statement to model inflated alibis.",
        "All four scores are doubled in a single line — Cole flags the results for the psychological profiler.",
    ),
    # 2 fill_blank
    (
        "Cole must measure the length of each witness statement in one pass to identify unusually brief or long accounts.",
        "Statement lengths computed instantly — Cole circles the outliers and schedules follow-up interviews.",
    ),
    # 3 mcq
    (
        "Only odd-numbered witness IDs fall in the evening shift — Cole filters them with a comprehension.",
        "The odd IDs are isolated — Cole cross-references them with the security log and finds a match.",
    ),
    # 4 arrange
    (
        "Cole needs the squared credibility scores for IDs one through five to rank witness reliability.",
        "The squared scores are printed — Cole pins the rankings to the board and identifies the most credible witness.",
    ),
    # 5 mcq
    (
        "Cole capitalises every suspect name in one operation to format the formal arrest brief.",
        "Every name is uppercased — the arrest brief is formatted and delivered to the district attorney.",
    ),
    # 6 fill_blank
    (
        "Only witness scores above five are reliable enough to use in court — Cole filters them with a comprehension.",
        "Low-reliability witnesses are filtered out — only the credible accounts remain in the court submission.",
    ),
    # 7 mcq
    (
        "Cole counts how many witnesses gave a credibility score below twenty to assess how many are unreliable.",
        "Three low-reliability witnesses identified — Cole notes their names and plans a second round of questioning.",
    ),
    # 8 mcq
    (
        "Cole must match a comprehension to its equivalent loop to understand the full investigative process behind the shorthand.",
        "The loop is correctly identified — Cole knows the comprehension is just a concise expression of the same logical steps.",
    ),
    # 9 mini_code
    (
        "Cole needs a list of all multiples of three from one to thirty to match against a numerical code found at the scene.",
        "All ten multiples are produced in one line — Cole scans the list and finds the matching code immediately.",
    ),
    # 10 mini_code
    (
        "Final deduction: filter the temperature readings above twenty-five with a comprehension — only the hottest moments correspond to the time of the crime.",
        "The critical readings are extracted in a single line — the timeline is confirmed, the case is closed, and Cole reaches for his coat.",
    ),
])

print("All done — Unit 6 story beats applied.")
