#------------------********************   Fungsi dan Prosedur   ********************------------------#
#######################  Kelompok Kerja Enkripsi, Dekripsi dan Formatting     #########################
def decrypt_StringToInteger(stringCheck,selectedPermutation):
    # I.S string yang dicek dan aturan yang digunakan valid
    # F.S Mengirimkan string yang sudah dikonvert ke integer dengan aturan 'selectedPermutation'
    value_int = 0
    for char in stringCheck:
        value_int = value_int*10 + selectedPermutation[uniqueChar.index(char)]
    return value_int

def encrypt_IntegerToString(integerCheck,selectedPermutation):
    # I.S string yang dicek dan aturan yang digunakan valid
    # F.S Mengirimkan integer yang sudah dikonvert ke string dengan aturan 'selectedPermutation'. String ini akan digunakan untuk validasi.
    # Jika aturan 'selectedPermutation' tidak bisa menerjemahkan balik maka akan mengirimkan string yang salah.
    value_str = ""
    integerCheck = str(integerCheck)
    counter = 0
    for char in integerCheck:
        try:
            value_str += (uniqueChar[selectedPermutation.index(int(char))])
            counter += 1
        except:
            if counter < len(solution):
                if solution[counter] in uniqueChar :
                    break
                else :
                    value_str += solution[counter]
                    counter += 1 
    return value_str

def formatInteger(integerResult):
    # I.S Integer yang diformat valid
    # F.S Mengirimkan integer yang sudah diformat menjadi string dan ditambahkan spasi antar elemennya
    str_integerResult = str(integerResult)
    value_str = ""
    first = True
    for char in str_integerResult:
        if (first):
            value_str += char
            first = False
        else :
            value_str = value_str + ' ' + char
    return value_str
#############################################################################################

#######################  Kelompok Kerja Permutasi dan Kombinasi     #########################
def bruteForcePermutation(accumulator,nowList):
    # Melakukan permutasi secara brute force yang dioptimisasi dengan rekursif
    # I.S accumulator mulanya adalah list kosong dan nowLIst adalah list yang akan dipermutasi
    # F.S accumulator berisikan salah satu permutasi dari "nowList", nowList menjadi kosong  dan "allPermutation" akan berisikan kumpulan dari accumulator 
    
    # Base Case => jika list yang akan dipermutasi kosong maka accumulator ditambahkan ke list permutasi
    if (nowList == []):
        allPermutation.append(accumulator)
    else :
        # Recursive Case => jika list yang akan dipermutasi belum kosong maka ambil salah satu elemennya
        # Lakukan rekursif hingga list yang akan dipermutasi kosong
        for integer in nowList:
            newAccumulator = accumulator.copy()
            newAccumulator.append(integer)
            newList = nowList.copy()
            newList.remove(integer)
            bruteForcePermutation(newAccumulator,newList)

def initPermutation(uniqueInteger):
    # Merupakan fungsi pemicu permutasi
    bruteForcePermutation([], uniqueInteger)

def bruteForceCombination(accumulator,nowList,nowIndex,numOfElement):
    # Melakukan kombinasi secara brute force yang dioptimisasi dengan rekursif
    # I.S Awalnya accumulator adalah list kosong, nowList berisi list yang akan dikombinasi, nowIndex adalah 0 , dan numOfElemen jumlah elemen yang akan di kombinasi
    # F.S Saat prosedur ini berakhir maka "allCombination" akan berisikan kombinasi dari "nowList" sebanyak "numOfElement" ( kombinasi didapat dari accumulator )
    
    # Base Case 1 => jika mengkombinasi 0 elemen maka tambahkan accumulator yang sekarang
    if (numOfElement==0):
        allCombination.append(accumulator)
    # Base Case 2 => jika jumlah angka yang mau dikombinasi == angka yang tersisa untuk dipilih maka angka sisanya langsung ditambahkan
    elif (nowIndex == len(nowList)-numOfElement):
        for i in range(nowIndex,len(nowList)):
            accumulator.append(nowList[i])
        allCombination.append(accumulator)
    # Recursion Case => Saat ada di index ke-0 anda dapat memilih untuk mengambil angka tersebut atau tidak dst. Sehingga ada 2 rekursif seperti pohon biner
    else:
        newAccumulator1 = accumulator.copy()
        newAccumulator2 = accumulator.copy()
        newAccumulator1.append(nowList[nowIndex])
        bruteForceCombination(newAccumulator1,nowList,nowIndex+1,numOfElement-1)
        bruteForceCombination(newAccumulator2,nowList,nowIndex+1,numOfElement)

def initCombination(uniqueInteger, numOfElement):
    # Merupakan fungsi pemicu kombinasi
    bruteForceCombination([],uniqueInteger,0,numOfElement)
################################################################################################
#------------------********************------------------********************------------------#

#------------------********************   Main Program   ********************------------------#
print('   ______                 __             _ __  __                   __  _         _____       __               ')
print('  / ____/______  ______  / /_____ ______(_) /_/ /_  ____ ___  ___  / /_(_)____   / ___/____  / /   _____  _____')
print(' / /   / ___/ / / / __ \/ __/ __ `/ ___/ / __/ __ \/ __ `__ \/ _ \/ __/ / ___/   \__ \/ __ \/ / | / / _ \/ ___/')
print('/ /___/ /  / /_/ / /_/ / /_/ /_/ / /  / / /_/ / / / / / / / /  __/ /_/ / /__    ___/ / /_/ / /| |/ /  __/ /    ')
print('\____/_/   \__, / .___/\__/\__,_/_/  /_/\__/_/ /_/_/ /_/ /_/\___/\__/_/\___/   /____/\____/_/ |___/\___/_/     ')
print('          /____/_/                                                                                             ')
print('===============================================================================================================')
print('Pastikan anda sudah Membaca Readme terlebih dahulu!')
print('Made by Reihan Andhika Putra 13519043 --- Enjoy')
print('===============================================================================================================')
# Important Notes
print("Waktu eksekusi dan jumlah pengecekan adalah untuk tiap solusi")

# Import library
import time

# Deklarasi Variabel-Variabel Penting
problems = []           # Kumpulan string operan
solution = []           # String hasil
uniqueChar = []         # Char unik dari solusi dan operan
allPermutation = []     # Semua permutasi sebanyak char unik dari 10 angka
allCombination = []     # Semua kombinasi sebanyak char unik dari 10 angka

#  Membaca input dari file txt dan menulisnya ke layar
import os
os.chdir("..") # Pindah ke directory atas

filename = input("Masukkan nama file (tanpa ekstensi): ")
inputs = open('test/'+ filename +'.txt','r').read().split('\n')
print("Soal")
for input in inputs:
    print(input)
print("")

# Mencatat waktu dimulai setelah membaca file 
startTime = time.perf_counter()

# Parsing input ( Membagi mana yang soal(operan) dan mana yang solusi (hasil penjumlahan) )
for input in inputs:
    if '-' in input:
        break
    else:
        if '+' in input:
            input = input.replace('+','')
        input = input.replace(' ', '')
        problems.append(input)
BanyakProblem = len(problems)
solution = inputs[len(inputs)-1].replace(' ', '')

# Parsing input (Menambahkan semua char unik ke dalam list "uniqueChar")
for problem in problems:
    for char in problem:
        if char not in uniqueChar:
            uniqueChar.append(char)
for char in solution:
    if char not in uniqueChar:
        uniqueChar.append(char)

# Mencari semua kemungkinan permutasi dengan mengkombinasikan huruf sebanyak uniqueChar dan mempermutasikannya satu-satu
initCombination([1,2,3,4,5,6,7,8,9,0],len(uniqueChar))
for combination in allCombination:
    initPermutation(combination)

# Algoritma Brute Force dengan Pengecekan Satu-Satu
print("Jawaban")
jumlahPengecekan = 0
solusiKe = 0
for permutation in allPermutation:
    jumlahPengecekan += 1
    integerResult = 0
    for problem in problems:
        integerResult += decrypt_StringToInteger(problem,permutation)
    # Pengecekan apakah dengan aturan yang sekarang integer hasil penjumlahan operan akan menjadi string solusi jika dikonvert
    stringResult = encrypt_IntegerToString(integerResult,permutation)
    if (stringResult == solution):
        solusiKe += 1
        print("Solusi ke-",solusiKe)
        print("Jumlah substitusi :", jumlahPengecekan, "substitusi")
        print("Waktu eksekusi : ", time.perf_counter() - startTime, " detik")
        formattedResult = formatInteger(integerResult)
        for i in range(BanyakProblem):
            formattedInteger = formatInteger(decrypt_StringToInteger(problems[i],permutation))
            if (i == BanyakProblem-1):
                print("+ "+" "*(len(formattedResult)-len(formattedInteger))+ formattedInteger)
            else :
                print("  "+" "*(len(formattedResult)-len(formattedInteger))+formattedInteger)
        print('  ' + '-'* len(formattedResult))
        print("  "+ formattedResult)
        print("")

if (solusiKe == 0):
    print("Tidak ada solusi yang memenuhi")
#------------------********************------------------********************------------------#
