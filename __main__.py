# File to solve sudoku in command line
import numpy as np
from stochasticsudokusolver import GeneticAlgorithm, SimulatedAnnealing, SAGA, BacktrackAlgorithm
from stochasticsudokusolver import SudokuSolver

if __name__ == "__main__":
    print('Sudoku Solver')
    print('-------------')

    correct_input = False
    print('Write your own puzzle? (y/n)')
    while not correct_input:
        choice = input('Enter choice: ')
        if choice == 'y':
            correct_input = True
            puzzle = np.zeros((9, 9), dtype=np.int8)
            print('Enter the puzzle row by row, with 0s as empty cells')
            for i in range(9):
                row = input(f'Enter row {i+1}: ')
                if len(row) != 9:
                    print('Please enter a valid row. Exiting...')
                    exit()
                else:
                    puzzle[i] = [int(x) for x in row]

        elif choice == 'n':
            print('-------------')
            print("What difficulty of puzzle?")
            print('1. Easy')
            print('2. Medium')
            print('3. Hard')
            print('4. Evil')
            while not correct_input:
                choice = int(input('Enter choise: '))
                if choice == 1:
                    puzzle = np.array([
                        [5, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5, 0, 0, 0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 0, 0, 6, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8, 0],
                        [0, 0, 0, 4, 1, 9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]
                    ])
                    correct_input = True

                elif choice == 2:
                    puzzle = np.array([
                        [0, 6, 7, 0, 8, 2, 9, 5, 0],
                        [1, 0, 0, 6, 0, 5, 7, 0, 8],
                        [0, 0, 8, 7, 1, 0, 0, 6, 0],
                        [0, 5, 0, 0, 7, 0, 0, 9, 0],
                        [0, 7, 9, 0, 5, 0, 0, 0, 6],
                        [2, 0, 0, 8, 0, 6, 0, 7, 0],
                        [0, 0, 2, 0, 6, 0, 5, 8, 0],
                        [9, 0, 6, 5, 0, 8, 0, 3, 7],
                        [0, 0, 5, 0, 0, 7, 6, 1, 0]
                    ])
                    correct_input = True

                elif choice == 3:
                    puzzle = np.array([
                        [0, 0, 6, 1, 0, 0, 0, 0, 8],
                        [0, 8, 0, 0, 9, 0, 0, 3, 0],
                        [2, 0, 0, 0, 0, 5, 4, 0, 0],
                        [4, 0, 0, 0, 0, 1, 8, 0, 0],
                        [0, 3, 0, 0, 7, 0, 0, 4, 0],
                        [0, 0, 7, 9, 0, 0, 0, 0, 3],
                        [0, 0, 8, 4, 0, 0, 0, 0, 6],
                        [0, 2, 0, 0, 5, 0, 0, 8, 0],
                        [1, 0, 0, 0, 0, 2, 5, 0, 0]
                    ])
                    correct_input = True

                elif choice == 4:
                    puzzle = np.array([
                        [3, 0, 0, 1, 0, 0, 2, 6, 0],
                        [1, 9, 0, 0, 0, 8, 0, 0, 3],
                        [0, 0, 5, 6, 0, 3, 1, 0, 0],
                        [0, 3, 0, 0, 9, 0, 0, 2, 5],
                        [5, 1, 0, 2, 0, 0, 0, 3, 0],
                        [9, 6, 2, 0, 0, 0, 0, 0, 1],
                        [0, 0, 1, 9, 6, 0, 3, 0, 0],
                        [8, 0, 3, 0, 1, 0, 0, 0, 6],
                        [0, 2, 0, 0, 0, 5, 0, 0, 4]
                    ])
                    correct_input = True

                else:
                    print('Please enter a valid choice. What difficulty of puzzle?')
        else:
            print('Please enter a valid choice. Write your own puzzle? (y/n)')

    print('-------------')
    print('Puzzle is:')
    SudokuSolver.print_puzzle(puzzle)
    print('-------------')
    print('Choose algorithm:')
    print('1. Genetic Algorithm')
    print('2. Simulated Annealing')
    print('3. SAGA (Simulated Annealing Genetic Algorithm)')
    print('4. Backtracking Algorithm (brute force)')
    print('5. Exit')
    choice = int(input('Enter choice: '))
    if choice == 1:
        algorithm = GeneticAlgorithm()
    elif choice == 2:
        algorithm = SimulatedAnnealing()
    elif choice == 3:
        print('SAGA is not implemented yet. Exiting...')
        exit()
    elif choice == 4:
        algorithm = BacktrackAlgorithm()
    else:
        exit()
    print('Solving...')
    solver = SudokuSolver(algorithm)
    solution = solver.solve(puzzle)
