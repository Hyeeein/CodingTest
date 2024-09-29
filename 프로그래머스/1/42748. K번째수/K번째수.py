def solution(array, commands):
    answer = []

    for com in range(len(commands)):
        i, j, k = commands[com][0], commands[com][1], commands[com][2]
        result = array[i-1:j]
        result.sort()
        answer.append(result[k-1])

    return answer