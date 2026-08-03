"""
Turtle Graphics: Anime-style Character Portrait (v2, closer match)
--------------------------------------------------------------------
Improvements over v1:
- Scalloped, pointed headpiece with gold zig-zag trim (was a plain dome)
- Bat-wing shaped black ear pieces at temple level (was bows on top)
- Soft layered bangs with a center V-part (was a triangular block)
- Thin natural eyebrows instead of thick black triangles
- Larger, blue-violet eyes
- Smooth wavy twin-tails with a red ribbon accent (was jagged zig-zag)
- Collar with pointed lapels, gold trim, red gem, and hanging red cords

Run with: python3 turtle_character.py
"""

import turtle
import random
import math

# ---------------------------------------------------------------
# Setup
# ---------------------------------------------------------------
screen = turtle.Screen()
screen.setup(600, 680)
screen.bgcolor("#5FB8DE")
screen.title("Turtle Graphics - Anime Character v2")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
screen.tracer(0, 0)


def goto_pen(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def filled_circle(x, y, radius, color):
    t.color(color)
    goto_pen(x, y - radius)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def filled_blob(points, color):
    """Crisp-edged filled polygon (straight lines) - good for pointed shapes."""
    t.color(color)
    goto_pen(*points[0])
    t.begin_fill()
    for p in points[1:]:
        t.goto(p)
    t.goto(points[0])
    t.end_fill()


def smooth_curve(points, color, steps=30):
    """Filled blob with Catmull-Rom smoothing - good for soft/organic shapes."""
    n = len(points)
    pts = []
    for i in range(n):
        p0 = points[(i - 1) % n]
        p1 = points[i]
        p2 = points[(i + 1) % n]
        p3 = points[(i + 2) % n]
        for s in range(steps):
            u = s / steps
            u2, u3 = u * u, u * u * u
            x = 0.5 * ((2*p1[0]) + (-p0[0]+p2[0])*u +
                       (2*p0[0]-5*p1[0]+4*p2[0]-p3[0])*u2 +
                       (-p0[0]+3*p1[0]-3*p2[0]+p3[0])*u3)
            y = 0.5 * ((2*p1[1]) + (-p0[1]+p2[1])*u +
                       (2*p0[1]-5*p1[1]+4*p2[1]-p3[1])*u2 +
                       (-p0[1]+3*p1[1]-3*p2[1]+p3[1])*u3)
            pts.append((x, y))
    t.color(color)
    goto_pen(*pts[0])
    t.begin_fill()
    for p in pts[1:]:
        t.goto(p)
    t.end_fill()


def stroke_path(points, color, width=3):
    t.color(color)
    t.width(width)
    goto_pen(*points[0])
    for p in points[1:]:
        t.goto(p)
    t.width(1)


# ---------------------------------------------------------------
# Palette
# ---------------------------------------------------------------
HAIR = "#8B7B63"       # ash-brown
HAIR_SHADOW = "#6E5F49"
SKIN = "#F5DEC9"
WHITE = "#FBFAF6"
GOLD = "#D9B45C"
BLACK = "#161616"
RED = "#A5222A"
IRIS = "#5B6FB8"
IRIS_DARK = "#31407A"


# ---------------------------------------------------------------
# Background sparkles
# ---------------------------------------------------------------
def draw_sparkles():
    random.seed(11)
    t.color("white")
    for _ in range(24):
        x = random.randint(-290, 290)
        y = random.randint(-330, 320)
        size = random.choice([2, 3, 4])
        goto_pen(x, y)
        t.begin_fill()
        t.circle(size)
        t.end_fill()

    def star(x, y, size, color):
        t.color(color)
        goto_pen(x, y - size)
        t.begin_fill()
        for _ in range(4):
            t.forward(size * 2)
            t.left(150)
            t.forward(size * 2)
            t.right(150 - 90)
        t.end_fill()

    star(-230, -200, 22, "white")
    star(220, 90, 12, "white")


draw_sparkles()


# ---------------------------------------------------------------
# Hair back mass + twin-tails (smooth wavy locks, drawn first/behind)
# ---------------------------------------------------------------
def draw_twintail(cx, top_y, side):
    """side = -1 (left) / +1 (right). A smooth wavy lock ending lower down."""
    pts = [
        (cx, top_y),
        (cx + side*45, top_y - 60),
        (cx + side*10, top_y - 120),
        (cx + side*50, top_y - 190),
        (cx + side*15, top_y - 260),
        (cx + side*45, top_y - 330),
        (cx + side*20, top_y - 380),
    ]
    stroke_path(pts, HAIR, width=34)
    stroke_path(pts, HAIR_SHADOW, width=6)
    # small red ribbon band near the top of the tail
    band_x, band_y = pts[1]
    filled_blob([
        (band_x - 16, band_y + 8), (band_x + 16, band_y + 10),
        (band_x + 14, band_y - 10), (band_x - 14, band_y - 12)
    ], RED)


draw_twintail(-90, -10, -1)
draw_twintail(90, -10, 1)

# hair back mass behind the head
smooth_curve([
    (-155, 60), (-115, 155), (-40, 195), (40, 195),
    (115, 155), (155, 60), (135, -30), (0, -60), (-135, -30)
], HAIR)


# ---------------------------------------------------------------
# Face
# ---------------------------------------------------------------
smooth_curve([
    (-95, 40), (-98, 105), (-70, 160), (-30, 192), (0, 202),
    (30, 192), (70, 160), (98, 105), (95, 40),
    (58, -70), (0, -95), (-58, -70)
], SKIN)


# ---------------------------------------------------------------
# Bangs (soft layered fringe with a center V-part)
# ---------------------------------------------------------------
smooth_curve([
    (-92, 115), (-72, 168), (-45, 150), (-18, 172),
    (0, 132), (18, 172), (45, 150), (72, 168), (92, 115),
    (65, 88), (0, 78), (-65, 88)
], HAIR)

t.width(2)
t.color(HAIR_SHADOW)
for (dx, dy, ang, length) in [
    (-35, 128, -95, 60), (-10, 130, -85, 65),
    (12, 130, -95, 65), (38, 128, -105, 60),
]:
    goto_pen(dx, dy)
    t.setheading(ang)
    t.pendown()
    t.forward(length)
t.width(1)


# ---------------------------------------------------------------
# Eyebrows (thin, natural colored)
# ---------------------------------------------------------------
stroke_path([(-52, 58), (-38, 64), (-20, 60)], HAIR_SHADOW, width=3)
stroke_path([(52, 58), (38, 64), (20, 60)], HAIR_SHADOW, width=3)


# ---------------------------------------------------------------
# Eyes (larger, blue-violet)
# ---------------------------------------------------------------
def draw_eye(cx, cy, mirror=1):
    filled_blob([
        (cx - 26*mirror, cy - 2), (cx - 16*mirror, cy + 16),
        (cx + 16*mirror, cy + 12), (cx + 26*mirror, cy - 6),
        (cx + 8*mirror, cy - 18), (cx - 16*mirror, cy - 12)
    ], "white")
    filled_circle(cx, cy - 2, 14, IRIS)
    filled_circle(cx, cy, 7.5, IRIS_DARK)
    filled_circle(cx - 4*mirror, cy + 5, 3, "white")
    filled_circle(cx + 3*mirror, cy - 6, 1.5, "white")
    stroke_path([
        (cx - 26*mirror, cy - 2), (cx - 16*mirror, cy + 16),
        (cx + 16*mirror, cy + 12), (cx + 26*mirror, cy - 6)
    ], BLACK, width=3)
    stroke_path([
        (cx - 20*mirror, cy - 8), (cx, cy - 16), (cx + 20*mirror, cy - 10)
    ], "#8A6B5E", width=1)


draw_eye(-33, 22, mirror=1)
draw_eye(33, 22, mirror=-1)


# ---------------------------------------------------------------
# Nose & mouth (minimal)
# ---------------------------------------------------------------
stroke_path([(0, -8), (-4, -20)], "#D8AF92", width=2)
stroke_path([(-12, -42), (10, -42)], "#B97A6B", width=2)


# ---------------------------------------------------------------
# Bat-wing black ear pieces (temple level, mirrors reference)
# ---------------------------------------------------------------
def ear_piece(cx, cy, mirror=1):
    filled_blob([
        (cx, cy),
        (cx + 30*mirror, cy + 25),
        (cx + 48*mirror, cy - 10),
        (cx + 22*mirror, cy - 35),
        (cx, cy - 15),
    ], BLACK)


ear_piece(-88, 42, mirror=-1)
ear_piece(88, 42, mirror=1)


# ---------------------------------------------------------------
# Headpiece: scalloped bonnet with gold zig-zag trim
# ---------------------------------------------------------------
top_edge = [
    (-140, 145), (-125, 205), (-95, 175), (-75, 235),
    (-35, 190), (0, 245), (35, 190), (75, 235),
    (95, 175), (125, 205), (140, 145),
]
bottom_edge = [
    (140, 145), (95, 158), (45, 168), (0, 172),
    (-45, 168), (-95, 158), (-140, 145),
]
filled_blob(top_edge + bottom_edge, WHITE)

# gold zig-zag trim following the scalloped top edge
stroke_path(top_edge, GOLD, width=4)

# small gold gem at the front center dip
filled_circle(0, 178, 7, GOLD)
filled_circle(0, 178, 3.2, "#8B5E1E")

# subtle shading folds on the bonnet lobes
stroke_path([(-95, 175), (-75, 150)], "#E9D8B0", width=2)
stroke_path([(95, 175), (75, 150)], "#E9D8B0", width=2)


# ---------------------------------------------------------------
# Hanging red cords (from behind the ear pieces, down past the collar)
# ---------------------------------------------------------------
stroke_path([(-95, 20), (-105, -60), (-90, -140), (-100, -220)], RED, width=3)
stroke_path([(95, 20), (105, -60), (90, -140), (100, -220)], RED, width=3)


# ---------------------------------------------------------------
# Collar (pointed lapels, gold trim, red gem)
# ---------------------------------------------------------------
filled_blob([
    (-95, -85), (-118, -55), (-65, -95), (0, -70),
    (65, -95), (118, -55), (95, -85),
    (70, -160), (0, -135), (-70, -160),
], BLACK)

stroke_path([
    (-95, -85), (-118, -55), (-65, -95), (0, -70),
    (65, -95), (118, -55), (95, -85)
], GOLD, width=3)

filled_circle(0, -110, 11, RED)
filled_circle(0, -110, 5, "#5E1013")


# ---------------------------------------------------------------
# Done
# ---------------------------------------------------------------
screen.update()
screen.exitonclick()
