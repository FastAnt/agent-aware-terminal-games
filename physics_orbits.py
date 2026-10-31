"""Click the orbit where Mercury should be.

A code game: the planets really orbit (inner ones faster, a nod
to Kepler), the sun's rays turn slowly. Click a ring to answer.

Authoring contract (see AGENTS.md): define GAME (meta), paint
(cr, view) and optionally target_at(view, x, y). Keep paint
fast and pure — it runs ~20x/second while the pane is open.
"""
import math

GAME = {
    "id": "physics-orbits-001",
    "kind": "quiz",
    "kicker": "MINI GAME",
    "topic": "Physics",
    "title": "Click the orbit where Mercury should be",
    "hint": "Choose the innermost orbit",
    "question": "Three planets are already placed. Which orbit is Mercury's?",
    "choices": [],
    "answer": "ring-1",
    "explanation": "Mercury is the closest planet to the Sun — the "
                   "innermost orbit. Then come Venus, Earth and Mars.",
}

RINGS = 4
# (ring index 1..N, starting angle in degrees) — ring 1 stays empty
PLANETS = [(2, 35), (3, 165), (4, 300)]


def _radii(view):
    return view.ring_radii(view.w, view.h, RINGS)


def paint(cr, view):
    cx, cy = view.w / 2, view.h / 2
    radii = _radii(view)
    strong = view.colors["square"]
    for i, r in enumerate(radii):
        cr.arc(cx, cy, r, 0, 6.2832)
        if view.answered and GAME["answer"] == f"ring-{i + 1}":
            cr.set_source_rgba(*strong, 0.95)
            cr.set_line_width(2.8)
        elif view.answered and view.chosen == f"ring-{i + 1}":
            cr.set_source_rgba(*view.colors["text"], 0.9)
            cr.set_line_width(2.2)
        else:
            cr.set_source_rgba(*view.colors["muted"], 0.55)
            cr.set_line_width(1.2)
        cr.stroke()
    # the sun, rays turning slowly
    cr.arc(cx, cy, 15, 0, 6.2832)
    cr.set_source_rgba(*strong, 0.95)
    cr.set_line_width(1.6)
    cr.stroke()
    cr.set_source_rgba(*strong, 0.75)
    cr.set_line_width(1.3)
    for k in range(8):
        a = k * 0.7854 + view.t * 0.05
        cr.move_to(cx + 21 * math.cos(a), cy + 21 * math.sin(a))
        cr.line_to(cx + 29 * math.cos(a), cy + 29 * math.sin(a))
    cr.stroke()
    # planets: angular speed falls off with distance (Kepler-ish)
    for ring, start in PLANETS:
        r = radii[ring - 1]
        speed = 14.0 / ring ** 1.5  # degrees per second
        a = math.radians(start + view.t * speed)
        cr.arc(cx + r * math.cos(a), cy + r * math.sin(a), 5, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.95)
        cr.fill()


def target_at(view, x, y):
    return view.orbit_hit(view.w / 2, view.h / 2, _radii(view), x, y)
