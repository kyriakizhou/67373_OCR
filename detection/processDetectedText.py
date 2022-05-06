# for each word, records the character count
def buildCharCount(word):
    return {e: word.count(e) for e in set(word)}

# build a word dictionary based on terms in wordDictionary.txt
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

# Find best match for the detected input word from the wordMap
def processDetectedText(text_detected):
    # trim leading and trailing white spaces
    text_detected = text_detected.strip()
    text_detected = text_detected.split(" ")
    word = max(text_detected)
    word = word.lower()
    count = buildCharCount(word)
    matchedWord = findBestMatch(count, wordMap)
    return matchedWord

# Format the 10x10 char grid.
def processGrid(text_detected):
    text_detected = text_detected.split("\n")
    output = ""
    for row in text_detected:
        if len(row) >= 10:
            r = []
            for c in row:
                if not (c.isspace()): r.append(c)
            r = r[:10]
            for c in r:
                output += c
            output += '\n'

    testCountLines = output.split('\n')
    lineLens = [len(s) for s in testCountLines]
    file = open("detection/grid.txt","w")
    file.write(output[:-1])
    file.close()