import os

folder = "/Users/olelokken/DEV/Machine-Learning/Age-Estimator/train"
set = os.listdir(folder)

for i in set:
    try:
        list = os.listdir(f"{folder}/{i}")
        num = len(list)
        for file in os.listdir(f"{folder}/{i}"):
            if(num <= 35):
                break
            path = f"{folder}/{i}/{file}"
            os.remove(path)
            num = num - 1
    except:
        print("penis")