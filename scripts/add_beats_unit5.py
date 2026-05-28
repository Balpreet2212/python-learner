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


# ──────────────────────────────────────────────
# LESSON 1 – Defining Functions
# ──────────────────────────────────────────────
L1 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_5\\lesson_1.yaml"

apply_beats(L1, 'fantasy', [
    # 0 concept
    ("Master Theo shows Elara that instead of rewriting the same potion step each time, she can define a reusable brew recipe.",
     "Elara sees the cauldron respond to the same recipe called twice — the magic is real, and it's repeatable."),
    # 1 mcq – say_hi / mix
    ("Elara tries a simpler recipe that takes no ingredients at all, just to prove a function can work on its own.",
     "The stirring message echoes through the workshop — even an empty recipe springs to life when called."),
    # 2 fill_blank – def keyword
    ("Master Theo hands Elara a half-written recipe scroll; she must fill in the very first word that begins every function.",
     "With the correct keyword inscribed, the scroll glows — the recipe is now properly declared."),
    # 3 arrange – build hello function
    ("Elara must arrange the magic tokens in the right order to build a bubble-chanting recipe from scratch and then cast it.",
     "The tokens snap into place and 'hello' rings out — Elara has written and called her first complete recipe."),
    # 4 mcq – show(5) prints 10
    ("Theo demonstrates how passing a number into a recipe can double the ingredient quantity automatically.",
     "Ten units appear — Elara realises the parameter is what makes each call to the same recipe different."),
    # 5 fill_blank – add +
    ("Two ingredient amounts need combining; Elara must choose the right rune to blend them inside the recipe.",
     "Seven combined units pour from the cauldron — the blending rune worked perfectly."),
    # 6 mcq – square loop prints 1 4 9
    ("Theo loops the squaring recipe over three ingredient potencies and asks Elara to predict the result.",
     "1, 4, 9 — the amplified series confirms that calling the same recipe repeatedly yields consistent magic."),
    # 7 mcq – what is a parameter
    ("Master Theo quizzes Elara on the precise meaning of the variable inside a recipe's parentheses.",
     "Elara answers correctly — a parameter is the placeholder that receives each new ingredient at call time."),
    # 8 arrange – call describe('Python')
    ("A recipe called describe is already defined; Elara only needs to arrange the tokens to invoke it with the right ingredient.",
     "The recipe fires with 'Python' as its ingredient — calling a function is as simple as name plus parentheses."),
    # 9 mcq – intro prints 'Alice is 25'
    ("Theo's two-ingredient recipe labels both a name and an age; Elara must trace what it prints.",
     "Alice is 25 — both parameters landed correctly, and Elara feels confident handling multi-ingredient recipes."),
    # 10 mini_code – double, call with 7 and 3
    ("Now Elara writes her own recipe: one that doubles any potency she passes in.",
     "14 and 6 appear in the cauldron's glow — Elara's first independent recipe works on every potency she tries."),
    # 11 mini_code – greet with 'World' and 'Alice'
    ("Master Theo asks Elara to craft a greeting recipe that welcomes any ingredient by name.",
     "The workshop echoes with 'Hello, World!' and 'Hello, Alice!' — Elara's recipe library has its first two spells."),
])

apply_beats(L1, 'scifi', [
    # 0 concept
    ("Chief Engineer Sana explains to Yara that instead of duplicating repair logic for every system, she should write one reusable subroutine.",
     "The repair subroutine fires for both engine and shields — Yara sees how a single definition handles any system."),
    # 1 mcq – activate prints 'Drone online!'
    ("Yara tests a zero-parameter boot subroutine to confirm the drone activates on command.",
     "Drone online — the simplest subroutine runs the moment it is called."),
    # 2 fill_blank – def keyword
    ("Sana's repair template is missing its opening keyword; Yara must supply the correct one to register the subroutine.",
     "The subroutine compiles cleanly — the correct keyword is all it took to bring the template to life."),
    # 3 arrange – build hello function
    ("Yara must sequence the code blocks to define and immediately deploy a basic drone routine.",
     "The routine executes successfully — define first, deploy second, that is the protocol."),
    # 4 mcq – show(5) prints 10
    ("Sana runs a power test: the same subroutine is called with a level of 5 to see what output it transmits.",
     "Output of 10 confirmed — the parameter doubles the reading, exactly as the spec required."),
    # 5 fill_blank – add +
    ("Two charge level readings must be summed inside the subroutine; Yara selects the correct operator.",
     "Seven total units logged — the subroutine combines both charge levels without a fault."),
    # 6 mcq – square loop prints 1 4 9
    ("Sana runs the power-boost subroutine at three increasing levels and asks Yara to predict the console output.",
     "1, 4, 9 confirmed on screen — squared outputs at each level match the expected energy curve."),
    # 7 mcq – what is a parameter
    ("Yara must correctly define what the variable inside a subroutine's parentheses actually represents.",
     "Parameter identified — it is the slot that accepts a different target system each time the subroutine is called."),
    # 8 arrange – call describe('Python')
    ("The describe subroutine already exists; Yara just needs to arrange the tokens to call it with the right argument.",
     "Subroutine deployed with 'Python' as target — the call syntax is now locked in."),
    # 9 mcq – intro prints 'Alice is 25'
    ("Sana's logging subroutine takes two parameters; Yara traces the output to verify both are recorded correctly.",
     "Alice is 25 — two-parameter subroutines work just like one-parameter ones, with an extra slot in the call."),
    # 10 mini_code – double
    ("Yara codes a power-doubling subroutine from scratch and runs it at two different levels.",
     "14 and 6 transmitted — the subroutine handles both inputs and the Helix's diagnostics are one step closer to complete."),
    # 11 mini_code – greet
    ("Sana needs a generic greeting subroutine for the ship's comm system; Yara writes it now.",
     "Hello, World! and Hello, Alice! broadcast successfully — the comm subroutine is ready for any crew member."),
])

apply_beats(L1, 'mystery', [
    # 0 concept
    ("Cole realises he keeps writing the same clue-examination steps for every piece of evidence, and decides to define a reusable analysis tool.",
     "The tool runs on both clues without rewriting a single line — Cole's case file is already more efficient."),
    # 1 mcq – log_clue prints 'Clue recorded!'
    ("Cole tests a simple tool with no parameters, just to confirm it logs a message when called.",
     "Clue recorded — even the simplest tool fires reliably, and Cole notes that defining is separate from running."),
    # 2 fill_blank – def keyword
    ("A half-written tool definition sits on Cole's desk; he must fill in the opening keyword before he can register it.",
     "The keyword is inscribed and the tool is officially defined — Cole can now call it any time he needs it."),
    # 3 arrange – build hello function
    ("Cole assembles the code blocks in the correct order to build a detective tool and then immediately deploy it.",
     "The tool runs on the first try — Cole knows the rule: define the procedure, then invoke it."),
    # 4 mcq – show(5) prints 10
    ("Cole passes the number 5 into a tool and traces exactly what value it prints to the case file.",
     "Output of 10 confirmed — the parameter doubles the clue weight, giving Cole a sharper suspicion score."),
    # 5 fill_blank – add +
    ("Two clue scores need combining inside one tool; Cole selects the right operator to add them together.",
     "A combined rating of 7 is written to the file — both scores blended cleanly with a single operator."),
    # 6 mcq – square loop prints 1 4 9
    ("Cole squares clue weights at three different levels and must predict what the tool prints each time.",
     "1, 4, 9 — the squared suspicion scores mount across the three clues, and the pattern is unmistakable."),
    # 7 mcq – what is a parameter
    ("Cole pauses to make sure he understands precisely what the variable inside a tool's parentheses actually is.",
     "Correct — a parameter is a placeholder that receives a specific clue value each time the tool is called."),
    # 8 arrange – call describe('Python')
    ("The tool describe already exists; Cole just needs to arrange the tokens to call it with the right clue.",
     "Tool invoked with 'Python' — Cole confirms that calling a function is just the name followed by the argument."),
    # 9 mcq – intro prints 'Alice is 25'
    ("Cole traces a two-parameter tool that logs both a suspect's name and age to the case file.",
     "Alice is 25 — both parameters landed in the right slots, and the suspect profile is correctly recorded."),
    # 10 mini_code – double
    ("Cole writes a tool that doubles any clue weight and tests it on two different cases.",
     "14 and 6 printed — the doubling tool is in the kit and ready to amplify any clue Cole encounters."),
    # 11 mini_code – greet
    ("Cole needs a greeting tool that introduces suspects by name; he writes it and tests it twice.",
     "Hello, World! and Hello, Alice! — the greeting tool works, and Cole's procedural toolkit is beginning to take shape."),
])


# ──────────────────────────────────────────────
# LESSON 2 – Return Values
# ──────────────────────────────────────────────
L2 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_5\\lesson_2.yaml"

apply_beats(L2, 'fantasy', [
    # 0 concept
    ("Elara's recipes have been printing results, but Master Theo explains that a truly powerful spell should bottle up its result and hand it back for later use.",
     "Seven units of combined potency are stored in the variable — Elara sees that return lets her save and reuse any result."),
    # 1 mcq – amplify(5) returns 25
    ("Elara tests an amplifying recipe and traces what bottled potency is revealed when it's printed.",
     "25 — the squared potency came back from the recipe and was displayed, just as Theo promised."),
    # 2 fill_blank – return keyword
    ("A recipe is brewing but has no keyword to bottle its result; Elara must choose the right word to send it back.",
     "With return in place the double-brewed potency is now captured rather than lost to the air."),
    # 3 mcq – label_potion returns greeting string
    ("Elara traces a labelling recipe that bottles up a formatted string and stores it before printing.",
     "Hello, Alice! — the label was bottled by return, stored in msg, and revealed intact."),
    # 4 arrange – max_val returns stronger potion
    ("Elara assembles a recipe that compares two potion strengths and returns the greater one.",
     "The stronger potion is selected and returned — Elara can now pick the best ingredient automatically."),
    # 5 mcq – nothing() returns None
    ("Theo warns Elara about a recipe that does work but never bottles anything; she must predict what comes back.",
     "None — Elara learns that every recipe without return yields an empty vial, so she'll always add return to useful recipes."),
    # 6 fill_blank – % operator
    ("Elara needs a parity rune inside a recipe that tells her whether a potion quantity splits evenly in two.",
     "The remainder rune is set; now the recipe returns True for even quantities and False for odd ones."),
    # 7 mcq – triple(triple(2)) = 18
    ("Theo nests one triple-potency recipe inside another and challenges Elara to trace the final amplified result.",
     "18 — the inner recipe bottled 6 and the outer one tripled it again, showing Elara how return enables chaining."),
    # 8 mcq – clamp returns 100
    ("A stabilising recipe keeps potency within safe limits; Elara must trace what it returns when given an over-limit value.",
     "100 — the recipe capped the runaway potency at the maximum safe level, protecting the cauldron."),
    # 9 mini_code – celsius_to_fahrenheit
    ("Master Theo's cauldron uses a different heat scale; Elara must write a conversion recipe that returns the transformed temperature.",
     "212.0 and 32.0 confirmed — the conversion recipe works perfectly and the cauldron temperatures are now calibrated."),
    # 10 mini_code – power(base, exp)
    ("Elara needs a potency amplifier recipe that raises a base ingredient to an exponential power and returns the result.",
     "1024 and 27 returned correctly — Elara's amplifier recipe is ready to supercharge any brew in the workshop."),
])

apply_beats(L2, 'scifi', [
    # 0 concept
    ("Yara notices that her subroutines print values but can't pass them to other modules; Sana shows her that return is the fix.",
     "The combined output of 7 is stored in a variable — Yara now understands that return is how subroutines communicate results."),
    # 1 mcq – power_reading(5) returns 25
    ("Yara traces a sensor subroutine that squares its input and transmits the result; she predicts the console output.",
     "25 transmitted — the squared reading came back from the subroutine and was printed to the console."),
    # 2 fill_blank – return keyword
    ("A boost subroutine is computing a doubled output but missing the keyword that transmits it back to the caller.",
     "With return inserted, the boosted value is now transmitted rather than discarded."),
    # 3 mcq – system_label returns greeting string
    ("Yara traces a labelling subroutine that returns a formatted string into a variable before it's displayed.",
     "Hello, Alice! — the label was returned, stored in msg, and printed to the console as expected."),
    # 4 arrange – max_val returns higher reading
    ("Yara builds a comparison subroutine that returns the higher of two power readings.",
     "The higher reading is selected and returned — Yara can now route the stronger signal automatically."),
    # 5 mcq – nothing() returns None
    ("Sana shows Yara a subroutine that runs but transmits nothing; Yara must identify what the caller receives.",
     "None — a subroutine without return sends nothing back, so Yara commits to always returning meaningful values."),
    # 6 fill_blank – % operator
    ("Yara needs a modulo check inside a subroutine to determine whether a sensor reading is even.",
     "The modulo operator is wired in; the parity check now returns True or False cleanly."),
    # 7 mcq – triple(triple(2)) = 18
    ("The drone boosts its output twice in sequence; Yara traces through both calls to find the final transmitted value.",
     "18 — the first boost returned 6 and the second amplified it to 18, demonstrating why return is essential for chaining."),
    # 8 mcq – clamp returns 100
    ("A safety-clamp subroutine limits power readings to valid bounds; Yara traces its return value for an over-limit input.",
     "100 — the clamp subroutine correctly capped the reading, preventing an out-of-range value from reaching other modules."),
    # 9 mini_code – celsius_to_fahrenheit
    ("The Helix's heat sensors speak Fahrenheit but the fuel data is in Celsius; Yara writes a conversion subroutine.",
     "212.0 and 32.0 confirmed — the calibration subroutine is ready and the thermal sensors are now in sync."),
    # 10 mini_code – power(base, exp)
    ("Yara needs a power-exponent subroutine to calculate exponential energy outputs for the ship's reactor simulations.",
     "1024 and 27 returned correctly — the energy subroutine is validated and cleared for use in the reactor model."),
])

apply_beats(L2, 'mystery', [
    # 0 concept
    ("Cole realises his analysis tools only print findings to the screen but can't hand the result to another tool; return is the missing piece.",
     "A combined score of 7 is stored in a variable — Cole sees that return is how one tool passes its finding to the next."),
    # 1 mcq – suspicion_score(5) returns 25
    ("Cole traces a scoring tool that squares a clue's weight and hands back the suspicion score.",
     "25 returned — the squared score came back from the tool, ready to be fed into further analysis."),
    # 2 fill_blank – return keyword
    ("A tool is computing a doubled suspicion rating but missing the keyword that hands it back to Cole.",
     "With return in place, the amplified rating is now handed back rather than silently discarded."),
    # 3 mcq – format_suspect returns string
    ("Cole traces a formatting tool that returns a labelled suspect string and stores it before printing.",
     "Hello, Alice! — the formatted label was returned, stored, and printed to the case file correctly."),
    # 4 arrange – max_val returns higher score
    ("Cole builds a comparison tool that returns the more suspicious of two clue scores.",
     "The higher score is returned — Cole can now automatically surface the most damning clue from any pair."),
    # 5 mcq – nothing() returns None
    ("A tool runs but hands back nothing; Cole must identify what Python gives the caller in that case.",
     "None — an empty report, and Cole notes this as a mistake to avoid when writing his own tools."),
    # 6 fill_blank – % operator
    ("Cole needs a remainder check inside a tool to determine whether a clue number splits evenly.",
     "The modulo operator is in place; the tool now returns True for even clue numbers and False for odd ones."),
    # 7 mcq – triple(triple(2)) = 18
    ("Cole multiplies a suspicion score by three, then triples the result again, and must trace the final number.",
     "18 — the chained triples work because each tool returned its result for the next one to use."),
    # 8 mcq – clamp returns 100
    ("A bounding tool keeps suspect scores within the valid range; Cole traces what it returns for an over-limit input.",
     "100 — the tool capped the score correctly, keeping the case file's numbers within valid bounds."),
    # 9 mini_code – celsius_to_fahrenheit
    ("Crime-scene temperature logs are in Celsius but the lab reports use Fahrenheit; Cole writes a conversion tool.",
     "212.0 and 32.0 confirmed — the conversion tool is ready and Cole can now cross-check temperature evidence instantly."),
    # 10 mini_code – power(base, exp)
    ("Cole needs an exponential scoring tool to calculate compounding suspicion ratings across multiple clues.",
     "1024 and 27 returned correctly — the scoring tool is ready, and Cole's analytical toolkit is growing fast."),
])


# ──────────────────────────────────────────────
# LESSON 3 – Multiple Parameters and Using Functions Together
# ──────────────────────────────────────────────
L3 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_5\\lesson_3.yaml"

apply_beats(L3, 'fantasy', [
    # 0 concept
    ("Master Theo shows Elara that a recipe can accept more than one ingredient, and that two recipes can work side-by-side on the same brew.",
     "20 and 18 — strength and cost both computed from one pair of ingredients, with each recipe doing exactly one job."),
    # 1 mcq – multiply(2,3,4) = 24
    ("Elara tries a three-ingredient recipe and predicts the combined potency when all three are multiplied.",
     "24 — three parameters work just like two, and the recipe handles them all in one line."),
    # 2 fill_blank – string concatenation
    ("Elara must join a potion name and its variant label into a single string inside a recipe.",
     "The full label is returned as one string — Elara can now name any variant of any potion."),
    # 3 mcq – default parameter greeting
    ("Theo shows a recipe with a default ingredient; Elara traces what it produces when called with only one argument.",
     "Hello, Alice! — the default greeting was used automatically, just as Theo's standard incantation promised."),
    # 4 arrange – tax(price, rate)
    ("Elara assembles a shop tax recipe that takes a price and a rate and returns the tax amount.",
     "The tax formula compiles correctly — Elara can now calculate the gold-coin cost for any potion at any rate."),
    # 5 mcq – double(triple(4)) = 24
    ("Theo chains a triple recipe inside a double recipe; Elara traces the final potency step by step.",
     "24 — triple brewed 12, then double amplified it to 24; Elara sees how chaining recipes multiplies power."),
    # 6 fill_blank – discount multiplication
    ("Elara must multiply a potion price by the discount rate to find the gold coins to subtract.",
     "The discount amount is calculated — Elara can now reduce any potion's price by any percentage."),
    # 7 mcq – add with default b=10
    ("Theo demonstrates a recipe with a default second ingredient; Elara traces outputs for two different calls.",
     "15 then 25 — the default is used once and overridden the next time, giving the recipe flexible behaviour."),
    # 8 mcq – bmi formula returns 22.9
    ("Elara tries a two-parameter density formula and predicts the rounded result it returns.",
     "22.9 — the formula handled two separate parameters and returned the precise density reading Theo needed."),
    # 9 mini_code – max_of_three
    ("Theo needs a recipe that accepts three potion potencies and returns the greatest; Elara writes it.",
     "9 and 5 returned correctly — the strongest-brew recipe works on any trio of potencies."),
    # 10 mini_code – celsius + fahrenheit conversion pair
    ("Master Theo needs two complementary temperature conversion recipes to calibrate the cauldron in either direction.",
     "32.0 and 100.0 confirmed — both conversion recipes work perfectly and the workshop can now translate temperatures freely."),
])

apply_beats(L3, 'scifi', [
    # 0 concept
    ("Sana shows Yara that sensor subroutines can accept multiple parameters and that chaining two modules gives the Helix richer data.",
     "20 and 18 — area and perimeter both computed from one scan pass, each module doing a single clean job."),
    # 1 mcq – multiply(2,3,4) = 24
    ("Yara runs a three-input multiply module and predicts the combined power output.",
     "24 — three power-level parameters multiply correctly and the combined output is ready for the next module."),
    # 2 fill_blank – string concatenation
    ("Yara must concatenate a system name and a module label into a single identifier string.",
     "The full identifier string is returned — Yara can now label any module in any subsystem."),
    # 3 mcq – default parameter greeting
    ("A boot subroutine has a default greeting message; Yara traces what it returns when called with one argument.",
     "Hello, Alice! — the default boot message was applied automatically, no extra argument needed."),
    # 4 arrange – tax(price, rate)
    ("Yara assembles a resource-cost subroutine that computes a percentage of any supply price.",
     "The cost formula is operational — Yara can now calculate the energy-credit overhead for any repair job."),
    # 5 mcq – double(triple(4)) = 24
    ("Two chained amplifier modules run in sequence; Yara traces the output that emerges from the chain.",
     "24 — triple returned 12, double boosted it to 24; chained subroutines compound the output exactly as expected."),
    # 6 fill_blank – discount multiplication
    ("Yara calculates the energy-credit savings by multiplying the repair cost by an efficiency percentage.",
     "The savings are computed — Yara can now budget any repair job with a precise efficiency discount."),
    # 7 mcq – add with default b=10
    ("A summing subroutine has a default second parameter; Yara traces two consecutive calls with different arguments.",
     "15 then 25 — the default works silently when omitted and is overridden cleanly when supplied."),
    # 8 mcq – bmi formula returns 22.9
    ("Yara runs a two-parameter structural-load formula and predicts the rounded output.",
     "22.9 — the subroutine handled both parameters correctly and the load reading is within safe limits."),
    # 9 mini_code – max_of_three
    ("Sana needs a subroutine that picks the highest of three power readings so the Helix always routes maximum energy.",
     "9 and 5 returned correctly — the peak-power subroutine is validated and ready for the routing system."),
    # 10 mini_code – celsius + fahrenheit conversion pair
    ("Yara must write two complementary thermal-conversion subroutines so the ship's sensors can work in either scale.",
     "32.0 and 100.0 confirmed — both conversion subroutines are calibrated and the Helix thermal system is now fully functional."),
])

apply_beats(L3, 'mystery', [
    # 0 concept
    ("Cole discovers that chaining two analysis tools on the same clue set gives him richer data than either tool alone.",
     "20 and 18 — weight and combined score both derived from the same evidence pair, each tool doing one precise job."),
    # 1 mcq – multiply(2,3,4) = 24
    ("Cole runs three clue weights through a multiplication tool and predicts the total suspicion product.",
     "24 — three parameters multiply cleanly and the combined suspicion score is ready for the case file."),
    # 2 fill_blank – string concatenation
    ("Cole must join a suspect's first and last names into a single string for the official report.",
     "The full name is assembled — Cole's tool can now format any suspect's identity correctly."),
    # 3 mcq – default parameter greeting
    ("A case-file greeting tool has a default salutation; Cole traces what it returns when only one argument is given.",
     "Hello, Alice! — the default greeting was applied automatically, keeping the case file consistent."),
    # 4 arrange – tax(price, rate)
    ("Cole assembles an informant-fee tool that calculates a percentage of any reward amount.",
     "The fee formula is ready — Cole can now compute the informant's cut for any reward at any agreed rate."),
    # 5 mcq – double(triple(4)) = 24
    ("Cole runs a suspicion score through a triple tool and then feeds the result into a double tool; he traces the output.",
     "24 — the two chained tools amplified the score from 4 to 12 to 24, confirming that return enables precise chaining."),
    # 6 fill_blank – discount multiplication
    ("Cole multiplies a reward by a tip-rate percentage to find the informant's precise cut.",
     "The cut is calculated — Cole can now settle informant payments to the cent, keeping every deal fair."),
    # 7 mcq – add with default b=10
    ("A scoring tool has a default second addend; Cole traces the output for two calls, one using the default and one overriding it.",
     "15 then 25 — defaults make tools flexible, and Cole notes he can always override them when the case demands it."),
    # 8 mcq – bmi formula returns 22.9
    ("Cole uses a two-parameter physical-profile tool to model a suspect's build and predicts the rounded result.",
     "22.9 — the tool handled both parameters and returned the profile metric Cole needed for the case file."),
    # 9 mini_code – max_of_three
    ("Cole needs a tool that picks the most damning of three clue scores so he can focus on the strongest lead.",
     "9 and 5 returned correctly — the peak-clue tool works on any trio and Cole can now rank evidence automatically."),
    # 10 mini_code – celsius + fahrenheit conversion pair
    ("Temperature evidence exists in two scales; Cole writes two conversion tools so he can translate freely in either direction.",
     "32.0 and 100.0 confirmed — both tools check out and Cole can now cross-reference any temperature reading on the case."),
])


# ──────────────────────────────────────────────
# LESSON 4 – Functions Returning Booleans
# ──────────────────────────────────────────────
L4 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_5\\lesson_4.yaml"

apply_beats(L4, 'fantasy', [
    # 0 concept
    ("Elara needs a way for her recipes to give a yes-or-no verdict — Master Theo introduces the Parity Oracle, a spell that returns True or False.",
     "True then False — the Oracle judges even and odd ingredient counts clearly, and Elara sees that functions can return truth itself."),
    # 1 mcq – is_positive(-3) returns False
    ("The Oracle tests whether a potion amount is above zero; Elara traces its verdict for a negative value.",
     "False — a negative amount means the ingredient is invalid, and the Oracle's boolean verdict makes that instantly clear."),
    # 2 fill_blank – > operator
    ("Elara must choose the right comparison rune so the Oracle returns True only for spell names longer than ten characters.",
     "The greater-than rune is inscribed; the Oracle now correctly judges long spell names from short ones."),
    # 3 mcq – is_adult(20) runs if block
    ("The Oracle approves apprentices who meet the minimum age; Elara traces what prints when the verdict is True.",
     "allowed — the Oracle returned True and the if block ran, letting the apprentice proceed."),
    # 4 arrange – is_divisible(n, d)
    ("Elara assembles an Oracle that tells her whether one ingredient quantity divides evenly into another.",
     "The divisibility Oracle is complete — Elara can now check any ingredient ratio with a single call."),
    # 5 mcq – both_positive(3, -1) returns False
    ("The Oracle checks two ingredient amounts at once; Elara traces its verdict when one of them is negative.",
     "False — both conditions must be True for the Oracle to approve, and one negative amount is enough to reject the brew."),
    # 6 fill_blank – and operator
    ("Elara must combine two conditions so the Oracle only returns True when a potion strength is within the safe range.",
     "The and rune binds both conditions — the Oracle now correctly validates any strength value between 0 and 100."),
    # 7 mcq – is_uppercase('HELLO') True, 'Hello' False
    ("The Oracle checks whether a spell word is shouted in all capital letters; Elara traces two verdicts.",
     "True then False — the Oracle tells Elara exactly which spell words meet the all-caps requirement."),
    # 8 mcq – why use boolean function
    ("Master Theo asks Elara why naming a condition as a function is better than writing it inline every time.",
     "A named Oracle like is_valid_ingredient makes the intent clear at a glance — Elara is convinced."),
    # 9 mini_code – is_palindrome
    ("Elara writes a palindrome Oracle that tells her whether a spell word reads the same forwards and backwards.",
     "racecar and madam pass; hello fails — the palindrome Oracle is ready to screen any spell name."),
    # 10 mini_code – is_prime
    ("Master Theo needs a prime Oracle to identify which ingredient potencies have no magical divisors.",
     "7 and 2 are prime, 9 is not — the prime Oracle is complete, and Elara's boolean spell library is now a powerful toolkit."),
])

apply_beats(L4, 'scifi', [
    # 0 concept
    ("Voss needs diagnostic checks that return a clear pass/fail signal rather than a number; she introduces Yara to boolean-returning subroutines.",
     "True then False — the parity diagnostic works on both even and odd sensor values, giving Yara a clean yes-or-no readout."),
    # 1 mcq – is_positive(-3) returns False
    ("Yara traces a positivity check on a sensor reading of -3 to see what the subroutine reports.",
     "False — a negative reading is flagged immediately by the diagnostic, and Yara appreciates how readable the boolean result is."),
    # 2 fill_blank – > operator
    ("Yara wires in the correct comparison operator so the subroutine flags log entries that are too long.",
     "The greater-than operator is in place; the log-length diagnostic now correctly identifies oversized entries."),
    # 3 mcq – is_adult(20) runs if block
    ("A crew-clearance check returns True for age 20; Yara traces whether the access block runs.",
     "allowed — the diagnostic returned True and the if block executed, granting the crew member access."),
    # 4 arrange – is_divisible(n, d)
    ("Yara assembles a divisibility check to determine whether a sensor reading divides cleanly by a given interval.",
     "The divisibility subroutine is operational — Yara can now check any reading against any interval with one call."),
    # 5 mcq – both_positive(3, -1) returns False
    ("Voss runs a dual-hull check; Yara traces the result when one of the two readings is negative.",
     "False — both readings must be positive for hull integrity to pass, and one bad reading fails the whole check."),
    # 6 fill_blank – and operator
    ("Yara combines two conditions with the right keyword so a hull-integrity score is only valid within bounds.",
     "The and operator ties both conditions together — the integrity check now correctly validates any score from 0 to 100."),
    # 7 mcq – is_uppercase('HELLO') True, 'Hello' False
    ("Voss checks whether status codes are formatted in all-uppercase protocol; Yara traces two results.",
     "True then False — HELLO passes protocol, Hello does not; Yara now knows which status strings need reformatting."),
    # 8 mcq – why use boolean function
    ("Voss asks Yara why wrapping a condition in a named subroutine is better than writing it inline every time.",
     "is_hull_safe(h) communicates intent far better than the raw condition — Yara agrees and commits to the pattern."),
    # 9 mini_code – is_palindrome
    ("Yara writes a palindrome check that will be used to validate symmetric command codes.",
     "racecar and madam pass; hello fails — the palindrome subroutine is validated and ready for the command-code system."),
    # 10 mini_code – is_prime
    ("Voss needs a prime-number diagnostic to identify prime-frequency channels for encrypted communications.",
     "7 and 2 are prime, 9 is not — the frequency diagnostic is complete, and Yara's boolean subroutine library is ready for deployment."),
])

apply_beats(L4, 'mystery', [
    # 0 concept
    ("Cole realises that instead of scattering raw conditions through his deduction code, he can write tools that simply answer True or False.",
     "True then False — the alibi-ID checker gives Cole a clear verdict at a glance, and he immediately sees the value of boolean tools."),
    # 1 mcq – is_positive(-3) returns False
    ("Cole runs a credibility-score tool on a witness with a negative score and traces the verdict.",
     "False — the negative score is rejected outright, and the boolean verdict keeps Cole's reasoning clean."),
    # 2 fill_blank – > operator
    ("Cole must choose the right comparison so the tool returns True only when an alibi statement is detailed enough.",
     "The greater-than operator is set — the tool now correctly flags short alibis that need more detail."),
    # 3 mcq – is_adult(20) runs if block
    ("A minimum-age check returns True for a 20-year-old suspect; Cole traces whether the case-proceeds block runs.",
     "allowed — the check returned True and the case moves forward; Cole notes the elegance of if plus a boolean tool."),
    # 4 arrange – is_divisible(n, d)
    ("Cole assembles a timeline-divisibility tool to detect whether a suspect's schedule has evenly-spaced gaps.",
     "The divisibility tool is ready — Cole can now flag any timeline with regular intervals that might hint at a pattern."),
    # 5 mcq – both_positive(3, -1) returns False
    ("Cole verifies two pieces of evidence simultaneously; he traces the result when one clue score is negative.",
     "False — both clues must be positive for the evidence to hold, and one bad number sinks the whole argument."),
    # 6 fill_blank – and operator
    ("Cole combines two conditions so his credibility tool only approves scores within the valid range.",
     "The and operator binds both bounds — the tool now correctly validates any credibility score from 0 to 100."),
    # 7 mcq – is_uppercase('HELLO') True, 'Hello' False
    ("Cole checks whether a suspect's name has been entered in all-uppercase as required by the case-file format.",
     "True then False — HELLO is properly formatted, Hello is not; Cole flags the inconsistency in the file."),
    # 8 mcq – why use boolean function
    ("Cole reflects on why naming a condition as a tool is clearer than writing the raw comparison every time.",
     "is_alibi_valid(a) reads like a question you'd ask in an interview — Cole adopts the pattern for every future check."),
    # 9 mini_code – is_palindrome
    ("Cole notices the killer's code phrases may be palindromes; he writes a tool to test any string instantly.",
     "racecar and madam are flagged; hello is clear — the palindrome tool is in Cole's kit and could crack the next message."),
    # 10 mini_code – is_prime
    ("The suspect used prime-numbered lockers to hide evidence; Cole writes a prime tool to identify them all.",
     "7 and 2 are prime, 9 is not — the prime tool is ready, and Cole's boolean toolkit can now answer almost any yes-or-no question the case throws at him."),
])


# ──────────────────────────────────────────────
# LESSON 5 – Functions Calling Functions
# ──────────────────────────────────────────────
L5 = "C:\\Users\\pyrot\\Documents\\Coding\\python-learner\\content\\units\\unit_5\\lesson_5.yaml"

apply_beats(L5, 'fantasy', [
    # 0 concept
    ("Elara has a library of tested spells; Master Theo shows her that a compound enchantment can call smaller spells from within, building complex magic from simple pieces.",
     "True — the absolute-zero compound spell called the helper conversion and returned a clear verdict; Elara is amazed at how spells can nest."),
    # 1 mcq – quadruple calls double twice
    ("A quadrupling spell doubles its result twice by calling the double spell from inside; Elara traces the final potency.",
     "12 — double(3)=6, double(6)=12; Elara sees that calling one spell from inside another is both clean and powerful."),
    # 2 fill_blank – call square helper
    ("Elara must name the helper spell that squares each ingredient before the two squares are summed.",
     "The square helper is called twice — the sum_of_squares compound spell now works correctly."),
    # 3 mcq – total calls add twice
    ("Three potion ingredients are combined by calling the add spell twice in sequence; Elara traces the total.",
     "6 — add(1,2)=3, add(3,3)=6; the pattern of building totals by chaining helper calls is clear."),
    # 4 arrange – hypotenuse uses square
    ("Elara assembles a compound spell that calculates a magical distance by calling the square helper and then taking a root.",
     "The hypotenuse spell is complete — it calls square for each side and combines the results, all in one elegant incantation."),
    # 5 mcq – count_even calls is_even
    ("Elara counts the even-numbered spell slots by calling is_even for every slot; she predicts the total count.",
     "3 — slots 2, 4, and 6 are even; the counting spell relies on the boolean is_even spell to do its work."),
    # 6 fill_blank – call negate helper
    ("Elara names the helper spell that flips a True to False so her odd-check spell is the inverse of is_even.",
     "negate is called with the even result — is_odd now correctly returns the opposite verdict."),
    # 7 mcq – why compose spells
    ("Master Theo asks Elara what the main benefit is of casting one spell from inside another.",
     "Code reuse — Elara doesn't repeat logic, she just calls the spell she already wrote; Theo nods approvingly."),
    # 8 mcq – normalize calls clamp
    ("A normalising spell calls the clamp spell to keep a power value within safe bounds; Elara traces the result.",
     "100 — the normalising spell delegated the clamping to clamp and returned the safe maximum, exactly as designed."),
    # 9 mini_code – is_odd calls is_even
    ("Elara writes is_odd as a spell that calls is_even and flips its answer, reusing the work she already did.",
     "All three tests pass — is_odd correctly delegates to is_even, and Elara's spell library grows without any duplicated logic."),
    # 10 mini_code – factorial recursion
    ("Master Theo introduces Elara to a factorial spell that calls itself — a spell that casts itself to compute growing potency.",
     "120 and 6 confirmed — the recursive factorial spell works perfectly, and Elara has mastered the deepest form of spell composition."),
])

apply_beats(L5, 'scifi', [
    # 0 concept
    ("Voss shows Yara that complex ship diagnostics can be built by calling smaller, already-tested subroutines from inside new ones.",
     "True — the absolute-zero check called the conversion subroutine internally; Yara immediately sees the elegance of composed subroutines."),
    # 1 mcq – quadruple calls double twice
    ("A quadruple-output subroutine calls double twice in sequence; Yara traces the final transmitted value.",
     "12 — double(3)=6, double(6)=12; nesting subroutine calls compounds the output without writing new logic."),
    # 2 fill_blank – call square helper
    ("Yara must name the helper subroutine that squares each sensor reading before summing the two results.",
     "The square helper is called twice and the sum_of_squares subroutine now works correctly."),
    # 3 mcq – total calls add twice
    ("Three subsystem outputs are totalled by chaining two add calls; Yara traces the combined result.",
     "6 — add(1,2)=3, add(3,3)=6; chaining the same helper twice avoids writing a new three-input subroutine from scratch."),
    # 4 arrange – hypotenuse uses square
    ("Yara assembles a navigation subroutine that computes distance by calling the square helper and then rooting the sum.",
     "The hypotenuse subroutine is operational — it reuses square for both legs and returns the precise distance."),
    # 5 mcq – count_even calls is_even
    ("Voss counts the even-numbered active modules by calling is_even for each module ID; Yara predicts the count.",
     "3 — modules 2, 4, and 6 are even; the counter subroutine delegates the individual check to is_even cleanly."),
    # 6 fill_blank – call negate helper
    ("Yara names the helper subroutine that flips a boolean so is_odd reports the opposite of is_even.",
     "negate is called with the even result — is_odd now correctly identifies odd module IDs."),
    # 7 mcq – why compose subroutines
    ("Voss asks Yara what the principal engineering advantage is of calling a subroutine from inside another.",
     "Code reuse — Yara doesn't duplicate logic, she calls what she already wrote; the Helix codebase stays lean."),
    # 8 mcq – normalize calls clamp
    ("A normalise subroutine delegates boundary enforcement to clamp; Yara traces the output for an over-limit input.",
     "100 — normalise called clamp and received the capped value back, keeping the reading within safe operational limits."),
    # 9 mini_code – is_odd calls is_even
    ("Yara codes is_odd to call is_even and flip its result, so no parity logic is ever duplicated.",
     "All three tests pass — is_odd reuses is_even perfectly, and Yara's subroutine library is composable and clean."),
    # 10 mini_code – factorial recursion
    ("Voss challenges Yara with a self-calling factorial subroutine that computes exponential values by calling itself.",
     "120 and 6 confirmed — the recursive subroutine works, and Yara has unlocked the most powerful form of subroutine composition on the Helix."),
])

apply_beats(L5, 'mystery', [
    # 0 concept
    ("Cole realises that his best deductions are built from smaller conclusions; he learns to call one tool from inside another to create layered reasoning.",
     "True — the absolute-zero deduction called a helper tool internally and returned a precise verdict; Cole files this technique immediately."),
    # 1 mcq – quadruple calls double twice
    ("A lead's strength is amplified twice by calling the double tool from inside another tool; Cole traces the final score.",
     "12 — double(3)=6, double(6)=12; Cole sees that each call hands its result to the next, just like building a chain of deductions."),
    # 2 fill_blank – call square helper
    ("Cole must name the helper tool that squares each clue weight before the two squares are summed into one suspicion score.",
     "The square helper is invoked twice — sum_of_squares now correctly compounds the two clue weights."),
    # 3 mcq – total calls add twice
    ("Three witness credibility scores are combined by chaining two add calls; Cole traces the final total.",
     "6 — add(1,2)=3, add(3,3)=6; three scores combined through two helper calls, no new logic needed."),
    # 4 arrange – hypotenuse uses square
    ("Cole assembles a geometric tool that calculates the straight-line distance between two locations by calling the square helper.",
     "The distance tool is ready — it calls square for each coordinate offset and returns the precise separation between sites."),
    # 5 mcq – count_even calls is_even
    ("Cole counts the even-numbered evidence items in a batch by calling is_even for each one; he predicts the total.",
     "3 — items 2, 4, and 6 are even; the counting tool delegates individual parity checks to is_even without any repeated code."),
    # 6 fill_blank – call negate helper
    ("Cole names the helper tool that flips a boolean so is_odd correctly identifies clues that don't pass the even check.",
     "negate is wired in — is_odd now returns the inverse of is_even and Cole can classify any clue number instantly."),
    # 7 mcq – why compose tools
    ("Cole reflects on why the best investigative tools are built from smaller, reusable ones rather than written from scratch.",
     "Code reuse — Cole doesn't rewrite logic he already has, he calls it; every tool in his kit earns its place."),
    # 8 mcq – normalize calls clamp
    ("A bounding tool calls clamp internally to keep a suspect score within the valid range; Cole traces the output.",
     "100 — the bounding tool delegated to clamp and returned the capped score, keeping the case file's numbers clean."),
    # 9 mini_code – is_odd calls is_even
    ("Cole writes is_odd to call is_even and flip the result, avoiding any duplicated parity logic in his toolkit.",
     "All three tests pass — is_odd reuses is_even perfectly, and Cole's toolkit now has layered tools that build on each other."),
    # 10 mini_code – factorial recursion
    ("Cole discovers that a suspect's code uses factorial numbers; he writes a self-calling tool to generate them.",
     "120 and 6 confirmed — the recursive factorial tool works, and Cole has cracked the code sequence, closing the final gap in the case."),
])

print("All done!")
