import json
import turtle
import random
import time


def generate_points(num_points, screen_width, screen_height):
    points = []
    for _ in range(num_points):
        x = random.randint(-screen_width // 2, screen_width // 2)
        y = random.randint(-screen_height // 2, screen_height // 2)
        points.append((x, y))
    return points


def connect_points(screen, points, colours):
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
        t.color(random.choice(colours))
        t.goto(point)
        screen.update()
        time.sleep(0.1)


def draw_branch(t, branch_length, depth, angle_range, color_palette):
    if depth == 0:
        return

    pen_size = max(1, depth * 1.5)
    t.pensize(pen_size)

    if depth > 5:
        t.color("#8B4513")
    else:
        t.color(random.choice(color_palette))

    t.forward(branch_length)

    current_angle_range = angle_range * (1 + (8 - depth) * 0.1)

    num_branches = random.randint(2, 3)
    angles = [random.uniform(-current_angle_range, current_angle_range) for _ in range(num_branches)]

    for angle in angles:
        t.right(angle)
        new_length = branch_length * random.uniform(0.6, 0.8)
        draw_branch(t, new_length, depth - 1, angle_range, color_palette)
        t.left(angle)

    t.backward(branch_length)


def main():
    with open("palettes.json", encoding="utf-8") as f:
        palletes_data = json.load(f)

    palettes = [pallete for pallete in palletes_data.values()]

    screen = turtle.Screen()
    screen.setup(width=1.0, height=1.0)
    screen.bgcolor("black")
    screen.title("Animation")
    screen.tracer(0)

    while True:
        choice = random.random()

        if choice > 0.15:
            pallete = random.choice(palettes)

            connect(screen, pallete)

        else:
            pallete = palletes_data["greenery"]

            tree(screen, pallete)



def connect(screen, pallete):
    screen.clear()
    screen.bgcolor("black")
    points = generate_points(random.randint(30, 60), screen.window_width(), screen.window_height())
    connect_points(screen, points, pallete)

    time.sleep(2)


def tree(screen, pallete):
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
    main()