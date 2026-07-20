# Day 2 - Python 基礎（二）

日期：2026-07-19

---

# 今日學習內容

## 1. while 迴圈

當不知道要執行幾次時，可以使用 while。

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

## 2. len()

取得 List 長度。

```python
numbers = [1, 2, 3]

print(len(numbers))
```

輸出：

```
3
```

---

## 3. Average（平均值）

平均值：

```python
average = total / len(scores)
```

流程：

1. 建立 total
2. 使用 for 累加
3. 除以 len()

---

## 4. 找最大值

流程：

1. 先假設第一個是最大值
2. 逐一比較
3. 遇到更大的就更新

---

## 5. def（函式）

建立函式：

```python
def calculate_average(scores):
    ...
```

格式：

```python
def 函式名稱(參數):
    程式內容
```

---

## 6. 呼叫函式

建立函式後，需要呼叫才會執行。

```python
calculate_average(defect_scores)
```

---

## 7. return

return 可以把函式計算完成的結果交回外面。

例如：

```python
def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    return total / len(scores)
```

使用：

```python
average = calculate_average(defect_scores)

print(average)
```

函式負責：

- 計算

外面負責：

- 使用
- 印出

---

# 今天記住的重點

1. Python 的 for 使用 `in`，不用自己寫 `i++`。
2. if、for、else 後面都要加 `:`
3. if、for、else 底下要縮排。
4. Python 註解使用 `#`，不是 `//`。
5. `count` 用來計數。
6. `total` 用來累加。
7. `len(list)` 可以取得 List 長度。
8. `=` 是指定值；`==` 是比較是否相等。
9. 不要使用 Python 內建函式名稱（如 `max`、`sum`、`len`、`list`）當變數名稱。
10. `def` 用來定義（建立）函式。
11. `return` 用來把函式計算完成的結果回傳給外面使用。

---

# 今日完成練習

- 11_calculate_average.py
- 12_return_average.py

---

# Git Commit

```bash
git add .
git commit -m "Day 2: Learn functions and return"
git push
```

---

# Day 2 完成

目前已學會：

- Variable
- List
- if / else
- for
- while
- count
- total
- len()
- Average
- Maximum
- def
- Parameter
- return

下一步：

Day 3：字串（String）與函式實戰。