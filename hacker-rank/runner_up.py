n = int(input())

best_runner = -1000000
runner_up = -1000000
scores = input().strip().split(' ')
for i in range(n):
    score = int(scores[i])
    if score > best_runner:
        runner_up = best_runner
        best_runner = score
    elif score < best_runner and score > runner_up:
        runner_up = score
print(runner_up)