# Sources, inspiration and licensing

All 102 games added in this batch are **original** questions,
explanations and cairo scenes written for this project. No text,
images, code or level data were copied from the sites below.
They were visited (Nov 2026) only to study what makes a good
2–3 minute task: one idea, a visible manipulation, a clear win
condition, calm presentation.

## Visited and what was taken (ideas only)

| Source | What was studied | How it maps here |
| --- | --- | --- |
| [Simon Tatham's Puzzles](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/) | 40+ tiny single-player puzzles meant to fill a few minutes; grid/placement logic (Bridges, Loopy, Unequal). Played in the browser. | The short-session format itself; our clickable node/orbit scenes. No code or rules copied. Tatham's own code is MIT, but we did not use it. |
| [PhET Simulations](https://phet.colorado.edu/en/simulations) | Pendulum, projectile, waves, circuits: one variable at a time, direct manipulation. Browsed the catalogue. | `physics-pendulum-period-001`, `physics-projectile-angle-001`, `physics-wave-speed-001`, `physics-series-resistance-001` — generic school physics, own wording. PhET HTML sims are CC BY-NC 4.0 (non-commercial), so **nothing** was copied or adapted from them. |
| [NRICH Interactive](https://nrich.maths.org/secondary-interactive-resources) | Short visual number/geometry problems with one clear question. | `math-*` sequences, primes, probability; `geometry-*` angle/symmetry tasks — standard school facts, own scenes. |
| [Mathigon](https://mathigon.org/) | Visual manipulation of shapes, symmetry, graphs. | `geometry-square-symmetry-001`, `programming-bst-left-001` style diagrams. No assets used. |
| [oPhysics](https://www.ophysics.com/) | Small physics scenarios (projectile vs. target, pendulums, orbits). | Projectile/orbit framing for `physics-*-orbit-001`. Generic physics only. |
| [VisuAlgo](https://visualgo.net/en) | Animated sorting/searching bars and trees. | `programming-bubble-sort-001`, `programming-binary-search-001`, bar/tree scenes. Own animation code. |
| [Red Blob Games — A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html) | Interactive grids, step-by-step pathfinding feel. | Grid scene used by several `*-001` games. No code copied. |
| [Nikoli](https://www.nikoli.co.jp/en/puzzles/) | Pen-and-paper logic rules (checked rule pages, not puzzles). | Not directly used: Nikoli puzzle designs are their content, so we only took the "one rule, one board" lesson. |
| [CS Unplugged](https://www.csunplugged.org/en/) | Binary numbers and sorting as physical games. | `math-binary-13-001`, sorting questions. Standard facts. |
| [Falstad Circuit Simulator](https://www.falstad.com/circuit/) | Interactive series/parallel circuits. | `physics-series-resistance-001`, `physics-parallel-voltage-001` — Ohm's-law facts, own drawing. |

## Licensing summary (checked on the sites)

- **Simon Tatham's Puzzles** — code MIT. Not used; safe to consult.
- **PhET HTML simulations** — CC BY-NC 4.0: commercial use and
  copying would need care. We use none of their content; our
  physics questions are generic curriculum facts. Do not paste
  PhET code/text into games here.
- **NRICH / Mathigon / GeoGebra / Nikoli / Puzzle Baron /
  BrainBashers / Brilliant** — site content is copyrighted /
  terms-restricted. Used as interaction references only.
- **Facts are not copyrightable**: angle sums, Ohm's law, Big-O,
  Fibonacci, etc. are stated in our own words everywhere.

## This batch

102 new code games (`*-001.py`) plus the 3 original base games =
105 games: physics 23+1, geometry 14, math 20, programming 20,
architecture 12+1, ml 13+1. Three interaction shapes copied from
the base games: button-choice quizzes with an animated scene,
clickable node diagrams (`target_at` via `view.node_hit`), and
clickable orbit rings (`view.orbit_hit`). All paint with
`view.colors` only, Inter, calm `view.t` motion, answered state
highlighted. Verified with `python3 tools/test_game.py games-base/`
(ALL OK) and by inspecting dark/light previews in
`/tmp/game-previews/`.
