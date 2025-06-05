import csv
import random

SOURCE = "NLLB-ENIE.txt"
NEW_CONTENT = "NLLB-ENIE-samples.csv"

with open(SOURCE) as opus:
    content = opus.readlines()
    NUMBER_OF_LINES = len(content)

with open(NEW_CONTENT, 'w', newline='') as csvfile:
    samples = csv.writer(csvfile)
    samples.writerow(["Sample", "Source"])

    for _ in range(50):
        line = random.randint(2, NUMBER_OF_LINES - 2)
        samples.writerow([''.join(content[line-4:line+5]), str("OPUS NLLB, lines " + str(line-3) + " to " + str(line+5))])