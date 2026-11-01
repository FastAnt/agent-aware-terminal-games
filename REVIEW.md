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

## Review — second batch (200 new games), 2026-11-01

Method: `tools/test_game.py` on all 303 files (303/303 pass —
loading, playthrough, click probes, motion), contact sheets of
all 200 new dark previews, full-size spot checks, meta audit of
all 200 questions (no duplicates, no duplicate ids).

### The feedback loop worked

The sine-wave trio from the first review is fixed properly:
`geometry-parallel-lines-001` now draws two parallel lines with
a transversal, `math-absolute-value-001` is a true V-graph,
`geometry-supplementary-001` shows two angles on a straight
line. 76 first-batch games were reworked; the direction is
right. INDEX.md exists and is a real ledger (303 rows). Overall
this batch is far stronger: Venn diagrams for set games,
gate diagrams with live inputs for logic gates, real
convolution/pooling layouts, superposition waves that actually
cancel. Verdicts: **Fits 109 · Partly fits 83 · Does not fit 8.**

### What still needs fixing

1. **Still nothing committed.** The 200 new games and 76
   reworks sat untracked/uncommitted (only doc commits landed).
   They are committed alongside this review, as last time.
   Commit per batch — this is the third reminder.
2. **`__pycache__/` is tracked in this repo.** Remove it from
   tracking and add it to `.gitignore`; bytecode is not source.
3. **New template families are forming.** Better than batch 1
   (each family is at least the right *kind* of picture), but
   watch the counts: equation flashcards for ~15 logic laws
   (two text boxes and an "="), the bare 2×2 matrix for ~20
   matrix games, the loss-bowl for gradient/L2/MSE, the spring
   icon for 6 SHM games, the 3-box flow for ~17 crypto games,
   the feedback loop for all 4 PID games, Caesar alphabets ×5.
   A template is allowed when it *is* the subject — gates,
   pooling, standing waves pass that test. Flashcards do not:
   the scene must add information beyond the question text.
4. **Topic skew.** New programming games are ~90%
   crypto/security/gates; physics leans on waves and springs;
   math on matrices and logic laws. Fine as depth, but the deck
   needs breadth (data structures, algorithms, everyday
   physics) — and project-domain games still live only in the
   Content Researcher track (none deposited yet in the projects
   checked).
5. **One rendering bug:** `physics-wave-amplitude-read-001`
   draws its wave off-canvas (amplitude overflows the frame,
   caption collides with the curve). Scale to the view.

### Fits — no mandatory visual rework (109)

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-beam-bending-001 | Fits | No |
| math-biconditional-001 | Fits | No |
| math-contradiction-law-001 | Fits | No |
| math-implication-false-001 | Fits | No |
| math-implies-vacuous-001 | Fits | No |
| math-matrix-add-compute-001 | Fits | No |
| math-matrix-diagonal-def-001 | Fits | No |
| math-matrix-dot-view-001 | Fits | No |
| math-matrix-identity-entries-001 | Fits | No |
| math-matrix-rotation-001 | Fits | No |
| math-matrix-scalar-001 | Fits | No |
| math-matrix-scaling-001 | Fits | No |
| math-matrix-shear-001 | Fits | No |
| math-matrix-symmetric-001 | Fits | No |
| math-matrix-trace-compute-001 | Fits | No |
| math-matrix-transpose-compute-001 | Fits | No |
| math-set-complement-001 | Fits | No |
| math-tautology-001 | Fits | No |
| math-venn-intersection-001 | Fits | No |
| math-venn-union-001 | Fits | No |
| ml-attention-score-001 | Fits | No |
| ml-conv-output-size-001 | Fits | No |
| ml-conv-padding-001 | Fits | No |
| ml-conv-purpose-001 | Fits | No |
| ml-conv-stride-001 | Fits | No |
| ml-cross-entropy-001 | Fits | No |
| ml-dropout-test-001 | Fits | No |
| ml-dropout-train-001 | Fits | No |
| ml-leaky-relu-001 | Fits | No |
| ml-perceptron-sum-001 | Fits | No |
| ml-pool-avg-001 | Fits | No |
| ml-pool-max-001 | Fits | No |
| ml-relu-formula-001 | Fits | No |
| ml-relu-negative-001 | Fits | No |
| ml-residual-why-001 | Fits | No |
| ml-sigmoid-range-001 | Fits | No |
| ml-sigmoid-zero-001 | Fits | No |
| ml-softmax-largest-001 | Fits | No |
| ml-softmax-sum-001 | Fits | No |
| ml-softmax-temperature-001 | Fits | No |
| ml-tanh-range-001 | Fits | No |
| physics-beats-frequency-001 | Fits | No |
| physics-bernoulli-001 | Fits | No |
| physics-center-mass-stability-001 | Fits | No |
| physics-continuity-eq-001 | Fits | No |
| physics-cosine-start-001 | Fits | No |
| physics-damping-effect-001 | Fits | No |
| physics-fourier-idea-001 | Fits | No |
| physics-fourier-square-001 | Fits | No |
| physics-gear-direction-001 | Fits | No |
| physics-gear-ratio-001 | Fits | No |
| physics-gear-torque-trade-001 | Fits | No |
| physics-harmonic-third-string-001 | Fits | No |
| physics-lever-balance-001 | Fits | No |
| physics-pascal-law-001 | Fits | No |
| physics-pulley-advantage-001 | Fits | No |
| physics-simple-supported-max-001 | Fits | No |
| physics-sine-derivative-001 | Fits | No |
| physics-standing-antinode-001 | Fits | No |
| physics-standing-node-001 | Fits | No |
| physics-string-wavelength-2nd-001 | Fits | No |
| physics-super-constructive-001 | Fits | No |
| physics-super-destructive-001 | Fits | No |
| physics-torque-def-001 | Fits | No |
| physics-wave-angular-freq-001 | Fits | No |
| physics-wave-period-freq-001 | Fits | No |
| physics-wave-phase-shift-001 | Fits | No |
| physics-wave-speed-harmonic-001 | Fits | No |
| physics-young-modulus-001 | Fits | No |
| programming-aes-block-001 | Fits | No |
| programming-and-gate-001 | Fits | No |
| programming-and-truth-row-001 | Fits | No |
| programming-asymmetric-pair-001 | Fits | No |
| programming-blockchain-link-001 | Fits | No |
| programming-brute-keyspace-001 | Fits | No |
| programming-caesar-decrypt-001 | Fits | No |
| programming-caesar-shift3-001 | Fits | No |
| programming-certificate-role-001 | Fits | No |
| programming-diffie-hellman-001 | Fits | No |
| programming-encoding-not-crypto-001 | Fits | No |
| programming-hash-avalanche-001 | Fits | No |
| programming-hash-oneway-001 | Fits | No |
| programming-hmac-purpose-001 | Fits | No |
| programming-key-128-001 | Fits | No |
| programming-nand-gate-001 | Fits | No |
| programming-negative-feedback-001 | Fits | No |
| programming-nonce-purpose-001 | Fits | No |
| programming-nor-gate-001 | Fits | No |
| programming-not-gate-001 | Fits | No |
| programming-onetime-pad-001 | Fits | No |
| programming-or-gate-001 | Fits | No |
| programming-or-truth-row-001 | Fits | No |
| programming-pid-d-001 | Fits | No |
| programming-pid-i-001 | Fits | No |
| programming-pid-p-001 | Fits | No |
| programming-pki-trust-001 | Fits | No |
| programming-public-encrypt-001 | Fits | No |
| programming-replay-attack-001 | Fits | No |
| programming-rot13-001 | Fits | No |
| programming-salt-purpose-001 | Fits | No |
| programming-signature-key-001 | Fits | No |
| programming-signature-purpose-001 | Fits | No |
| programming-symmetric-key-001 | Fits | No |
| programming-tls-session-001 | Fits | No |
| programming-xnor-gate-001 | Fits | No |
| programming-xor-cipher-rev-001 | Fits | No |
| programming-xor-compute-001 | Fits | No |
| programming-xor-exactly-one-001 | Fits | No |
| programming-xor-gate-001 | Fits | No |

### Partly fits — partial visual rework required (83)

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-arch-compression-001 | Partly fits | Yes — partial |
| architecture-cantilever-001 | Partly fits | Yes — partial |
| architecture-load-path-001 | Partly fits | Yes — partial |
| math-absorption-law-001 | Partly fits | Yes — partial |
| math-commutative-and-001 | Partly fits | Yes — partial |
| math-contrapositive-001 | Partly fits | Yes — partial |
| math-demorgan-and-001 | Partly fits | Yes — partial |
| math-demorgan-or-001 | Partly fits | Yes — partial |
| math-distributive-law-001 | Partly fits | Yes — partial |
| math-domination-law-001 | Partly fits | Yes — partial |
| math-double-negation-001 | Partly fits | Yes — partial |
| math-existential-negation-001 | Partly fits | Yes — partial |
| math-harmonic-function-def-001 | Partly fits | Yes — partial |
| math-harmonic-mean-value-001 | Partly fits | Yes — partial |
| math-harmonic-series-math-001 | Partly fits | Yes — partial |
| math-idempotent-law-001 | Partly fits | Yes — partial |
| math-identity-law-001 | Partly fits | Yes — partial |
| math-matrix-add-rule-001 | Partly fits | Yes — partial |
| math-matrix-det-compute-001 | Partly fits | Yes — partial |
| math-matrix-det-diag-001 | Partly fits | Yes — partial |
| math-matrix-det-formula-001 | Partly fits | Yes — partial |
| math-matrix-det-meaning-001 | Partly fits | Yes — partial |
| math-matrix-dims-product-001 | Partly fits | Yes — partial |
| math-matrix-eigen-identity-001 | Partly fits | Yes — partial |
| math-matrix-eigenvector-001 | Partly fits | Yes — partial |
| math-matrix-identity-prop-001 | Partly fits | Yes — partial |
| math-matrix-incompatible-001 | Partly fits | Yes — partial |
| math-matrix-inverse-exists-001 | Partly fits | Yes — partial |
| math-matrix-orthogonal-001 | Partly fits | Yes — partial |
| math-matrix-product-inverse-001 | Partly fits | Yes — partial |
| math-matrix-product-transpose-001 | Partly fits | Yes — partial |
| math-matrix-rank-001 | Partly fits | Yes — partial |
| math-matrix-rowswap-det-001 | Partly fits | Yes — partial |
| math-matrix-singular-001 | Partly fits | Yes — partial |
| math-matrix-trace-def-001 | Partly fits | Yes — partial |
| math-matrix-transpose-def-001 | Partly fits | Yes — partial |
| math-matrix-triangular-det-001 | Partly fits | Yes — partial |
| math-matrix-vector-shape-001 | Partly fits | Yes — partial |
| math-matrix-zero-product-001 | Partly fits | Yes — partial |
| math-modus-ponens-001 | Partly fits | Yes — partial |
| math-quantifier-negation-001 | Partly fits | Yes — partial |
| math-sin-cos-identity-001 | Partly fits | Yes — partial |
| math-subset-relation-001 | Partly fits | Yes — partial |
| ml-attention-heads-001 | Partly fits | Yes — partial |
| ml-attention-weights-001 | Partly fits | Yes — partial |
| ml-backprop-chain-001 | Partly fits | Yes — partial |
| ml-batch-iteration-001 | Partly fits | Yes — partial |
| ml-batch-norm-001 | Partly fits | Yes — partial |
| ml-embedding-meaning-001 | Partly fits | Yes — partial |
| ml-gradient-step-nn-001 | Partly fits | Yes — partial |
| ml-l2-regularization-001 | Partly fits | Yes — partial |
| ml-layer-norm-001 | Partly fits | Yes — partial |
| ml-matrix-ml-weights-001 | Partly fits | Yes — partial |
| ml-mse-loss-001 | Partly fits | Yes — partial |
| ml-pool-why-001 | Partly fits | Yes — partial |
| ml-weight-multiply-001 | Partly fits | Yes — partial |
| physics-ductile-vs-brittle-001 | Partly fits | Yes — partial |
| physics-energy-shm-001 | Partly fits | Yes — partial |
| physics-fatigue-001 | Partly fits | Yes — partial |
| physics-forced-oscillation-001 | Partly fits | Yes — partial |
| physics-friction-brakes-001 | Partly fits | Yes — partial |
| physics-harmonic-fundamental-001 | Partly fits | Yes — partial |
| physics-harmonic-second-001 | Partly fits | Yes — partial |
| physics-hydrostatic-001 | Partly fits | Yes — partial |
| physics-motor-vs-generator-001 | Partly fits | Yes — partial |
| physics-organ-pipe-fundamental-001 | Partly fits | Yes — partial |
| physics-pendulum-harmonic-001 | Partly fits | Yes — partial |
| physics-quality-factor-001 | Partly fits | Yes — partial |
| physics-resonance-bridge-001 | Partly fits | Yes — partial |
| physics-resonance-def-001 | Partly fits | Yes — partial |
| physics-shm-period-spring-001 | Partly fits | Yes — partial |
| physics-shm-restoring-001 | Partly fits | Yes — partial |
| physics-strain-def-001 | Partly fits | Yes — partial |
| physics-stress-def-001 | Partly fits | Yes — partial |
| physics-two-waves-speed-001 | Partly fits | Yes — partial |
| programming-affirming-consequent-001 | Partly fits | Yes — partial |
| programming-checksum-vs-hash-001 | Partly fits | Yes — partial |
| programming-crypto-random-001 | Partly fits | Yes — partial |
| programming-entropy-meaning-001 | Partly fits | Yes — partial |
| programming-nyquist-001 | Partly fits | Yes — partial |
| programming-password-storage-001 | Partly fits | Yes — partial |
| programming-slow-hash-001 | Partly fits | Yes — partial |
| programming-substitution-leak-001 | Partly fits | Yes — partial |

### Does not fit — full visual redo required (8)

| Game | Visual fits the game? | Visual rework needed? |
| --- | --- | --- |
| architecture-safety-factor-001 | Does not fit | Yes — full redo |
| architecture-truss-triangles-001 | Does not fit | Yes — full redo |
| math-disjoint-sets-001 | Does not fit | Yes — full redo |
| ml-adam-optimizer-001 | Does not fit | Yes — full redo |
| ml-augmentation-001 | Does not fit | Yes — full redo |
| physics-power-vi-001 | Does not fit | Yes — full redo |
| physics-thermal-expansion-001 | Does not fit | Yes — full redo |
| physics-wave-amplitude-read-001 | Does not fit | Yes — full redo |

Per-game direction for the redos: safety-factor → capacity vs
load bars at 3:1; truss-triangles → an actual triangular truss;
disjoint-sets → two separate, non-overlapping circles (the
current overlapping Venn teaches the opposite); adam →
per-parameter adaptive step sizes on a loss curve;
augmentation → one example spawning flipped/rotated copies;
power-vi → V and I quantities multiplying into P;
thermal-expansion → a bar that lengthens with ΔL marks;
wave-amplitude-read → fix the scale bug, then annotate A.

### What to do next, in order (batch 3)

1. Commit per batch; keep INDEX.md in the same commit.
2. The 8 redos above, then the flashcard family (draw one
   scene per law: Venn shading, truth-table row highlight,
   set diagrams — not text in boxes).
3. Bare-matrix games: draw the operation (highlight the
   diagonal for det/trace, flip arrows for transpose, a vector
   before/after for eigenvectors).
4. Broaden topics; keep families honest.
