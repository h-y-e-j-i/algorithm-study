# https://www.acmicpc.net/problem/4485

# 각 테스트 케이스의 첫째 줄에는 동굴의 크기를 나타내는 정수 N이 주어진다. 
cave_size = int(input())

# N = 0인 입력이 주어지면 전체 입력이 종료된다.
while cave_size!=0:
    for _ in range(cave_size):
