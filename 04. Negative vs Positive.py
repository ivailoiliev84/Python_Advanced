def filtered_negative(num, neg_num=0):
    for n in num:
        if n < 0:
            neg_num += n
    return neg_num


def filtered_positive(num, positive_num=0):
    for n in num:
        if n > 0:
            positive_num += n
    return positive_num


def comparison(positive, negative):
    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


nums = [int(n) for n in input().split()]
print(filtered_negative(nums))
print(filtered_positive(nums))
comparison(filtered_positive(nums), filtered_negative(nums))
