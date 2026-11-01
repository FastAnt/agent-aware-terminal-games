"""Prime Number — click a component. See games-base/SOURCES.md."""
import math

GAME = {'id': 'math-prime-29-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Math', 'title': 'Prime Number', 'question': 'Click the prime number.', 'choices': [{'id': 'n29', 'label': '29'}, {'id': 'n21', 'label': '21'}, {'id': 'n33', 'label': '33'}], 'answer': 'n29', 'explanation': '29 has no divisors besides 1 and itself; 21 = 3*7 and 33 = 3*11.'}

NODES = [('n29', '29'), ('n21', '21'), ('n33', '33')]
EDGES = [('n29', 'n21'), ('n21', 'n33'), ('n33', 'n29')]
POS = [(0.5, 0.18), (0.2, 0.78), (0.8, 0.78)]


def _rects(view):
    nodes = [{"id": nid, "label": label, "x": POS[i][0], "y": POS[i][1], "w": 0.3, "h": 0.15} for i, (nid, label) in enumerate(NODES)]
    return view.node_rects(nodes, view.w, view.h), nodes


def _rounded(cr, x, y, w, h, r):
    cr.new_path()
    cr.arc(x + w - r, y + r, r, -1.5708, 0)
    cr.arc(x + w - r, y + h - r, r, 0, 1.5708)
    cr.arc(x + r, y + h - r, r, 1.5708, 3.1416)
    cr.arc(x + r, y + r, r, 3.1416, 4.7124)
    cr.close_path()


def paint(cr, view):
    rects, nodes = _rects(view)
    centers = {k: (v[0] + v[2] / 2, v[1] + v[3] / 2) for k, v in rects.items()}
    text = view.colors["text"]
    for a, b in EDGES:
        ax, ay = centers[a]; bx, by = centers[b]
        cr.move_to(ax, ay); cr.line_to(bx, by)
        cr.set_source_rgba(*view.colors["muted"], 0.45); cr.set_line_width(1.2); cr.stroke()
        ang = math.atan2(by - ay, bx - ax)
        px, py = ax + (bx - ax) * 0.66, ay + (by - ay) * 0.66
        cr.move_to(px, py)
        cr.line_to(px - 9 * math.cos(ang - 0.42), py - 9 * math.sin(ang - 0.42))
        cr.line_to(px - 9 * math.cos(ang + 0.42), py - 9 * math.sin(ang + 0.42))
        cr.close_path(); cr.set_source_rgba(*text, 0.8); cr.fill()
    if EDGES:
        span = (view.t * 0.33) % len(EDGES); idx, frac = int(span), span - int(span)
        a, b = EDGES[idx]; ax, ay = centers[a]; bx, by = centers[b]
        cr.arc(ax + (bx - ax) * frac, ay + (by - ay) * frac, 4.5, 0, 6.2832)
        cr.set_source_rgba(*text, 0.9); cr.fill()
    cr.select_font_face("Inter", 0, 0); cr.set_font_size(15)
    for n in nodes:
        x, y, w, h = rects[n["id"]]
        right = view.answered and GAME["answer"] == n["id"]
        wrong = view.answered and view.chosen == n["id"] and not right
        _rounded(cr, x, y, w, h, 12)
        if right:
            cr.set_source_rgba(*view.colors["square"], 0.95); cr.fill()
            cr.set_source_rgba(*view.colors["bg"], 1)
        else:
            cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*text, 0.85 if wrong else 0.5)
            cr.set_line_width(2.2 if wrong else 1.2); cr.stroke()
            cr.set_source_rgba(*text, 1)
        ext = cr.text_extents(n["label"])
        cr.move_to(x + w / 2 - (ext.width / 2 + ext.x_bearing), y + h / 2 - (ext.height / 2 + ext.y_bearing))
        cr.show_text(n["label"])


def target_at(view, x, y):
    rects, _ = _rects(view)
    return view.node_hit(rects, x, y)
