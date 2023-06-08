import re
import os
from unidecode import unidecode

## Utility

### Roman str to int
d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}


def romanToInt(s):
    res, p = 0, "I"
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c
    return res


### Regex prep

chapStart = re.compile(
    r"^(?P<part>M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})), (?P<book>\d+), (?P<chapter>\d+)*"
)
wordRegex = re.compile(r"(\w{5,15})")

## Global variables
words = []
wordCount = 100

in_filename = "raw_input.txt"
pathToFile = ""
fileName = ""
outfile = 0

with open(in_filename, encoding="utf-8") as inFile:
    for line in inFile.readlines():
        m = chapStart.match(line)
        if m:
            pathToFile = "input/"
            if not os.path.exists(pathToFile):
                os.makedirs(pathToFile)

            fileName = (
                "p"
                + str(romanToInt(m.group("part")))
                + "-b"
                + str(m.group("book"))
                + "-c"
                + str(m.group("chapter"))
                + ".txt"
            )

            outfile = open(pathToFile + fileName, "w")
            words = []
            continue
        if outfile and not outfile.closed:
            if len(words) <= wordCount:
                words += wordRegex.findall(unidecode(line).lower())
            else:
                outfile.write(" ".join(words[:wordCount]))
                outfile.close()
