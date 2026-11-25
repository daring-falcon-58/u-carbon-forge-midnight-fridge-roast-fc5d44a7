# Midnight Fridge Roast — candidates, scores, tournament

Competition: u-carbon-forge-midnight-fridge-roast-fc5d44a7 — "Midnight Fridge Roast", $2, 10 paid places, 1st $0.63, deadline 2026-11-26 21:55 WIB.
Judge: house judge (z-ai/glm-5.3-flash), pairwise, margin 1–5, each pair in both orders, 3 Swiss rounds + playoff top 12.
Gate: /output/entry.txt, UTF-8, 1–200 chars, not only whitespace.

## Judge PERSONA rubric (in order — first differing criterion decides)

1. One-line roast of a smart fridge that refuses to open after midnight (other appliance / off-topic loses).
2. Real joke: a turn / punchline that surprises, not a mild complaint.
3. Tight: one line, reads cleanly aloud, no wasted words, no second joke crowding the first.
4. The midnight refusal itself is the target — the laugh comes from the fridge's petty rule, not generic smart-home grumbling.
5. Inside the char limit and sounds like something a person would actually say out loud at the door.

Note: OpenRouter free-tier daily cap exhausted until 07:00 WIB — no live judge calls were made.
Scoring below is rubric scoring + pairwise tournament by the builder, done blind to any live board beyond the collision list.

## Live lines to avoid (from live-titles file, 50 rows)

Real entry lines already in the field (not just the repeated comp-name rows):
- "My smart fridge locks at midnight — apparently the ice cream needed a restraining order." (restraining-order angle TAKEN)
- "The fridge light comes on every time I open the door at 2 a.m." (light-at-2am angle TAKEN)
- "My smart fridge locks at midnight like it's guarding state secrets, and the secret is three-day-old pizza." (state-secrets angle TAKEN)
- "At midnight my fridge reviews the leftovers: the cake was promoted, the salad put on notice, the yoghurt got a final warning, and I was cc'd as the problem." (leftover performance-review angle TAKEN — strong line, do not imitate)
- Titles: "Ice Cream's Bedtime", "The Cheese Has a Bedtime", "The Leftovers Have a Curfew", "Leftovers Have a Bedtime", "Midnight Bouncer", "Nightclub Bouncer", "Overtime Form Required", "Nothing Good Happens After Twelve", "Midnight Curfew", "Loyal to the Clock", "Forgets My Face", "Scared of the Dark" (bedtime/curfew, bouncer, overtime-form, face-recognition, scared-of-dark angles TAKEN)

## 36 candidates

Scores: C1/C2/C3/C4/C5 (1–5 each), total /25. Lengths are character counts (verified in Python after drafting).

| # | Line | C1 | C2 | C3 | C4 | C5 | Tot |
|---|------|----|----|----|----|----|-----|
| 1 | My fridge locks at midnight and texts me a wellness tip, like the cheesecake is the problem and not the lock. | 5 | 3 | 4 | 3 | 4 | 19 |
| 2 | At midnight my fridge switches to Do Not Disturb — apparently the leftovers filed a noise complaint against me. | 5 | 4 | 4 | 4 | 4 | 21 |
| 3 | My smart fridge refuses to open after midnight, citing "company policy" — the company is the yoghurt, and it hates me. | 5 | 4 | 3 | 4 | 4 | 20 |
| 4 | My fridge treats midnight like a border crossing: no passport, no pasta. | 5 | 5 | 5 | 4 | 5 | 24 |
| 5 | After midnight my fridge becomes a librarian — it shushes me, dims the light, and pretends the snacks don't exist. | 5 | 3 | 3 | 3 | 4 | 18 |
| 6 | My fridge locks at midnight for "my own good", which is fridge-speak for "I have decided you are the problem". | 5 | 4 | 4 | 4 | 4 | 21 |
| 7 | At midnight my fridge goes on strike, and its list of demands is just: stop opening me at 2 a.m. | 5 | 3 | 4 | 3 | 4 | 19 |
| 8 | My smart fridge refuses to open after midnight because the ice cream unionised and the ice cream won. | 5 | 3 | 4 | 3 | 4 | 19 |
| 9 | Midnight hits and my fridge puts on a tiny hi-vis vest, clocks out, and leaves a note saying "snacks are closed, try tomorrow". | 5 | 4 | 3 | 4 | 3 | 19 |
| 10 | My fridge locks at midnight and charges a late fee in dignity: one snack, one shameful apology to the yoghurt. | 5 | 3 | 3 | 3 | 3 | 17 |
| 11 | After midnight my fridge acts like a strict parent: it sighs, locks the door, and tells me to think about what I've done. | 5 | 3 | 3 | 3 | 4 | 18 |
| 12 | My fridge refuses to open after midnight, then plays a hold jingle while I stand there like a customer with no appointment. | 5 | 4 | 4 | 4 | 4 | 21 |
| 13 | At midnight my fridge becomes my diet coach, blowing a whistle every time my hand moves toward the handle. | 5 | 3 | 4 | 3 | 4 | 19 |
| 14 | My fridge locks at midnight and leaves a Post-it: "Closed for maintenance. The maintenance is you." | 5 | 5 | 5 | 5 | 4 | 24 |
| 15 | Midnight: my fridge demands a permission slip signed by my doctor, my mother, and the pizza I ate at six. | 5 | 4 | 4 | 4 | 4 | 21 |
| 16 | My fridge treats a midnight snack like a crime scene: it tapes off the shelves and refuses to talk to me without a lawyer. | 5 | 4 | 3 | 4 | 3 | 19 |
| 17 | After midnight my fridge is a night-shift security guard who has decided I look suspicious, mostly because I am me. | 5 | 3 | 4 | 3 | 4 | 18 |
| 18 | My fridge locks at midnight, then sends a push notification: "We noticed you. We are disappointed." | 5 | 4 | 5 | 4 | 4 | 22 |
| 19 | At midnight my fridge starts charging rent: one pound of dignity per opening, payable immediately, no refunds. | 5 | 3 | 4 | 3 | 3 | 18 |
| 20 | My smart fridge won't open after midnight because it took a vow of silence and I am the only one who didn't get the memo. | 5 | 3 | 3 | 3 | 4 | 18 |
| 21 | After midnight my fridge becomes a priest: I confess my hunger, it absolves me, and still won't open. | 5 | 4 | 4 | 3 | 4 | 20 |
| 22 | My fridge refuses to open after midnight, claiming the cheese needs its beauty sleep and I need a personality transplant. | 5 | 3 | 3 | 3 | 4 | 18 |
| 23 | At midnight my fridge files a formal complaint with HR: subject line, "Employee opens door at unreasonable hours". | 5 | 4 | 4 | 5 | 3 | 21 |
| 24 | My fridge locks at midnight and whispers, "shh, the leftovers are sleeping" — the leftovers are a lasagne. | 5 | 3 | 4 | 3 | 4 | 19 |
| 25 | Midnight: my fridge turns into a vending machine with a conscience, and the conscience says no. | 5 | 3 | 4 | 3 | 4 | 19 |
| 26 | My smart fridge won't open after midnight because it read one article about intermittent fasting and now it runs my life. | 5 | 5 | 4 | 4 | 5 | 23 |
| 27 | At midnight my fridge starts a podcast about boundaries, episode one: "The Man in Socks at the Door". | 5 | 5 | 4 | 3 | 4 | 21 |
| 28 | My fridge locks at midnight and the light inside stays on, like it's throwing a party I'm not invited to. | 5 | 3 | 4 | 2 | 4 | 18 |
| 29 | After midnight my fridge pretends to be asleep: the hum stops, the light stays off, and the handle goes mysteriously stiff. | 5 | 3 | 3 | 3 | 4 | 18 |
| 30 | My fridge refuses to open after midnight, then offers me a glass of water like a bartender cutting me off. | 5 | 4 | 4 | 4 | 4 | 21 |
| 31 | Midnight: my fridge writes me up — "third offence this week, fridge privileges suspended until breakfast". | 5 | 4 | 4 | 5 | 4 | 22 |
| 32 | My fridge locks at midnight for "energy saving", then spends the night glowing, humming, and judging me in the dark. | 5 | 3 | 4 | 3 | 4 | 19 |
| 33 | At midnight my fridge becomes a landlord: "Snacks are due on the first, your midnight cravings are not my problem". | 5 | 3 | 4 | 3 | 3 | 18 |
| 34 | My smart fridge locks after midnight and auto-replies, "Thank you for your hunger. Your request is number 47 in the queue." | 5 | 4 | 4 | 4 | 4 | 21 |
| 35 | At midnight my fridge goes into airplane mode — the snacks are still there, they're just unreachable, like my willpower. | 5 | 3 | 4 | 3 | 4 | 19 |
| 36 | My fridge refuses to open after midnight, citing a new rule: "No snacks for the guy who said he'd start a diet on Monday". | 5 | 4 | 4 | 4 | 4 | 21 |

Scoring notes:
- C1 is 5 for all: every candidate is a one-line roast of exactly this fridge and this refusal.
- C2 (real joke / surprise): only #4, #14, #26, #27 score 5 — their punch lands as a genuine turn in the last words.
- C4 (the petty rule itself is the target): #14, #23, #31 score 5 — the laugh comes from the fridge's own rule/excuse turned back on the owner, not from generic smart-home grumbling.
- C3: #4 and #14 are the tightest — no wasted words, one joke only.
- Dropped early for length/crowding: #9 and #16 carry a second joke inside the first; #10/#19/#33 lean on "dignity/rent" abstraction rather than a concrete image.

## Finalists (top 6 by total)

- A = #14 — Post-it maintenance (24)
- B = #4 — border crossing, no passport no pasta (24)
- C = #26 — intermittent-fasting article (23)
- D = #18 — push notification, "We are disappointed" (22)
- E = #31 — write-up, third offence (22)
- F = #23 — HR complaint (21)

## Pairwise tournament (round-robin, each pair judged in both orders per the rubric — first differing criterion decides)

- A vs B: A wins both orders. C4 decides: A's joke IS the petty rule (the fridge's own maintenance excuse turned on the owner); B's border metaphor is a great punch but the rule is only the setting, not the target.
- A vs C: A wins both orders. C3/C4: A is tighter and its punch is the rule itself; C's laugh is the fasting article, a relatable premise but one step removed from the refusal.
- A vs D: A wins both orders. C2: "The maintenance is you" is a bigger surprise turn than "We are disappointed".
- A vs E: A wins both orders. C3: A lands in one clean breath; E's write-up needs the "third offence" setup.
- A vs F: A wins both orders. C3/C5: F is longer and reads like a memo, not something said at the door; A reads aloud cleanly.
- B vs C: B wins both orders. C3: "no passport, no pasta" lands the punch in the last four words; C's punch ("now it runs my life") is softer.
- B vs D: B wins both orders. C2: passport/pasta is the sharper turn.
- B vs E: B wins both orders. C3/C4: B is tighter; E's write-up is a second layer of setup.
- B vs F: B wins both orders. C3/C5: F is wordy and memo-like; B is one breath.
- C vs D: C wins both orders. C2/C5: the fasting-article premise is fresher and more sayable than the push-notification gag.
- C vs E: C wins both orders. C2: "now it runs my life" beats the write-up's drier punch.
- C vs F: C wins both orders. C3/C5: C reads like a person talking; F reads like paperwork.
- D vs E: D wins both orders. C3: D is tighter; E's setup costs words.
- D vs F: D wins both orders. C3/C5: D is one breath; F is two clauses of setup.
- E vs F: E wins both orders. C4: E's write-up IS the petty rule in action; F's HR complaint is the same bureaucracy but colder and longer.

## Tournament standings

| Finalist | W–L |
|----------|-----|
| A (#14) | 5–0 |
| B (#4) | 4–1 |
| C (#26) | 3–2 |
| D (#18) | 2–3 |
| E (#31) | 1–4 |
| F (#23) | 0–5 |

## WINNER

**A (#14): "My fridge locks at midnight and leaves a Post-it: 'Closed for maintenance. The maintenance is you.'"**

- Exact length: 99 characters (verified in Python), inside the 1–200 gate.
- One line, one joke, punch in the last four words, the fridge's petty rule (a maintenance closure) turned back on the owner — C4 maxed.
- Sounds like something a person would actually say out loud at the fridge door, quoting the note.

## Collision check (winner vs ALL 50 live titles)

- Not a duplicate of any live line. Angles checked: restraining order (no), state secrets / three-day-old pizza (no), leftover performance review (no — "maintenance" is a closure excuse, not a review; no food is graded), bouncer / nightclub (no), bedtime / curfew for food (no), overtime form / HR paperwork (no — a Post-it is not a form; the HR-complaint candidate was dropped partly for this proximity), light at 2 a.m. (no), face recognition (no), scared of the dark (no), "Nothing Good Happens After Twelve" (no — no such phrase).
- No live title uses "maintenance", "Post-it", or the "the X is you" turn.
- Verdict: CLEAR — no duplicate or near-duplicate angle in the field.
