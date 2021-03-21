import os
import webview


class Api():
    def setGridType(self, grid_type):
        print(f"Set grid type {grid_type}")

    def setGridSize(self, height, width):
        print(f"Set grid type {grid_type}")

    def print(self, x):
        print("PRINT FROM JS:\n", x, "\nEND PRINT FROM JS")

    def toggleFullscreen(self):
        webview.windows[0].toggle_fullscreen()


if __name__ == '__main__':
    api = Api()
    webview.create_window('Roomba Problem PDDL Maker',
                          'assets/index.html', js_api=api, min_size=(600, 450))
    webview.start()
