# У некоторого султана было два мудреца: Али-ибн-Вали и Вали-ибн-Али.
# Желая убедиться в их мудрости, султан призвал мудрецов к себе и сказал:
# «Я задумал два числа. Оба они целые, каждое больше единицы, но меньше ста.
# Я перемножил эти числа и результат сообщу Али и при этом Вали я скажу сумму этих чисел.
# Если вы и вправду так мудры, как о вас говорят, то сможете узнать исходные числа».

# Мудрецы задумались. Первым нарушил молчание Али.
# — Я не знаю этих чисел, — сказал он, опуская голову.
# — Я это знал, — подал голос Вали.
# — Тогда я знаю эти числа, — обрадовался Али.
# — Тогда и я знаю! — воскликнул Вали.
# И мудрецы сообщили пораженному царю задуманные им числа.

mult = lambda i, j: i * j
summ = lambda i, j: i + j

a_d = {}
b_d = {}
for i in range(2, 100):
    for j in range(2, 100):
        if j > i:
            continue
        pair = (i, j)
        sm = i + j
        ml = i * j
        a_d[ml] = a_d.get(ml, []) + [pair]
        b_d[sm] = b_d.get(sm, []) + [pair]

# 1
def remove_by_one(d):
    removed = []
    for x, pairs in d.items():
        if len(pairs) <= 1:
            removed.append(x)

    for r in removed:
        del d[r]

remove_by_one(a_d)
remove_by_one(b_d)


# 2
def all_in_another(source, dest, dest_func):
    removed = []
    for res, pairs in source.items():
        exist = True
        for i, j in pairs:
            check = dest_func(i, j)
            if check not in dest:
                exist = False
                break
        if not exist:
            removed.append(res)

    for r in removed:
        del source[r]

all_in_another(b_d, a_d, mult)

# 3
def in_another(source, dest, dest_func):
    for x, pairs in source.items():
        remove_pairs = []
        for i, j in pairs:
            check_sm = dest_func(i, j)
            if check_sm not in dest:
                remove_pairs.append((i, j))
        for r_pair in remove_pairs:
            pairs.remove(r_pair)

in_another(a_d, b_d, summ)

def remove_not_one(source):
    removed = []
    for x, pairs in source.items():
        if len(pairs) != 1:
            removed.append(x)
    for r in removed:
        del source[r]

remove_not_one(a_d)

# 4

in_another(b_d, a_d, mult)
remove_not_one(b_d)

all_in_another(a_d, b_d, summ)

print a_d
print b_d
