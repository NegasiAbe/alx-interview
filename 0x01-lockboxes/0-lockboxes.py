
#!/usr/bin/python3
'''This is a  module for working with lockboxes.
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices)     '''
    n = len(boxes)
    boxes_seen = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in boxes_seen:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            boxes_seen.add(boxIdx)
    return n == len(boxes_seen)
