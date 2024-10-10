#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    n is the number of boxes
    """
    n = len(boxes)

    """
    Set of unlocked boxes starting with box 0 (unlocked by default)
    """
    unlocked = set([0])

    """
    List of keys to explore. Initially it contains 0 since box 0 is unlocked
    """
    keys = [0]

    """
    Loop while there are still keys to explore
    """
    while keys:
        """
        Take the next key (box) to explore
        """
        current_box = keys.pop()

        """
        For each key inside the current box, try to unlock new boxes
        """
        for key in boxes[current_box]:
            """
            If the box corresponding to this key has not been unlocked yet
            and it is within bounds (key < n), unlock it
            """
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    """
    Check if we unlocked all boxes by comparing the number of unlocked boxes
    to the total number of boxes (n)
    """
    return len(unlocked) == n

