#n = 3
double = 0
double_ = 0
result = []

n = int(input('введите n '))
#while n < 21:
for j in range(1, n):
    for k in range(1, n):

            # ищем ключи:
        if n % (j + k) == 0 and j != k:

                # ищем дубли:
            for i in range(0, len(result), 2):
                if j > 1 and result[i] == k and result[i+1] == j:
                    double += 1 # нужно пропустить занесение в список
            if double == double_:  # дублей может быть несколько
                result.append(j)
                result.append(k)
            else:
                double_=double

                # ищем дубли_2:
            #     for i in range(0, len(result), 2):
            #         if j > 1 and result[i] == k and result[i + 1] == j:
            #             continue
            #         continue
            # result.append(j)
            # result.append(k)
print(f' {n} - {result}')
result = []
double = 0
double_ = 0
#    n += 1
