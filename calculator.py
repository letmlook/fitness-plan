"""
fitness-plan 减肥计划追踪器
身高 170cm | 体重 92kg | 目标：88kg
"""

import datetime
import json
from pathlib import Path

# === 个人数据 ===
USER_HEIGHT = 170  # cm
USER_WEIGHT = 92   # kg
TARGET_WEIGHT = 88 # kg
START_DATE = datetime.date(2026, 5, 13)
DAILY_DEFICIT = 500  # kcal

# 计算基础代谢 (Mifflin-St Jeor)
def bmr(weight, height, age=25, sex='male'):
    if sex == 'male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    return 10 * weight + 6.25 * height - 5 * age - 161

# 目标热量
daily_calorie = bmr(USER_WEIGHT, USER_HEIGHT) * 1.4 - DAILY_DEFICIT

print(f"=== 💪 fitness-plan 减肥计划 ===")
print(f"身高: {USER_HEIGHT}cm | 起始体重: {USER_WEIGHT}kg")
print(f"目标: {TARGET_WEIGHT}kg | 计划期: 30天")
print(f"BMI: {USER_WEIGHT / (USER_HEIGHT/100)**2:.1f}")
print(f"基础代谢(BMR): {bmr(USER_WEIGHT, USER_HEIGHT):.0f} kcal")
print(f"日目标摄入: ~{daily_calorie:.0f} kcal")
print(f"日热量赤字: {DAILY_DEFICIT} kcal")
print()
print("预计减重速度: ~0.5kg/周 (健康范围)")
print(f"达成目标预计需: {(USER_WEIGHT - TARGET_WEIGHT) / 0.5 * 7:.0f} 天")
print()
print("加油！坚持就是胜利 💪")
