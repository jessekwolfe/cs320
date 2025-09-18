# Solution to find all possible solutions of nqueens
def nQueensAll(queen_count):
    if queen_count < 4:
        raise ValueError("Input must be 4 or greater.")

    def check_next_row(solution_so_far, total_queens):
        current_index = len(solution_so_far)

        if current_index == total_queens:
            valid_solutions.append(translate_to_coordinates(solution_so_far))

        for i in range(0, total_queens, 1):
            unique_in_solution = i not in solution_so_far

            if unique_in_solution and not_on_diagonal(solution_so_far, i):
                check_next_row(solution_so_far + [i], total_queens)

    valid_solutions = []

    for i in range(0, queen_count, 1):
        check_next_row([i], queen_count)

    return valid_solutions


# Helper function for all nQueensAll solution
def translate_to_coordinates(solution):
    coordinate_solution = []

    for index, number in enumerate(solution):
        coordinate_solution.append((index, number))

    return coordinate_solution


# Helper function for all nQueensAll solution
def not_on_diagonal(existing_solution, test_number):
    # Because we are building as we go we do not need to check down only up.
    test_index = len(existing_solution)

    for index, number in enumerate(existing_solution):
        diagonal_difference = test_index - index
        if (test_number + diagonal_difference == number) or (
            test_number - diagonal_difference == number
        ):
            return False

    # If no diagonals hit
    return True


# To find just one solution in O(n).
def nQueens(int):
    if int < 4:
        raise ValueError("Input must be 4 or greater.")

    valid_solutions = []
    y_cord = 1

    for i in range(0, int, 1):
        valid_solutions.append((i, y_cord))
        y_cord += 2
        if y_cord > int - 1:
            y_cord = 0

    return valid_solutions
