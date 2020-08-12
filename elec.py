used_elec =  int(input("이번 달 전기 사용량은?"))

if used_elec < 100:
    c = 330
    cost_elec = used_elec * 52
elif used_elec <= 200:
    c = 660
    cost_elec = used_elec * 88.5
elif used_elec <= 300:
    c = 1130
    cost_elec = used_elec * 127.8
elif used_elec <= 400:
    c = 2710
    cost_elec = used_elec * 184.3
elif used_elec <= 500:
    c = 5130
    cost_elec = used_elec * 274.3
else:
    c = 9330
    cost_elec = used_elec * 494.0
tax = (c + cost_elec) * 0.09
cost = c + cost_elec + tax 
print(cost)