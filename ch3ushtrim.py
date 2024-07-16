salary = [340, 210, 450, 600, 230, 500, 550, 300]
shuma = 0
for paga in salary:
    shuma = shuma + paga
print(f"Shuma e pagave eshte: {shuma}")

pagamesatare = shuma / len(salary)
print(pagamesatare)

pagaMin = salary[0]
for pagaaktuale in salary:
    if (pagaaktuale < pagaMin):
        pagaMin = pagaaktuale
print(f"Paga minimale eshte {pagaMin}")



pagamax = salary[0]
for x in salary:
    if (x > pagamax):
        pagamax = x
        print(f"Paga maximale eshte {pagamax}")