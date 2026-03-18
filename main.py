def average_value(values, round_to=2):
    return round(sum(values)/len(values), round_to)
print(average_value([1200, 980, 1430],))

def computer_score_delta(score, baseline, multiplier=1.0, round_to=2):
    return  round((score - baseline) * multiplier, round_to)
print(computer_score_delta(1540, 1200, round_to=1))
print(computer_score_delta(1540, 1200, 0.5, round_to=3))

def local_demo():
    value = "local"
    print("Uvnitr funkce:", value)

def normalize_signal(values, min_value=0, max_value=1):
    low = min(values)
    high = max(values)
    scale = high - low
    return [min_value + (v - low) * (max_value - min_value) / scale for v in values]


print(normalize_signal([2, 4, 6], max_value=100))
print(normalize_signal([2, 4, 6], 0, 100))

