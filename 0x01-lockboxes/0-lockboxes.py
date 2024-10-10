#!/usr/bin/python3
"""Lockboxes."""


def canUnlockAll(boxes):
    """Lockboxes."""
    n = len(boxes)  # Number of boxes
    opened = [False] * n  # Keep track of which boxes are opened
    opened[0] = True  # Box 0 is initially unlocked
    stack = [0]  # Stack to hold the boxes to process (DFS approach)

    # While there are boxes to process
    while stack:
        box_index = stack.pop()  # Get the current box
        for key in boxes[box_index]:  # Iterate over the keys in this box
            if key < n and not opened[key]:
                opened[key] = True  # Unlock the box
                stack.append(key)

    return all(opened)  # Check if all boxes are opened
