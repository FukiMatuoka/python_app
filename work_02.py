# - プログラムが5〜15秒の間でランダムな時間待機した後合図を出す。
# - 合図が出てからエンターが押されるまでの時間を計る。
# - 連打などへの対策として、反応速度が0.01秒未満で押されていた場合は不正とする
import time
import random

while True:
    print("\n⏳ 準備してください...（5〜15秒後に合図が出ます）")

    # 5〜15秒の間でランダムに待機
    wait_time = random.uniform(5, 15)
    time.sleep(wait_time)

    # 合図を出す
    print("👉 今だ！Enterキーを押してください！")

    # 合図が出てからEnterが押されるまでの時間を計測
    start_time = time.time()
    input()  # Enter待ち
    reaction_time = time.time() - start_time

    # 不正判定
    if reaction_time < 0.01:
        print("⚠️ 不正検出！早すぎます（連打は禁止です）")
    else:
        print(f"あなたの反応時間: {reaction_time:.3f} 秒")

    # リプレイ確認
    again = input("\nもう一度挑戦しますか？ (Yes/No): ")
    if again.lower() != "yes":
        print("\n👋 おつかれさまでした！")
        break
