n = int(input("数字は何だい: "))

def apple(x):
    return x * x

print(apple(n))
"""数字の2乗を表示する。"""

def show(text):
    print(text)

show("成功してるよ")
"""showに代入するのは、print(text)で、表示されるよって意味"""

def sample(a, b, c, d=0, e=0):
    print(a, b, c, d, e)

sample(1, 2, 3)
"""abcは、数を指定していないので、入れないとエラーになるけど,dとeは、数字を指定しているので代入しなくてもいい。"""

def half(x):
    return x // 2

def times4(x):
    return x * 4

n = 10

a = half(n)
b = times4(a)

print(b)
"""halfには、xを2で割って整数で出すという役割を設けた、time4にはxかける４をする役割。nは、１０と決めた。つまり、10*2をしてその結果を４倍したのが、bっていうこと"""

def a(x):
    try:
        return float(x)
    except:
        return "無理だよ"

print(a("1.23"))
"""tryは、エラーが出るかもしれないけど試すという意味。できなかったら、exceptの内容を実行する"""
