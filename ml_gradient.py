"""Gradient Descent — pick the update formula.

A code game: pulses of "gradient" flow through the network from
inputs (left) to outputs (right), endlessly.
"""
import math

GAME = {
    "type": "game",
    "id": "ml-gradient-001",
    "kind": "quiz",
    "kicker": "ML BASICS",
    "topic": "Machine learning",
    "title": "Gradient Descent",
    "question": "Which formula describes a single step of gradient "
                "descent for updating model parameters?",
    "choices": [
        {"id": "minus", "label": "θ = θ − α · ∇θL(θ)"},
        {"id": "plus", "label": "θ = θ + α · ∇θL(θ)"},
        {"id": "swap", "label": "θ = ∇θL(θ) · θ"},
    ],
    "answer": "minus",
    "explanation": "Gradient descent steps against the gradient: "
                   "θ moves opposite to ∇θL(θ), scaled by the "
                   "learning rate α.",
}

LAYERS = [3, 4, 2]


def paint(cr, view):
    pts = view.network_positions(LAYERS, view.w, view.h)
    by_layer = {}
    for x, y, li in pts:
        by_layer.setdefault(li, []).append((x, y))
    strong = view.colors["square"]
    cr.set_source_rgba(*view.colors["muted"], 0.18)
    cr.set_line_width(1.0)
    links = []
    for li in sorted(by_layer)[:-1]:
        for x1, y1 in by_layer[li]:
            for x2, y2 in by_layer[li + 1]:
                cr.move_to(x1, y1)
                cr.line_to(x2, y2)
                links.append((x1, y1, x2, y2))
    cr.stroke()
    # gradient pulses travelling left -> right along the links
    for i, (x1, y1, x2, y2) in enumerate(links):
        frac = (view.t * 0.45 + i * 0.13) % 1.0
        cr.arc(x1 + (x2 - x1) * frac, y1 + (y2 - y1) * frac,
               2.6, 0, 6.2832)
        cr.set_source_rgba(*strong, 0.5)
        cr.fill()
    for x, y, li in pts:
        wave = math.sin(view.t * 2.0 - li * 1.1)
        cr.arc(x, y, 13 + 2.5 * wave, 0, 6.2832)
        cr.set_source_rgba(*view.colors["bg"], 1)
        cr.fill_preserve()
        cr.set_source_rgba(*strong, 0.6 + 0.35 * wave)
        cr.set_line_width(1.4)
        cr.stroke()
