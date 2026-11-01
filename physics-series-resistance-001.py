"""Series Resistors - bespoke scene per REVIEW.md. See SOURCES.md."""
import math

GAME = {'id': 'physics-series-resistance-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Physics', 'title': 'Series Resistors', 'question': 'Resistors of 2 and 3 ohms are connected in series. What is the total?', 'choices': [{'id': 'r5', 'label': '5 ohms'}, {'id': 'r1', 'label': '1.2 ohms'}, {'id': 'r6', 'label': '6 ohms'}], 'answer': 'r5', 'explanation': 'Series resistances simply add: 2 + 3 = 5 ohms.'}

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


def paint(cr, view):
    w, h, t = view.w, view.h, view.t
    x0, x1, yt, yb = w*0.16, w*0.84, h*0.26, h*0.72
    _line(cr, view, x0, yt, x1, yt, "text", 0.75); _line(cr, view, x0, yb, x1, yb, "text", 0.75)
    _line(cr, view, x0, yt, x0, yb, "text", 0.75); _line(cr, view, x1, yt, x1, yb, "text", 0.75)
    for i, xx in enumerate((w*0.38, w*0.62)):
        _box(cr, view, xx - 38, yt - 16, 76, 32, f"R{i+1} zigzag", 10)
    _box(cr, view, x0 - 24, h/2 - 16, 48, 32, "cell", 11, fill_col="square")
    per = (x1-x0)*2 + (yb-yt)*2; d = (t*60) % per
    # dot walks the loop clockwise
    if d < x1-x0: px, py = x0 + d, yt
    elif d < x1-x0 + (yb-yt): px, py = x1, yt + d - (x1-x0)
    elif d < 2*(x1-x0) + (yb-yt): px, py = x1 - (d - (x1-x0) - (yb-yt)), yb
    else: px, py = x0, yb - (d - 2*(x1-x0) - (yb-yt))
    _circ(cr, view, px, py, 5, "square", 0.95, fill=True)
    _t(cr, view, w/2, h*0.14, "one loop: resistances add", 13, "muted")
    _ans(cr, view)

