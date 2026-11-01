"""Binary 13 — a calm animated quiz scene.
Generated in the style of the three base games: monochrome,
view.colors only, Inter, slow motion from view.t.
Inspiration notes: see games-base/SOURCES.md (original idea, no copied assets).
"""
import math

GAME = {'id': 'math-binary-13-001', 'kind': 'quiz', 'kicker': 'MINI GAME', 'topic': 'Math', 'title': 'Binary 13', 'question': 'What is 13 written in binary?', 'choices': [{'id': 'b1101', 'label': '1101'}, {'id': 'b1011', 'label': '1011'}, {'id': 'b1110', 'label': '1110'}], 'answer': 'b1101', 'explanation': '13 = 8 + 4 + 1, so bits 1101 (one eight, one four, no two, one one).'}

SCENE = "bits"


def _frame(cr, view):
    if not view.answered:
        return
    col = view.colors["square"] if view.chosen == GAME["answer"] else view.colors["text"]
    cr.rectangle(10, 10, view.w - 20, view.h - 20)
    cr.set_source_rgba(*col, 0.9)
    cr.set_line_width(2.6 if view.chosen == GAME["answer"] else 1.6)
    cr.stroke()


def paint(cr, view):
    w, h, t = view.w, view.h, view.t
    cx, cy = w / 2, h / 2
    strong, text, muted = view.colors["square"], view.colors["text"], view.colors["muted"]
    cr.select_font_face("Inter", 0, 0)
    if SCENE == "pendulum":
        ang = 0.55 * math.sin(t * 0.9)
        length = min(w, h) * 0.34
        bx, by = cx + length * math.sin(ang), 34 + length * math.cos(ang)
        cr.move_to(cx, 34); cr.line_to(bx, by)
        cr.set_source_rgba(*muted, 0.7); cr.set_line_width(1.4); cr.stroke()
        cr.arc(cx, 34, 5, 0, 6.2832); cr.set_source_rgba(*strong, 0.9); cr.fill()
        cr.arc(bx, by, 13, 0, 6.2832); cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
        cr.set_source_rgba(*strong, 0.95); cr.set_line_width(1.6); cr.stroke()
        for k in range(5):
            a = -0.6 + k * 0.3
            cr.arc(cx + (length + 26) * math.sin(a), 34 + (length + 26) * math.cos(a), 2, 0, 6.2832)
            cr.set_source_rgba(*muted, 0.5); cr.fill()
    elif SCENE == "wave":
        cr.move_to(30, cy)
        for x in range(30, int(w - 29)):
            y = cy + 52 * math.sin(x * 0.022 - t * 1.1) * math.sin(t * 0.4 + x * 0.002)
            cr.line_to(x, y)
        cr.set_source_rgba(*strong, 0.85); cr.set_line_width(1.8); cr.stroke()
        cr.move_to(30, cy); cr.line_to(w - 30, cy)
        cr.set_source_rgba(*muted, 0.4); cr.set_line_width(1.0); cr.stroke()
        for k in range(4):
            x = 80 + k * (w - 160) / 3
            cr.arc(x, cy + 52 * math.sin(x * 0.022 - t * 1.1), 4, 0, 6.2832)
            cr.set_source_rgba(*text, 0.9); cr.fill()
    elif SCENE == "bars":
        vals = [0.42, 0.78, 0.3, 0.62, 0.9, 0.5]
        bw = min(64, w / 10)
        base = h * 0.82
        for i, v in enumerate(vals):
            bh = (v + 0.06 * math.sin(t * 1.2 - i)) * h * 0.58
            x = cx + (i - 2.5) * (bw + 18) - bw / 2
            cr.rectangle(x, base - bh, bw, bh)
            cr.set_source_rgba(*strong, 0.28 + 0.1 * i); cr.fill_preserve()
            cr.set_source_rgba(*text, 0.6); cr.set_line_width(1.1); cr.stroke()
        cr.move_to(40, base); cr.line_to(w - 40, base)
        cr.set_source_rgba(*muted, 0.6); cr.stroke()
    elif SCENE == "network":
        layers = [3, 4, 2]
        pts = view.network_positions(layers, w, h)
        by = {}
        for x, y, li in pts:
            by.setdefault(li, []).append((x, y))
        cr.set_source_rgba(*muted, 0.18); cr.set_line_width(1.0)
        links = []
        for li in sorted(by)[:-1]:
            for x1, y1 in by[li]:
                for x2, y2 in by[li + 1]:
                    cr.move_to(x1, y1); cr.line_to(x2, y2); links.append((x1, y1, x2, y2))
        cr.stroke()
        for i, (x1, y1, x2, y2) in enumerate(links):
            f = (t * 0.4 + i * 0.13) % 1.0
            cr.arc(x1 + (x2 - x1) * f, y1 + (y2 - y1) * f, 2.6, 0, 6.2832)
            cr.set_source_rgba(*strong, 0.5); cr.fill()
        for x, y, li in pts:
            wave = math.sin(t * 2.0 - li * 1.1)
            cr.arc(x, y, 13 + 2.5 * wave, 0, 6.2832)
            cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*strong, 0.6 + 0.35 * wave); cr.set_line_width(1.4); cr.stroke()
    elif SCENE == "orbits":
        radii = view.ring_radii(w, h, 4)
        for i, r in enumerate(radii):
            cr.arc(cx, cy, r, 0, 6.2832); cr.set_source_rgba(*muted, 0.55); cr.set_line_width(1.2); cr.stroke()
        cr.arc(cx, cy, 14, 0, 6.2832); cr.set_source_rgba(*strong, 0.95); cr.set_line_width(1.6); cr.stroke()
        for ring, start in ((1, 20), (2, 150), (3, 280), (4, 90)):
            r = radii[ring - 1]; a = math.radians(start + t * 14.0 / ring ** 1.5)
            cr.arc(cx + r * math.cos(a), cy + r * math.sin(a), 5, 0, 6.2832)
            cr.set_source_rgba(*strong, 0.95); cr.fill()
    elif SCENE == "triangle":
        pts = [(cx, h * 0.16), (w * 0.2, h * 0.84), (w * 0.8, h * 0.84)]
        for i in range(3):
            x1, y1 = pts[i]; x2, y2 = pts[(i + 1) % 3]
            cr.move_to(x1, y1); cr.line_to(x2, y2)
        cr.close_path(); cr.set_source_rgba(*muted, 0.8); cr.set_line_width(1.6); cr.stroke()
        f = (t * 0.25) % 3; idx = int(f); frac = f - idx
        x1, y1 = pts[idx]; x2, y2 = pts[(idx + 1) % 3]
        cr.arc(x1 + (x2 - x1) * frac, y1 + (y2 - y1) * frac, 5, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.95); cr.fill()
        for x, y in pts:
            cr.arc(x, y, 6 + 1.5 * math.sin(t * 1.6), 0, 6.2832)
            cr.set_source_rgba(*text, 0.8); cr.set_line_width(1.2); cr.stroke()
    elif SCENE == "grid":
        n = 4; cell = min(w, h) * 0.13; x0, y0 = cx - n * cell / 2, cy - n * cell / 2
        order = [(r, c) for r in range(n) for c in range(n)]
        for idx, (r, c) in enumerate(order):
            pulse = 0.25 + 0.55 * (0.5 + 0.5 * math.sin(t * 1.1 - idx * 0.45))
            cr.rectangle(x0 + c * cell + 3, y0 + (n - 1 - r) * cell + 3, cell - 6, cell - 6)
            cr.set_source_rgba(*strong, pulse); cr.fill()
    elif SCENE == "spiral":
        for k in range(90):
            a = k * 0.24 + t * 0.35; r = 4 + k * min(w, h) * 0.0042
            cr.arc(cx + r * math.cos(a), cy + r * math.sin(a), 2.4, 0, 6.2832)
            cr.set_source_rgba(*strong, 0.25 + 0.6 * k / 90); cr.fill()
    elif SCENE == "circles":
        for k in range(6):
            x = cx + (k - 2.5) * w * 0.11 + 12 * math.sin(t * 0.8 + k)
            y = cy + 44 * math.sin(t * 1.1 + k * 1.7)
            cr.arc(x, y, 15 + 4 * math.sin(t + k), 0, 6.2832)
            cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*strong, 0.75); cr.set_line_width(1.3); cr.stroke()
    elif SCENE == "stack":
        bw, bh = min(w * 0.42, 300), 34
        for k in range(5):
            off = 8 * math.sin(t * 0.9 - k * 0.7)
            cr.rectangle(cx - bw / 2 + off, h * 0.8 - k * (bh + 8), bw, bh)
            cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*text, 0.65); cr.set_line_width(1.2); cr.stroke()
        cr.arc(cx, h * 0.8 - 5 * (bh + 8) - 14 + 5 * math.sin(t * 1.4), 5, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.95); cr.fill()
    elif SCENE == "parabola":
        x0, y0, x1 = w * 0.14, h * 0.82, w * 0.86
        cr.move_to(x0, y0)
        for i in range(41):
            f = i / 40; cr.line_to(x0 + (x1 - x0) * f, y0 - math.sin(f * 3.1416) * h * 0.52)
        cr.set_source_rgba(*muted, 0.6); cr.set_line_width(1.2); cr.stroke()
        f = (t * 0.28) % 1.0
        cr.arc(x0 + (x1 - x0) * f, y0 - math.sin(f * 3.1416) * h * 0.52, 6, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.95); cr.fill()
        cr.move_to(30, y0); cr.line_to(w - 30, y0); cr.set_source_rgba(*muted, 0.5); cr.stroke()
    elif SCENE == "tree":
        nodes = [(cx, h * 0.16), (w * 0.3, h * 0.48), (w * 0.7, h * 0.48), (w * 0.18, h * 0.8), (w * 0.42, h * 0.8), (w * 0.58, h * 0.8), (w * 0.82, h * 0.8)]
        edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
        for a, b in edges:
            cr.move_to(*nodes[a]); cr.line_to(*nodes[b])
        cr.set_source_rgba(*muted, 0.5); cr.set_line_width(1.2); cr.stroke()
        f = (t * 0.3) % len(edges); idx = int(f); frac = f - idx
        a, b = edges[idx]
        cr.arc(nodes[a][0] + (nodes[b][0] - nodes[a][0]) * frac, nodes[a][1] + (nodes[b][1] - nodes[a][1]) * frac, 4.5, 0, 6.2832)
        cr.set_source_rgba(*text, 0.9); cr.fill()
        for x, y in nodes:
            cr.arc(x, y, 11, 0, 6.2832); cr.set_source_rgba(*view.colors["bg"], 1); cr.fill_preserve()
            cr.set_source_rgba(*strong, 0.8); cr.set_line_width(1.3); cr.stroke()
    else:  # bits
        for k in range(5):
            x = cx + (k - 2) * 58 - 22; y = cy - 22 + 6 * math.sin(t * 1.3 + k)
            cr.rectangle(x, y, 44, 44)
            on = (k + int(t * 0.8)) % 2 == 0
            if on:
                cr.set_source_rgba(*strong, 0.85); cr.fill()
            else:
                cr.set_source_rgba(*text, 0.55); cr.set_line_width(1.2); cr.stroke()
    _frame(cr, view)
