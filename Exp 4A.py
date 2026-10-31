students = ['Arun', 'Bala', 'Chitra', 'Divya']

enrolled = {
    'Arun': {'KE', 'DS'},
    'Bala': {'KE'},
    'Chitra': {'DS'},
    'Divya': {'KE', 'DS'}
}

attends = {'Arun', 'Bala', 'Divya'}

ds_marks = {
    'Arun': 92,
    'Chitra': 78,
    'Divya': 85
}

S1 = all(
    ('KE' not in enrolled[x]) or (x in attends)
    for x in students
)

S2 = any(
    ('DS' in enrolled[x] and ds_marks.get(x, 0) >= 90)
    for x in students
)

S3 = all(
    any(True for c in enrolled[x])
    for x in students
)

S4 = not any(
    ('KE' in enrolled[x] and x not in attends)
    for x in students
)

S5 = all(
    ds_marks.get(x, 0) >= 80
    for x in students if 'DS' in enrolled[x]
)

print("S1: forall x (Enrolled(x,KE) -> Attends(x)) :", S1)
print("S2: exists x (Enrolled(x,DS) and Marks(x,DS)>=90) :", S2)
print("S3: forall x exists c Enrolled(x,c) :", S3)
print("S4: not exists x (Enrolled(x,KE) and not Attends(x)) :", S4)
print("S5: forall x (Enrolled(x,DS) -> Marks(x,DS)>=80) :", S5)

print("Quantifier duality holds (S1 == S4):", S1 == S4)

