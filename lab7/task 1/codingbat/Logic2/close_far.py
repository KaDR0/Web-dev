def close_far(a, b, c):
    close_to_a = abs(a - b) <= 1
    close_to_a_or_b = abs(a - c) <= 1 or abs(b - c) <= 1
    far_from_others = abs(a - b) >= 2 and abs(a - c) >= 2
    far_from_others = far_from_others or (abs(b - c) >= 2 and abs(a - c) >= 2)
    return (close_to_a and far_from_others) or (close_to_a_or_b and far_from_others)

print(close_far(int(input()), int(input()), int(input())))