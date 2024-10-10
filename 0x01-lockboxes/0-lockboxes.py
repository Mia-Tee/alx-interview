#!/usr/bin/python3
"""
Solution to the lockboxes problem
"""

def canUnlockAll(boxes):
    """
    Determines whether all boxes can be unlocked.
    The first box (box 0) is always unlocked, and from there,
    keys in each box can be used to unlock other boxes.

    Parameters:
    boxes (list of lists): A list where each index represents a box and contains a list of keys.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
    if not isinstance(boxes, list) or len(boxes) == 0:
        return False

    """
    Initialize a set to track the boxes that have been unlocked.
    Start with box 0, which is always unlocked.
    """
    unlocked = set([0])

    """
    Initialize a list to store the keys we need to explore.
    Start with the keys from box 0.
    """
    keys_to_check = [0]

    """
    Process each key while there are still keys to explore.
    """
    while keys_to_check:
        current_box = keys_to_check.pop()

        """
        Loop through all keys in the current_box.
        If the corresponding box is not already unlocked and is within bounds,
        unlock it and add it to the keys_to_check list for further exploration.
        """
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys_to_check.append(key)

    """
    If all boxes have been unlocked (the length of the unlocked set
    matches the number of boxes), return True. Otherwise, return False.
    """
    return len(unlocked) == len(boxes)

