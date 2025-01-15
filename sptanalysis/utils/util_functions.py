def dic_union_two(dic_1, dic_2):
    """Documentation for dic_union_two
    Find the unique union of two dictionaries, assumes the values are lists

    Parameters:
    -----------
    dic_1 : dict
        dictionary 1
    dic_2 : dict
        dictionary 2

    Returns:
    --------
    dic_union : dict
        dictionary of the unique union of the two dictionaries

    Notes:
    ------
    The values of the dictionaries must be lists for the list concatenation to work properly
    This function turns the values of the dictionaries into lists, if arrays are needed then the values must be converted back to arrays

    """
    # create a dictionary to store the union
    dic_union = {}
    # loop through the keys in the first dictionary
    for key, value in dic_1.items():
        # check if the key is in the second dictionary
        if key in dic_2:
            # if the key is in both dictionaries then add the values together
            dic_union[key] = list(value) + list(dic_2[key])
        else:
            # if the key is only in the first dictionary then add the value to the union
            dic_union[key] = value
    # loop through the keys in the second dictionary
    for key, value in dic_2.items():
        # check if the key is in the first dictionary
        if key in dic_1:
            # if the key is only in the second dictionary then add the value to the union
            dic_union[key] = list(value) + list(dic_1[key])
        else:
            # if the key is only in the second dictionary then add the value to the union
            dic_union[key] = list(value)
    # return the union
    return dic_union
