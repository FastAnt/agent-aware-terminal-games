"""Earth's Orbit — click an orbit. See games-base/SOURCES.md."""
import math

GAME = {'id': 'physics-earth-orbit-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Physics', 'title': "Earth's Orbit", 'hint': 'Choose an orbit', 'question': "Three planets are placed. Click Earth's orbit.", 'choices': [], 'answer': 'ring-3', 'explanation': 'Earth is the third planet from the Sun, after Mercury and Venus and before Mars.'}
RINGS = 4
PLANETS = [(1, 35), (2, 165), (4, 300)]


def _radii(view):
    return view.ring_radii(view.w, view.h, RINGS)


def paint(cr, view):
    cx, cy = view.w / 2, view.h / 2
    radii = _radii(view)
    strong = view.colors["square"]
    for i, r in enumerate(radii):
        cr.arc(cx, cy, r, 0, 6.2832)
        if view.answered and GAME["answer"] == f"ring-{i + 1}":
            cr.set_source_rgba(*strong, 0.95); cr.set_line_width(2.8)
        elif view.answered and view.chosen == f"ring-{i + 1}":
            cr.set_source_rgba(*view.colors["text"], 0.9); cr.set_line_width(2.2)
        else:
            cr.set_source_rgba(*view.colors["muted"], 0.55); cr.set_line_width(1.2)
        cr.stroke()
    cr.arc(cx, cy, 15, 0, 6.2832); cr.set_source_rgba(*strong, 0.95); cr.set_line_width(1.6); cr.stroke()
    cr.set_source_rgba(*strong, 0.75); cr.set_line_width(1.3)
    for k in range(8):
        a = k * 0.7854 + view.t * 0.05
        cr.move_to(cx + 21 * math.cos(a), cy + 21 * math.sin(a))
        cr.line_to(cx + 29 * math.cos(a), cy + 29 * math.sin(a))
    cr.stroke()
    for ring, start in PLANETS:
        r = radii[ring - 1]
        a = math.radians(start + view.t * 14.0 / ring ** 1.5)
        cr.arc(cx + r * math.cos(a), cy + r * math.sin(a), 5, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.95); cr.fill()


def target_at(view, x, y):
    return view.orbit_hit(view.w / 2, view.h / 2, _radii(view), x, y)
