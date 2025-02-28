x = float(input().strip())

resultado = f"{x:.4E}"

m, e = resultado.split('E')
e = int(e)

if x > 0:
    print(f"+{m}E{e:+03}")
else:
    print(f"{m}E{e:+03}")
