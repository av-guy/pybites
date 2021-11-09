def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    if start <= 0:
        return start
    print(start)
    countdown_recursive(start=start-1)
    if start == 1:
        print('time is up')


if __name__ == "__main__":
    countdown_recursive()
