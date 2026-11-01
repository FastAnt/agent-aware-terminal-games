# AGENTS.md — how to author games

This repository holds **base games** for Agent-Aware Terminal:
mini games and quizzes shown to the developer while a coding
agent works. The main app mounts this repo as the `games-base/`
git submodule; user- and agent-written games can additionally be
dropped into `~/.local/share/agent-aware-terminal/content/`
at runtime and are hot-loaded, no restart.

## Games are code

A game is a **single Python module**. Real code, real animation —
you draw with cairo and compute anything you like:

```python
import math

GAME = {
    "id": "physics-orbits-001",
    "kind": "quiz",                    # or "card" (unscored)
    "kicker": "MINI GAME",
    "title": "Click the orbit where Mercury should be",
    "hint": "Choose the innermost orbit",
    "question": "Three planets are placed. Which orbit is Mercury's?",
    "choices": [],                     # or [{id, label}, ...]
    "answer": "ring-1",                # a choice id or click target
    "explanation": "Mercury is closest to the Sun…",
}

def paint(cr, view):
    # cr: cairo context. view: w, h, t (seconds since served),
    # view.colors = {"square", "text", "muted", "bg"} (r, g, b),
    # view.chosen / view.answered, plus geometry helpers:
    # view.ring_radii / node_rects / network_positions /
    # view.orbit_hit / node_hit
    ...

def target_at(view, x, y):
    # optional: map a scene click to a target id (or None)
    return view.orbit_hit(view.w / 2, view.h / 2, radii, x, y)
```

The three modules in this repo are complete working examples —
copy their structure. Scoring, the no-repeat deck, progress and
the pane lifecycle are the engine's job; yours is `GAME` +
`paint` (+ `target_at` if the scene is clickable).

**Trust model, honestly:** games execute inside the app with the
user's privileges. That is the point (an agent writes a game and
it just runs), and it means: only load games from directories
you trust, and review game diffs like code. The test tool runs
each game in a timeout subprocess, but that is crash protection,
not a security sandbox.

## Content types (every file declares one)

Mark each file inside itself with `"type"` (in `GAME` for
Python modules, as a top-level field for JSON):

| type | Behaviour in the pane |
| --- | --- |
| `game` | quiz: answered for **points** (score + streak shown) |
| `fact` | interesting fact: **Skip / Next** only, never scored |
| `idea` | proposal the user can **Save** — saved ideas land in the project's `.aat/research/saved_ideas.jsonl` for an agent to implement later |
| `news` | news item: **Skip / Next** plus an **Open link** button |

Per-type requirements: `game` needs an `answer` + `explanation`
(+ choices or click targets). `fact` / `idea` / `news` need
`title` + `body`; `news` additionally needs an http(s) `link`;
`idea` should carry an `action_hint` (first step for the
implementing agent). Legacy files without `type` still work:
`kind: quiz` reads as `game`, `kind: card` as `fact`.

## Canonical sources

If this file and the code disagree, **the code wins**:

1. `backend/app/content_engine.py` in the main repo
   ([FastAnt/meta_hack](https://github.com/FastAnt/meta_hack),
   `agent-aware-terminal/`) — `load_py_pack()` is the loading
   contract, `GameView` is what paint receives, `validate_pack()`
   has the hard meta rules.
2. The three games here are the style reference.

## Rules for paint()

- **Fast and pure.** paint runs ~20×/second while the pane is
  open. No I/O, no sleeps, no network, stdlib + `math` only.
  Precompute in module scope, not per frame.
- **Colors only from `view.colors`.** Never hardcode RGB — the
  app follows the system theme (dark/light); painted games must
  look native in both. Monochrome: shades, not hues.
- **Layout from `view.w`/`view.h`** every frame (the pane
  resizes). Animation comes from `view.t` — an animated scene
  is the default expectation; a still picture is a missed
  opportunity. Calm motion: this sits next to someone's work.
- **Handle the answered state.** When `view.answered`, show the
  outcome in the scene (highlight `GAME["answer"]`, mark
  `view.chosen` if wrong). The engine prints the explanation.
- **Clickable scenes**: `target_at` must return the `answer` id
  somewhere reachable — the test tool probes your click surface
  on a grid and fails unreachable answers. Make targets generous.
- File name = `<topic>-<slug>-<nnn>.py`; `GAME["id"]` equals the
  file stem and never changes once shipped (progress keys on
  id). Topics: `physics`, `geometry`, `math`, `programming`,
  `architecture`, `ml`, `news`, `refactor`.
- Facts must be true, one idea per game, question in one
  sentence, explanation 1–2 sentences and teaching something.
  English text.

## Project-correlated content (the Content Researcher)

A separate agent component creates games and fact cards about
a *specific project's* domain (audio spectrograms, cloud
bottlenecks, ciphers), keyed to the user's latest task. It has
its own skills and lifecycle and deposits into the project's
hidden `.aat/content/` folder, never into this base repo. Read
`content-researcher/README.md` and `SKILL.md` in the main repo
before doing project work.

Legacy note: the engine also renders declarative JSON packs
(`scene: orbits|diagram|network`) — fine for simple unscored
cards, but new games should be code.

## Test your game before you ship it (required)

```bash
cd agent-aware-terminal
python3 tools/test_game.py games-base/my_new_game.py
```

Per game it runs: load + meta validation → a scripted
playthrough in the real engine (correct target scores, wrong
ones fail, cards don't score) → a click-surface probe (your
answer must be clickable) → **preview PNGs** (dark + light, two
time frames) in `/tmp/game-previews/`.

**Open the previews and look at them.** You have vision; use it.
Do the two frames differ (it moves)? Do labels fit? Does it look
like it belongs next to the terminal in both themes? Iterate
until yes.

Live smoke test afterwards: copy the file into
`~/.local/share/agent-aware-terminal/content/`, give an agent a
>7 s task in the app, confirm `[content] serving <your-id>` in
`~/.local/share/agent-aware-terminal/decisions.log`.

Ship checklist: `tools/test_game.py` green · previews looked at
(both themes, motion visible) · answered state handled ·
explanation teaches something · id stable.
