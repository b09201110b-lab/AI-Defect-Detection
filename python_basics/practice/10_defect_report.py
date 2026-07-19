defect_scores = [0.92, 0.35, 0.81, 0.67, 0.91, 0.22]

length=len(defect_scores)
i=0

while i <= length-1:
    if defect_scores[i]>=0.8:
        print("Image ",i+1,"Defect")
    else:
        print("Image ",i+1,"Normal")
    i=i+1
