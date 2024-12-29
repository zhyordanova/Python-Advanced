def print_stronger_sum_nums(iters):
    positive_sum = sum(filter(lambda x: x > 0, iters))
    negative_sum = sum(filter(lambda x: x < 0, iters))
    print(negative_sum, positive_sum, sep='\n')
    if positive_sum > abs(negative_sum):
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")



numbers = list(map(int, input().split()))
print_stronger_sum_nums(numbers)