class Sorting:
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(n - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
        return self.array

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.array[min_index] > self.array[j]:
                    min_index = j
            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]
        return self.array

    def insertion_sort(self):
        n = len(self.array)
        for i in range(1, n):
            key = self.array[i]
            j = i - 1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
        return self.array

    def merge_sort(self, array):
        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    def quick_sort(self, array):
        if len(array) <= 1:
            return array

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
    s = Sorting(array)
    print(s.bubble_sort())
    print(s.selection_sort())
    print(s.insertion_sort())
    print(s.merge_sort(array))
    print(s.quick_sort(array))
