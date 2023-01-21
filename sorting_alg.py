class sorting:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array) - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def selection_sort(self):
        for i in range(len(self.array)):
            min_index = i
            for j in range(i + 1, len(self.array)):
                if self.array[min_index] > self.array[j]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        return self.array

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return self.array

    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            self.merge_sort(left)
            self.merge_sort(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        return array

    def quick_sort(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array.pop()

        items_greater = []
        items_lower = []

        for item in array:
            if item > pivot:
                items_greater.append(item)
            else:
                items_lower.append(item)

        return self.quick_sort(items_lower) + [pivot] + self.quick_sort(items_greater)


if __name__ == "__main__":
    array = [1, 8, 3, 2, 9, 6, 4, 8, 15, 10]
    s = sorting(array)
    print(s.bubble_sort())
    print(s.selection_sort())
    print(s.insertion_sort())
    print(s.merge_sort(array))
    print(s.quick_sort(array))
