"""OR Truth Table - bespoke scene (logic/matrices/harmonics/NN/crypto/engineering batch). See SOURCES.md."""
import math

GAME = {'id': 'programming-or-truth-row-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Programming', 'title': 'OR Truth Table', 'question': 'In the OR truth table, the output is 0 for which row?', 'choices': [{'id': 'ff', 'label': 'A=0, B=0 only'}, {'id': 'tt', 'label': 'A=1, B=1'}, {'id': 'tf', 'label': 'A=1, B=0'}], 'answer': 'ff', 'explanation': 'OR fails only when nobody raises a hand: both inputs 0.'}

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


MODE = "table"
DATA = {'head': ['A', 'B', 'OR'], 'rows': [['1', '1', '1'], ['1', '0', '1'], ['0', '1', '1'], ['0', '0', '0']]}

def _grid(cr, view, mat, x0, y0, cell, hl=None):
    for r, row in enumerate(mat):
        for c, v in enumerate(row):
            x, y = x0 + c * cell, y0 + r * cell
            on = hl and (r, c) in hl
            cr.rectangle(x + 2, y + 2, cell - 4, cell - 4)
            if on:
                cr.set_source_rgba(*view.colors["square"], 0.85); cr.fill()
                _t(cr, view, x + cell/2, y + cell/2, str(v), 13, "bg")
            else:
                cr.set_source_rgba(*view.colors["text"], 0.5); cr.set_line_width(1); cr.stroke()
                _t(cr, view, x + cell/2, y + cell/2, str(v), 13, "text", 0.9)

def _wave(cr, view, amp, freq, phase, ybase, col="square", alpha=0.9, x0f=0.08, x1f=0.92):
    w, h = view.w, view.h
    cr.move_to(w * x0f, ybase)
    for i in range(121):
        f = i / 120
        cr.line_to(w * (x0f + (x1f - x0f) * f), ybase - amp * math.sin(freq * 6.2832 * f + phase + view.t * 0.7))
    cr.set_source_rgba(*view.colors[col], alpha); cr.set_line_width(1.8); cr.stroke()

def paint(cr, view):
    w, h, t = view.w, view.h, view.t
    d = DATA
    if MODE == "gate":
        a, b = d["in"]
        _box(cr, view, w*0.06, h*0.26, w*0.14, h*0.13, f"A={a}", 14)
        if b is not None: _box(cr, view, w*0.06, h*0.58, w*0.14, h*0.13, f"B={b}", 14)
        _box(cr, view, w*0.4, h*0.34, w*0.22, h*0.24, d["gate"], 18, fill_col="square")
        _line(cr, view, w*0.2, h*0.32, w*0.4, h*0.42, "muted", 0.7)
        if b is not None: _line(cr, view, w*0.2, h*0.64, w*0.4, h*0.5, "muted", 0.7)
        _arr(cr, view, w*0.62, h*0.46, w*0.8, h*0.46, "text", 0.85)
        out = d["out"]
        _circ(cr, view, w*0.86, h*0.46, 17, "square", 0.95, 1.8, fill=bool(out))
        _t(cr, view, w*0.86, h*0.6, f"out = {out}", 14, "square")
        f = (t * 0.5) % 1; _circ(cr, view, w*0.2 + f * w*0.2, h*0.37, 4, "text", 0.9, fill=True)
    elif MODE == "table":
        rows = d["rows"]
        for j, hd in enumerate(d["head"]): _t(cr, view, w*(0.3 + j*0.14), h*0.2, hd, 14, "square" if j == len(d["head"])-1 else "text")
        for i, row in enumerate(rows):
            y = h*0.32 + i * h*0.13
            if int(t * 0.8) % len(rows) == i:
                cr.rectangle(w*0.2, y - 13, w*0.6, 26); cr.set_source_rgba(*view.colors["square"], 0.2); cr.fill()
            for j, v in enumerate(row): _t(cr, view, w*(0.3 + j*0.14), y, v, 14, "square" if j == len(row)-1 else "text", 0.95)
    elif MODE == "venn":
        cx, cy, r = w/2, h/2, min(w, h)*0.27
        off = r * 0.72
        _circ(cr, view, cx - off/2, cy, r, "text", 0.8, 1.5); _circ(cr, view, cx + off/2, cy, r, "text", 0.8, 1.5)
        cr.new_path(); cr.arc(cx + (off/2 if d.get("zone") == "union" else -off/2) * 0 + (0 if d.get("zone") != "right" else off/2), cy, 4, 0, 6.2832)
        zone = d.get("zone", "both")
        zx = cx if zone == "both" else (cx - off if zone == "left" else (cx + off if zone == "right" else cx))
        pulse = 12 + 4 * math.sin(t * 1.8)
        _circ(cr, view, zx, cy, pulse, "square", 0.95, fill=True)
        _t(cr, view, cx - off, cy - r - 14, d["left"], 14); _t(cr, view, cx + off, cy - r - 14, d["right"], 14)
        _t(cr, view, cx, cy + r + 30, d["cap"], 13, "muted")
    elif MODE == "law":
        _box(cr, view, w*0.08, h*0.36, w*0.34, h*0.2, d["lhs"], 13)
        _t(cr, view, w/2, h*0.46, "=", 22, "square")
        _box(cr, view, w*0.58, h*0.36, w*0.34, h*0.2, d["rhs"], 13)
        _t(cr, view, w/2, h*0.26, d["cap"], 13, "muted")
        f = (t * 0.4) % 1; _circ(cr, view, w*0.08 + f * w*0.84, h*0.64, 4, "square", 0.9, fill=True)
    elif MODE in ("matrix", "matrix_op"):
        cell = min(w, h) * 0.11
        _grid(cr, view, d["a"], w*0.08, h*0.3, cell)
        if MODE == "matrix_op":
            _t(cr, view, w*0.36, h*0.48, d["op"], 24, "square")
            _grid(cr, view, d["b"], w*0.42, h*0.3, cell)
            _arr(cr, view, w*0.68, h*0.48, w*0.76, h*0.48, "text", 0.85)
            hl = {(0, 0), (1, 1)} if d.get("hl") == "diag" else None
            _grid(cr, view, d["res"], w*0.78, h*0.3, cell, hl)
        _t(cr, view, w/2, h*0.16, d["cap"], 13, "muted")
        k = int(t * 0.9) % 4
        cr.rectangle(w*0.08 + (k % 2) * cell, h*0.3 + (k // 2) * cell, cell, cell)
        cr.set_source_rgba(*view.colors["square"], 0.55); cr.set_line_width(2); cr.stroke()
    elif MODE == "transform":
        cx, cy, s = w/2, h/2, min(w, h)*0.2
        grow = 0.75 + 0.25 * math.sin(t * 0.8)
        pts = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        _rot = 0.35 * math.sin(t * 0.7)
        cr.new_path()
        for i, (px, py) in enumerate(pts):
            px, py = px * math.cos(_rot) - py * math.sin(_rot), px * math.sin(_rot) + py * math.cos(_rot)
            X, Y = px * s * (d.get("sx", 1) * grow if d.get("anim") == "x" else 1), py * s * (d.get("sy", 1) * grow if d.get("anim") == "y" else 1)
            X, Y = cx + X, cy + Y
            cr.move_to(X, Y) if i == 0 else cr.line_to(X, Y)
        cr.close_path(); cr.set_source_rgba(*view.colors["square"], 0.85); cr.set_line_width(1.8); cr.stroke()
        _line(cr, view, cx - s*1.4, cy, cx + s*1.4, cy, "muted", 0.5); _line(cr, view, cx, cy - s*1.4, cx, cy + s*1.4, "muted", 0.5)
        _t(cr, view, cx, cy + s*1.55, d["cap"], 13, "muted")
    elif MODE == "wave":
        _line(cr, view, w*0.06, h/2, w*0.94, h/2, "muted", 0.5)
        _wave(cr, view, d["amp"] * h * 0.28, d["freq"], 0, h/2)
        _arr(cr, view, w*0.5, h/2, w*0.5, h/2 - d["amp"] * h * 0.28, "text", 0.85)
        _t(cr, view, w*0.5 + 10, h/2 - d["amp"] * h * 0.16, f"A = {d['amp']}", 13, "text", align="l")
        _t(cr, view, w/2, h*0.14, d["cap"], 13, "muted")
    elif MODE == "super":
        _line(cr, view, w*0.06, h*0.3, w*0.94, h*0.3, "muted", 0.4)
        _line(cr, view, w*0.06, h*0.72, w*0.94, h*0.72, "muted", 0.4)
        _wave(cr, view, h*0.09, d["f1"], 0, h*0.3, "text", 0.7)
        _wave(cr, view, h*0.09, d["f2"], d.get("phase", 0), h*0.3, "muted", 0.7)
        _wave(cr, view, h*0.13 * d.get("gain", 1), d["f1"], 0, h*0.72, "square", 0.95)
        _t(cr, view, w*0.1, h*0.18, "two waves", 12, "muted", align="l")
        _t(cr, view, w*0.1, h*0.6, d["cap"], 12, "square", align="l")
    elif MODE == "fourier":
        for k, (amp, fq) in enumerate(d["terms"]):
            _wave(cr, view, h * amp, fq, 0, h * (0.22 + k * 0.18), "text" if k else "square", 0.75)
            _t(cr, view, w*0.9, h * (0.22 + k * 0.18), f"x{fq}", 11, "muted", align="r")
        _t(cr, view, w/2, h*0.88, d["cap"], 12, "muted")
    elif MODE == "standing":
        _line(cr, view, w*0.06, h/2, w*0.94, h/2, "muted", 0.45)
        for sgn in (1, -1):
            cr.move_to(w*0.08, h/2)
            for i in range(121):
                f = i/120; cr.line_to(w*(0.08 + 0.84*f), h/2 - sgn * h*0.24 * math.sin(f * 6.2832 * d["half"]) * math.sin(t * 1.6))
            cr.set_source_rgba(*view.colors["muted"], 0.6); cr.set_line_width(1.2); cr.stroke()
        _wave(cr, view, h*0.24 * abs(math.sin(t * 1.6)), d["half"], 0, h/2, "square", 0.9)
        for k in range(d["half"] + 1):
            _circ(cr, view, w*(0.08 + 0.84 * k / d["half"]), h/2, 5, "square", 0.95, fill=True)
        _t(cr, view, w/2, h*0.16, "nodes stay still, antinodes swing most", 12, "muted")
    elif MODE == "spring":
        x0, y0 = w*0.14, h/2
        stretch = 1 + 0.25 * math.sin(t * 1.5)
        cr.move_to(x0, y0)
        for i in range(13):
            f = i/12; cr.line_to(x0 + f * w*0.4 * stretch, y0 + (18 if i % 2 else -18) * (1 if 0 < i < 12 else 0))
        cr.set_source_rgba(*view.colors["text"], 0.85); cr.set_line_width(1.7); cr.stroke()
        bx = x0 + w*0.4 * stretch
        _box(cr, view, bx, y0 - 24, 54, 48, "m", 15, fill_col="square")
        _t(cr, view, w/2, h*0.2, d["cap"], 13, "muted")
    elif MODE == "conv":
        cell = min(w, h) * 0.075
        _grid(cr, view, d["a"], w*0.06, h*0.24, cell)
        kx = int(t * 0.8) % 3; ky = (int(t * 0.8) // 3) % 3
        cr.rectangle(w*0.06 + kx * cell, h*0.24 + ky * cell, cell * 2, cell * 2)
        cr.set_source_rgba(*view.colors["square"], 0.9); cr.set_line_width(2.4); cr.stroke()
        _t(cr, view, w*0.06, h*0.16, "input", 12, "muted", align="l")
        _grid(cr, view, d["k"], w*0.52, h*0.24, cell)
        _t(cr, view, w*0.52, h*0.16, "kernel", 12, "muted", align="l")
        _arr(cr, view, w*0.78, h*0.48, w*0.84, h*0.48, "text", 0.85)
        _grid(cr, view, [[k + ky * 3 for k in range(3)]], w*0.85, h*0.42, cell, {(0, (int(t) % 3))})
        _t(cr, view, w*0.88, h*0.34, "map", 12, "muted")
    elif MODE == "pool":
        cell = min(w, h) * 0.1
        _grid(cr, view, d["a"], w*0.12, h*0.26, cell, {(0, 1), (1, 0), (2, 3), (3, 2)})
        _arr(cr, view, w*0.58, h*0.48, w*0.68, h*0.48, "text", 0.85)
        _grid(cr, view, d["res"], w*0.7, h*0.32, cell * 1.4, {(int(t) % 2, int(t * 0.5) % 2)})
        _t(cr, view, w/2, h*0.16, d["cap"], 13, "muted")
    elif MODE == "curve":
        x0, y0, x1, y1 = w*0.14, h*0.78, w*0.88, h*0.2
        _line(cr, view, x0, y0, x1, y0, "muted", 0.5); _line(cr, view, w/2, y0, w/2, y1, "muted", 0.5)
        kind = d["kind"]
        cr.move_to(x0, y0 if kind != "relu" else y0)
        for i in range(81):
            f = i/80; x = x0 + (x1-x0)*f; u = f - 0.5
            if kind == "relu": y = y0 - (y0-y1) * max(0, u) * 1.4
            elif kind == "sigmoid": y = y0 - (y0-y1) / (1 + math.exp(-u * 10))
            elif kind == "tanh": y = (y0 + y1)/2 - (y0-y1)*0.42 * math.tanh(u * 5)
            elif kind == "leaky": y = y0 - (y0-y1) * (u if u > 0 else u * 0.15) * 1.4
            else: y = y0 - (y0-y1) * (u*u if kind == "square" else abs(u))
            cr.line_to(x, y)
        cr.set_source_rgba(*view.colors["square"], 0.95); cr.set_line_width(2); cr.stroke()
        f = (t * 0.3) % 1; _circ(cr, view, x0 + (x1-x0)*f, y0 - (y0-y1)*0.4, 4, "text", 0.9, fill=True)
        _t(cr, view, x1, y1, d["cap"], 13, "square", align="r")
    elif MODE == "bars_hint":
        vals = d["vals"]; mx = max(vals)
        for i, v in enumerate(vals):
            x = w*0.16 + i * w*0.22; bh = (v/mx) * h*0.5
            cr.rectangle(x, h*0.76 - bh, w*0.13, bh); cr.set_source_rgba(*view.colors["square"], 0.4 + 0.4*v/mx); cr.fill()
            _t(cr, view, x + w*0.065, h*0.84, str(v), 12, "muted")
        _t(cr, view, w/2, h*0.14, d["cap"], 13, "muted")
        cr.rectangle(w*0.16 + (int(t) % len(vals)) * w*0.22 - 4, h*0.2, w*0.13 + 8, h*0.6); cr.set_source_rgba(*view.colors["text"], 0.5); cr.set_line_width(1.2); cr.stroke()
    elif MODE == "softmax":
        vals = d["vals"]; mx = max(vals); ex = [math.exp(v - mx) for v in vals]; tot = sum(ex); probs = [e/tot for e in ex]
        for i, (v, p) in enumerate(zip(vals, probs)):
            x = w*0.14 + i * w*0.2; bh = p * h*0.52
            cr.rectangle(x, h*0.76 - bh, w*0.12, bh); cr.set_source_rgba(*view.colors["square"], 0.35 + 0.55*p/max(probs)); cr.fill()
            _t(cr, view, x + w*0.06, h*0.76 - bh - 14, f"{p:.2f}", 12, "square")
            _t(cr, view, x + w*0.06, h*0.84, f"z={v}", 12, "muted")
        _t(cr, view, w/2, h*0.14, "probabilities sum to 1", 13, "muted")
        cr.rectangle(w*0.14 + (int(t) % len(vals)) * w*0.2 - 4, h*0.2, w*0.12 + 8, h*0.6); cr.set_source_rgba(*view.colors["text"], 0.5); cr.set_line_width(1.2); cr.stroke()
    elif MODE == "attention":
        cell = min(w, h) * 0.085
        _grid(cr, view, d["a"], w*0.18, h*0.22, cell)
        _t(cr, view, w*0.18, h*0.16, "Q K^T scores -> weights", 12, "muted", align="l")
        k = int(t * 1.2) % 9
        cr.rectangle(w*0.18 + (k % 3) * cell, h*0.22 + (k // 3) * cell, cell, cell)
        cr.set_source_rgba(*view.colors["square"], 0.95); cr.set_line_width(2.4); cr.stroke()
        _arr(cr, view, w*0.62, h*0.48, w*0.72, h*0.48, "text", 0.85)
        _box(cr, view, w*0.74, h*0.38, w*0.18, h*0.18, "weighted V", 12)
    elif MODE == "nodes_net":
        pts = view.network_positions(d["layers"], w, h)
        by = {}
        for x, y, li in pts: by.setdefault(li, []).append((x, y))
        cr.set_source_rgba(*view.colors["muted"], 0.2); cr.set_line_width(1)
        links = []
        for li in sorted(by)[:-1]:
            for x1, y1 in by[li]:
                for x2, y2 in by[li+1]: cr.move_to(x1, y1); cr.line_to(x2, y2); links.append((x1, y1, x2, y2))
        cr.stroke()
        off = set(d.get("off", [])); flat = [p for p in pts]
        for i, (x, y, li) in enumerate(flat):
            dead = i in off and int(t * 1.4) % 2 == 0
            _circ(cr, view, x, y, 12, "muted" if dead else "square", 0.35 if dead else 0.9, 1.3)
        for i, (x1, y1, x2, y2) in enumerate(links):
            f = (t * 0.4 + i * 0.17) % 1; _circ(cr, view, x1 + (x2-x1)*f, y1 + (y2-y1)*f, 2.4, "square", 0.55, fill=True)
        _t(cr, view, w/2, h*0.1, d["cap"], 13, "muted")
    elif MODE == "residual":
        _box(cr, view, w*0.08, h*0.4, w*0.16, h*0.15, "x", 15)
        _box(cr, view, w*0.36, h*0.4, w*0.2, h*0.15, "F(x)", 15)
        _circ(cr, view, w*0.7, h*0.475, 16, "square", 0.95, 1.8); _t(cr, view, w*0.7, h*0.475, "+", 18)
        _arr(cr, view, w*0.72, h*0.46, w*0.86, h*0.46, "text", 0.85); _t(cr, view, w*0.9, h*0.46, "y", 15)
        _arr(cr, view, w*0.24, h*0.48, w*0.36, h*0.48, "muted", 0.7)
        cr.move_to(w*0.16, h*0.4); cr.line_to(w*0.16, h*0.2); cr.line_to(w*0.7, h*0.2); cr.line_to(w*0.7, h*0.44)
        cr.set_source_rgba(*view.colors["square"], 0.8); cr.set_line_width(1.5); cr.stroke()
        _t(cr, view, w*0.42, h*0.15, "skip connection", 12, "square")
        f = (t * 0.45) % 1; _circ(cr, view, w*0.16 + f * w*0.54, h*0.2, 4, "square", 0.95, fill=True)
    elif MODE == "shift":
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        sh = d["shift"]
        y = h * 0.34
        for i, ch in enumerate(letters[:13]):
            x = w*0.06 + i * w*0.07
            _t(cr, view, x, y, ch, 14, "square" if i == int(t) % 13 else "text", 0.95)
            _t(cr, view, x, y + 36, letters[(i + sh) % 26], 14, "muted", 0.9)
        _arr(cr, view, w*0.2, h*0.56, w*0.34, h*0.56, "text", 0.8)
        _t(cr, view, w/2, h*0.2, f"each letter shifts by {sh}", 13, "muted")
        _t(cr, view, w*0.42, h*0.56, d["cap"], 13, "square", align="l")
    elif MODE == "xorbits":
        for r, (lbl, bits) in enumerate(d["rows"]):
            y = h*0.26 + r * h*0.18
            _t(cr, view, w*0.08, y, lbl, 12, "muted", align="l")
            for i, bit in enumerate(bits):
                x = w*0.34 + i * 44
                _box(cr, view, x, y - 15, 34, 30, bit, 13, fill_col="square" if (r == 2 and i == int(t*1.5) % len(bits)) else None)
        _t(cr, view, w/2, h*0.86, "same bits -> 0, different -> 1", 12, "muted")
    elif MODE == "hashbits":
        for r, lbl in enumerate(("input A", "input B", "hash A", "hash B")):
            y = h*0.2 + r * h*0.17
            _t(cr, view, w*0.06, y, lbl, 12, "muted", align="l")
            bits = d["rows"][r]
            for i, bit in enumerate(bits):
                flip = r >= 2 and i in d.get("flip", []) and r == 3
                _box(cr, view, w*0.3 + i * 36, y - 13, 28, 26, str(bit), 11, fill_col="square" if flip else None)
        _circ(cr, view, w*0.3 + ((t * 42) % (w*0.5)), h*0.9, 4, "square", 0.8, fill=True)
        _t(cr, view, w/2, h*0.96, d["cap"], 11, "muted")
    elif MODE == "keys":
        _box(cr, view, w*0.06, h*0.38, w*0.2, h*0.18, d["left"], 12)
        _box(cr, view, w*0.4, h*0.38, w*0.2, h*0.18, d["mid"], 12, fill_col="square")
        _box(cr, view, w*0.74, h*0.38, w*0.2, h*0.18, d["right"], 12)
        _arr(cr, view, w*0.26, h*0.47, w*0.4, h*0.47, "muted", 0.7); _arr(cr, view, w*0.6, h*0.47, w*0.74, h*0.47, "muted", 0.7)
        _t(cr, view, w/2, h*0.26, d["cap"], 13, "muted")
        f = (t * 0.45) % 1; _circ(cr, view, w*0.06 + f * w*0.88, h*0.47, 5, "text", 0.9, fill=True)
    elif MODE == "chain":
        for i in range(3):
            x = w*0.08 + i * w*0.3
            _box(cr, view, x, h*0.36, w*0.22, h*0.22, f"block {i}", 13)
            _t(cr, view, x + w*0.11, h*0.52, d["hashes"][i], 10, "muted")
            if i < 2: _arr(cr, view, x + w*0.22, h*0.47, x + w*0.3, h*0.47, "square", 0.9)
        _t(cr, view, w/2, h*0.24, "each block stores the previous hash", 12, "muted")
        pulse = int(t * 0.8) % 3; _circ(cr, view, w*0.08 + pulse * w*0.3 + w*0.11, h*0.3, 5, "square", 0.95, fill=True)
    elif MODE == "beam":
        y = h * 0.34
        _line(cr, view, w*0.1, y, w*0.9, y, "text", 0.9, 2.4)
        _line(cr, view, w*0.1, y, w*0.1, h*0.78, "text", 0.8, 2); _line(cr, view, w*0.9, y, w*0.9, h*0.78, "text", 0.8, 2)
        cr.move_to(w*0.1, y + 4)
        for i in range(41):
            f = i/40; cr.line_to(w*(0.1 + 0.8*f), y + 4 + h*0.22 * math.sin(f * 3.1416) * (0.8 + 0.2*math.sin(t)))
        cr.set_source_rgba(*view.colors["square"], 0.85); cr.set_line_width(1.8); cr.stroke()
        _arr(cr, view, w/2, h*0.14, w/2, y - 4, "square", 0.95, 2)
        _t(cr, view, w/2, h*0.1, d["cap"], 12, "square")
    elif MODE == "gear":
        for cx, cy, r, teeth, sgn, lbl in d["gears"]:
            cxp, cyp = w*cx, h*cy
            for k in range(teeth):
                a = k * 6.2832/teeth + sgn * t * 0.5
                _line(cr, view, cxp + r*0.82*math.cos(a), cyp + r*0.82*math.sin(a), cxp + r*math.cos(a), cyp + r*math.sin(a), "text", 0.8, 2.4)
            _circ(cr, view, cxp, cyp, r*0.82, "text", 0.85, 1.6); _circ(cr, view, cxp, cyp, 6, "square", 0.95, fill=True)
            _t(cr, view, cxp, cyp + r + 22, lbl, 12, "muted")
    elif MODE == "lever":
        cx, cy = w * d.get("fulcrum", 0.5), h*0.62
        tilt = 0.1 * math.sin(t * 1.1)
        x1, y1, x2, y2 = w*0.12, cy - (cx - w*0.12) * tilt, w*0.88, cy + (w*0.88 - cx) * tilt
        _line(cr, view, x1, y1, x2, y2, "text", 0.9, 3)
        cr.new_path(); cr.move_to(cx, cy); cr.line_to(cx - 20, h*0.78); cr.line_to(cx + 20, h*0.78); cr.close_path()
        cr.set_source_rgba(*view.colors["square"], 0.9); cr.fill()
        _box(cr, view, x1 + 6, y1 - 44, 62, 34, d.get("left", "load"), 11)
        _arr(cr, view, x2 - 10, y2 - 54, x2 - 10, y2 - 8, "square", 0.95)
        _t(cr, view, x2 - 10, y2 - 66, d.get("right", "effort"), 11, "square")
        _t(cr, view, cx, h*0.86, "fulcrum", 12, "muted")
    elif MODE == "pulley":
        cx, cy, r = w/2, h*0.26, 34
        _circ(cr, view, cx, cy, r, "text", 0.9, 1.8)
        lift = 14 * math.sin(t * 1.2)
        _line(cr, view, cx - r, cy, cx - r, h*0.66 + lift, "muted", 0.8); _line(cr, view, cx + r, cy, cx + r, h*0.5, "muted", 0.8)
        _box(cr, view, cx - r - 30, h*0.66 + lift, 60, 36, "load", 12)
        _arr(cr, view, cx + r, h*0.5, cx + r, h*0.72, "square", 0.95)
        _t(cr, view, cx + r + 10, h*0.64, "pull", 11, "square", align="l")
        _t(cr, view, w/2, h*0.9, d["cap"], 12, "muted")
    elif MODE == "engcurve":
        x0, y0, x1, y1 = w*0.14, h*0.78, w*0.88, h*0.2
        _line(cr, view, x0, y0, x1, y0, "muted", 0.5); _line(cr, view, x0, y0, x0, y1, "muted", 0.5)
        cr.move_to(x0, y0)
        for i in range(61):
            f = i/60
            y = y0 - (y0-y1) * (f*1.15 if f < 0.55 else 0.63 + 0.1*math.sin(f*22)*(1-f))
            cr.line_to(x0 + (x1-x0)*f, y)
        cr.set_source_rgba(*view.colors["square"], 0.95); cr.set_line_width(1.9); cr.stroke()
        _t(cr, view, x0 + 8, y1, d["ylabel"], 12, "muted", align="l"); _t(cr, view, x1, y0 + 24, d["xlabel"], 12, "muted", align="r")
        _f = (t * 0.25) % 1; _y = y0 - (y0-y1) * (_f*1.15 if _f < 0.55 else 0.63)
        _circ(cr, view, x0 + (x1-x0)*_f, _y, 5, "text", 0.95, fill=True)
    elif MODE == "feedback":
        _box(cr, view, w*0.06, h*0.4, w*0.18, h*0.15, "setpoint", 11)
        _circ(cr, view, w*0.32, h*0.475, 14, "square", 0.95, 1.6); _t(cr, view, w*0.32, h*0.475, "-", 16)
        _box(cr, view, w*0.42, h*0.4, w*0.18, h*0.15, d.get("ctrl", "controller"), 11)
        _box(cr, view, w*0.7, h*0.4, w*0.2, h*0.15, d.get("plant", "plant"), 11)
        _arr(cr, view, w*0.24, h*0.47, w*0.3, h*0.47, "muted", 0.7); _arr(cr, view, w*0.34, h*0.47, w*0.42, h*0.47, "muted", 0.7); _arr(cr, view, w*0.6, h*0.47, w*0.7, h*0.47, "muted", 0.7)
        cr.move_to(w*0.8, h*0.55); cr.line_to(w*0.8, h*0.76); cr.line_to(w*0.32, h*0.76); cr.line_to(w*0.32, h*0.52)
        cr.set_source_rgba(*view.colors["square"], 0.85); cr.set_line_width(1.5); cr.stroke()
        _t(cr, view, w*0.56, h*0.82, "measured output feeds back", 11, "muted")
        f = (t * 0.5) % 1; _circ(cr, view, w*0.8 - f * w*0.48, h*0.76, 4, "square", 0.95, fill=True)
    elif MODE == "tube":
        y, hh = h*0.44, h*0.14
        for xfrac, wid, lbl, spd in d["sections"]:
            x = w * xfrac
            cr.rectangle(x, y - wid/2, w*0.24, wid); cr.set_source_rgba(*view.colors["text"], 0.55); cr.set_line_width(1.4); cr.stroke()
            _t(cr, view, x + w*0.12, y + wid/2 + 24, lbl, 11, "muted")
            for k in range(3):
                fx = x + ((t * spd * 30 + k * 30) % (w*0.22))
                _circ(cr, view, fx, y + (k-1)*wid*0.22, 3.4, "square", 0.9, fill=True)
        _t(cr, view, w/2, h*0.16, d["cap"], 12, "muted")
    _ans(cr, view)

