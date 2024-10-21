# 백준 9465
'''
문제 접근
이 문제는 다이나믹 프로그래밍으로 이 2n 배열이 가지는 의미와 규칙을 파악해야 한다.

DP 배열
다이나믹프로그래밍의 핵심은 dp 배열일 가지는 의미와 계산하는 방법이다.

1. 문제에서 배열은 최대 2행 그리고 최대 n열로 이루어져 있다.
2. 공유하지 않는 변을 제외하여 스티커의 최댓값을 구해야 한다.
3. n번째 (즉, [0][n], [1][n])를 선택했을 때의 최댓값을 구해야 한다.
4. 왜냐면 최댓값을 구해야 하는 문제인데 n번째 값이 빠지면 안되기 때문이다. n-1번째 값을 쓴다고 할지라도 대각선 방향으로 n번째 값을 쓸 수 있다.
5. 우리가 원하는 답도 dp 배열의 마지막에 위치하게 된다.
6. 그런데 문제는 n열에서 2개의 선택지가 있다. 그래서 dp배열을 2개의 행으로 만들어서 풀어야 한다. 같은 방식을 두번 처리하면 된다.
7. dp[i][n] = n열에서 i행 스티커를 마지막으로 골랐을 때의 최댓값
8. 결과적으로 답은 dp[0][-1] 과 dp[1][-1]중의 최댓값이다.

구체적인 문제 풀이 방법
1. 대충 윤곽으로 dp[0][n] = max(cas1, case2, ...) + arr[0][n]의 형태를 가진다.
2. 첫번째 케이스는 arr[0][n]에서 대각선 방향인 arr[1][n-1]의 경우이다. 
3. 두번째 케이스는 n-1열을 안고르고 n-2열에서 n열로 바로 넘어오면서 최댓값을 만들 수 있다.
    arr[1][n-2] + arr[0][n]가 arr[0][n-2] + arr[1][n-1] + arr[0][n]보다 큰 경우, 오히려 n-1을 건너뛰는 것이 최댓값을 만들 수 있다.
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    # 2행 DP배열 형성
    dp = [[0] * N for _ in range(2)]
    
    # 스티커 길이가 1인 경우
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if N == 1:    
        print(max(dp[0][0], dp[1][0]))
        continue
    
    # 스티커 길이가 2인 경우
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3이상일 경우
    for i in range(2, N):
        # 메인 아이디어
        dp[0][i] = max(dp[1][i - 2], dp[1][i - 1]) + arr[0][i]
        dp[1][i] = max(dp[0][i - 2], dp[0][i - 1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][N -1]))