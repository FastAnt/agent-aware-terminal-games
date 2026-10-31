# Agent-Aware Terminal — base content packs

Mini games, quizzes and cards that Agent-Aware Terminal shows in
its companion pane while a coding agent works (the pane takes
over after ~7 s of agent work; the developer plays instead of
watching the terminal).

Packs are **declarative JSON, never code** — the app's content
engine (`backend/app/content_engine.py` in
[FastAnt/meta_hack](https://github.com/FastAnt/meta_hack))
validates and renders them. This repo is mounted into the app as
the `games-base/` git submodule; additional packs can be dropped
into `~/.local/share/agent-aware-terminal/content/` at runtime
and are hot-loaded without restarting.

## Base games

| Pack | Scene | Idea |
| --- | --- | --- |
| `physics-orbits-001` | orbits | Click the orbit where Mercury belongs |
| `architecture-mvc-001` | diagram | Which MVC component receives input first |
| `ml-gradient-001` | network | Pick the gradient-descent update formula |

The engine serves packs in a shuffled cycle — no repeats until
every pack has been shown (the cycle persists across restarts).

**Authoring a game?** Read [AGENTS.md](AGENTS.md): schema, scene
types, animation, style guide — and the required test loop
(`python3 tools/test_game.py` in the main repo validates a pack,
plays it through automatically, and renders previews to look at).
