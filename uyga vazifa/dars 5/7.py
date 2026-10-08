def otgan_ballar(ballar):
    return [ball for ball in ballar if ball >= 60]


assert otgan_ballar([59, 60, 75, 40]) == [60, 75]
assert otgan_ballar([60]) == [60]
assert otgan_ballar([]) == []