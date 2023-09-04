import heapq

def main(): 
    li_1 = [5, 7, 9, 4, 3]
    li_2 = [5, 7, 9, 4, 3]

    # using heapif() to convert list into heap
    heapq.heapify(li_1)
    heapq.heapify(li_2)
    print(f"Created heap: {li_1}")
    print(type(li_1))

    # using heappush() to push elements into heap - pushes 8
    heapq.heappush(li_1, 8)
    print(f"New heap: {li_1}")

    # using heappop() to pop smallest element
    print(f"Deleting smallest element from heap in li_1: {heapq.heappop(li_1)}")
    print(f"New heap after deletion: {li_1}")

    # using heappushpop() to push and pop items simultaneously
    # pops 2
    print(f"The popped item: {heapq.heappushpop(li_1, 2)}")

    # using heapreplace() to push and pop items simultaneously
    # pops 3
    print(f"The popped item: {heapq.heapreplace(li_2, 2)}")

    #* nlargest() & nsmallest()
    li_3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
    heapq.heapify(li_3)

    print(f"\nHeap for nlargest() & nsmallest(): {li_3}")
    print(f"3 largest numbers: {heapq.nlargest(3, li_3)}")
    print(f"3 smallest numbers: {heapq.nsmallest(3, li_3)}")



if __name__ == "__main__":
    main()