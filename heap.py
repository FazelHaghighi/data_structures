class Heap:
    @staticmethod
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Heap.heapify(arr, n, largest)

    @staticmethod
    def insert(array, newNum):
        array.append(newNum)
        size = len(array)
        for i in range((size // 2) - 1, -1, -1):
            Heap.heapify(array, size, i)

    @staticmethod
    def deleteNode(array, num):
        size = len(array)
        i = 0
        for i in range(0, size):
            if num == array[i]:
                break

        array[i], array[size - 1] = array[size - 1], array[i]

        array.remove(num)

        for i in range((len(array) // 2) - 1, -1, -1):
            Heap.heapify(array, len(array), i)


if __name__ == "__main__":
    arr = []

    Heap.insert(arr, 3)
    Heap.insert(arr, 4)
    Heap.insert(arr, 9)
    Heap.insert(arr, 5)
    Heap.insert(arr, 2)

    print(str(arr))

    Heap.deleteNode(arr, 4)
    print(str(arr))
