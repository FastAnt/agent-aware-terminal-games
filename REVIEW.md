# Review — 2026-11-01 night batch (102 new games)

Reviewed by: the terminal team, 2026-11-01. Method:
`tools/test_game.py` on all files (105/105 pass technically —
loading, playthrough, click probes, motion), contact sheets of
all 105 dark previews, full-size spot checks, and a meta audit
of every question. This file is the feedback to work from.

## Headline

The style is right (monochrome, calm, theme-safe) and everything
*works*. But most scenes are not *about* their question. The
batch was built from ~11 recycled scene templates stamped onto
unrelated questions. A player sees the same picture for cache,
cubes, factorials and SQL. That breaks the one promise of this
pane: the picture helps you think about THIS question.

Verdicts on the 102 new games: **KEEP 24 · FIX 35 · REDO 43.**
(The 3 original games are not reviewed here.)

## Process failures (fix these first)

1. **Nothing was committed** — 104 files sat uncommitted in the
   working tree. Commit per batch, as the task said.
2. **No INDEX.md** was created. The ledger is how 300 games
   avoid repeating mechanics; start it now, backfill this batch.
3. **105 of 300 games**, and **zero about our project** (the
   brief required ≥40). Definition-recall trivia is fine as
   filler, but project games are the point of the feature.
4. Questions that say "Click the polygon…" must show polygons.
   Several games ask to click things that are not on screen
   (you click a text label in a triangle instead).

## The template problem

| Template | Used for (examples) | Count |
| --- | --- | --- |
| 4×4 grey grid | cache, cube faces, symmetry, factorial, precision, supervised, pressure, SQL… | ~9 |
| 6 grey bars | scaling, gcd, lcm, median, friction, kinetic energy, momentum, bubble sort… (identical heights everywhere — the bars never sort) | ~9 |
| sine wave | parallel lines (!), supplementary angles (!), absolute value (!), activation, overfitting | ~6 |
| dot spiral | similar shapes, Gauss sum, next prime, epoch, density | ~6 |
| floating circles | backup, radius, percent, clustering, floating, Newton's 3rd | ~6 |
| empty triangle | equilateral, Pythagoras, right angle, triangle area, slope | ~5 |
| orbits + sun | Earth/Jupiter/Mars/Venus/Mercury + generalization | ~6 |
| network mesh | load balancer, microservices, REST, DNS, hash, 404, linked list, parallel voltage | ~8 |
| 3-box triangle | gateway, MVC clone, hexagon sides, stack ops, Ohm's law… | ~12 |
| hill/parabola | derivative, loss, regression, free fall, projectile | ~5 |
| 5 bit squares | authn, binary 13, log2, power, boolean AND, const/var | ~6 |

New rule, non-negotiable: **a scene must depict the object the
question is about.** A template may be reused only when it *is*
the subject (a tree for tree questions, bits for binary). If the
scene would work unchanged for a different question, it is
wrong for both.

## Consolidate (duplicates)

- `architecture-mvc-001` — same question as base
  `architecture_mvc.py`. Delete.
- `physics-orbits-001` — same question as base
  `physics_orbits.py` (Mercury). Delete.
- `ml-gradient-001` — the base game already asks the gradient
  formula. Retarget (e.g. descent steps on a hill) or delete.
- Planet family `physics-earth/jupiter/mars/venus-orbit-001`:
  one mechanic, four copies. Keep at most two, label the
  planets, vary the rings by real order/distance — or fold
  into one game.

## Per-game verdicts

### KEEP (scene fits; polish only if noted)

| Game | Note |
| --- | --- |
| architecture-api-gateway-001 | add a Client node on the left |
| architecture-database-store-001 | — |
| architecture-db-index-001 | put key values inside tree nodes |
| geometry-triangle-angles-001 | add angle arcs that gather to 180° |
| math-binary-13-001 | label bit weights 8·4·2·1 |
| math-derivative-x2-001 | a tangent line sliding along the curve |
| math-fibonacci-next-001 | show 1,1,2,3,5 near the spiral |
| math-log2-32-001 | — |
| math-next-prime-001 | highlight the primes on the spiral |
| ml-classification-001 | — |
| ml-loss-function-001 | a ball descending the hill |
| ml-regression-output-001 | scatter points + fitted line, not a bare hill |
| physics-current-unit-001 | — |
| physics-electron-shell-001 | — |
| physics-energy-conversion-001 | label KE / PE at the swing ends |
| physics-pendulum-period-001 | — |
| physics-projectile-angle-001 | — |
| physics-sound-vacuum-001 | fade the wave out in the vacuum half |
| physics-wave-speed-001 | mark one wavelength λ |
| programming-bst-left-001 | — |
| programming-get-request-001 | — |
| programming-git-commit-001 | a commit chain reads better than a tree |
| programming-recursion-base-001 | — |
| programming-sql-select-001 | highlight the selected rows |

### FIX (right family, concrete defect named)

| Game | Fix |
| --- | --- |
| architecture-cache-purpose-001 | grid becomes cache lines that light up on hits |
| architecture-cdn-role-001 | label the centre Origin and the dots Edge nodes |
| architecture-horizontal-scaling-001 | show server boxes multiplying, not bare bars |
| architecture-message-queue-001 | FIFO cells with messages entering/leaving |
| architecture-microservices-001 | same mesh as 3 others — label services, distinct layout |
| geometry-circumference-001 | one circle; a dot travels it; mark C = 2πr |
| geometry-equilateral-angles-001 | equal-side ticks + 60° angle arcs |
| geometry-pythagoras-345-001 | right-angle marker + side labels 3·4·5 |
| geometry-right-angle-001 | animate an angle opening to exactly 90° |
| geometry-triangle-area-001 | shade base × height |
| math-even-number-001 | numbers as plain cards; drop the fake diagram arrows |
| math-gcd-12-18-001 | two number lines, divisor ticks meeting at 6 |
| math-lcm-4-6-001 | rows of multiples aligning at 12 |
| math-marble-probability-001 | a jar of marbles with counts per shade |
| math-median-379-001 | number cards that sort; the middle one glows |
| math-power-2-5-001 | doubling cascade 2→4→8→16→32 |
| math-prime-29-001 | same card treatment as even-number |
| math-square-sequence-001 | growing squares sized 1·4·9·16 |
| ml-activation-001 | draw a sigmoid, not a sine |
| ml-clustering-001 | dots drift into 3 visible clusters |
| ml-feature-001 | one data row: features in, label out |
| ml-overfitting-001 | points with a too-wiggly fit vs a smooth one |
| ml-precision-001 | a labelled 2×2 confusion matrix, not 4×4 noise |
| ml-test-split-001 | one bar split 80/20 with labels |
| physics-free-fall-001 | vertical drop with accelerating spacing (current arc reads as projectile) |
| physics-kinetic-energy-001 | a moving block; show speed doubling → energy ×4 |
| programming-binary-search-001 | sorted labelled bars; animate the halving mid |
| programming-boolean-and-001 | an AND truth table (4 rows) |
| programming-bubble-sort-001 | the bars must actually bubble-sort (they currently never move) |
| programming-compiler-role-001 | flow boxes: source → compiler → machine code |
| programming-queue-fifo-001 | a visible queue; the front item exits |
| programming-stable-sort-001 | labelled equal keys that keep their order |
| programming-stack-pop-001 | a vertical stack; the top element pops off |
| programming-tree-root-001 | draw the tree (your BST scene) with the root marked |
| physics-earth-orbit-001 | planet labels + family dedupe (see Consolidate) |
| physics-jupiter-orbit-001 | planet labels + family dedupe |
| physics-mars-orbit-001 | planet labels + family dedupe |
| physics-venus-orbit-001 | planet labels + family dedupe |

### REDO (scene contradicts or ignores the question)

| Game | Redo as |
| --- | --- |
| architecture-authn-authz-001 | two gates in sequence: “who are you?” → “what may you do?” |
| architecture-backup-purpose-001 | a file being copied to a second disk, timestamped |
| architecture-load-balancer-001 | client → balancer → three servers fan-out with traffic dots |
| architecture-rest-stateless-001 | self-contained request cards; no session thread between them |
| geometry-cube-faces-001 | a cube net unfolding; count the 6 faces |
| geometry-hexagon-sides-001 | draw square/pentagon/hexagon/octagon; the player clicks a real polygon |
| geometry-pentagon-sides-001 | same polygon scene family as hexagon |
| geometry-parallel-lines-001 | two parallel lines + transversal; they never meet (currently a sine wave) |
| geometry-radius-diameter-001 | one circle with radius and diameter lines drawn |
| geometry-similar-shapes-001 | the same shape at two scales, matching angles marked |
| geometry-square-symmetry-001 | a square with its 4 symmetry axes folding in |
| geometry-supplementary-001 | two angles on a straight line summing to 180° (currently a sine wave) |
| math-absolute-value-001 | the V-shaped graph of \|x\| (currently a sine wave) |
| math-factorial-4-001 | cascade 4·3·2·1 multiplying out to 24 |
| math-fraction-half-001 | a circle/bar split in half, one half shaded |
| math-gauss-sum-001 | pairing arcs 1+100, 2+99, 3+98… |
| math-roman-xv-001 | X and V drawn as stroke glyphs (10 + 5) |
| math-slope-001 | a line with a rise/run staircase |
| ml-epoch-001 | a dataset row swept once per epoch with a counter |
| ml-generalization-001 | train vs test error curves that diverge |
| ml-learning-rate-001 | steps descending a loss hill: huge overshoots, tiny crawls |
| ml-supervised-001 | labelled examples (x → y) feeding a model box |
| physics-density-formula-001 | balance: mass block vs volume block, ρ = m/V |
| physics-floating-001 | water line; a block floating with its submerged part shown |
| physics-friction-direction-001 | a sliding block; friction arrow opposing motion |
| physics-momentum-formula-001 | two blocks colliding with p = mv vectors |
| physics-moon-gravity-001 | jump height on Earth vs Moon, side by side |
| physics-newton-third-001 | paired opposite arrows on two touching bodies |
| physics-parallel-voltage-001 | a circuit with two parallel branches sharing V |
| physics-pressure-formula-001 | the same force on a shrinking area; pressure reading rises |
| physics-reflection-angle-001 | mirror + incoming/outgoing rays with equal angles marked |
| physics-series-resistance-001 | resistors chained in a single loop |
| programming-big-o-binary-001 | growth curves O(log n) vs O(n) vs O(n²) |
| programming-constant-var-001 | a locked const box vs an editable var box |
| programming-dns-role-001 | browser → DNS server → IP → web server flow |
| programming-hash-lookup-001 | a key hashing into bucket slots |
| programming-http-404-001 | a request path that ends at a 404 |
| programming-linked-list-001 | nodes in a chain with next arrows, head/tail marked |
| programming-while-loop-001 | a circular loop arrow with a counter and an exit |

## Visual-fit audit (explicit addendum)

This addendum answers the two visual questions directly for
every agent-authored game in this batch. It is the authoritative
visual decision list where the summary counts above differ.

- **Fits** — the picture identifies the object or mechanism in
  the question. No mandatory visual rework; only the optional
  polish already noted in the per-game verdicts.
- **Partly fits** — the visual family is right, but the exact
  relationship asked about is missing or ambiguous. Partial
  visual rework is required.
- **Does not fit** — the picture is generic, unrelated, or
  teaches the wrong visual idea. A full visual redo is required.

Counts: **Fits 24 · Partly fits 38 · Does not fit 40 · Total 102.**

Coverage correction: `math-percent-150-001` was omitted from
the verdict tables above. It is included below as **Does not
fit / Full redo**: six floating circles do not show 20% of 150.
Use a 150-unit quantity bar or a percent grid with the relevant
portion clearly highlighted. The three original files
`architecture_mvc.py`, `ml_gradient.py`, and `physics_orbits.py`
remain excluded because they are base games, not batch items.

### Fits — no mandatory visual rework

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-api-gateway-001 | Fits | No |
| architecture-database-store-001 | Fits | No |
| architecture-db-index-001 | Fits | No |
| geometry-triangle-angles-001 | Fits | No |
| math-binary-13-001 | Fits | No |
| math-derivative-x2-001 | Fits | No |
| math-fibonacci-next-001 | Fits | No |
| math-log2-32-001 | Fits | No |
| math-next-prime-001 | Fits | No |
| ml-classification-001 | Fits | No |
| ml-loss-function-001 | Fits | No |
| ml-regression-output-001 | Fits | No |
| physics-current-unit-001 | Fits | No |
| physics-electron-shell-001 | Fits | No |
| physics-energy-conversion-001 | Fits | No |
| physics-pendulum-period-001 | Fits | No |
| physics-projectile-angle-001 | Fits | No |
| physics-sound-vacuum-001 | Fits | No |
| physics-wave-speed-001 | Fits | No |
| programming-bst-left-001 | Fits | No |
| programming-get-request-001 | Fits | No |
| programming-git-commit-001 | Fits | No |
| programming-recursion-base-001 | Fits | No |
| programming-sql-select-001 | Fits | No |

### Partly fits — partial visual rework required

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-cache-purpose-001 | Partly fits | Yes — partial |
| architecture-cdn-role-001 | Partly fits | Yes — partial |
| architecture-horizontal-scaling-001 | Partly fits | Yes — partial |
| architecture-message-queue-001 | Partly fits | Yes — partial |
| architecture-microservices-001 | Partly fits | Yes — partial |
| geometry-circumference-001 | Partly fits | Yes — partial |
| geometry-equilateral-angles-001 | Partly fits | Yes — partial |
| geometry-pythagoras-345-001 | Partly fits | Yes — partial |
| geometry-right-angle-001 | Partly fits | Yes — partial |
| geometry-triangle-area-001 | Partly fits | Yes — partial |
| math-even-number-001 | Partly fits | Yes — partial |
| math-gcd-12-18-001 | Partly fits | Yes — partial |
| math-lcm-4-6-001 | Partly fits | Yes — partial |
| math-marble-probability-001 | Partly fits | Yes — partial |
| math-median-379-001 | Partly fits | Yes — partial |
| math-power-2-5-001 | Partly fits | Yes — partial |
| math-prime-29-001 | Partly fits | Yes — partial |
| math-square-sequence-001 | Partly fits | Yes — partial |
| ml-activation-001 | Partly fits | Yes — partial |
| ml-clustering-001 | Partly fits | Yes — partial |
| ml-feature-001 | Partly fits | Yes — partial |
| ml-overfitting-001 | Partly fits | Yes — partial |
| ml-precision-001 | Partly fits | Yes — partial |
| ml-test-split-001 | Partly fits | Yes — partial |
| physics-free-fall-001 | Partly fits | Yes — partial |
| physics-kinetic-energy-001 | Partly fits | Yes — partial |
| programming-binary-search-001 | Partly fits | Yes — partial |
| programming-boolean-and-001 | Partly fits | Yes — partial |
| programming-bubble-sort-001 | Partly fits | Yes — partial |
| programming-compiler-role-001 | Partly fits | Yes — partial |
| programming-queue-fifo-001 | Partly fits | Yes — partial |
| programming-stable-sort-001 | Partly fits | Yes — partial |
| programming-stack-pop-001 | Partly fits | Yes — partial |
| programming-tree-root-001 | Partly fits | Yes — partial |
| physics-earth-orbit-001 | Partly fits | Yes — partial |
| physics-jupiter-orbit-001 | Partly fits | Yes — partial |
| physics-mars-orbit-001 | Partly fits | Yes — partial |
| physics-venus-orbit-001 | Partly fits | Yes — partial |

### Does not fit — full visual redo required

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-authn-authz-001 | Does not fit | Yes — full redo |
| architecture-backup-purpose-001 | Does not fit | Yes — full redo |
| architecture-load-balancer-001 | Does not fit | Yes — full redo |
| architecture-rest-stateless-001 | Does not fit | Yes — full redo |
| geometry-cube-faces-001 | Does not fit | Yes — full redo |
| geometry-hexagon-sides-001 | Does not fit | Yes — full redo |
| geometry-pentagon-sides-001 | Does not fit | Yes — full redo |
| geometry-parallel-lines-001 | Does not fit | Yes — full redo |
| geometry-radius-diameter-001 | Does not fit | Yes — full redo |
| geometry-similar-shapes-001 | Does not fit | Yes — full redo |
| geometry-square-symmetry-001 | Does not fit | Yes — full redo |
| geometry-supplementary-001 | Does not fit | Yes — full redo |
| math-absolute-value-001 | Does not fit | Yes — full redo |
| math-factorial-4-001 | Does not fit | Yes — full redo |
| math-fraction-half-001 | Does not fit | Yes — full redo |
| math-gauss-sum-001 | Does not fit | Yes — full redo |
| math-percent-150-001 | Does not fit | Yes — full redo |
| math-roman-xv-001 | Does not fit | Yes — full redo |
| math-slope-001 | Does not fit | Yes — full redo |
| ml-epoch-001 | Does not fit | Yes — full redo |
| ml-generalization-001 | Does not fit | Yes — full redo |
| ml-learning-rate-001 | Does not fit | Yes — full redo |
| ml-supervised-001 | Does not fit | Yes — full redo |
| physics-density-formula-001 | Does not fit | Yes — full redo |
| physics-floating-001 | Does not fit | Yes — full redo |
| physics-friction-direction-001 | Does not fit | Yes — full redo |
| physics-momentum-formula-001 | Does not fit | Yes — full redo |
| physics-moon-gravity-001 | Does not fit | Yes — full redo |
| physics-newton-third-001 | Does not fit | Yes — full redo |
| physics-parallel-voltage-001 | Does not fit | Yes — full redo |
| physics-pressure-formula-001 | Does not fit | Yes — full redo |
| physics-reflection-angle-001 | Does not fit | Yes — full redo |
| physics-series-resistance-001 | Does not fit | Yes — full redo |
| programming-big-o-binary-001 | Does not fit | Yes — full redo |
| programming-constant-var-001 | Does not fit | Yes — full redo |
| programming-dns-role-001 | Does not fit | Yes — full redo |
| programming-hash-lookup-001 | Does not fit | Yes — full redo |
| programming-http-404-001 | Does not fit | Yes — full redo |
| programming-linked-list-001 | Does not fit | Yes — full redo |
| programming-while-loop-001 | Does not fit | Yes — full redo |

## What to do next, in order

1. Commit in batches and start INDEX.md (id · topic · mechanic
   · one-line idea) — backfill this batch.
2. Delete the 3 duplicates; consolidate the planet family.
3. REDO list, worst first: the sine-wave trio
   (parallel-lines, supplementary, absolute-value) actively
   teaches wrong pictures.
4. FIX list.
5. Then continue to 300 — with ≥40 games about THIS project
   (read the app: square states, System-1, the deck, adapters),
   and scene-first design: sketch the picture, then the question.
