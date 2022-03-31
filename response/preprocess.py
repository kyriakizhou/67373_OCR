from tkinter import Grid
import numpy as np
import pandas as pd

(width, height) = (10,10)
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
        for word in [right, left]:
            for l in range(min_len, len(word)):
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
        grid = np.array([list(r[:-1]) for r in original_grid],dtype=object)
        return (get_row_words(grid)+
                get_row_words(grid.transpose())+
                get_diagonal_words(grid))
        # return get_diagonal_words(grid)

def get_valid_words(words):
    # print(words)
    terms = pd.read_csv("climate_change_terms.csv")
    #we ignore spaces so need convert 
    all_terms = set("".join(t.split()).lower() for t in terms["term"])
    # print(all_terms)
    return list(filter(lambda w: w in all_terms, words))

def extract_words(path):
    """
    requires: path to txt of text detected by ocr. 
    Assume text is in a grid of dimensions width x height.

    returns a list of valid words detected in the txt file,
    where words are in the climate_change_terms.csv and
    words are read: in rows left and right, in columns top and bottom,
    in all diagonals.
    """
    all_words = get_all_words(path)
    return get_valid_words(all_words)

if __name__ == "__main__":
    print(extract_words("preprocess_test.txt"))