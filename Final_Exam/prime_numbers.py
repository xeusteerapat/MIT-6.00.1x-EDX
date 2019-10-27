def primes_list(N):
    '''
    N: an integer
    '''
    answer = []

    def is_prime(N):
        if N <= 1:
            return False

        for factor in range(2, N):
            if N % factor == 0:
                return False

        return True

    for num in range(1, N+1):
        if is_prime(num):
            answer.append(num)
    return answer


print(primes_list(2))
