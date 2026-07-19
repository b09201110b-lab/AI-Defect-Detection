defect_scores = [0.92, 0.35, 0.81, 0.67, 0.91, 0.22]

max=0

for score in defect_scores:
    if score>max:
        max=score

print(max)