'''
Final Exam
CMPT 306
@author: Aidan Crump
'''

def triangle(board): 
    total = [0 for m in range(len(board))]
    
    for m in range(len(board[len(board) - 1])):  
        total[m] = board[len(board) - 1][m]  
  
    for m in range(len(board) - 2, -1, -1):  
        for n in range(len(board[m + 1]) - 1):  
            total[m] = board[m][n] + min(total[m], total[n + 1])
    return total[0] 


if __name__ == "__main__":
    #board = [[2],[5,4],[1,4,7],[8,6,9,6]]
    #board = [[1]]
    board = [[1],[2,3],[7,5,9]]
    print(triangle(board))

