# kwadraty = [x**2 for x in range (1, 101)]

# print([i/10] for i in range(1,11))

# print = {(x, x**2, x**3) for x in range(1, 101)}

zbior_napisow = {'abc', 'ala ma kota', 'slowacki wielkim poetą był', 'supermen'}
print({x:len(x) for x in zbior_napisow})

print([x for x in range(1,101) if x%3==0])
