
def max_fund(village):
    current_maximum = village[0]
    maximum_so_far = village[0]
    indexes = []
    for index in range(1, len(village)):
        if village[index] > current_maximum + village[index]:
            indexes = [index]
        current_maximum = max(village[index], current_maximum + village[index])
        if current_maximum > maximum_so_far:
            indexes.append(index)
            maximum_so_far = current_maximum
    if maximum_so_far <= 0:
        return 0, 0, 0
    return maximum_so_far, indexes[0] + 1, indexes[len(indexes)-1] + 1
