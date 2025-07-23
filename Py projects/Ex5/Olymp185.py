n = int(input())
s = ""
min_ratio = 0
previous_word_amount = 0
ork_of_year = 0
min_ratio_existence = False
previous_word_amount_existense = False
winner_existence = False
for j in range(1, n + 1):

    s = str(input())
    m = len(s)
    syllable = "AUOEauoe"
    word_amount = 1
    syllable_amount = 0

    for i in range(0, m):
        if s[i] in syllable:
            syllable_amount += 1
        x = s.split()
        word_amount = len(x)

    ratio = syllable_amount / word_amount

    if min_ratio_existence is False:
        min_ratio = ratio
        min_ratio_existence = True

    if previous_word_amount_existense is False:
        previous_word_amount = word_amount
        previous_word_amount_existense = True

    if min_ratio == ratio:
        if word_amount > previous_word_amount:
            ork_of_year = j
            winner_existence = True
        elif word_amount == previous_word_amount:
            winner_existence = False

    if min_ratio > ratio:
        min_ratio = ratio
        ork_of_year = j
        winner_existence = True

    previous_word_amount = word_amount

if winner_existence is True:
    print(ork_of_year)
else:
    print("O-o-o-rks...")

# https://www.eolymp.com/uk/submissions/9924420 - 60%
