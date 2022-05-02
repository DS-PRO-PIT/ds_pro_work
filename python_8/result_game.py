
from math import log2

def binary_search(hidden_number: int = 1) -> int:
    """Use binary search algorithm to reveal hidden number from 1 to 100

    Args:
        hidden_number (int, optional): Hidden number to reveal. Defaults to 1.

    Returns:
        int: Counted attempts for win
    """
    
    interval = (1, 101) # mathematially half-open left-closed interval - [1, 101)
    max_attempts_to_panic = int(1 + log2(len(range(*interval))))
    
    for attempt_index in range(max_attempts_to_panic):
        
        predict_number = int(sum(interval) / 2)
        
        if predict_number == hidden_number:
            return attempt_index+1

        if predict_number < hidden_number:
            interval = (predict_number+1, interval[1])
        elif hidden_number < predict_number:
            interval = (interval[0], predict_number)

    raise RuntimeError('Algorithm working not like expected')

#print(binary_search(1))
