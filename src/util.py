import random

def random_point_on_perimeter(rect):
    # Calculate the lengths of the sides
    top_side_length = rect.width
    right_side_length = rect.height
    bottom_side_length = rect.width
    #left_side_length = rect.height
    
    # Total perimeter length
    perimeter = 2 * (rect.width + rect.height)
    
    # Randomly choose a point along the perimeter
    random_perimeter_point = random.uniform(0, perimeter)
    
    if random_perimeter_point < top_side_length:
        # Top side
        x = rect.left + random_perimeter_point
        y = rect.top
    elif random_perimeter_point < top_side_length + right_side_length:
        # Right side
        x = rect.right
        y = rect.top + (random_perimeter_point - top_side_length)
    elif random_perimeter_point < top_side_length + right_side_length + bottom_side_length:
        # Bottom side
        x = rect.right - (random_perimeter_point - top_side_length - right_side_length)
        y = rect.bottom
    else:
        # Left side
        x = rect.left
        y = rect.bottom - (random_perimeter_point - top_side_length - right_side_length - bottom_side_length)
    
    return (x, y)