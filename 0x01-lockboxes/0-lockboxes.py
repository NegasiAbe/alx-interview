def canUnlockAll(boxes):
    # Create a set to keep track of all the boxes we can currently open
    unlocked_boxes = set([0])
    
    # Iterate through all the keys in all the boxes we have unlocked so far
    while True:
        previous_unlocked_boxes = unlocked_boxes.copy() # Make a copy of the unlocked boxes to detect changes
        for box in unlocked_boxes:
            for key in boxes[box]:
                if key not in unlocked_boxes: # If we have a key that opens a new box
                    unlocked_boxes.add(key) # Unlock the box
                    
        if previous_unlocked_boxes == unlocked_boxes: # If we didn't unlock any new boxes in this iteration
            break # Stop iterating
        
    return len(unlocked_boxes) == len(boxes) # Return True if we unlocked all the boxes, else False
