"""MVC — which component receives user input first?

A code game: a dot endlessly travels the MVC cycle
(Model -> Controller -> View -> Model) while you think.
Click a component or use the choices below.
"""
import math

GAME = {
    "id": "architecture-mvc-001",
    "kind": "quiz",
    "kicker": "ARCHITECTURE",
    "topic": "Architecture",
    "title": "MVC",
    "hint": "Model · View · Controller",
    "body": "MVC separates data, interface, and logic. It suits our "
            "project because it keeps the terminal UI, agent control "
            "flow, and project state clearly separated.",
    "question": "A user clicks a button in the interface. Which "
                "component receives the input first?",
    "choices": [
        {"id": "model", "label": "Model"},
        {"id": "view", "label": "View"},
        {"id": "controller", "label": "Controller"},
    ],
    "answer": "controller",
    "explanation": "The Controller takes user input first, updates "
                   "the Model, and the View re-renders from the "
                   "Model's state.",
}

NODES = [
    {"id": "model", "label": "Model", "x": 0.5, "y": 0.18,
     "w": 0.3, "h": 0.15},
    {"id": "view", "label": "View", "x": 0.2, "y": 0.78,
     "w": 0.3, "h": 0.15},
    {"id": "controller", "label": "Controller", "x": 0.78, "y": 0.78,
     "w": 0.3, "h": 0.15},
]
EDGES = [("model", "controller"), ("controller", "view"),
         ("view", "model")]


def _rounded(cr, x, y, w, h, r):
    cr.new_path()
    cr.arc(x + w - r, y + r, r, -1.5708, 0)
    cr.arc(x + w - r, y + h - r, r, 0, 1.5708)
    cr.arc(x + r, y + h - r, r, 1.5708, 3.1416)
    cr.arc(x + r, y + r, r, 3.1416, 4.7124)
    cr.close_path()


def paint(cr, view):
    rects = view.node_rects(NODES, view.w, view.h)
    centers = {k: (v[0] + v[2] / 2, v[1] + v[3] / 2)
               for k, v in rects.items()}
    text = view.colors["text"]
    for a, b in EDGES:
        ax, ay = centers[a]
        bx, by = centers[b]
        cr.move_to(ax, ay)
        cr.line_to(bx, by)
        cr.set_source_rgba(*view.colors["muted"], 0.45)
        cr.set_line_width(1.2)
        cr.stroke()
        ang = math.atan2(by - ay, bx - ax)
        px, py = ax + (bx - ax) * 0.66, ay + (by - ay) * 0.66
        cr.move_to(px, py)
        cr.line_to(px - 9 * math.cos(ang - 0.42),
                   py - 9 * math.sin(ang - 0.42))
        cr.line_to(px - 9 * math.cos(ang + 0.42),
                   py - 9 * math.sin(ang + 0.42))
        cr.close_path()
        cr.set_source_rgba(*text, 0.8)
        cr.fill()
    # the travelling dot: one full cycle every ~9 seconds
    span = (view.t * 0.33) % len(EDGES)
    idx, frac = int(span), span - int(span)
    a, b = EDGES[idx]
    ax, ay = centers[a]
    bx, by = centers[b]
    cr.arc(ax + (bx - ax) * frac, ay + (by - ay) * frac, 4.5, 0, 6.2832)
    cr.set_source_rgba(*text, 0.9)
    cr.fill()
    cr.select_font_face("Inter", 0, 0)
    cr.set_font_size(15)
    for n in NODES:
        x, y, w, h = rects[n["id"]]
        right = view.answered and GAME["answer"] == n["id"]
        wrong = view.answered and view.chosen == n["id"] and not right
        _rounded(cr, x, y, w, h, 12)
        if right:
            cr.set_source_rgba(*view.colors["square"], 0.95)
            cr.fill()
            cr.set_source_rgba(*view.colors["bg"], 1)
        else:
            cr.set_source_rgba(*view.colors["bg"], 1)
            cr.fill_preserve()
            cr.set_source_rgba(*text, 0.85 if wrong else 0.5)
            cr.set_line_width(2.2 if wrong else 1.2)
            cr.stroke()
            cr.set_source_rgba(*text, 1)
        ext = cr.text_extents(n["label"])
        cr.move_to(x + w / 2 - (ext.width / 2 + ext.x_bearing),
                   y + h / 2 - (ext.height / 2 + ext.y_bearing))
        cr.show_text(n["label"])


def target_at(view, x, y):
    return view.node_hit(view.node_rects(NODES, view.w, view.h), x, y)
