def recursion(points: int) -> None:
    if points < 1:
        print("Stop recursion")
        return None
    else:
        print(f"Before recursion: {points}")
        recursion(points - 1)
        print(f"After recursion: {points}")
        return None


def fib(n: int) -> int:
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n - 1) + fib(n - 2)


def main():
    recursion(points=3)
    print(f"Fib 7: {fib(7)}")


if __name__ == "__main__":
    main()
