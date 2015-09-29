'''Fibbonacci sequence module'''

def fibo(N):
    '''Generate a Fibbonacci sequence
    
    Args:
        N (int): Length of sequence to calculate
    Returns:
        (list) [0, 1, 1, 2, 3, 5, 8, ...]
    '''
    fibo_nums = [0, 1]
    while len(fibo_nums) < N:
        fibo_nums.append(fibo_nums[-2] + fibo_nums[-1])
    return fibo_nums
