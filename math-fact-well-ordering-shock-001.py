"""Accept choice and every set can be lined up — fact card with a bespoke visual.
See FACT_VISUALS.md for the design note. Text in FACTS_INDEX.md."""
import math

GAME = {'type': 'fact', 'id': 'math-fact-well-ordering-shock-001', 'kicker': 'FACT', 'topic': 'Math', 'title': 'Accept choice and every set can be lined up', 'body': "The well-ordering theorem, equivalent to the axiom of choice, says even the real numbers admit an ordering where every nonempty subset has a least element. No one can exhibit such an order; Zermelo's 1904 proof only shows consistency demands it exists. Many mathematicians at the time wrote him angry letters. Existence outran construction again.", 'source_hint': 'Zermelo (1904), well-ordering theorem'}

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

def _sphere(cr, view, cx, cy, r):
    _circ(cr, view, cx, cy, r, "text", 0.8, 1.5)
    cr.new_path(); cr.move_to(cx - r, cy); cr.line_to(cx + r, cy)
    cr.set_source_rgba(*view.colors["muted"], 0.45); cr.set_line_width(1); cr.stroke()
    cr.new_path()
    for i in range(25):
        f = i / 24; a = f * 3.1416
        x = cx + r * math.cos(a); y = cy + r * 0.28 * math.sin(a)
        cr.line_to(x, y) if i else cr.move_to(x, y)
    cr.set_source_rgba(*view.colors["muted"], 0.45); cr.set_line_width(1); cr.stroke()

def _bars(cr, view, items, x0, y0, bw, gap, maxv):
    for i, (lbl, v, val) in enumerate(items):
        bh = (v / maxv) * (view.h * 0.42)
        cr.rectangle(x0 + i * (bw + gap), y0 - bh, bw, bh)
        cr.set_source_rgba(*view.colors["square"], 0.35 + 0.5 * v / maxv); cr.fill()
        _t(cr, view, x0 + i * (bw + gap) + bw / 2, y0 + 20, lbl, 11, "muted")
        _t(cr, view, x0 + i * (bw + gap) + bw / 2, y0 - bh - 12, val, 11, "text")


def paint(cr,view):
    w,h,t=view.w,view.h,view.t
    rng=_rnd.Random(2)
    for _ in range(16):
        _circ(cr,view,w*(0.08+rng.random()*0.3),h*(0.2+rng.random()*0.5),4,"muted",0.7,fill=True)
    _t(cr,view,w*0.22,h*0.82,"any messy set",10,"muted")
    _arr(cr,view,w*0.42,h*0.46,w*0.52,h*0.46,"square",0.9)
    for i in range(7):
        x=w*(0.54+i*0.06); _circ(cr,view,x,h*0.46,6,"square",0.95,1.5); _t(cr,view,x,h*0.56,str(i+1),9,"square")
    _line(cr,view,w*0.54,h*0.46,w*0.94,h*0.46,"muted",0.5)
    _t(cr,view,w*0.74,h*0.34,"... lined up, first to last",10,"square")
    _t(cr,view,w/2,h*0.9,"with choice, even the reals can be well-ordered",11,"square")

