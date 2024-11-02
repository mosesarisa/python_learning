def can_drink_alcohol(age, is_born_male):
    """Can someone drink alcohol of the given age and what genger """
    return is_born_male and (age >=18)
print(can_drink_alcohol(17, True))
print(can_drink_alcohol(18, True))
print(can_drink_alcohol(22, False))
