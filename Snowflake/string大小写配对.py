input = "bdAAaBDbadCC"

prefix_sum = [[0 for i in range(len(input))] for j in range(26)]
for i in range(26):
    for j in range(len(input)):
        if 'a' <= input[j] <= 'z':
            if ord(input[j]) - ord('a') == i:
                prefix_sum[i][j] = prefix_sum[i][j - 1] + 1
            else:
                prefix_sum[i][j] = prefix_sum[i][j - 1]
        else:
            if ord(input[j]) - ord('A') == i:
                prefix_sum[i][j] = prefix_sum[i][j - 1] - 1
            else:
                prefix_sum[i][j] = prefix_sum[i][j - 1]

map = {}
start, end = 0, 0
ans = 0
for i in range(len(input)):
    string = ""
    for j in range(26):
        string += str(prefix_sum[j][i])
    if string in map:
        if ans < i - (map[string] + 1):
            ans = i - map[string]
            start, end = map[string] + 1, i
    else:
        map[string] = i
print (input[start:end+1])


