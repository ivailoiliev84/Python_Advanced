def age_assignment(*args, **kwargs):
    sheet = {}
    for letter, age in kwargs.items():
        for name in args:
            if letter in name:
                sheet[name] = age
    return sheet


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
