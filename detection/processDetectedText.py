import string

def buildCharCount(word):
    return {e: word.count(e) for e in set(word)}

def buildWordMap():
    f = open("detection/wordDictionary.txt", "r")
    words = f.read()
    words = words.split("\n")
    wordMap = []
    for word in words:
        count = buildCharCount(word)
        wordMap.append({word: count})
    f.close()
    return wordMap


wordMap = buildWordMap()
# print("wordMap", wordMap)

def score(count1, count2):
    score = 0
    for c in count1:
        if c in count2:
            score += min(count1[c], count2[c])
    return score

def findBestMatch(count, wordMap):
    bestMatch, highestScore = None, 0
    for wordCount in wordMap:
        for word in wordCount:
            s = score(count, wordCount[word])
            if s > highestScore:
                highestScore = s
                bestMatch = word
    return bestMatch

# for single word
def processDetectedText(text_detected):
    # trim leading and trailing white spaces
    text_detected = text_detected.strip()
    text_detected = text_detected.split(" ")
    word = max(text_detected)
    word = word.lower()
    count = buildCharCount(word)
    matchedWord = findBestMatch(count, wordMap)
    return matchedWord


def processGrid(text_detected):
    text_detected = text_detected.split("\n")
    # print("text_detected", text_detected)
    output = ""
    for row in text_detected:
        if len(row) >= 10:
            row = row[:10]
            for c in row:
                if not c.isspace():
                    output += c
            output += '\n'

    # print("OUTPUT", output)
    testCountLines = output.split('\n')
    lineLens = [len(s) for s in testCountLines]
    # print(f'height: {testCountLines}')
    # print(lineLens)
    file = open("detection/grid.txt","w")
    file.write(output[:-1])
    file.close()