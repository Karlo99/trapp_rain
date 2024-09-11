board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

rows = {}
columns = {}

for i in range(len(board)):
    for j in range(len(board[i])):
        if i not in rows.keys():
            rows[i] = [board[i][j]]
        else:
            rows[i].append(board[i][j])
        if j not in columns.keys():
            columns[j] = [board[i][j]]
        else:
            columns[j].append(board[i][j])

def contains_duplicates(X):
    seen = set()
    seen_add = seen.add
    for x in X:
        if x == '.':
            continue
        elif x in seen or seen_add(x):
            return True
    return False

# flag = False
# for key in rows.keys():
#     if contains_duplicates(rows[key]):
#         flag = True
# if flag == True:
#     # return True
# else:
#     for column in columns.keys():
#         if contains_duplicates(columns[column]):
#             flag = True
# return flag

board = [[".",".",".",".","5",".",".","1","."],
 [".","4",".","3",".",".",".",".","."],
 [".",".",".",".",".","3",".",".","1"],
 ["8",".",".",".",".",".",".","2","."],
 [".",".","2",".","7",".",".",".","."],
 [".","1","5",".",".",".",".",".","."],
 [".",".",".",".",".","2",".",".","."],
 [".","2",".","9",".",".",".",".","."],
 [".",".","4",".",".",".",".",".","."]]

squares = {1:[], 2:[] , 3:[] , 4:[] , 5:[] , 6:[] , 7:[] , 8:[] , 9:[] }
start_key = 1
end_key = 1

for i in range(len(board)):
    end_key = start_key
    for j in range(len(board[i])):
        if (j + 1) % 3 == 0:
            squares[end_key].append(board[i][j])
            end_key += 1
        else:
            squares[end_key].append(board[i][j])
    if (i + 1) % 3 == 0:
        print(end_key)
        start_key = end_key

print(squares)