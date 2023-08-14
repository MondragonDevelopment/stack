# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

temperatures = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = [] # Will consist of pairs (index, temp)
    for i, temp in enumerate(temperatures):  # Here we name the indexes i and the temperatures temp
        while stack and temp > stack[-1][-1]: # indexes -1 represent the last temperature on our stack
            stackI, stackTemp = stack.pop()
            answer[stackI] = i - stackI
        stack.append((i, temp))
    return answer


x = dailyTemperatures(temperatures)
print(x)