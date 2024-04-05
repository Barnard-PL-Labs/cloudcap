def value_exists_in_nested_structure(structure, value):
    """
    Check if a value exists in an arbitrarily nested dictionary that can have lists nested inside as well.

    Args:
    structure (dict or list): The nested dictionary or list to search in.
    value: The value to search for.

    Returns:
    bool: True if the value exists, False otherwise.
    """
    if isinstance(structure, dict):
        # Check if the value exists in the dictionary
        if value in structure.values():
            return True
        # Recursively search in each value of the dictionary
        for v in structure.values():
            if value_exists_in_nested_structure(v, value):
                return True
    elif isinstance(structure, list):
        # Recursively search in each element of the list
        for item in structure:
            if item == value:
                return True
            if value_exists_in_nested_structure(item, value):
                return True
    # If the value is not found in the current level, return False
    return False
