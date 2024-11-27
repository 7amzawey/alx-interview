#!/usr/bin/python3
def greedy_coin_change(coins, total):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            print(f"coin: {coin}")
            total -= coin
            print(f"total: {total}")
            count += 1
    return count if total == 0 else -1

# Example usage
coins = [1, 2, 5, 10, 20, 50, 100]
total = 93
print(greedy_coin_change(coins, total))  # Output: 5 (50 + 20 + 20 + 2 + 1)
