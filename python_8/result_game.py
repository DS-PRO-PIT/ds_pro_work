
from math import log2
import numpy as np

def binary_search(hidden_number: int = 1) -> int:
    """Use binary search algorithm to reveal hidden number from 1 to 100

    Args:
        hidden_number (int, optional): Hidden number to reveal. Defaults to 1.

    Returns:
        int: Counted attempts for win
    """
    if not(1 <= hidden_number <= 100):
        raise ValueError('Expected value from 1 to 100')
    
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


def reveal_max_attempts(search_function,
                       number_of_repetitions: int = 1000) -> int:
    """Reveal max attempts count by calling several times with random hidden number

    Args:
        search_function (callable): Checking function
        number_of_repetitions (int, optional): Number of repetitions to check. Defaults to 1000.

    Returns:
        int: Max attempts count 
    """
    hidden_numbers = np.random.randint(1, 101, size=number_of_repetitions)
    
    attempts_count = []
    for hidden_number in hidden_numbers:
        attempts_count.append(search_function(hidden_number))
        
    max_attempt_count = max(*attempts_count)
    print(f'Search algorithm needs maximum {max_attempt_count} attempts count')

    return max_attempt_count


def score_attempts(search_function,
                   number_of_repetitions: int = 1000) -> int:
    """Reveal arithmetic mean of attempts by calling several times with random hidden number

    Args:
        search_function (callable): Checking function
        number_of_repetitions (int, optional): Number of repetitions to check. Defaults to 1000.

    Returns:
        int: Arithmetic mean of attempts
    """
    hidden_numbers = np.random.randint(1, 101, size=number_of_repetitions)
    
    attempts_count = []
    for hidden_number in hidden_numbers:
        attempts_count.append(search_function(hidden_number))

    score = int(np.mean(attempts_count))
    print(f'Search algorithm needs {score} attempts')
    
    return score


#reveal_max_attempts(binary_search)
#score_attempts(binary_search)
