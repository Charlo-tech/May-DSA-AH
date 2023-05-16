def min_steps_to_delete_series(series):
    if not series:
        return 0

    stack = [series[0]]
    steps = 0

    for char in series[1:]:
        if char == stack[-1]:
            stack.append(char)
        else:
            stack = [char]
            steps += 1

    return steps + 1

series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjkefjekihutrieruhi\
gtefhgbjkkkknbmssdsdsfdvneurghiueor"

result = min_steps_to_delete_series(series)
print(f"Minimum number of steps required to delete the series: {result}")