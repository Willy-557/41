import random

data_nilai = { 
'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
'10': 10, 'J': 10, 'Q': 10, 'K': 10, 'As': 11 
} 

player = {
    'Tumpukan' : [],
    'KartuPlayer' : [],
    'TotalKartuPlayer' : [],
    'KartuMeja' : [],
}

def Menu():
    print("=" * 40)
    print("         GAME KARTU 41 (SIMPLE)")
    print("=" * 40)
    user = int(input("Jumlah pemain (2-4) >> "))
    MakeUser(user)
    MakeAndShuffleCards()
    PlayCards(user)

def MakeUser(InputUser):
    for _ in range(InputUser):
        player['KartuPlayer'].append([])
        player['TotalKartuPlayer'].append([])

def MakeAndShuffleCards():
    angka = list(data_nilai.keys())
    for i in angka:
        for _ in range(4):
            player['Tumpukan'].append(i)

    random.shuffle(player['Tumpukan'])

    player['KartuMeja'].append(player['Tumpukan'][0])
    player['Tumpukan'].pop(0)

    for i in range(len(player['KartuPlayer'])):
        for _ in range(4):
            player['KartuPlayer'][i].append(player['Tumpukan'][0])
            player['Tumpukan'].pop(0)

    for kartu in range(len(player['KartuPlayer'])):
        for j in player['KartuPlayer'][kartu]:
            nilaiAsli = data_nilai[j]
            player['TotalKartuPlayer'][kartu].append(nilaiAsli)

    # print(player['KartuMeja'])
    # print(player['KartuPlayer'])
    # print(player['TotalKartuPlayer'])
    # print(player['Tumpukan'])

def PrintCards(User):
    idx = User - 1
    for i in range (len(player['KartuPlayer'][idx])):
        print(f"{i+1}. {player['KartuPlayer'][idx][i]}")

def PlayCards(User):
    TotalPlayer = User
    counterGiliran = 1

    while sum(player['TotalKartuPlayer'][counterGiliran-1]) != 41:
        print("=" * 27)
        print(f"*** GILIRAN PEMAIN KE-{counterGiliran} ***")
        print("=" * 27)

        print(f"[ KARTU DI MEJA ] {player['KartuMeja'][0]}")
        print("-" * 27)
        print(f"[ KARTU ANDA ] (Skor : {sum(player['TotalKartuPlayer'][counterGiliran-1])})")
        PrintCards(counterGiliran)
        print("-" * 27)
        

        print("Pilih aksi:")
        print("1. Ambil dari meja")
        print("2. Ambil dari Tumpukan (Acak)")
        opsi = int(input("Aksi >> "))
        if opsi == 1:
            TakeFromTable(counterGiliran)
        elif opsi == 2:
            TakeFromDecks(counterGiliran)
        else:
            print("Invalid input!")
            continue

        if sum(player['TotalKartuPlayer'][counterGiliran-1]) == 41:
            print("=" * 27)
            print(f"*** GILIRAN PEMAIN KE-{counterGiliran} ***")
            print("=" * 27)
            print(f"Pemain ke-{counterGiliran} MENANG dengan skor {sum(player['TotalKartuPlayer'][counterGiliran-1])}!")
            break

        ChangePlayer = input("Tekan [Enter] untuk ganti pemain...")
        counterGiliran += 1

        if counterGiliran > TotalPlayer:
            counterGiliran = 1
        
def TakeFromTable(Num):
    idx_player = Num - 1
    print(f"\nAnda mengambil '{player['KartuMeja'][0]}' dari meja\n ")
    player['KartuPlayer'][idx_player].append(player['KartuMeja'][0])
    value_kartu = player['KartuMeja'][0]
    player['TotalKartuPlayer'][idx_player].append(data_nilai[value_kartu])
    print("-" * 27)
    print("Sekarang kartu Anda ada 5")
    while True:
        print("Pilih nomor kartu untuk dibuang:")
        PrintCards(Num)
        buang = int(input("Buang Nomor >> "))
        idx_buang = buang - 1
        if 1 <= buang <= len(player['KartuPlayer'][idx_player]):
            print(f"Anda membuang '{player['KartuPlayer'][idx_player][idx_buang]}'\n")
            player['KartuMeja'].append(player['KartuPlayer'][idx_player][idx_buang])
            player['KartuPlayer'][idx_player].pop(idx_buang)
            player['TotalKartuPlayer'][idx_player].pop(idx_buang)
            player['KartuMeja'].pop(0)
            print("-" * 27)
            break
        else:
            print("\nInvalid input!\n")
            continue

def TakeFromDecks(Num):
    idx_player = Num - 1
    print(f"\nAnda mengambil kartu acak : '{player['Tumpukan'][0]}'\n ")
    player['KartuPlayer'][idx_player].append(player['Tumpukan'][0])
    value_kartu = player['Tumpukan'][0]
    player['TotalKartuPlayer'][idx_player].append(data_nilai[value_kartu])
    player['Tumpukan'].pop(0)
    print("-" * 27)
    print("Sekarang kartu Anda ada 5")
    while True:
        print("Pilih nomor kartu untuk dibuang:")
        PrintCards(Num)
        buang = int(input("Buang Nomor >> "))
        idx_buang = buang - 1
        
        if 1 <= buang <= len(player['KartuPlayer'][idx_player]):
            print(f"Anda membuang '{player['KartuPlayer'][idx_player][idx_buang]}'\n")
            player['KartuMeja'].append(player['KartuPlayer'][idx_player][idx_buang])
            player['KartuPlayer'][idx_player].pop(idx_buang)
            player['TotalKartuPlayer'][idx_player].pop(idx_buang)
            player['KartuMeja'].pop(0)
            print("-" * 27)
            break
        else:
            print("\nInvalid input!\n")
            continue

if __name__=="__main__":
    Menu()