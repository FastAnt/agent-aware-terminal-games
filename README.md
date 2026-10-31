# Agent-Aware Terminal — base content packs

Mini games, quizzes and cards that Agent-Aware Terminal shows in
its companion pane while a coding agent works (the pane takes
over after ~7 s of agent work; the developer plays instead of
watching the terminal).

A game is a **single Python module** (`GAME` meta + a cairo
`paint()` function) — real code, so animation and game logic are
unlimited. The app's content engine (`backend/app/content_engine.py`
in [FastAnt/meta_hack](https://github.com/FastAnt/meta_hack))
loads, scores and cycles them. This repo is mounted into the app
as the `games-base/` git submodule; additional games can be
dropped into `~/.local/share/agent-aware-terminal/content/` at
runtime and are hot-loaded without restarting.

## Base games

| Game | Idea |
| --- | --- |
| `physics_orbits.py` | Planets really orbit (inner = faster); click Mercury's ring |
| `architecture_mvc.py` | A dot travels the MVC cycle; which part takes input first |
| `ml_gradient.py` | Gradient pulses flow through a network; pick the formula |

The engine serves packs in a shuffled cycle — no repeats until
every pack has been shown (the cycle persists across restarts).

**Authoring a game?** Read [AGENTS.md](AGENTS.md): schema, scene
types, animation, style guide — and the required test loop
(`python3 tools/test_game.py` in the main repo validates a pack,
plays it through automatically, and renders previews to look at).
