import csv
import random

CORPUS = "NLLB-ENIE" # <- change this to the desired corpus name
NUMBER_OF_SAMPLES = 50 # <- adjust this number to change the number of samples

SOURCE = CORPUS + ".txt"
NEW_CONTENT = CORPUS + "-samples.csv"

with open(SOURCE) as opus:
    content = opus.readlines()
    NUMBER_OF_LINES = len(content)

with open(NEW_CONTENT, 'w', newline='') as csvfile:
    samples = csv.writer(csvfile)
    samples.writerow(["Sample", "Source"])
    for _ in range(NUMBER_OF_SAMPLES):
        line = random.randint(2, NUMBER_OF_LINES - 2)
        samples.writerow([''.join(content[line-4:line+5]), str("OPUS " + CORPUS + ", lines " + str(line-3) + " to " + str(line+5))])