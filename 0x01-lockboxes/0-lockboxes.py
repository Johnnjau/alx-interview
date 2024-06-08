#!/usr/bin/python3
"""
    determin wether the boxes would open
"""


def canUnlockAll(boxes):
    """
    return true if all boxes are open
    """
    if boxes is None:
        return False

    total_length = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        current = stack.pop()

        if current not in visited:
            visited.add(current)

            for key in boxes[current]:
                if key < total_length and key not in visited:
                    stack.append(key)

    return len(visited) == total_length
