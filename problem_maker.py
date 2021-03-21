"""
plan
takes a 2D array and creates:
    - objects, paths
    - sets is-dirty, is-empty, is-clean, is-charger, is-trashplace, at roomba, battery-amount, trash-amount, steps

1. Take 2D array and validate it (check it has a roomba and the array size is valid)
2. Ask for the initial battery amount, trash-amount and steps
3. 


e.g.    ["T_C",
        "_O_",
        "X__"]

        X - starting
        C - charger
        T - trash
        O - Obstacles
        _ - dirty/empty spot
        (all occupied positions are clean by default)
"""
import random


def generateLocationObjects(grid):
    objects = []

    objects.append("roomba - roomba")

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            item = grid[y][x]
            objects.append(f"x{x}y{y} - location")

    return objects


def generateInitObjects(grid, charge_amount, trash_amount):
    objects = []

    objects.append(f"(=(battery-amount roomba) {charge_amount})")
    objects.append(f"(=(trash-amount roomba) {trash_amount})")

    # initial steps is always 0
    objects.append("(= (steps) 0)")

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            item = grid[y][x]
            # is-empty means obstacle
            if item == "_":
                # _ = empty and dirty
                objects.append(f"(is-empty x{x}y{y})")
                objects.append(f"(is-dirty x{x}y{y})")
            elif item == "O":
                # O = obstacle is clean
                objects.append(f"(is-clean x{x}y{y})")
            elif item == "C":
                # C = charger is clean
                objects.append(f"(is-empty x{x}y{y})")
                objects.append(f"(is-charger x{x}y{y})")
                objects.append(f"(is-clean x{x}y{y})")
            elif item == "T":
                # T = trash is clean
                objects.append(f"(is-empty x{x}y{y})")
                objects.append(f"(is-trashplace x{x}y{y})")
                objects.append(f"(is-clean x{x}y{y})")
            elif item == "X":
                # X = starting/roomba is dirty
                objects.append(f"(at roomba x{x}y{y})")
                objects.append(f"(is-empty x{x}y{y})")
                objects.append(f"(is-dirty x{x}y{y})")

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            item = grid[y][x]

            # check each direction and see if you can have a path
            if x - 1 >= 0:
                objects.append(f"(has-path x{x}y{y} x{x - 1}y{y})")
            if x + 1 < len(grid[y]):
                objects.append(f"(has-path x{x}y{y} x{x + 1}y{y})")
            if y + 1 < len(grid):
                objects.append(f"(has-path x{x}y{y} x{x}y{y + 1})")
            if y - 1 >= 0:
                objects.append(f"(has-path x{x}y{y} x{x}y{y - 1})")

            # if item != "O":
            #     # O = obstacle has no paths

            #     # check each direction and see if you can have a path
            #     if x - 1 >= 0 and grid[y][x - 1] != "O":
            #         objects.append(f"(has-path x{x}y{y} x{x - 1}y{y})")
            #     if x + 1 < len(grid[y]) and grid[y][x + 1] != "O":
            #         objects.append(f"(has-path x{x}y{y} x{x + 1}y{y})")
            #     if y + 1 < len(grid) and grid[y + 1][x] != "O":
            #         objects.append(f"(has-path x{x}y{y} x{x}y{y + 1})")
            #     if y - 1 >= 0 and grid[y - 1][x] != "O":
            #         objects.append(f"(has-path x{x}y{y} x{x}y{y - 1})")

    return objects


def generateGoalObjects(grid):
    objects = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            item = grid[y][x]
            objects.append(f"(is-clean x{x}y{y})")

    return objects


def generateProblem(grid, initial_charge, initial_trash_amount, n=0):
    location_objects = "\n".join(generateLocationObjects(grid))
    util_objects = "\n".join(
        generateInitObjects(grid, initial_charge, initial_trash_amount))
    goal_objects = "\n".join(generateGoalObjects(grid))

    problem_comment = ""
    for row in grid:
        problem_comment += f"; {row}\n"

    a = f"""
    (define (problem roomba_problem{n})\n
    	(:domain roomba)\n
    """

    b = f"""
        (:objects 
            {location_objects}
        )\n
    """

    c = f"""
        (:init 
            {util_objects}
        )\n
    """

    d = f"""
        (:goal
            (and
                {goal_objects}
            )
        )\n
    """

    e = f"""
        (:metric minimize
            (steps)
        )
    )\n
    """

    problem = problem_comment + a + b + c + d + e

    return problem


def isGridValid(grid, initial_charge, initial_trash_amount):
    width = len(grid[0])
    for row in grid:
        if len(row) != width:
            return False
    return True


def main():
    while True:
        input_grid = input("""Enter your grid like the follow example:

        T_C,_O_,X__

        This represents the following:

        e.g.["T_C",
            "_O_",
            "X__"]

            X - starting
            C - charger
            T - trash
            O - Obstacles
            _ - dirty/empty spot

        (all occupied positions are clean by default)\n\n\n\n\n""")

        print("\n\n\n\n")

        grid = input_grid.split(",")

        # initial_charge = int(input("Enter initial charge for the roombo (int): "))
        initial_charge = 100
        # initial_trash_amount = int(input("Enter initial trash amount for the roombo (int): "))
        initial_trash_amount = 0

        if (isGridValid(grid, initial_charge, initial_trash_amount)):
            break
        else:
            print("This is not a valid input.")

    problem = generateProblem(grid, initial_charge,
                              initial_trash_amount, "latest")

    file = open(f"problem_newest.pddl", "w")
    file.write(problem)
    file.close()

    print("Done.")


def random_problems(n):
    for i in range(n):
        width = random.randint(3, 3)
        height = random.randint(3, 3)
        initial_charge = random.randint(50, 100)
        initial_trash_amount = random.randint(0, 50)
        initial_charge = 100
        initial_trash_amount = 0

        options = ["C", "T", "C", "T", "C", "T", "O", "O", "O", "_", "_", "_",
                   "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]

        rows = []
        for y in range(height):
            row = ""
            for x in range(width):
                row += random.choice(options)
            rows.append(row)

        row_to_change = rows[random.randint(0, height - 1)]
        # right now the top left is always the roomba
        rows[0] = "X" + row_to_change[1:]
        grid = ",".join(rows)

        grid = grid.split(",")

        file = open(f"problem_{i}.pddl", "w")
        problem = generateProblem(grid, initial_charge, initial_trash_amount,
                                  i)
        file.write(problem)
        file.close()

    print("Finished all random problems.")


if __name__ == "__main__":
    main()
    # random_problems(1)
