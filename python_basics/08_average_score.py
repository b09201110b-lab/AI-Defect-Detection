defect_scores = [0.92, 0.35, 0.81, 0.67, 0.91, 0.22]

total=0
l=len(defect_scores)
for score in defect_scores:
    total=total+score

print(total/l)





















#len(defect_scores) 可以取得 List 長度。