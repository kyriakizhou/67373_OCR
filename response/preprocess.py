from tkinter import Grid
import numpy as np
import pandas as pd

#width and height of a grid
(width, height) = (10,10)
#minimum length of a word
min_len = 3

def get_row_words(grid):
    all_row_words = []
    for row in range(len(grid)):
        s = "".join(grid[row])
        for length in range(min_len, width+1):
            for i in range(width-length+1):
                all_row_words.append(s[i:i+length])
    return all_row_words + [s[::-1] for s in all_row_words]

def get_diagonal_words(grid):
    res = []
    for i in range(width-min_len+1):
        right = "".join(grid.diagonal(i))
        left = "".join(grid.diagonal(-i))
        # print(right)
        for word in [right, left]:
            for l in range(min_len, len(word)+1):
                for i in range(len(word)-l+1):
                    res.append(word[i:i+l])
                    res.append(word[i:i+l][::-1])
    return res

def get_all_words(path_to_file):
    """
    returns all valid words in a txt grid
    """
    with open(path_to_file) as f:
        original_grid = (f.readlines())
        original_grid[-1] += '\n'
        grid = np.array([list(r[:-1]) for r in original_grid],dtype=object)
        return (get_row_words(grid)+
                get_row_words(grid.transpose())+
                get_diagonal_words(grid) +
                get_diagonal_words(np.fliplr(grid)))
        # return get_diagonal_words(grid)

def get_valid_words(words):
    terms = pd.read_csv("response/climate_change_terms.csv")
    # terms = pd.read_csv("climate_change_terms.csv")
    #we ignore spaces so need convert 
    # print(words)
    all_terms = set("".join(t.split()).lower() for t in terms["term"])
    # print(all_terms)
    return set(filter(lambda w: w in all_terms, [w.lower() for w in words]))

def extract_words(path):
    """
    requires: path to txt of text detected by ocr. 
    the text MUST be in a grid of dimensions width x height.

    returns a list of valid words detected in the txt file,
    where words are in the climate_change_terms.csv and
    words are read: in rows left and right, in columns top and bottom,
    in all diagonals.
    """
    all_words = get_all_words(path)
    return get_valid_words(all_words)

if __name__ == "__main__":
    print("start preprocess")
    # print(extract_words("./tests/preprocess_test.txt"))
    # """argo, bondevent, climate"""
    # print(extract_words("./tests/horizontal1.txt"))
    # """climate, cosmicrays, ecotax"""
    # print(extract_words("./tests/vertical1.txt"))
    # """gulfstream, icecore"""
    # print(extract_words("./tests/diagonal1.txt"))
    # """gulfstream, icecore"""
    # print(extract_words("./tests/diagonal2.txt"))
    print(extract_words("./tests/test3.txt"))