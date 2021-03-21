import os
import webview


class Api():
    # e.g. T_C,_O_,X__
    def generatePDDL(self, grid):
        print(f"Got the following input: {grid}")

    def print(self, x):
        print("PRINT FROM JS:\n", str(x), "\nEND PRINT FROM JS")

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


if __name__ == '__main__':
    api = Api()
    webview.create_window('Roomba Problem PDDL Maker',
                          'assets/index.html', js_api=api, min_size=(600, 450))
    webview.start()
