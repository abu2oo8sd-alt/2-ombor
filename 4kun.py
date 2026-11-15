
import json

# 1. JSON faylni o'qish
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

# 2. Eng yuqori baholi talaba
best = max(students, key=lambda student: student["grade"])

# 3. Eng past baholi talaba
worst = min(students, key=lambda student: student["grade"])

# 4. O'rtacha bahoni hisoblash
average = sum(student["grade"] for student in students) / len(students)

# 5. Natijani chiqarish
print(f"Eng yaxshi talaba: {best['name']} — {best['grade']}")
print(f"Eng past baho: {worst['name']} — {worst['grade']}")
print(f"O'rtacha baho: {average:.1f}")

