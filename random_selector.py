import csv
import random

NUMBER_OF_LINES = 22172

with open("ga.txt") as opus:
    content = opus.readlines()

with open('samples.csv', 'w', newline='') as csvfile:
    samples = csv.writer(csvfile)
    samples.writerow(["Sample", "Source"])

    for _ in range(2):
        line = random.randint(2, NUMBER_OF_LINES - 2)
        samples.writerow([''.join(content[line-4:line+5]), line-4])