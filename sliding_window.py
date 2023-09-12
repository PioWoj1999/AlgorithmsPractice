"""Sliding window algorithm presentation in Python."""

def sliding_window(table: list | str, size: int) -> None:
    """Function to implement basic sliding window algorithm. Check if a string is a permutation of other."""
    if len(table) <= size: 
        print(table)
    else: 
        for i in range(0, len(table)-size+1):
            print(table[i:i+size])
    return None

def sliding_window_generator(table: list, size: int) -> list:
    """Sliding window algorithm with generators."""
    if len(table) <= size: 
        return table
    else: 
        for i in range(0, len(table)-size+1):
            yield table[i:i+size]

def main():
    data = [x for x in range(1, 9)]

    print(f"data: {data}")
    sliding_window(table=data, size=3)

    print("\nSliding window with generators:")
    sw_gen = sliding_window_generator(table=data, size=3)
    print(next(sw_gen))
    print(next(sw_gen))

    print("\nTest for string, to check if one is permutation of others:")
    sliding_window(table="eidbaooo", size=2)



if __name__ == "__main__":
    main()