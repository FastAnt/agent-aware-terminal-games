# FACTS.md — how to author fact cards (the 500-fact campaign)

Fact cards are the unscored content type: the pane shows the
fact, the reader thinks for a moment, presses **Skip / Next**.
No question, no answer, no points. A fact earns its place by
being *interesting*: surprising, true, and explained.

This file is canonical for facts. `AGENTS.md` has the general
content rules; the engine contract lives in the main repo
(`backend/app/content_engine.py`, `validate_pack()`).

## The format

One fact per file, JSON, in this repo:

```json
{
  "type": "fact",
  "id": "physics-fact-venus-day-001",
  "kicker": "FACT",
  "topic": "Physics",
  "title": "A Venusian day outlasts its year",
  "body": "Venus rotates so slowly that one full spin takes 243 Earth days — longer than the 225 days it needs to orbit the Sun. The rotation is also retrograde: on Venus, the Sun rises in the west.",
  "source_hint": "IAU planetary rotation/orbit data"
}
```

Field rules:
- `type`: always `"fact"`. `id` = file stem, never changes.
- File name: `<topic>-fact-<slug>-<NNN>.json`
  (e.g. `math-fact-pi-001.json`). NNN is per-slug-family.
- `title` ≤ 60 chars: the hook, a statement (not a question).
- `body`: 2–4 sentences, ~40–70 words. The fact **plus why it
  is true or why it matters**. No questions to the reader.
- `source_hint`: required. Name where a reviewer can check the
  claim — a standard, paper, doc, or well-known historical
  record. *No source you can name → no card.*

## What makes a fact interesting (the bar)

A fact passes if a smart developer would say "huh, really?"
and walk away knowing something. Concretely:

1. **Surprising or counterintuitive.** Scale shocks ("GPS
   clocks gain 38 µs/day from relativity; uncorrected, GPS
   would drift ~10 km daily"), paradoxes (0.999… = 1),
   inversions (Venus's day > its year).
2. **It has a mechanism.** State *why*, not just *what*. "The
   first computer bug was a moth" is trivia; "…a moth taped
   into Harvard's 1947 logbook — though Edison already called
   faults 'bugs'" teaches something.
3. **Concrete numbers, honestly rounded.** Exact where known,
   "about/roughly" where not. **Never invent precision.** If
   you are not sure a number is right, verify it or drop the
   fact — a wrong fact is worse than no fact.
4. **Evergreen.** No versions, no "recently", no benchmarks of
   current hardware. It must read true in five years. (Time-
   sensitive items are `news`, a different type.)
5. **One idea per card.** If you need "and also…", that's a
   second card.

Fails the bar: definitions ("HTTP is a protocol"), bare
vocabulary, self-evident statements, listicles compressed into
one card, and rewordings of facts already in the catalogue.

## The 500-fact campaign

Target ~500 fact cards, quotas by topic:

| Topic prefix | Target | Angles to mine |
| --- | ---: | --- |
| programming | 110 | language history, famous bugs, algorithms' origins, complexity surprises |
| math | 80 | paradoxes, constants, proofs with a punchline, estimation |
| physics | 80 | scale, relativity, quantum oddities, units & constants |
| architecture | 70 | distributed-systems lessons, famous outages' root causes, protocols |
| ml | 60 | training surprises, data quirks, history of ideas |
| geometry | 50 | impossible figures, map projections, packing, curves |
| audio | 20 | hearing, codecs, sampling, instruments |
| cloud | 15 | latency numbers, failure modes, data-transfer physics |
| security | 15 | crypto history, famous flaws, attack mechanics |

Work in **batches of 25** (one topic per batch is fine):

1. Read `FACTS_INDEX.md` (create it with your first batch) and
   grep existing titles/bodies — no near-duplicates. Same fact
   at a different angle still counts as a duplicate unless the
   *mechanism* differs.
2. Write the 25 files.
3. Test: `python3 tools/test_game.py games-base/<each new file>`
   (or the whole dir at batch end). Facts must validate and
   must not score.
4. Append one line per fact to `FACTS_INDEX.md`:
   `id · topic · one-line hook`.
5. Commit the batch: `Facts: <topic> batch N (25)`.

Calibration: the three facts already in this repo
(`audio-fact-sample-rate-001`, `physics-fact-venus-day-001`,
`programming-fact-first-bug-001`) are the style reference —
match their length, tone, and sourcing.

## Rules that never bend

- Facts are true or they don't ship. Verify uncertain claims
  from knowledge you trust; when in doubt, choose another fact.
- English. Monochrome world: no emoji, no exclamation marks.
- Stable ids forever — progress and the index key on them.
- Facts never ask, quiz, or score. If it has an answer, it's a
  `game`, not a fact.
