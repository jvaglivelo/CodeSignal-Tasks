def solution(a):
    rowL = len(a)
    colL = len(a[0])
    mat = []
    
    for r in range(rowL):
        nRow = []
        for c in range(colL):
            nRow.insert(0, a[c][r])
        mat.append(nRow)
        
    return mat