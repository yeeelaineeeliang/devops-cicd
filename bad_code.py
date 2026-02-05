def duplicate_code_1():

    data = []
    for i in range(10):
        data.append(i * 2)
    total = 0
    for item in data:
        total += item
    return total
