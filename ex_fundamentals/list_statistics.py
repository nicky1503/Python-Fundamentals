num_of_nums = int(input())
positives = []
negatives = []
for _ in range(num_of_nums):
    num = float(input())
    if num < 0:
        negatives.append(num)
    else:
        positives.append(num)
print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}. Sum of negatives:{sum(negatives)}')
