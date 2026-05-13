"""
每日打卡追踪
Usage: python3 tracker.py
"""

import datetime
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data.json"
START_WEIGHT = 92.0
TARGET_WEIGHT = 88.0

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE) as f:
            return json.load(f)
    return {"records": []}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2))

def log_today():
    data = load_data()
    today = str(datetime.date.today())

    weight = float(input("今日体重(kg): "))
    calories = int(input("今日摄入(kcal): "))
    exercise = input("运动(有氧/力量/HIIT/休息): ").strip()
    water = int(input("喝水量(ml): "))
    mood = input("今日心情(好/一般/差): ").strip()
    note = input("备注: ").strip()

    record = {
        "date": today,
        "weight": weight,
        "calories": calories,
        "exercise": exercise,
        "water_ml": water,
        "mood": mood,
        "note": note
    }
    data["records"].append(record)
    save_data(data)

    # 计算进度
    lost = START_WEIGHT - weight
    remaining = weight - TARGET_WEIGHT
    print(f"\n📊 今日打卡完成！")
    print(f"已减: {lost:.1f}kg | 剩余: {remaining:.1f}kg | 目标进度: {lost/4*100:.0f}%")

def show_stats():
    data = load_data()
    records = data.get("records", [])
    if not records:
        print("暂无记录，请先打卡: python3 tracker.py")
        return
    print(f"\n=== 📈 统计 (共 {len(records)} 条记录) ===")
    latest = records[-1]
    earliest = records[0]
    weight_change = earliest["weight"] - latest["weight"]
    print(f"起始体重: {earliest['weight']}kg")
    print(f"当前体重: {latest['weight']}kg")
    print(f"已减体重: {weight_change:.1f}kg")
    print(f"剩余目标: {latest['weight'] - TARGET_WEIGHT:.1f}kg")
    print(f"今日摄入: {latest.get('calories', 0)} kcal")
    print(f"今日运动: {latest.get('exercise', '-')}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--stats":
        show_stats()
    else:
        log_today()
