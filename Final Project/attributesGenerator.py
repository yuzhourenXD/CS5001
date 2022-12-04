import random
import csv

def generator(filename: str):
    age = ["minor", "adult", "senior"]
    area = ["urban", "suburban", "rural"]
    pet = ["yes", "no"]
    gender = ["male", "female"]
    with open(filename, 'w', newline = '') as f:
        writer = csv.writer(f, delimiter=",")
        header = ["index", "age", "area", "pet", "gender"]
        writer.writerow(header)
        for i in range(100):
            list = []
            list.append(i)
            idx1 = random.randint(0, 2)
            list.append(age[idx1])
            idx2 = random.randint(0, 2)
            list.append(area[idx2])
            idx3 = random.randint(0, 1)
            list.append(pet[idx3])
            idx4 = random.randint(0, 1)
            list.append(gender[idx4])
            writer.writerow(list)

def main():
    generator("viewer_attributes.csv")
    generator("ads_attributes.csv")

if __name__ == "__main__":
    main()


