import os 
import re
from termcolor import colored


def generateAddress(pattern, pos):
    output = os.popen("vanitygen -r " + pattern).read()
    # print(output)
    start = re.search("Address: ", output, flags=0).span()[-1]
    print(output[start:start + pos], end='')
    print(colored(output[start + pos], "red"), end='')
    print(output[start + pos + 1:start + 33])


def generatePatterns(poem):
    refix = ".*$"
    length = len(poem)
    pattern = []
    for i in range(length):
        pattern.append( generatePrefix(i) + poem[i] + refix )
        # print(pattern[i])
    return pattern


def generatePrefix(pos):
    prefix="^1"
    for x in range(pos):
        prefix = prefix + "."
    return prefix


def base58Cnvert(poem):
    poem = poem.replace("l", "L")
    poem = poem.replace("O", "o")
    poem = poem.replace("I", "i")
    return poem
        
    
def main():
    poem = "ToBeOrNotToBeThatIsAQuestion"
    poem = base58Cnvert(poem)
    length = len(poem)
    if length > 32:
        poem = poem[0:32]
        length = 32
    pattern = generatePatterns(poem)
    for x in range(length): 
        # print(pattern[x])
        generateAddress(pattern[x], x+1)


if __name__ == "__main__":
    # execute only if run as a script
    main()


