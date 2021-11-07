import sys
import container


def read(file):
    for line in file:
        yield from line.split()


if __name__ == '__main__':
    arguments = sys.argv

    if len(arguments) != 4:
        print("Only 4 arguments can be entered!")
        exit()

    container = container.Container()
    try:
        if arguments[1] == 'random':
            size = int(arguments[2])
            container.random_input(size)
        elif arguments[1] == 'file':
            with open(arguments[2], 'r') as file_input:
                data = read(file_input)
                container.file_input(data)
        else:
            raise ValueError("This command is not available!")
    except ValueError as exception:
        print(exception)
        exit()
    except OSError:
        print("This file does not exists!")
        exit()

    with open(arguments[3], 'w') as file_output:
        container.file_output(file_output)
        container.shaker_sort()
        file_output.write("\nAfter shaker sort...\n")
        container.file_output(file_output)

    print("\nProgram has terminated :)\n")
