"""Idempotent Law - bespoke scene (batch-3 review fix). See REVIEW.md."""
import math

GAME = {"type": "game", 'id': 'math-idempotent-law-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Math', 'title': 'Idempotent Law', 'question': 'A AND A is equivalent to what?', 'choices': [{'id': 'a', 'label': 'A'}, {'id': 'true', 'label': 'True'}, {'id': 'false', 'label': 'False'}], 'answer': 'a', 'explanation': 'Repeating the same operand changes nothing for AND or OR.'}

CARDS = []
POLYS = []

def _t(cr, view, x, y, s, size=15, col="text", alpha=1.0, align="c"):
    cr.select_font_face("Inter", 0, 0); cr.set_font_size(size)
    cr.set_source_rgba(*view.colors[col], alpha)
    ext = cr.text_extents(s)
    if align == "c":
        x = x - (ext.width / 2 + ext.x_bearing)
    elif align == "r":
        x = x - (ext.width + ext.x_bearing)
    cr.move_to(x, y - (ext.height / 2 + ext.y_bearing)); cr.show_text(s)

def _line(cr, view, x1, y1, x2, y2, col="muted", alpha=0.6, wdt=1.3):
    cr.move_to(x1, y1); cr.line_to(x2, y2)
    cr.set_source_rgba(*view.colors[col], alpha); cr.set_line_width(wdt); cr.stroke()

def _arr(cr, view, x1, y1, x2, y2, col="text", alpha=0.85, wdt=1.4):
    import math as _m
    _line(cr, view, x1, y1, x2, y2, col, alpha, wdt)
    ang = _m.atan2(y2 - y1, x2 - x1)
    cr.move_to(x2, y2)
    cr.line_to(x2 - 10 * _m.cos(ang - 0.42), y2 - 10 * _m.sin(ang - 0.42))
    cr.line_to(x2 - 10 * _m.cos(ang + 0.42), y2 - 10 * _m.sin(ang + 0.42))
    cr.close_path(); cr.set_source_rgba(*view.colors[col], alpha); cr.fill()

def _circ(cr, view, x, y, r, col="square", alpha=0.9, wdt=1.4, fill=False):
    cr.new_path(); cr.arc(x, y, r, 0, 6.2832)
    if fill:
        cr.set_source_rgba(*view.colors[col], alpha); cr.fill()
    else:
        cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
        cr.set_source_rgba(*view.colors[col], alpha); cr.set_line_width(wdt); cr.stroke()

def _box(cr, view, x, y, w, h, label="", size=14, col="text", alpha=0.55, wdt=1.2, fill_col=None, fill_alpha=0.95):
    cr.new_path()
    r = 10
    cr.arc(x + w - r, y + r, r, -1.5708, 0); cr.arc(x + w - r, y + h - r, r, 0, 1.5708)
    cr.arc(x + r, y + h - r, r, 1.5708, 3.1416); cr.arc(x + r, y + r, r, 3.1416, 4.7124)
    cr.close_path()
    if fill_col:
        cr.set_source_rgba(*view.colors[fill_col], fill_alpha); cr.fill()
        if label: _t(cr, view, x + w / 2, y + h / 2, label, size, "bg", 1)
    else:
        cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
        cr.set_source_rgba(*view.colors[col], alpha); cr.set_line_width(wdt); cr.stroke()
        if label: _t(cr, view, x + w / 2, y + h / 2, label, size, "text", 1)

def _ans(cr, view):
    if not view.answered:
        return
    label = GAME["answer"]
    for c in GAME.get("choices") or []:
        if c["id"] == GAME["answer"]:
            label = c["label"]
    ok = view.chosen == GAME["answer"]
    _t(cr, view, view.w / 2, view.h - 18, "Answer: " + label, 14, "square" if ok else "text", 0.95)

def _card_rects(view):
    out = {}
    for cid, label, fx, fy, fw, fh in CARDS:
        w, h = fw * view.w, fh * view.h
        out[cid] = (fx * view.w - w / 2, fy * view.h - h / 2, w, h, label)
    return out

def _draw_cards(cr, view):
    for cid, (x, y, w, h, label) in _card_rects(view).items():
        right = view.answered and GAME["answer"] == cid
        wrong = view.answered and view.chosen == cid and not right
        if right:
            _box(cr, view, x, y, w, h, label, 15, fill_col="square")
        else:
            _box(cr, view, x, y, w, h, label, 15, "text", 0.85 if wrong else 0.55, 2.2 if wrong else 1.2)

def _poly_pts(cx, cy, r, sides, rot=-1.5708):
    import math as _m
    return [(cx + r * _m.cos(rot + i * 6.2832 / sides), cy + r * _m.sin(rot + i * 6.2832 / sides)) for i in range(sides)]

def _draw_polys(cr, view):
    import math as _m
    for pid, label, fx, fy, sides, rf in POLYS:
        cx, cy, r = fx * view.w, fy * view.h, rf * min(view.w, view.h)
        pts = _poly_pts(cx, cy, r, sides, -2.356 if sides == 4 else -1.5708)
        right = view.answered and GAME["answer"] == pid
        wrong = view.answered and view.chosen == pid and not right
        cr.new_path(); cr.move_to(*pts[0])
        for p in pts[1:]: cr.line_to(*p)
        cr.close_path()
        if right:
            cr.set_source_rgba(*view.colors["square"], 0.95); cr.fill()
        else:
            cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*view.colors["text"], 0.85 if wrong else 0.6); cr.set_line_width(2.2 if wrong else 1.4); cr.stroke()
        # a travelling vertex dot
        k = int(view.t * 0.7) % sides
        _circ(cr, view, pts[k][0], pts[k][1], 4, "square", 0.95, fill=True)
        _t(cr, view, cx, cy + r + 26, label, 14, "text", 0.9)

def _grid(cr, view, mat, x0, y0, cell, hl=None):
    for r, row in enumerate(mat):
        for c, v in enumerate(row):
            x, y = x0 + c * cell, y0 + r * cell
            on = hl and (r, c) in hl
            cr.new_path(); cr.rectangle(x + 2, y + 2, cell - 4, cell - 4)
            if on:
                cr.set_source_rgba(*view.colors["square"], 0.85); cr.fill()
                _t(cr, view, x + cell/2, y + cell/2, str(v), 13, "bg")
            else:
                cr.set_source_rgba(*view.colors["text"], 0.5); cr.set_line_width(1); cr.stroke()
                _t(cr, view, x + cell/2, y + cell/2, str(v), 13, "text", 0.9)

def _lamp(cr, view, x, y, on, label=""):
    _circ(cr, view, x, y, 13, "square", 0.95, 1.7, fill=bool(on))
    if label: _t(cr, view, x, y + 28, label, 11, "square" if on else "muted")

def _gate(cr, view, x, y, w, h, label):
    _box(cr, view, x, y, w, h, label, 13, fill_col="square")

COMBOS = [(0,0),(0,1),(1,0),(1,1)]


def _combo(view):
    return COMBOS[int(view.t * 0.7) % 4]

def _mat3(cr, view, a, b, res, op, cap, hl=None, bmat=None):
    w, h = view.w, view.h; cell = min(w, h) * 0.12
    _grid(cr, view, a, w*0.07, h*0.3, cell, hl)
    _t(cr, view, w*0.34, h*0.46, op, 18, "square")
    if bmat is not None: _grid(cr, view, bmat, w*0.4, h*0.3, cell)
    _arr(cr, view, w*0.64, h*0.46, w*0.72, h*0.46, "text", 0.85)
    _grid(cr, view, res, w*0.74, h*0.3, cell, hl)
    _t(cr, view, w/2, h*0.16, cap, 13, "muted")

def paint(cr, view):
    w, h, t = view.w, view.h, view.t
    a = int(t * 0.8) % 2
    _box(cr, view, w*0.06, h*0.4, w*0.14, h*0.12, f"A={a}", 12, fill_col="square")
    _line(cr, view, w*0.2, h*0.44, w*0.36, h*0.4, "square", 0.8); _line(cr, view, w*0.2, h*0.5, w*0.36, h*0.54, "square", 0.8)
    _gate(cr, view, w*0.36, h*0.34, w*0.2, h*0.22, "AND")
    _t(cr, view, w*0.46, h*0.28, "same A twice", 11, "muted")
    _lamp(cr, view, w*0.72, h*0.45, a, f"= A = {a}")
    _ans(cr, view)

