

nums = [153456,123406,124456,323456,123458,123756]


def find_key(nums):
    passcode = list()
    matrix = list()
    for serie in nums:
       matrix.append([int(num) for num in str(serie)])

    counts = dict()
    for index in range(len(matrix)):
        if matrix[index][0] not in counts:
            counts[matrix[index][0]] = 1
        else:
            counts[matrix[index][0]] += 1
            passcode.append(min(counts, key=counts.get))
            break
    
    
    return passcode

#change column matrix[0][1]
#change row matrix[1][0]
#checking every row, same column
print(find_key(nums))
