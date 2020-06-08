
def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}
    for i in range(length):
        get_dict = weight_dict.get(limit - weights[i])
        if get_dict is None:
            weight_dict[weights[i]] = i
        else:
            return (i, get_dict)
