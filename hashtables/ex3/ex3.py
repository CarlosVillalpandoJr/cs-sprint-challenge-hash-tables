def intersection(arrays):
    dict = {}
    result = []

    for a in arrays:
        for b in a:
            if dict.get(b):
                dict[b] += 1
            else:
                dict[b] = 1
            
        for key, value in dict.items():
            if value > len(arrays) - 1:
                result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
