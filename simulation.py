import argparse


def check_initial_population_input(init_pop):
    if init_pop < 0 or init_pop > 1:
        raise ValueError("Please enter a decimal value between 0 and 1")


def check_growth_rate_input(growth_rate):
    if growth_rate is str or growth_rate < 0 or growth_rate > 4:
        raise ValueError("Please enter a number between 0 and 4")


def check_iterations_input(iterations):
    if iterations < 0:
        raise ValueError("Please enter a whole number that is greater than 0")


def pop_equation(pop, rate):
    result = round(rate * pop * (1 - pop), 3)
    return result


def create_pop_list(init_pop, rate, iterations):
    pop = round(init_pop, 3)
    sim_results = []

    iteration = 0
    while iteration < iterations:
        if iteration < 1:
            sim_results.append(pop)
            iteration += 1
        else:
            pop = pop_equation(pop, rate)
            sim_results.append(pop)
            iteration += 1

    return sim_results


def population_simulation():
    parser = argparse.ArgumentParser(
        description="Get initial population, growth rate, iterations, and output file from command line")

    parser.add_argument('initial_population', type=float,
                        help="Enter an initial population as a decimal percentage (between 0 and 1)")

    parser.add_argument('growth_rate', type=float,
                        help="Enter the growth rate as a number between 0 and 4")

    parser.add_argument('iterations', type=int,
                        help="Enter number of iterations for the simulation as a whole number")

    parser.add_argument('output_file', type=str,
                        help="name of the output file for the data")

    args = parser.parse_args()

    check_initial_population_input(args.initial_population)
    check_growth_rate_input(args.growth_rate)
    check_iterations_input(args.iterations)

    results = create_pop_list(args.initial_population, args.growth_rate, args.iterations)

    for n in range(len(results)):
        print(f"{results[n]:.3f}")


def main():
    population_simulation()


main()
