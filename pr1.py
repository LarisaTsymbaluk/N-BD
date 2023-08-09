#Программа для нахождения минимальной стоимости, за которую кузнечик может добраться из точки 0 до n :)
Cost = list(map(int, input().split()))
n = len(Cost) - 1
def min_cost(Cost):
    n = len(Cost) - 1
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        dp[i] = Cost[i ]+min(dp[i - 1] , dp[i - 2] )

    return dp[n]

print(min_cost(Cost))
