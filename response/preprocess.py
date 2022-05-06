import pandas as pd
import copy

#words is global set of valid words
def get_valid_words():
    terms = pd.read_csv("response/demo_terms.csv")
    all_terms = set("".join(t.split()).lower() for t in terms["word"])
    return all_terms

words = get_valid_words()

def find_starts_with(s):
    l1 = [w for w in words if w.startswith(s)]
    l2 = [w for w in l1 if w==s]
    if len(l2)>0:
        return True, l2[0]
    else:
        return False, l1

def search(grid, s, i,j, di, dj):
    if not (0 <= i < len(grid)): return False
    if not (0 <= j < len(grid[0])): return False

    c = grid[i][j]
    s2 = s+c
    found, a = find_starts_with(s2)
    if found:
        return a
    if len(a) > 0:
        return search(grid, s2, i+di, j+dj, di, dj)
    else:
        return False

def search_east( grid, i, j):
    return search(grid, '', i, j, 0, +1)
def search_west( grid, i, j):
    return search(grid, '', i, j, 0, -1)
def search_south( grid, i, j):
    return search( grid, '', i, j, +1, 0)
def search_north( grid, i, j):
    return search( grid, '', i, j, -1, 0)
def search_south_east( grid, i, j):
    return search( grid, '', i, j, +1, +1)
def search_north_west( grid, i, j):
    return search( grid, '', i, j, -1, -1)
def search_south_west( grid, i, j):
    return search( grid, '', i, j, +1, -1)
def search_north_east( grid, i, j):
    return search( grid, '', i,j, -1, +1)

def p1(grid):
    X, Y = len(grid), len(grid[0])
    dirs = [('E', search_east), 
            ('W', search_west),
            ('S', search_south),
            ('N', search_north),
            ('SE', search_south_east), 
            ('NW', search_north_west),
            ('SW', search_south_west), 
            ('NE', search_north_east)]
    ans = []
    for i in range(0, X):
        for j in range(0,Y):
            for d, f in dirs:
                tmp = f(grid, i,j)
                if tmp:
                    ans += [(i,j, d, tmp)]
    return ans

def fill_letter(a, w, i,j,k, di, dj):
    if k >= len(w): return 
    a[i][j] =w[k]
    fill_letter(a, w, i+di, j+dj, k+1, di, dj)

def cleanup( words):
    l2 = ['.']*10
    l3 = []
    for i in range(10):
        l3 += [copy.deepcopy(l2)]
    
    grid = l3
    for i,j,d,w in words:
        if d=='E':
            fill_letter(grid, w, i,j, 0, 0, +1)
        elif d=='W':
            fill_letter(grid, w, i,j, 0, 0, -1)
        elif d=='S':
            fill_letter(grid, w, i,j, 0, +1, 0)
        elif d=='N':
            fill_letter(grid, w, i,j, 0, -1, 0)
        elif d=='SE':
            fill_letter(grid, w, i, j, 0, +1, +1)
        elif d=='NE':
            fill_letter(grid, w, i, j, 0, -1, +1)
        elif d=='SW':
            fill_letter(grid, w, i, j, 0, +1, -1)
        elif d=='NW':
            fill_letter(grid, w, i, j, 0, -1, -1)
            
    ans = [''.join(lst) for lst in grid]
    ans = '\n'.join(ans)
    return ans

def extract_words(path):
    """
    requires a path to the txt file of the grid
    returns a list of recognized words according to terms present in demo_terms.csv
    also prints the grid with recognized words, removing characters not present in the word
    """
    with open(path) as f:
        grid = f.readlines()
        grid = list(map(lambda x: x[:-1].lower(),grid[:-1]))+[grid[-1].lower()]
        words = p1(grid)
        cleaned_grid = cleanup(words)
        print('Clean processed grid: \n')
        print(cleaned_grid, "\n")
        return list(map(lambda x: x[-1], words))

# if __name__ == "__main__":
#     print("start preprocess")
#     # print(extract_words("./tests/preprocess_test.txt"))
#     # """argo, bondevent, climate"""
#     # print(extract_words("./tests/horizontal1.txt"))
#     # """climate, cosmicrays, ecotax"""
#     # print(extract_words("./tests/vertical1.txt"))
#     # """gulfstream, icecore"""
#     # print(extract_words("./tests/diagonal1.txt"))
#     # """gulfstream, icecore"""
#     # print(extract_words("./tests/diagonal2.txt"))
    # print(extract_words("./tests/test3.txt"))
