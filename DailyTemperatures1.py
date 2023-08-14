# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days
# you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0 instead.
# First try, have an issue counting for the answer index

temperatures = [73,74,75,71,69,72,76,73]


def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)):
        counter = 0
        while stack and temperatures[i] > stack[-1]:
            counter += 1
            print(stack, counter, i)
            answer[i-counter] = (len(stack))
            stack.pop()
        stack.append(temperatures[i])

    return answer



x = dailyTemperatures(temperatures)
print(x)