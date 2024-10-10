#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    n is the number of boxes
    """
    n = len(boxes)
    unlocked = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == n

