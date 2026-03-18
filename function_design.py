



def analyze_password(password, min_length=8, require_digit=True, require_upper=True, require_symbol=False, banned_words=["heslo","password","1234"]):
    is_strong = True
    count_active = 0
    count_not = 0
    nesplneno = []

    if min_length > 0:
        count_active = count_active + 1
    if len(password) < min_length:
        is_strong = False
        count_not += 1
        nesplneno.append(min_length)
    if require_digit:
        count_active += 1
    if require_upper:
        count_active += 1
    if require_symbol:
        count_not += 1
    if password == banned_words:
        count_not += 1
        nesplneno.append(password)
    return is_strong, count_active, count_not, nesplneno
print(analyze_password("1cdi45bAff", 10, False))



