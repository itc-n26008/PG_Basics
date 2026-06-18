a = [5,29,27]

while True:
    answer = input("数字を入力してください('q'で終了)")
    if answer == "q":
        print("またやってね")
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字かqじゃないと無理だよ。がんば")
        continue
    if answer in a:
        print("正解です。　天才だね")
    else:
        print("不正解です。まだ君には早かったようだね。")
