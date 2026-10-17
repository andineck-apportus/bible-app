"""Sprechblase als eine einzige Form: abgerundetes Rechteck mit eingebauter Spitze (kein Übergang, keine Abdeckung).

Die Spitze geht von der Seite aus, die der sprechenden Figur (tx, ty) zugewandt ist, und sitzt dort möglichst nahe bei ihr.
"""


def bubble_path(x, y, w, h, tx, ty, r=8, half=4.5):
    dx = tx - min(max(tx, x), x + w)
    dy = ty - min(max(ty, y), y + h)
    side = ("bottom" if dy > 0 else "top") if abs(dy) >= abs(dx) else ("right" if dx > 0 else "left")
    bx = min(max(tx, x + r + half), x + w - r - half)
    by = min(max(ty, y + r + half), y + h - r - half)
    f = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")  # noqa: E731
    t = f"L{f(tx)} {f(ty)}"
    d = [f"M{f(x + r)} {f(y)}"]
    if side == "top":
        d.append(f"L{f(bx - half)} {f(y)}{t}L{f(bx + half)} {f(y)}")
    d.append(f"H{f(x + w - r)}A{r} {r} 0 0 1 {f(x + w)} {f(y + r)}")
    if side == "right":
        d.append(f"L{f(x + w)} {f(by - half)}{t}L{f(x + w)} {f(by + half)}")
    d.append(f"V{f(y + h - r)}A{r} {r} 0 0 1 {f(x + w - r)} {f(y + h)}")
    if side == "bottom":
        d.append(f"L{f(bx + half)} {f(y + h)}{t}L{f(bx - half)} {f(y + h)}")
    d.append(f"H{f(x + r)}A{r} {r} 0 0 1 {f(x)} {f(y + h - r)}")
    if side == "left":
        d.append(f"L{f(x)} {f(by + half)}{t}L{f(x)} {f(by - half)}")
    d.append(f"V{f(y + r)}A{r} {r} 0 0 1 {f(x + r)} {f(y)}Z")
    return "".join(d)
