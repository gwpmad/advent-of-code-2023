def main():
    import importlib
    import sys

    day = sys.argv[1]
    solution = importlib.import_module(f"day_{day}.main").solution()
    print(f"Solution for day {day}:\n1: {solution[0]}\n2: {solution[1]}")


if __name__ == "__main__":
    main()
