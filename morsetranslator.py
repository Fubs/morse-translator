import sys
from optparse import OptionParser


morsedict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----"

}

# Global vars
stripCheck = False # Becomes true if non-alphanumeric characters were stripped

# For finding letter associated with morse string
def getLetter(searchValue):
    for key, value in morsedict.items():
        if value == searchValue:
            return key

def stripNonAlphanumericChars(string):
    newstring = ""
    stripCheck = False
    for c in range(len(string)):
        if string[c].isalnum() or string[c] == " " or string[c] == "\n":
            newstring += string[c]
        else:
            stripCheck = True
    return newstring


def txt2morse(inputstr, wordsep):

    inputstr = stripNonAlphanumericChars(inputstr)

    inputwords = inputstr.split() # list of words in inputstr

    morseoutwords = []
    morseoutchars = inputwords

    for w in range(len(inputwords)):
        morseoutchars[w] = list(inputwords[w])

    for w in range(len(morseoutchars)):
        for c in range(len(morseoutchars[w])):
            morseoutchars[w][c] = morsedict.get(str(morseoutchars[w][c]).lower())

    for w in range(len(morseoutchars)):
        morseoutwords.append(" ".join(morseoutchars[w]))

    morseout = wordsep.join(morseoutwords)

    return morseout

def main():
    argparser = OptionParser()
    argparser.add_option("-v", action="store_true", dest="verbose", default=False)
    (options, args) = argparser.parse_args()
    opts = (options,args)


    filepath = opts[1][0]
    inputfile = open(filepath, "r")
    inputstr = inputfile.read() # raw string of inputfile
    if options.verbose:
        print("[Input]")
        print(inputstr)
        print("")
        print("[Output]")
        print(txt2morse(inputstr, " / "))
    else:
        print(txt2morse(inputstr, " / "))


if __name__ == "__main__":
    main()

