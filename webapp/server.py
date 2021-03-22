from flask import Flask, render_template, request, jsonify
from problem_maker import generateProblem
from problem_maker import generate_random_problem
app = Flask(__name__)


def generatePDDL(grid, initial_charge, initial_trash_amount):
    grid = grid.split(",")
    problem = generateProblem(
        grid, initial_charge, initial_trash_amount, "custom")

    return problem


def generateRandomPDDL():
    problem = generate_random_problem()

    return problem


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/problem/new', methods=['POST'])
def problem_new():
    data = request.json
    print(f"Generating problem... \n {data}")
    problem = generatePDDL(data['grid'], data['charge'], data['trash'])

    return jsonify(problem)


@app.route('/problem/random/new', methods=['POST'])
def problem_random_new():
    print("Generating random problem...")
    problem = generateRandomPDDL()
    return jsonify(problem)


if __name__ == '__main__':
    app.run()
