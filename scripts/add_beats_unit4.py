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


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 1 — for Loops with range()
# ─────────────────────────────────────────────────────────────────────────────
L1 = "C:/Users/pyrot/Documents/Coding/python-learner/content/units/unit_4/lesson_1.yaml"

apply_beats(L1, "fantasy", [
    # 0 concept
    (
        "Mira's spell-book calls for visiting every herb patch in the meadow — one by one, in order.",
        "The loop visits each patch in turn; now Mira must decide how many patches to cover.",
    ),
    # 1 mcq
    (
        "The apothecary needs exactly three rare herbs — Mira sets the loop to visit just three patches.",
        "Three patches, three herbs — Mira's satchel is filling up; next she must make the loop visit the right number.",
    ),
    # 2 fill_blank
    (
        "Mira reaches for her spell-book: only one incantation can conjure the exact number of patches she needs.",
        "With range() in hand, Mira can summon any count of patches; now she wonders how many trips that really means.",
    ),
    # 3 mcq
    (
        "The master wants seven rare roots — Mira checks how many times her loop will send her into the forest.",
        "Seven trips confirmed; Mira packs her satchel and prepares to arrange the spell in the right order.",
    ),
    # 4 arrange
    (
        "Mira lays out five patch-markers on the workshop floor and must arrange the foraging spell from first to last.",
        "The spell snaps into shape, visiting patches 0 through 4; Mira notices she can also tally what she collects.",
    ),
    # 5 mcq
    (
        "After each patch Mira drops the herb number into her satchel total — she wants to know the final haul.",
        "A sum of six — Mira sees how accumulation works; now she wants to measure each patch by doubling its number.",
    ),
    # 6 fill_blank
    (
        "Each patch yields twice as many leaves as its patch number — Mira needs the right operator in her spell.",
        "Multiplication slots into place, doubling every patch number; Mira realises she can also skip patch zero.",
    ),
    # 7 mcq
    (
        "Patch zero holds only mud — Mira adjusts the spell to begin at patch one instead.",
        "Starting from patch one feels cleaner; Mira now wants to arrange the full route from patch one to five.",
    ),
    # 8 arrange
    (
        "Mira traces patches 1 through 5 on the map and must build the loop that walks that exact route.",
        "The route is set; Mira realises she can also multiply each patch's value to measure total potency.",
    ),
    # 9 mcq
    (
        "For a powerful tincture Mira must multiply the potency of each patch together — the loop does the work.",
        "Twenty-four total potency — the tincture is ready; Mira's final task is to print batch sizes in threes.",
    ),
    # 10 mini_code
    (
        "The master orders herbs in batches of three — Mira must loop through the first five multiples to know each batch size.",
        "Five neat multiples of three roll off the quill; Mira's last errand is tallying every patch from one to ten.",
    ),
    # 11 mini_code
    (
        "After the harvest Mira wants one grand total — the sum of every patch number from one to ten.",
        "Fifty-five herbs tallied — the master nods in approval, and Mira's foraging loop is complete.",
    ),
])

apply_beats(L1, "scifi", [
    # 0 concept
    (
        "Yara's diagnostic protocol must sweep every sector in the grid — the probe visits each one in sequence.",
        "Sectors 0 through 4 are logged; Yara now needs to calibrate the probe for a shorter sweep.",
    ),
    # 1 mcq
    (
        "Command requests a three-sector emergency scan — Yara configures the loop before launching.",
        "Three sector IDs confirmed on the console; Yara adjusts the probe count for the next assignment.",
    ),
    # 2 fill_blank
    (
        "Only one built-in function can generate the sector sequence Yara needs for the probe.",
        "range() locks in the sequence; Yara checks how many full passes the probe will complete.",
    ),
    # 3 mcq
    (
        "The Helix command deck is asking for a seven-sector sweep — Yara verifies the loop count before launch.",
        "Seven passes logged; Yara is ready to arrange the scan instructions in the correct transmission order.",
    ),
    # 4 arrange
    (
        "Yara must sequence the five-sector scan command correctly before uploading it to the probe.",
        "The command sequence is transmitted; Yara now wants to accumulate the total star count across sectors.",
    ),
    # 5 mcq
    (
        "Yara sums star readings sector by sector to compile the mission report.",
        "Total of six stars logged; now Yara wants to record signal strength by doubling each sector ID.",
    ),
    # 6 fill_blank
    (
        "Signal strength doubles per sector — Yara selects the right operator to compute each reading.",
        "Amplified readings are on the display; Yara shifts the scan to start at sector one, skipping the base.",
    ),
    # 7 mcq
    (
        "Sector zero is the docking bay and off-limits — Yara adjusts the sweep to start at sector one.",
        "Scan now begins at sector one; Yara must sequence the five-sector deep-space route.",
    ),
    # 8 arrange
    (
        "Yara uploads the sector-1-to-5 routing table to the probe's navigation core.",
        "Route confirmed from sector 1 to 5; Yara compounds signal readings to compute cumulative power.",
    ),
    # 9 mcq
    (
        "To measure total scan power Yara multiplies each sector's reading — the loop handles each factor.",
        "Cumulative power reads 24; Yara's last calibration is pinging every third distance unit.",
    ),
    # 10 mini_code
    (
        "The probe pings every 3 units of distance — Yara needs the first five ping distances printed.",
        "Five ping distances confirmed; Yara completes the mission by totalling all sector star counts.",
    ),
    # 11 mini_code
    (
        "Before filing the report Yara needs the grand total of star counts across sectors 1 through 10.",
        "Fifty-five stars logged in the manifest — the sector scan is complete and mission data is filed.",
    ),
])

apply_beats(L1, "mystery", [
    # 0 concept
    (
        "Cole has a stack of numbered case files to review — the only way through is to read each one in order.",
        "Files 0 through 4 opened and closed; Cole now sets the loop to cover the exact number he needs.",
    ),
    # 1 mcq
    (
        "The captain hands Cole three files and tells him to report back — he confirms the loop will run exactly three times.",
        "Three files, three reads; Cole double-checks the count before combing through a longer archive.",
    ),
    # 2 fill_blank
    (
        "Cole reaches for the only function that generates a numbered sequence of files to review.",
        "range() produces the file list; Cole next verifies how many reads that will add up to.",
    ),
    # 3 mcq
    (
        "Seven files sit on Cole's desk — he needs to know how many times the loop will send him back to the cabinet.",
        "Seven trips confirmed; Cole organises the files in the right reading order.",
    ),
    # 4 arrange
    (
        "Cole lays out files 0 through 4 and must write the review loop from start to finish.",
        "The loop is written; Cole now tallies up the clue counts file by file.",
    ),
    # 5 mcq
    (
        "Cole keeps a running tally of clues — he adds each file's number to the total as he reads.",
        "Six clues in the tally; Cole realises each file actually has two pages and adjusts the count.",
    ),
    # 6 fill_blank
    (
        "Every file has double the pages its number suggests — Cole picks the right operator to calculate each page count.",
        "Page counts doubled; Cole shifts the reading list to start at file one instead of the empty file zero.",
    ),
    # 7 mcq
    (
        "File zero turned up empty — Cole updates the loop to skip it and begin at file one.",
        "Reading now starts at file one; Cole lays out the path from file one to five.",
    ),
    # 8 arrange
    (
        "Cole numbers the files 1 through 5 on his corkboard and must build the loop that reads them in sequence.",
        "Files 1 to 5 read in order; Cole multiplies lead weights to measure overall case strength.",
    ),
    # 9 mcq
    (
        "To score the case Cole multiplies the lead weight from each file — each factor compounds the others.",
        "Case strength: 24; Cole's final step is flagging every third piece of evidence.",
    ),
    # 10 mini_code
    (
        "Evidence is tagged every third item — Cole needs to print the first five multiples to track each flag.",
        "Five evidence flags noted; Cole wraps up by summing every tag number from one to ten.",
    ),
    # 11 mini_code
    (
        "Before closing the file Cole needs the total of all evidence tag numbers from files 1 through 10.",
        "Fifty-five — every tag accounted for; the case log is sealed and filed.",
    ),
])


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 2 — for Loops with Lists
# ─────────────────────────────────────────────────────────────────────────────
L2 = "C:/Users/pyrot/Documents/Coding/python-learner/content/units/unit_4/lesson_2.yaml"

apply_beats(L2, "fantasy", [
    # 0 concept
    (
        "Mira empties her satchel onto the workbench — she needs to inspect each herb by name, one after another.",
        "Moonleaf, Thornroot, Glowcap — each herb examined in turn; now Mira checks the count in each pouch.",
    ),
    # 1 mcq
    (
        "Three pouches sit on the shelf; Mira loops through them to read the count in each.",
        "Counts confirmed; next Mira must give the loop variable a proper name so each herb is addressed correctly.",
    ),
    # 2 fill_blank
    (
        "Mira labels the loop variable so the spell knows it is handling one herb at a time from the list.",
        "Variable named; Mira now tests a spell that weighs each herb by doubling its value.",
    ),
    # 3 arrange
    (
        "Mira measures each pouch by doubling its weight — she must arrange the loop spell to do the maths.",
        "Double weights calculated; now Mira bellows each herb's name across the workshop.",
    ),
    # 4 mcq
    (
        "The master wants the herb names called out in full voice — Mira's loop converts each name to uppercase.",
        "Names echoed loudly; Mira moves on to accumulating the combined potency of everything in the satchel.",
    ),
    # 5 fill_blank
    (
        "Mira needs the total potency of all her herbs — she picks the operator that adds each value to the running sum.",
        "Potency values summed; Mira checks the total weight of everything she has collected.",
    ),
    # 6 mcq
    (
        "Mira's three herb weights need to be combined into one grand total for the master's ledger.",
        "Thirty grams total — the satchel is weighed; now Mira counts how many herbs she collected overall.",
    ),
    # 7 arrange
    (
        "Mira keeps a tally counter and increments it for every herb she passes over in the list.",
        "Herb count complete; now Mira searches the collection for the most potent specimen.",
    ),
    # 8 mcq
    (
        "The master asks for the single most potent herb — Mira loops through and tracks the highest value.",
        "Best potency found at 5; Mira labels every herb with its position so the shelves stay organised.",
    ),
    # 9 mcq
    (
        "Mira uses enumerate to number each herb slot so she can find any item on the shelf instantly.",
        "Herbs numbered 0, 1, 2 with their names; Mira's final task is filtering out the cooler clearings.",
    ),
    # 10 mini_code
    (
        "Five forest clearings have warmth readings — Mira only wants those above 20 to know where herbs thrive.",
        "Warm clearings identified; Mira finishes by calculating the average weight across her whole haul.",
    ),
    # 11 mini_code
    (
        "Before restocking the workshop Mira needs the average herb weight from her list of five measurements.",
        "Average weight: 30.0 — Mira's satchel analysis is done and the herbs are ready for the master.",
    ),
])

apply_beats(L2, "scifi", [
    # 0 concept
    (
        "Yara pulls up the crew manifest — she must log each crew member's name to confirm everyone is aboard.",
        "All three names logged; Yara turns to a list of probe readings that need processing.",
    ),
    # 1 mcq
    (
        "Three probe readings have come in from the outer ring — Yara loops through to display each one.",
        "Readings displayed; Yara now assigns a clean variable name to each item as the loop runs.",
    ),
    # 2 fill_blank
    (
        "Yara names the loop variable so the code treats each star in the survey list as a distinct entry.",
        "Variable labelled; Yara doubles the sensor readings to calibrate instrument output.",
    ),
    # 3 arrange
    (
        "Each sensor reading needs to be doubled to match the amplified signal — Yara arranges the loop.",
        "Amplified readings printed; Yara now formats planet codes for the transmission log.",
    ),
    # 4 mcq
    (
        "Transmission protocol requires all planet codes in uppercase — Yara's loop converts each one.",
        "Codes formatted; Yara accumulates total energy from each probe's reading.",
    ),
    # 5 fill_blank
    (
        "Yara sums the energy readings from three probes into a single running total for the engineering log.",
        "Energy accumulated; Yara now totals the fuel cell levels to check remaining range.",
    ),
    # 6 mcq
    (
        "Three fuel cells report their levels — Yara loops through and adds them into one total.",
        "Thirty units of fuel remaining; Yara counts how many probes have been deployed.",
    ),
    # 7 arrange
    (
        "Yara increments a counter for each deployed probe in the list to get an accurate deployment tally.",
        "Deployment count complete; now Yara scans for the strongest signal in the survey data.",
    ),
    # 8 mcq
    (
        "Five signal readings came back — Yara loops through to find and report the strongest one.",
        "Peak signal identified at 5; Yara indexes each sector for the final survey log.",
    ),
    # 9 mcq
    (
        "The survey log needs both the sector index and its ID printed together — Yara uses enumerate.",
        "Index-ID pairs logged; Yara filters surface temperature readings for habitable worlds.",
    ),
    # 10 mini_code
    (
        "Five planetary surface temperatures are on record — Yara flags only those above 20 for colonisation review.",
        "Habitable candidates identified; Yara wraps up by computing the average signal strength across all sectors.",
    ),
    # 11 mini_code
    (
        "Before submitting the mission report Yara needs the average signal strength from the five-sector data set.",
        "Average signal: 30.0 — data filed; Yara's crew manifest and sensor analysis are complete.",
    ),
])

apply_beats(L2, "mystery", [
    # 0 concept
    (
        "Cole unrolls the witness list — he must read each name aloud to confirm who was at the scene.",
        "Nina, Omar, Petra — all noted; now Cole checks the numeric tags on each piece of evidence.",
    ),
    # 1 mcq
    (
        "Three evidence tags sit on the table — Cole loops through to read the number on each one.",
        "Tags confirmed; Cole assigns the loop variable a name that makes each clue identifiable.",
    ),
    # 2 fill_blank
    (
        "Cole labels the loop variable so each iteration handles exactly one clue from the evidence list.",
        "Variable named; Cole cross-references each tag number by doubling it against the master index.",
    ),
    # 3 arrange
    (
        "Every tag number needs to be doubled to match the master index — Cole arranges the loop.",
        "Cross-references complete; Cole stamps priority keywords in uppercase for the report.",
    ),
    # 4 mcq
    (
        "Priority evidence keywords must appear in all caps in the official report — Cole's loop handles the formatting.",
        "Keywords stamped; Cole now scores each suspect's relevance and accumulates a total.",
    ),
    # 5 fill_blank
    (
        "Cole adds each suspect's relevance score to a running total to rank the overall threat level.",
        "Scores accumulated; Cole tallies the physical weight of all collected evidence.",
    ),
    # 6 mcq
    (
        "Three evidence bags need their weights combined for the forensic report — Cole's loop sums them.",
        "Thirty grams of evidence logged; Cole now counts how many case files he has reviewed.",
    ),
    # 7 arrange
    (
        "Cole increments a file counter for each item in the case list to get a precise review tally.",
        "File count confirmed; Cole searches for the single most damning piece of evidence.",
    ),
    # 8 mcq
    (
        "Somewhere in the evidence list is the most critical item — Cole loops through to track the highest score.",
        "Most damning evidence scored at 5; Cole numbers every witness for the official report.",
    ),
    # 9 mcq
    (
        "The report requires each witness numbered in order — Cole uses enumerate to pair index with name.",
        "Witnesses numbered; Cole filters interview urgency levels to prioritise follow-ups.",
    ),
    # 10 mini_code
    (
        "Five witness interviews have urgency ratings — Cole only wants those above 20 for immediate follow-up.",
        "High-priority interviews flagged; Cole wraps up by averaging relevance scores across all leads.",
    ),
    # 11 mini_code
    (
        "Before presenting to the captain Cole calculates the average relevance score from his five key leads.",
        "Average score: 30.0 — the report is filed and Cole's evidence loop is closed.",
    ),
])


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 3 — range() with Start, Stop, Step
# ─────────────────────────────────────────────────────────────────────────────
L3 = "C:/Users/pyrot/Documents/Coding/python-learner/content/units/unit_4/lesson_3.yaml"

apply_beats(L3, "fantasy", [
    # 0 concept
    (
        "Mira's new foraging route skips every second patch to avoid the nettles — she needs a strided loop.",
        "Even-numbered patches visited cleanly; now Mira checks which patches she hits when jumping by three.",
    ),
    # 1 mcq
    (
        "The rare moonflowers only grow at patches 1, 4, and 7 — Mira traces the stride to confirm.",
        "Patch 1, 4, 7 — just right; now Mira needs to retreat through the forest one patch at a time.",
    ),
    # 2 fill_blank
    (
        "Mira must walk back from patch 10 to patch 1 — she selects the step that moves her backward.",
        "Step set to -1; Mira checks the full countdown sequence as she retreats.",
    ),
    # 3 mcq
    (
        "Mira backtracks from patch 5 all the way to patch 1, counting down as she goes.",
        "Patches 5, 4, 3, 2, 1 revisited; now Mira arranges a strided advance through even patches.",
    ),
    # 4 arrange
    (
        "The even-numbered patches hold the best herbs — Mira builds the loop that visits 2, 4, 6, 8, 10.",
        "Even-patch route arranged; Mira experiments with a loop that dips into negative patch territory.",
    ),
    # 5 mcq
    (
        "Beyond the forest edge the terrain drops below zero — Mira sees what values the loop produces there.",
        "Negative patches 0 to -4 mapped; Mira sets the stop value for a long backward stride.",
    ),
    # 6 fill_blank
    (
        "Mira plans a grand retreat from the deepest grove, patch 100, stopping just before the forest entrance.",
        "Stop value fixed at 0; Mira counts how many strides that long route actually takes.",
    ),
    # 7 mcq
    (
        "Mira strides in jumps of 5 from patch 0 — she counts how many patches she actually visits.",
        "Four strides in all; Mira finishes by squaring the potency value of each patch from 1 to 5.",
    ),
    # 8 mini_code
    (
        "The master asks Mira to count down from her deepest patch, number 10, all the way back to patch 1.",
        "Countdown complete from 10 to 1; Mira's last challenge is visiting only the odd-numbered deep patches.",
    ),
    # 9 mini_code
    (
        "Only odd-numbered patches deep in the forest hold the rarest specimens — Mira loops through them all.",
        "Odd patches 1, 3, 5 … 19 visited; Mira's strided foraging route is finished and she heads home.",
    ),
])

apply_beats(L3, "scifi", [
    # 0 concept
    (
        "Yara configures the probe to ping every other sector to save power during the long-range sweep.",
        "Sectors 0, 2, 4, 6, 8 logged with half the energy; Yara checks a sweep with a step of three.",
    ),
    # 1 mcq
    (
        "The outer constellation requires sampling sectors 1, 4, and 7 — Yara verifies the step pattern.",
        "Step-3 sequence confirmed; Yara now programs the probe to retreat back toward base.",
    ),
    # 2 fill_blank
    (
        "Recall protocol: the probe steps back one sector at a time from sector 10 toward sector 1.",
        "Retreat step set; Yara verifies the full recall countdown before uploading it.",
    ),
    # 3 mcq
    (
        "The probe counts down from sector 5 to sector 1 during the emergency recall — Yara reads the log.",
        "Recall sequence 5 to 1 confirmed; Yara programs a forward stride across even-numbered sectors.",
    ),
    # 4 arrange
    (
        "Efficiency mode requires pinging only even sectors 2 through 10 — Yara builds that loop.",
        "Even-sector scan programmed; Yara tests the probe's behaviour in negative sector space.",
    ),
    # 5 mcq
    (
        "The sensor grid extends into negative sector IDs near the dark zone — Yara checks what the loop logs.",
        "Negative sectors 0 to -4 mapped; Yara sets the long-range retreat endpoint.",
    ),
    # 6 fill_blank
    (
        "The probe must retreat from sector 100 all the way back, stopping just before it returns to sector 0.",
        "Retreat endpoint locked in; Yara counts how many pings that long-range sweep produces.",
    ),
    # 7 mcq
    (
        "With a step of 5 the probe hits far fewer sectors — Yara counts exactly how many pings result.",
        "Four pings total; Yara calculates cumulative signal power by squaring each sector's reading.",
    ),
    # 8 mini_code
    (
        "Emergency recall protocol counts down from sector 10 to sector 1 — Yara runs the sequence.",
        "Recall logged from 10 to 1; Yara's last calibration samples only odd-numbered sectors.",
    ),
    # 9 mini_code
    (
        "Odd sectors carry the clearest signal — Yara programs the probe to sample sectors 1, 3, 5 through 19.",
        "Odd-sector scan complete; the probe's calibration data is transmitted back to the Helix.",
    ),
])

apply_beats(L3, "mystery", [
    # 0 concept
    (
        "Cole decides to read every other file to speed up the initial pass — he sets a step of 2.",
        "Files 0, 2, 4, 6, 8 reviewed; Cole checks which files get flagged with a larger interval.",
    ),
    # 1 mcq
    (
        "A pattern in the archive suggests files 1, 4, and 7 are linked — Cole traces the step to confirm.",
        "Interval confirmed at step 3; now Cole needs to re-read the files in reverse order.",
    ),
    # 2 fill_blank
    (
        "New evidence means Cole must retrace his steps one file at a time, from file 10 back to file 1.",
        "Backward step set; Cole rehearses the full reverse read before committing.",
    ),
    # 3 mcq
    (
        "Cole works backwards from file 5 to file 1, re-examining each one for overlooked details.",
        "Files 5 to 1 re-read; Cole now builds a loop to check only the even-numbered files.",
    ),
    # 4 arrange
    (
        "Even-numbered files contain the financial records — Cole builds the strided loop to visit 2, 4, 6, 8, 10.",
        "Even files examined; Cole digs into archived files with negative reference numbers.",
    ),
    # 5 mcq
    (
        "The cold-case archive uses negative reference numbers — Cole checks what the loop reads there.",
        "Negative references 0 to -4 noted; Cole now sets how far back his big backward sweep should go.",
    ),
    # 6 fill_blank
    (
        "Cole sweeps the archive backward from file 100 in steps of 10, stopping just before file 0.",
        "Sweep endpoint established; Cole counts exactly how many files that interval covers.",
    ),
    # 7 mcq
    (
        "With a jump of 5, Cole lands on far fewer files — he counts exactly how many he visits.",
        "Four files hit; Cole squares each file's relevance score from 1 to 5 to weight the evidence.",
    ),
    # 8 mini_code
    (
        "Cole re-reads the files in reverse, counting back from file 10 to file 1 for a final review.",
        "Reverse read complete from 10 to 1; Cole's last sweep flags only the odd-numbered priority files.",
    ),
    # 9 mini_code
    (
        "Odd-numbered files are marked priority leads — Cole prints them all from file 1 to file 19.",
        "Priority files 1, 3, 5 … 19 flagged; Cole closes the archive and heads to the precinct.",
    ),
])


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 4 — while Loops
# ─────────────────────────────────────────────────────────────────────────────
L4 = "C:/Users/pyrot/Documents/Coding/python-learner/content/units/unit_4/lesson_4.yaml"

apply_beats(L4, "fantasy", [
    # 0 concept
    (
        "The champion must train until she has completed every required step — a while loop keeps her going as long as she must.",
        "Five training steps done; the champion sees the countdown begin as she prepares for battle.",
    ),
    # 1 mcq
    (
        "Three rounds remain before the duel — the champion counts down with each strike.",
        "Countdown hits zero and the duel begins; now the champion must keep doubling her intensity until she peaks.",
    ),
    # 2 fill_blank
    (
        "Training intensity must keep doubling while it has not yet exceeded the master's threshold of 100.",
        "Condition locked in; the champion now tallies her strike points round by round.",
    ),
    # 3 mcq
    (
        "Round by round the champion adds her strike points — the while loop runs until all four rounds are done.",
        "Ten strike points total; the champion arranges her victory-round counter from scratch.",
    ),
    # 4 arrange
    (
        "The champion sets up the counter at 1 and builds a while loop that announces each of her three victory rounds.",
        "Rounds 1, 2, 3 declared; the champion reflects on when while is the right choice over for.",
    ),
    # 5 mcq
    (
        "The training master quizzes the champion: when should she choose while over for?",
        "Concept clear — while for unknown repetitions, for for known sequences; the champion drains her hp next.",
    ),
    # 6 fill_blank
    (
        "Each training round costs the champion 10 hp — she selects the operator that reduces hp correctly.",
        "hp drains 10 per round; the champion watches her power double until the final threshold.",
    ),
    # 7 mcq
    (
        "The champion's power doubles every round — she needs to know what value it reaches when the loop ends.",
        "Power lands at 32; the champion considers what would happen if the condition never turned False.",
    ),
    # 8 mcq
    (
        "The master warns of the infinite loop — a trial that never ends because the condition stays True.",
        "Infinite loop understood; the champion's final challenge is doubling her strength until it exceeds 1000.",
    ),
    # 9 mini_code
    (
        "The champion starts at power 1 and keeps doubling — she must find the first value that surpasses 1000.",
        "Power reaches 1024; the champion's last trial is announcing every seventh-round milestone below 50.",
    ),
    # 10 mini_code
    (
        "The champion earns a milestone banner every 7 rounds — she must print all multiples of 7 below 50.",
        "Banners raised at 7, 14, 21 … 49 — the champion's trial is complete and she is proclaimed worthy.",
    ),
])

apply_beats(L4, "scifi", [
    # 0 concept
    (
        "Yara must charge the power cell step by step — the while loop keeps adding charge as long as the cell needs more.",
        "Charge levels 0 through 4 logged; now Yara runs a countdown timer before reactor ignition.",
    ),
    # 1 mcq
    (
        "The reactor ignition sequence counts down from 3 — Yara verifies the while loop decrements correctly.",
        "Countdown 3, 2, 1 confirmed; Yara now doubles reactor output while it stays within safe limits.",
    ),
    # 2 fill_blank
    (
        "Reactor output must keep doubling while it has not yet exceeded the safety ceiling of 100.",
        "Condition set; Yara accumulates power readings cycle by cycle.",
    ),
    # 3 mcq
    (
        "Yara logs power readings from four consecutive cycles and sums them as the while loop runs.",
        "Total of 10 power units logged; Yara now builds the power-level monitor loop from scratch.",
    ),
    # 4 arrange
    (
        "Yara initialises the counter at 1 and constructs a while loop that logs power levels 1, 2, 3 then halts.",
        "Power levels logged; Yara reviews when while is preferable to for in engineering scenarios.",
    ),
    # 5 mcq
    (
        "The engineering manual asks: when should Yara use while instead of for?",
        "Distinction understood; Yara now programs the energy drain simulation.",
    ),
    # 6 fill_blank
    (
        "Each cycle drains 10 units from the ship's energy reserve — Yara picks the operator for the drain.",
        "Energy drains by 10 per cycle; Yara watches the reactor output double toward its cap.",
    ),
    # 7 mcq
    (
        "Reactor output doubles each cycle — Yara reads the final value when the condition fails.",
        "Output settles at 32; Yara considers what an infinite reactor loop would mean for the ship.",
    ),
    # 8 mcq
    (
        "An infinite loop in the power system would run the reactor forever — Yara identifies what causes it.",
        "Root cause understood; Yara's final task is doubling the power cell charge until it exceeds 1000.",
    ),
    # 9 mini_code
    (
        "The emergency cell starts at 1 and must double until it exceeds 1000 — Yara runs the simulation.",
        "Cell reaches 1024; Yara's last check is listing every seventh power milestone below 50.",
    ),
    # 10 mini_code
    (
        "Maintenance windows occur at every 7th power unit — Yara prints all multiples of 7 below 50.",
        "Maintenance points logged at 7, 14 … 49 — the power build-up sequence is complete.",
    ),
])

apply_beats(L4, "mystery", [
    # 0 concept
    (
        "Cole must search every room in the building — the while loop keeps him moving as long as rooms remain.",
        "Rooms 0 through 4 searched; Cole now counts down before cracking the next locked safe.",
    ),
    # 1 mcq
    (
        "Three tumblers remain on the safe's dial — Cole decrements the counter with each click.",
        "Clicks 3, 2, 1 — the safe opens; Cole now expands his search radius while it stays manageable.",
    ),
    # 2 fill_blank
    (
        "Cole widens the search radius by doubling it each pass, as long as it has not exceeded 100 blocks.",
        "Doubling condition set; Cole tallies clue scores room by room.",
    ),
    # 3 mcq
    (
        "Cole scores each room's clues and accumulates the total as the while loop runs through four rooms.",
        "Ten clue points tallied; Cole builds the room-search counter loop from scratch.",
    ),
    # 4 arrange
    (
        "Cole starts at room 1 and constructs a while loop that searches rooms 1, 2, 3 then stops.",
        "Rooms 1 to 3 searched; Cole considers when while is the right tool versus for.",
    ),
    # 5 mcq
    (
        "Cole's partner asks him to explain the difference between for and while — Cole obliges.",
        "Difference noted; Cole's next step is tracking stamina as he searches each room.",
    ),
    # 6 fill_blank
    (
        "Each room costs Cole 10 stamina points — he selects the operator that deducts correctly.",
        "Stamina drains by 10 per room; Cole watches the number of leads double with each tip.",
    ),
    # 7 mcq
    (
        "The tip chain keeps doubling — Cole reads the final count when the while condition fails.",
        "Leads reach 32; Cole thinks about what an infinite search would mean if the condition never cleared.",
    ),
    # 8 mcq
    (
        "A search that never ends — Cole identifies the exact reason a while loop can run forever.",
        "Infinite-loop trap understood; Cole's final task is doubling the lead count until it exceeds 1000.",
    ),
    # 9 mini_code
    (
        "Starting from a single lead, Cole doubles the count until it surpasses 1000 — he needs the final tally.",
        "Lead count hits 1024; Cole's last sweep prints every seventh clue milestone below 50.",
    ),
    # 10 mini_code
    (
        "Every 7th clue gets a priority flag — Cole prints all multiples of 7 below 50.",
        "Priority clues flagged at 7, 14 … 49 — the investigation loop is closed and the case moves forward.",
    ),
])


# ─────────────────────────────────────────────────────────────────────────────
# LESSON 5 — break and continue
# ─────────────────────────────────────────────────────────────────────────────
L5 = "C:/Users/pyrot/Documents/Coding/python-learner/content/units/unit_4/lesson_5.yaml"

apply_beats(L5, "fantasy", [
    # 0 concept
    (
        "Finn is racing through the enchanted corridor — the Break Rune will shatter the loop the moment he triggers it.",
        "The loop halts at tile 5; Finn now tests how early an exit happens inside a shorter corridor.",
    ),
    # 1 mcq
    (
        "A three-tile cursed passage — Finn needs to know exactly which tiles he passes before the rune fires.",
        "Tiles 0, 1, 2 cleared before the rune; now Finn learns the companion spell that skips a single bad tile.",
    ),
    # 2 concept
    (
        "The Skip Charm lets Finn bypass cursed tile 2 without abandoning the whole corridor run.",
        "Tile 2 skipped cleanly; Finn now tests the charm against every even tile in a longer passage.",
    ),
    # 3 mcq
    (
        "Even tiles are booby-trapped — Finn applies the Skip Charm to leap past each one.",
        "Odd tiles 1, 3, 5 traversed; now Finn drills placing the Break Rune at the right spot in the code.",
    ),
    # 4 fill_blank
    (
        "Finn must place the Break Rune exactly where the exit-rune item appears so the loop stops instantly.",
        "Rune placed correctly; Finn now arranges a full corridor that skips only the forbidden fifth tile.",
    ),
    # 5 arrange
    (
        "Finn lays out tiles 0 through 9 and must insert the Skip Charm so tile 5 is bypassed seamlessly.",
        "Tile 5 skipped; Finn faces a while-True corridor that relies on the Break Rune to end at all.",
    ),
    # 6 mcq
    (
        "The corridor runs indefinitely — only the Break Rune at round 4 can shut it down.",
        "Rounds 1, 2, 3 logged before the rune fires; next Finn places the Skip Charm to ignore the lower tiles.",
    ),
    # 7 fill_blank
    (
        "Tiles below position 5 are cursed — Finn uses the Skip Charm to continue past each one without printing it.",
        "Lower tiles bypassed; Finn finally clarifies which rune exits and which merely skips.",
    ),
    # 8 mcq
    (
        "Master Aldric quizzes Finn: which rune ends the whole run and which only skips a single tile?",
        "Break exits, continue skips — Finn masters the difference; now he hunts for the first tile divisible by both 6 and 8.",
    ),
    # 9 mini_code
    (
        "The exit portal only opens at the first tile divisible by both 6 and 8 — Finn must find it and break.",
        "Portal found at 24; Finn's last task is continuing through tiles 1 to 20, skipping every third.",
    ),
    # 10 mini_code
    (
        "Every third tile crumbles underfoot — Finn uses the Skip Charm to continue past them and print the rest.",
        "All safe tiles from 1 to 20 printed; Finn emerges from the corridor triumphant, runes mastered.",
    ),
])

apply_beats(L5, "scifi", [
    # 0 concept
    (
        "Yara's hull-integrity scan runs module by module — an emergency stop at module 5 will abort the entire sweep.",
        "Scan halts at module 5; Yara now checks which modules are logged before a fault triggers a halt.",
    ),
    # 1 mcq
    (
        "A critical fault at module 3 triggers the emergency stop — Yara reads how many modules were logged first.",
        "Modules 0, 1, 2 logged before the halt; now Yara learns to skip a single offline module mid-scan.",
    ),
    # 2 concept
    (
        "Module 2 is offline — Yara's continue directive skips it and lets the scan carry on without full abort.",
        "Module 2 bypassed; Yara now handles a scan where all even-indexed modules are damaged.",
    ),
    # 3 mcq
    (
        "Even-indexed modules are flagged as damaged and must be skipped — Yara confirms which ones get logged.",
        "Odd modules 1, 3, 5 processed; Yara now places the shutdown trigger in the right position.",
    ),
    # 4 fill_blank
    (
        "When the shutdown signal arrives in the item stream, Yara must trigger an immediate emergency stop.",
        "Shutdown wired in; Yara builds a full scan loop that skips only the compromised fifth module.",
    ),
    # 5 arrange
    (
        "Yara sequences a ten-module scan that uses continue to bypass module 5 and logs all others.",
        "Module 5 skipped cleanly; Yara runs a while-True alert loop that relies on break to terminate.",
    ),
    # 6 mcq
    (
        "The alert system cycles indefinitely — only the break at counter 4 shuts it down.",
        "Alert ended after 3 logs; now Yara programs the scan to skip all modules below level 5.",
    ),
    # 7 fill_blank
    (
        "Modules below level 5 are in low-power mode and must be skipped — Yara inserts continue to bypass them.",
        "Low-power modules skipped; Yara documents the exact operational difference between break and continue.",
    ),
    # 8 mcq
    (
        "The mission report asks Yara to define the distinction: does break halt or skip, and does continue halt or skip?",
        "Definitions confirmed — break halts, continue skips; Yara's last diagnostic finds the first dual-divisible module.",
    ),
    # 9 mini_code
    (
        "The docking bay opens only at the first module number divisible by both 6 and 8 — Yara finds it and breaks.",
        "Bay opens at module 24; Yara's final scan lists all modules from 1 to 20 except those divisible by 3.",
    ),
    # 10 mini_code
    (
        "Every third module is undergoing maintenance and must be skipped — Yara continues past them and logs the rest.",
        "All active modules from 1 to 20 logged; the Helix's emergency scan protocol is fully validated.",
    ),
])

apply_beats(L5, "mystery", [
    # 0 concept
    (
        "Cole is reviewing a list of leads — the moment he hits the key suspect at position 5, he breaks off and arrests.",
        "Investigation halts at lead 5; Cole now practises stopping at an earlier point in a shorter lead list.",
    ),
    # 1 mcq
    (
        "The key clue sits at index 3 — Cole reads how many leads he reviews before breaking off.",
        "Leads 0, 1, 2 logged before the break; now Cole learns to skip a single irrelevant lead mid-loop.",
    ),
    # 2 concept
    (
        "Lead 2 is a dead end — continue lets Cole skip it and move straight to lead 3 without abandoning the sweep.",
        "Lead 2 bypassed; Cole now skips every even-indexed dead-end in the full list.",
    ),
    # 3 mcq
    (
        "Even-indexed leads are all dead ends — Cole applies continue and logs only the promising odd ones.",
        "Odd leads 1, 3, 5 logged; Cole now drills placing the case-closed break in exactly the right spot.",
    ),
    # 4 fill_blank
    (
        "The case-closed signal ends the investigation — Cole must place break so it fires the moment that item appears.",
        "Break placed correctly; Cole now arranges a full lead-review loop that skips only lead 5.",
    ),
    # 5 arrange
    (
        "Cole reviews leads 0 through 9 and inserts continue at precisely the right line to skip lead 5.",
        "Lead 5 skipped; Cole faces a while-True session loop that only a break can end.",
    ),
    # 6 mcq
    (
        "Cole's review session runs until the counter exceeds 3 — he reads how many sessions are logged before the break.",
        "Sessions 1, 2, 3 noted before the case closes; Cole now skips all low-priority leads below index 5.",
    ),
    # 7 fill_blank
    (
        "Low-priority leads below index 5 waste time — Cole inserts continue to bypass them and focus on the rest.",
        "Low-priority leads skipped; Cole articulates the exact difference between his two most important tools.",
    ),
    # 8 mcq
    (
        "The captain asks Cole to explain: does break close the case or skip one lead, and does continue close or skip?",
        "Break closes, continue skips — Cole is ready; his final task is finding the first lead divisible by both 6 and 8.",
    ),
    # 9 mini_code
    (
        "The confession is hidden at the first number divisible by both 6 and 8 — Cole must find it and break.",
        "Confession found at 24; Cole's last sweep prints all leads from 1 to 20 except those divisible by 3.",
    ),
    # 10 mini_code
    (
        "Every third lead is a planted distraction — Cole uses continue to skip them and logs only the genuine ones.",
        "Genuine leads from 1 to 20 logged; Cole closes the casebook — the investigation is solved.",
    ),
])

print("All Unit 4 story beats applied.")
