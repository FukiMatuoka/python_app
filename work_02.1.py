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


import sqlite3
import time
import random
from datetime import datetime

# データベース設定
DB_NAME = "reaction_records.db"
TABLE_NAME = "reaction_results"

# データベース初期化（なければ作成）
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            record_time REAL,
            started_at TEXT
        )
    """)
    conn.commit()
    conn.close()

# 前回の記録を取得（ユーザーごと）
def get_last_record(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"""
        SELECT record_time, started_at
        FROM {TABLE_NAME}
        WHERE name = ?
        ORDER BY id DESC
        LIMIT 1
    """, (name,))
    result = c.fetchone()
    conn.close()
    return result

# 自分のハイスコア（最速）を取得
def get_best_record(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"""
        SELECT MIN(record_time)
        FROM {TABLE_NAME}
        WHERE name = ?
    """, (name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result and result[0] is not None else None

# 全体の上位5件を取得
def get_top5_records():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(f"""
        SELECT name, record_time, started_at
        FROM {
