import itertools

symbols = ['M', 'A', 'D', 'S']  # Motion, Armed, Door open, Siren

def kb(v):
    r1 = (not (v['M'] and v['A'])) or v['S']  # (M AND A) -> S
    r2 = (not v['D']) or v['M']              # D -> M

    return r1 and r2 and v['A'] and v['D']


def entails(query):
    print(f"{'M':<3}{'A':<3}{'D':<3}{'S':<3}{'KB':<4}{'Query':<6}")

    ok = True

    for vals in itertools.product([True, False], repeat=len(symbols)):
        v = dict(zip(symbols, vals))

        k, q = kb(v), query(v)

        print(f"{int(v['M']):<3}{int(v['A']):<3}{int(v['D']):<3}{int(v['S']):<3}{int(k):<4}{int(q):<6}")

        if k and not q:
            ok = False

    return ok


print("Query: S (siren rings)")
print("KB entails S ?", entails(lambda v: v['S']))

print("\nQuery: not S")
print("KB entails not S ?", entails(lambda v: not v['S']))

