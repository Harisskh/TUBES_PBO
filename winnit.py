import os
os.system('cls')

arr = [['1','2','3'],
       ['4','5','6'],
       ['7','8','9']]

print("GAME TIC TAC TOE")
def papan():
    print(f" === === ===\n| {arr[0][0]} | {arr[0][1]} | {arr[0][2]} |\n === === ===\n| {arr[1][0]} | {arr[1][1]} | {arr[1][2]} |\n === === ===\n| {arr[2][0]} | {arr[2][1]} | {arr[2][2]} |\n === === ===")

def cek(arr)->bool:
    #horizontal
    panjang_arr = len(arr)
    cekX = 'X'
    cekO = 'O'
    temp = True
    #horizontal
    #x
    for i in range(panjang_arr):
        for j in range(panjang_arr):
            if arr[i][j] == cekX:
                if j == panjang_arr-1:
                    temp = False
                    print("Player 1 Menang")
            else :
                break
    #o
    for i in range(panjang_arr):
        for j in range(panjang_arr):
            if arr[i][j] == cekO:
                if j == panjang_arr-1:
                    temp = False
                    print("Player 2 Menang")
            else :
                break
    #vertikal
    #X
    for i in range(0,panjang_arr):
        for j in range(0,panjang_arr):
            if arr[j][i] == cekX :
                # cek == arr[j][i]
                if j == panjang_arr-1:
                    temp = False
                    print("Player 1 Menang")
            else :
                break
    #O
    for i in range(0,panjang_arr):
        for j in range(0,panjang_arr):
            if arr[j][i] == cekO:
                # cek == arr[j][i]
                if j == panjang_arr-1:
                    temp = False
                    print("Player 2 Menang")
            else :
                break

    #diagonal
    #X        
    if arr[0][0] == 'X' and arr[1][1] == 'X' and arr[2][2] == 'X' or arr[0][2] == 'X' and arr[1][1] == 'X' and arr[2][0] == 'X':
        temp = False
        print("Player 1 Menang")
    #O
    if arr[0][0] == 'O' and arr[1][1] == 'O' and arr[2][2] == 'O' or arr[0][2] == 'O' and arr[1][1] == 'O' and arr[2][0] == 'O':
        temp = False
        print("Player 2 Menang")
    
    if temp :
        return True
    else :
        return False

def sort(mark):
    for i in range(1, len(mark)):
        mark[i-1] = mark[i]
    mark.pop() 
    return mark

# main
papan()
mark = []
panjang_mark = len(mark)
win = True
giliran = 0;
player = ""
panjang_arr = len(arr)
player = ""
pilihan = ""
while win:
    if giliran % 2 == 0 :
        player = "Player 1 (X)"
        pilihan = "X"
    else :
        player = "Player 2 (O)"
        pilihan = "O"
    inputpilihan = input(f"{player} silahkan pilih angka yang tersedia pada papan (1-9) : ")
    if inputpilihan == "X" or inputpilihan == "O" :
        print("silahkan masukkan ulang")
        inputpilihan = input(f"{player} silahkan pilih angka yang tersedia pada papan (1-9) : ")
    for i in range(0,panjang_arr):
        for j in range(0,panjang_arr):
            if arr[i][j] == inputpilihan and player == "Player 1 (X)":
                mark.append([i,j])
                arr[i][j] = pilihan
            elif arr[i][j] == inputpilihan and player == "Player 2 (O)":
                mark.append([i,j])
                arr[i][j] = pilihan    
                

    # if len(mark) == 6 :
    #     if mark[0][0] == 0 and mark[0][1] == 0:
    #         arr[0][0] = '1'
    #     elif mark[0][0] == 0 and mark[0][1] == 1:
    #         arr[0][1] = '2'
    #     elif mark[0][0] == 0 and mark[0][1] == 2:
    #         arr[0][2] = '3'
    #     elif mark[0][0] == 1 and mark[0][1] == 0:
    #         arr[1][0] = '4'
    #     elif mark[0][0] == 1 and mark[0][1] == 1:
    #         arr[1][1] = '5'
    #     elif mark[0][0] == 1 and mark[0][1] == 2:
    #         arr[1][2] = '6'
    #     elif mark[0][0] == 2 and mark[0][1] == 0:
    #         arr[2][0] = '7'
    #     elif mark[0][0] == 2 and mark[0][1] == 1:
    #         arr[2][1] = '8'
    #     elif mark[0][0] == 2 and mark[0][1] == 2:
    #         arr[2][2] = '9'
    #     sort(mark)
    
    #logika agar langkah 1 kembali menjadi angka semula
    if len(mark) == 6 :
        if mark[0] == [0,0]:
            arr[0][0] = '1'
        elif mark[0] == [0,1]:
            arr[0][1] = '2'
        elif mark[0] == [0,2]:
            arr[0][2] = '3' 
        elif mark[0] == [1,0]:
            arr[1][0] = '4' 
        elif mark[0] == [1,1]:
            arr[1][1] = '5' 
        elif mark[0] == [1,2]:
            arr[1][2] = '6' 
        elif mark[0] == [2,0]:
            arr[2][0] = '7' 
        elif mark[0] == [2,1]:
            arr[2][1] = '8' 
        elif mark[0] == [2,2]:
            arr[2][2] = '9'
        sort(mark)

    print(f"{len(mark)}")
    papan()
    giliran += 1
    win = cek(arr)
    