import random


def quiz_game():
    # ルール説明
    print("―――――――――――――――")
    print("名産品クイズを始めます！")
    print("名産品が表示されますので、それがどこの都道府県のものかを答えてください。")
    print("では、さっそく行きましょう！")
    print("―――――――――――――――\n")

    # 名産品データ（例として5件だけ）
    souvenirs = {
        "りんご": "青森県",  # 青森県の名産品として「りんご」など。 :contentReference[oaicite:0]{index=0}
        "さくらんぼ": "山形県",  # 山形県の名産品として。 :contentReference[oaicite:1]{index=1}
        "うなぎ": "静岡県",  # 静岡県のウナギ養殖など。 :contentReference[oaicite:2]{index=2}
        "松阪牛": "三重県",  # 三重県の松阪牛。 :contentReference[oaicite:3]{index=3}
        "納豆": "茨城県",  # 茨城県の納豆など。 :contentReference[oaicite:4]{index=4}
    }

    # ランダムで１問
    item, correct_pref = random.choice(list(souvenirs.items()))

    # クイズ表示
    print(f"【問題】「{item}」はどこの都道府県の名産品でしょう？")
    user_answer = input("あなたの答え（都道府県名を入力）: ")

    # 判定
    if user_answer.strip() == correct_pref:
        print("🎉 正解です！")
    else:
        print(f"❌ 不正解。正しい答えは「{correct_pref}」でした。")


if __name__ == "__main__":
    quiz_game()
