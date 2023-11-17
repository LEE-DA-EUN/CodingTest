n, w, L = map(int, input().split()) # n = 다리를 건너는 트럭의 수, w = 다리의 길이, L = 다리의 최대하중
ls = list(map(int, input().split())) # 트럭들의 무게 ls[0]부터 건넌다
bridge = [0] * w
time = 0
while bridge:
    time += 1
    bridge.pop(0)
    if ls:
        if sum(bridge) + ls[0] <= L:
            bridge.append(ls.pop(0))
        else:
            bridge.append(0)
print(time)

