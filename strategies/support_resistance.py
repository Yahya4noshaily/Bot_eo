def check_support_resistance(price):
    support = 1.19
    resistance = 1.31
    return abs(price - support) < 0.01 or abs(price - resistance) < 0.01