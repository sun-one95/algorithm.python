'''
백준 2579

규칙
1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
3. 마지막 도착 계단은 반드시 밟아야 한다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.

1. 먼저, 각 계단에 도착하여 얻을 수 있는 점수의 최댓값을 저장할 리스트 dp를 선언한다. (dp = [0] * n)
2. 다이나믹프로그래밍 식을 정의하기 전에 기본값을 정의 해야한다. (0에서 2까지 계단 최댓값 정의)
 - dp[0] = arr[0] (첫 계단은 당연히 그 계단에 적힌 점수만이 최댓값이다.)
 - dp[1] = arr[0] + arr[1] (둘째 계단은 첫번째와 둘째 계단의 점수를 합한 값이 최댓값이다.)
 - dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) (세번째 계단은 세번연달아서 규칙2에 의해 세번 연달아서 갈 수 없다. 그러므로
    첫번째 계단 + 세번째 계단의 합, 두번째 계단 + 세번째 계단의 합 중에서 가장 큰 값이 최댓값이 된다.)
3. 이제 그 이후부터는 식을 만들어서 일반화할 수 있다.
 - 헷갈릴 수 있기 때문에 나는 이해하기 쉽게 실제 i가 3이라고 생각하고 식을 짜겠다.
 - dp[3] = max(dp[0] + arr[2] + arr[3], dp[1] + arr[3]) 3을 기준으로 연속으로 세번 연달아서 점수를 합할 수 없으니까
 3을 기준으로 0번째까지 계단의 최댓값 + 2번째 계단의 점수 + 3번째 계단의 점수, 1번째까지의 계단의 최댓값 + 3번째 계단의 점수 중에서 가장 큰 값이
 4번째 계단의 최댓값이 된다.
 - 즉 dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

문제를 해결하는데 어려웠던 점
이 문제를 예전에 푼 기억이 있었는데도 풀이 방식이 쉽게 떠오르지 않았다.
다이나믹프로그래밍 문제는 뭔가 규칙이 대부분 비슷하면서도 규칙을 찾는게 너무 어렵다.
규칙을 이해했지만 이것을 식으로 표현하는데 어려웠다.
기본값을 저장했다 쳐도 그 이후에 dp식을 작성하는데 어려움이 있었다.

n = 6
arr = [
    0 - 10
        1 - 20
            2 - 15
                3 - 25
                    4 - 10
                        5 - 20

]
dp = [
    0 - 10
    1 - 30
    2 - 35
    3 - dp[0] + arr[2] + arr[3], dp[1] + arr[3] = 50, 55 = 55
    4 - dp[1] + arr[3] + arr[4], dp[2] + arr[4] = 30 + 25 + 10, 35 + 10 = 65, 45 = 65
    5 = dp[2] + arr[4] + arr[5], dp[3] + arr[5] = 35 + 10 + 20, 55 + 20 = 65, 75 = 75
]


'''

import sys

input = sys.stdin.readline

n = int(input())
arr = [0 for i in range(301)]
for i in range(n):
    arr[i] = int(input())

dp = [0 for i in range(301)]
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) 
for i in range(3, n):
    dp[i] = max(dp[i - 3] + arr[i-1] + arr[i], dp[i - 2] + arr[i])

print(dp[n - 1])