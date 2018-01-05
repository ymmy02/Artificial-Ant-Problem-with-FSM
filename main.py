from mealymachine import MealyMachine
from antsimulator import AntSimulator
from antrun import run_with_fsm

def createToyMealyMachine():
    states = [0,]
    init_state = states[0]
    input_symbols = [0, 1]  # 0: Not Found, 1: Found
    output_symbols = [0, 1, 2] # 0: Forward 1: Left 2: Right
    transition = {0: {0: 0, 1: 0}}
    action = {0: {0: 0, 1: 0}}
    mm = MealyMachine(states, init_state, input_symbols,  \
            output_symbols, transition, action)
    return mm

def createMealyMachine():
    states = [0, 1, 2, 3, 4]
    init_state = states[0]
    input_symbols = [0, 1]  # 0: Not Found, 1: Found
    output_symbols = [0, 1, 2] # 0: Forward 1: Left 2: Right
    transition = {0: {0: 2, 1: 3},
            1: {0: 0, 1: 1},
            2: {0: 4, 1: 4},
            3: {0: 1, 1: 1},
            4: {0: 3, 1: 1}
                }
    action = {0: {0: 2, 1: 0},
            1: {0: 2, 1: 0},
            2: {0: 2, 1: 2},
            3: {0: 0, 1: 0},
            4: {0: 2, 1: 0}
                }
    mm = MealyMachine(states, init_state, input_symbols,  \
            output_symbols, transition, action)
    return mm

def main():

    max_moves = 600
    ant = AntSimulator(max_moves)
    #mm = createMealyMachine()
    mm = createMealyMachine()
    with open("mapdata/santafe_trial.txt", 'r') as trial_file:
        ant.parse_matrix(trial_file)
    fitness = run_with_fsm(ant, mm)
    print(fitness)
    ant.print_route()
    ant.write_route("route.txt")

if __name__ == "__main__":
    main()
