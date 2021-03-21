import os
import webview
from problem_maker import generateProblem


class Api():
    # e.g. T_C,_O_,X__
    def generatePDDL(self, grid, initial_charge, initial_trash_amount, problem_name):
        print(f"Got the following input: {grid} called {problem_name} ")

        file = open(f"problem_{problem_name}.pddl", "w")
        
        problem = generateProblem(
            grid, initial_charge, initial_trash_amount, problem_name)

        file.write(problem)
        file.close()

    def print(self, x):
        print("PRINT FROM JS:\n", str(x), "\nEND PRINT FROM JS")

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


if __name__ == '__main__':
    api = Api()
    webview.create_window('Roomba Problem PDDL Maker',
                          'assets/index.html', js_api=api, min_size=(720, 480))
    webview.start()
