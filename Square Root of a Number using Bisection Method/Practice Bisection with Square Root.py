def square_root(target, tolerance = 1e-7, max_iterations = 100): #tolerance is how close the square of mid and desired number to be square rooted is and max iterations is how many times the code should be repeated until it must be stopped even when a root is not found
    if target < 0:
        raise ValueError('Negative numbers do not have a square root.')
    
    if target == 0:
        root = 0 
        print(f'Square root of {target} is 0.')
    elif target == 1:
        root = 1
        print(f'Square root of {target} is 1.')
    
    else:
        low = 0
        high = max(1,target) #sets the range for bisection
        root = None

        for _ in range(max_iterations):
            mid_point = (low + high)/2 #finds mid point of range
            mid_point_squared = mid_point**2 #squared to check if it matches desired number to be square rooted.

            if abs(mid_point_squared - target) < tolerance: #checks if difference falls within tolerance difference.
                root = mid_point 
                break #root identified and can move out of for loop
            elif mid_point_squared > target: 
                high = mid_point #since too big, will want a smaller range for a smaller mid point so high becomes midpoint and low remains 0 in the first encounter of the too big value unless low has been changed from the previous iteration.
            else:
                low = mid_point #since too small, will want bigger range for a larger mid point so low becomes mid point and high becomes the number desired to be square rooted in first encounter of too small value unless high has been changed in the previous iteration.
                #lines 24-27 ensure that the following mid points calculated will have a closer value to the number desired to be square rooted when squared.
        if root is None:
            print(f'Failed to find approximate root after exceeding {max_iterations} iterations.')
        else:
            print(f'Approximate square root of {target} is {root}.')
    
    return root

N = 3655
square_root(N)


