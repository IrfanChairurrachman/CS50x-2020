from cs50 import get_int


def main():
    while True:
        height = get_int('Height: ')
        if height > 0 and height <= 8:
            break

    for i in range(1, height + 1):
        hashes = i
        spaces = height - hashes

        print(' ' * spaces, end='')
        print('#' * hashes, end='')

        print('  ', end='')

        print('#' * hashes)

main()