defect_scores = [0.92, 0.35, 0.81, 0.67, 0.91, 0.22]

def calculate_average(x):
    total = 0

    for score in x:
        total += score

    return(total/len(x))

print(calculate_average(defect_scores))