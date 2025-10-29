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
    c.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_time REAL,
            started_at TEXT
        )
    """
    )
    conn.commit()
    conn.close()


# 前回の記録を取得
def get_last_record():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        f"SELECT record_time, started_at FROM {TABLE_NAME} ORDER BY id DESC LIMIT 1"
    )
    result = c.fetchone()
    conn.close()
    return result


# 結果を保存
def save_record(record_time):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    started_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute(
        f"INSERT INTO {TABLE_NAME} (record_time, started_at) VALUES (?, ?)",
        (record_time, started_at),
    )
    conn.commit()
    conn.close()


# ゲーム本体
def play_game():
    print("\n⏳ 準備してください...（5〜15秒後に合図が出ます）")

    wait_time = random.uniform(5, 15)
    time.sleep(wait_time)

    print("👉 今だ！Enterキーを押してください！")

    start_time = time.time()
    input()
    reaction_time = time.time() - start_time

    if reaction_time < 0.01:
        print("⚠️ 不正検出！早すぎます（連打は禁止です）")
        return None
    else:
        print(f"あなたの反応時間: {reaction_time:.3f} 秒")
        save_record(reaction_time)
        return
