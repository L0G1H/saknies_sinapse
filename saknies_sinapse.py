import json
import turtle
import random
import time


def generate_points(
    num_points: int, screen_width: int, screen_height: int
) -> list[int, int]:
    points = []
    for _ in range(num_points):
        x = random.randint(-screen_width // 2, screen_width // 2)
        y = random.randint(-screen_height // 2, screen_height // 2)
        points.append((x, y))
    return points


def connect_points(
    screen: turtle.Screen, points: list[int, int], pallete: list[str]
) -> None:
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(10)

    for point in points:
        t.penup()
        t.goto(point)
        t.dot(10, "white")

    points_copy = points.copy()

    point = points_copy.pop(random.randint(0, len(points_copy) - 1))
    t.penup()
    t.goto(point)
    t.pendown()

    while points_copy:
        point = points_copy.pop(random.randint(0, len(points_copy) - 1))
        t.color(random.choice(pallete))
        t.goto(point)
        screen.update()
        time.sleep(0.1)


def draw_branch(
    t: turtle.Turtle,
    branch_length: int,
    depth: int,
    angle_range: int,
    color_palette: list[str],
) -> None:
    if depth == 0:
        return

    pen_size = max(1, depth * 1.5)
    t.pensize(pen_size)

    max_depth_before_one_color = 6

    if depth > max_depth_before_one_color:
        t.color("#8B4513")
    else:
        t.color(random.choice(color_palette))

    t.forward(branch_length)

    current_angle_range = angle_range * (1 + (8 - depth) * 0.1)

    num_branches = random.randint(2, 3)
    angles = [
        random.uniform(-current_angle_range, current_angle_range)
        for _ in range(num_branches)
    ]

    for angle in angles:
        t.right(angle)
        new_length = branch_length * random.uniform(0.6, 0.8)
        draw_branch(t, new_length, depth - 1, angle_range, color_palette)
        t.left(angle)

    t.backward(branch_length)


def connect(screen: turtle.Screen, pallete: list[str]) -> None:
    screen.clear()
    screen.bgcolor("black")
    points = generate_points(
        random.randint(30, 60), screen.window_width(), screen.window_height()
    )
    connect_points(screen, points, pallete)

    time.sleep(2)


def tree(screen: turtle.Screen, pallete: list[str]) -> None:
    screen.clear()
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.left(90)
    t.penup()
    t.goto(0, -200)
    t.pendown()

    initial_length = 120
    depth = 8
    angle_range = 30

    draw_branch(t, initial_length, depth, angle_range, pallete)
    screen.update()

    time.sleep(2)


if __name__ == "__main__":
    with open("palettes.json", encoding="utf-8") as f:
        palletes_data = json.load(f)

    palettes = list(palletes_data.values())

    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("black")
    screen.title("Animation")
    screen.tracer(0)

    chance_for_tree = 0.15

    while True:
        choice = random.random()

        if choice < chance_for_tree:
            pallete = palletes_data["greenery"]
            tree(screen, pallete)
        else:
            pallete = random.choice(palettes)
            connect(screen, pallete)
