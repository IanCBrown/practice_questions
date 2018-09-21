import sys 

def bijele(kings, queens, rooks, bishops, knights, pawns):
    kings = int(kings)
    queens = int(queens)
    rooks = int(rooks)
    bishops = int(bishops)
    knights = int(knights)
    pawns = int(pawns)
    pieces_needed = [0] * 6 

    if kings < 1:
        pieces_needed[0] = 1 - kings
    else:
        pieces_needed[0] = (kings - 1) * -1 
    if queens < 1:
        pieces_needed[1] = 1 - queens
    else: 
        pieces_needed[1] = (queens - 1) * -1
    if rooks < 2:
        pieces_needed[2] = 2 - rooks
    else:
        pieces_needed[2] = (rooks - 2) * -1
    if bishops < 2:
        pieces_needed[3] = 2 - bishops
    else:
        pieces_needed[3] = (bishops - 2) * -1
    if knights < 2: 
        pieces_needed[4] = 2 - knights
    else:
        pieces_needed[4] = (knights - 2) * -1
    if pawns < 8:
        pieces_needed[5] = 8 - pawns
    else: 
        pieces_needed[5] = (pawns - 8) * -1 
    
    ret_string = ' '.join(str(i) for i in pieces_needed)

    return ret_string




if __name__ == "__main__":
    pieces = sys.stdin.readline().split()
    kings = pieces[0]
    queens = pieces[1]
    rooks = pieces[2]
    bishops = pieces[3]
    knights = pieces[4]
    pawns = pieces[5]

    print(bijele(kings, queens, rooks, bishops, knights, pawns))
