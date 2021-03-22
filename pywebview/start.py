import os
import webview
from problem_maker import generateProblem
from problem_maker import random_problems


class Api():
    # e.g. T_C,_O_,X__
    def generatePDDL(self, grid, initial_charge, initial_trash_amount, problem_name):
        print(f"Got the following input: {grid} called {problem_name} ")

        file = open(f"problem_{problem_name}.pddl", "w")

        grid = grid.split(",")
        problem = generateProblem(
            grid, initial_charge, initial_trash_amount, problem_name)

        file.write(problem)
        file.close()

    def generateRandomPDDL(self, n):
        random_problems(int(n))

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


if __name__ == '__main__':
    api = Api()
    webview.create_window('Roomba Problem PDDL Maker',
                          'assets/index.html', js_api=api, min_size=(720, 480))
    webview.start()
