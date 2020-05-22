def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    numbers = {}
    for y in range(len(arrays)):
        for x in range(len(arrays[y])):
            if arrays[y][x] not in numbers.keys():
                numbers[arrays[y][x]] = 1
            else:
                numbers[arrays[y][x]] += 1

    for key in numbers.keys():
        if numbers[key] >= len(arrays):
            result.append(key)

    print(result)
    return result


array = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1]
]

intersection(array)


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
