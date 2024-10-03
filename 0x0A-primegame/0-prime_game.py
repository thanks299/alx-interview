#!/usr/bin/python3


def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    max_num = max(nums)
    
    # Sieve of Eratosthenes to find all prime numbers up to max_num
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_num**0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False
    
    # List to count the number of prime numbers up to each number n
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    # Count wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1  # Ben wins if the number of primes is even
        else:
            maria_wins += 1  # Maria wins if the number of primes is odd
    
    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Example usage:
x = 5
nums = [2, 5, 1, 4, 3]
print(f"Winner: {isWinner(x, nums)}")
