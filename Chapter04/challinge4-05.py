def a(x):
    try:
        return float(x)
    except:
        return "無理だよ"

print(a("1.23"))
