import random

data_nilai = { 
'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
'10': 10, 'J': 10, 'Q': 10, 'K': 10, 'As': 11 
} 

player = {
    'Tumpukan' : [],
    'KartuPlayer' : [],
    'TotalKartuPlayer' : [],
}

def Menu():
    print("=" * 40)
    print("         GAME KARTU 41 (SIMPLE)")
    print("=" * 40)
    user = int(input("Jumlah pemain (2-4) >> "))
    MakeUser(user)
    MakeAndShuffleCards()

def MakeUser(InputUser):
    for _ in range(InputUser):
        player['KartuPlayer'].append([])
        player['TotalKartuPlayer'].append([])

def MakeAndShuffleCards():
    angka = list(data_nilai.keys())
    for i in angka:
        for _ in range(4):
            player['Tumpukan'].append(i)

    print(player['KartuPlayer'])
    print(player['TotalKartuPlayer'])
    print(player['Tumpukan'])

def PlayCards():
    

if __name__=="__main__":
    Menu()