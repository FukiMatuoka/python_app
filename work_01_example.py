# 数当てゲーム
import random

# - コンピュータ(python)が1〜100の中からランダムに選んだ数を当てるゲームを作る。
# - 5回まで挑戦できて、当たったら「当たり！」と表示して終わり
# - 最後まで当たらなければ正解を教えてくれる（もう一回挑戦したくなるような感じで）

# 重要ポイント１ 標準出力・標準入力を使う
# 数字をランダムに選ぶ
number = random.randint(1, 100)
print(number)  # デバッグ用に正解を表示

player_number_str = input()  # str は文字列
print(f"あなたの入力: {player_number_str}")


player_number = int(player_number_str)  # int は整数に変える

# 重要ポイント２ 分岐を使う
# 正解かを判断する
if player_number == number:
    print("当たり！")
else:
    print("はずれ！")

# 重要ポイント３ 繰り返しを使う
# 5回まで挑戦できる
for i in range(5):  # range(5) は 0,1,2,3,4 の5回繰り返す
    print(i)
    player_number_str = input("1から100の数字を当ててください: ")
    player_number = int(player_number_str)

    if player_number == number:
        print("当たり！")
        # 当たったら、何回で当てたかをカウントして表示
        print(f"{i + 1}回で当てました！")
        break  # 正解したら繰り返しを終わる breakは繰り返しを途中で終わらせる命令
    else:
        print("はずれ！")
