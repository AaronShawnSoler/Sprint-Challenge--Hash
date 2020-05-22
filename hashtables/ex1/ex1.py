def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    left_over = 0
    memory = {}
    for index, weight in enumerate(weights):
        left_over = limit - weight
        if left_over in memory.keys():
            return [index, memory[left_over]]
        memory[weight] = index
    print(None)
    return None


weights = [4, 6, 10, 15, 16]
length = 5
limit = 21

get_indices_of_item_weights(weights, length, limit)
