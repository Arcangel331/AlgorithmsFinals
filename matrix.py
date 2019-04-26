'''
Final Exam
CMPT 306
@author: Aidan Crump
'''

def matrix(board): 
    if len(board) == 0:
        return 0

    if len(board) == 1:
        return min(board[0][j] for j in range(len(board)))
    '''
    for m in range(0, len(board)):
        total += (min(board[m][n] for n in range(len(board[1]))))
    return total
    '''
    total = [0 for m in range(len(board))]
  
    for m in range(len(board) - 1):  
        for n in range(len(board[1]) - 1):  
            total[m] = board[m][n] + (min((min(board[m + 1][n - 1], board[m + 1][n + 1])), min(board[m + 1][n - 1], board[m + 1][n])))
    return total[-2] 


if __name__ == "__main__":
    board = [[1,2,3],[4,5,6],[7,0,2]]
    #board = [[1]]
    #board = [[1,2,3]]
    #board = [[1,2,3,0],[4,5,1,6],[7,0,2,0]]
    print(matrix(board))

