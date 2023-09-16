from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def minimize_lunch_cost(lunch_prices, n):
    lunch_prices.insert(0, 0)
    dp = []
    for i in range(n + 1):
        dp.append([10**9] * (n + 1))
    dp[0][0] = 0
    for i in range(1, n + 1):
        if lunch_prices[i] <= 100:
            for j in range(n):
                dp[i][j] = min(dp[i - 1][j] + lunch_prices[i], dp[i - 1][j + 1])
        else:
            for j in range(n):
                dp[i][j] = min(dp[i - 1][j - 1] + lunch_prices[i], dp[i - 1][j + 1])
    total_price = min(dp[n])
    for i in range(n):
        if total_price == dp[n][i]:
            k1 = i
    j = k1
    i = n
    k2 = 0
    coupon_days = []
    while i != 0 or j != 0:
        if lunch_prices[i] <= 100:
            if dp[i - 1][j] + lunch_prices[i] <= dp[i - 1][j + 1]:
                i -= 1
            else:
                coupon_days.append(i)
                i -= 1
                j += 1
                k2 += 1
        elif dp[i - 1][j - 1] + lunch_prices[i] <= dp[i - 1][j + 1]:
            i -= 1
            j -= 1
        else:
            coupon_days.append(i)
            i -= 1
            j += 1
            k2 += 1
    return total_price, k1, k2, coupon_days


def main():
    # Чтение входных данных
    with open('input.txt', 'r') as input_file:
        n = int(input_file.readline())
        lunch_prices = [int(input_file.readline()) for _ in range(n)]

    # Вычисление результата
    result = minimize_lunch_cost(lunch_prices, n)

    # Запись результата
    with open('output.txt', 'w') as output_file:
        output_file.write(str(result[0]) + '\n')
        output_file.write(str(result[1]) + ' ' + str(result[2]) + '\n')
        for i in sorted(result[3]):
            output_file.write(str(i) + '\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
