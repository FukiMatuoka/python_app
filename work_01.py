# - コンピュータ(python)が1〜100の中からランダムに選んだ数を当てるゲームを作る。
# - 5回まで挑戦できて、当たったら「当たり！」と表示して終わり
# - 最後まで当たらなければ正解を教えてくれる（もう一回挑戦したくなるような感じで）

import random

while True:
    # ランダムな答えを作成
    answer = random.randint(1, 100)
    print(answer)  # デバッグ用：答えを表示
    print("\n🎲 1〜100の数を当ててください！チャンスは5回です。")

    # 5回まで繰り返す
    for turn in range(1, 6):
        print(f"\n{turn}回目の予想:")
        guess = int(input("あなたの予想: "))

        # 当たり判定
        if guess == answer:
            print("🎉 正解！おめでとう！")
            break

        # 差を計算
        diff = abs(answer - guess)

        # 大きいか小さいか
        if guess > answer:
            print("答えはもっと小さいです。")
        else:
            print("答えはもっと大きいです。")

        # 離れ具合の判定
        if diff >= 30:
            print("離れすぎ！💦")
        elif diff >= 10:
            print("ちょっと遠いです。")
        else:
            print("かなり近い！🔥")

        # 残りチャンス
        print(f"残りチャンス: {5 - turn}回")

    else:
        # 5回とも外れたとき
        print("\n💀 ゲームオーバー！答えは", answer, "でした。")

    # リプレイ確認
    again = input("\nもう一度プレイしますか？ (Yes/No): ")

    if again.lower() != "yes":
        print("\n👋 遊んでくれてありがとう！またね！")
        break
