students = {}
ocenki = [5,3,3,5,4]
summa_ocenok = sum([5,3,3,5,4])
kol_ocenok = len([5,3,3,5,4])
sredniy_ball = summa_ocenok/kol_ocenok
print('Aaron:' ,sredniy_ball)
ocenki1 = [2,2,2,3]
summa_ocenok1 = sum([2,2,2,3])
kol_ocenok1 = len([2,2,2,3])
sredniy_ball1 = summa_ocenok1/kol_ocenok1
print('Bilbo:' ,sredniy_ball1)
ocenki2 = [4,5,5,2]
summa_ocenok2 = sum([4,5,5,2])
kol_ocenok2 = len([4,5,5,2])
sredniy_ball2 = summa_ocenok2/kol_ocenok2
print('Johnny:' ,sredniy_ball2)
ocenki3 = [4,4,3]
summa_ocenok3 = sum([4,4,3])
kol_ocenok3 = len([4,4,3])
sredniy_ball3 = summa_ocenok3/kol_ocenok3
print('Khendrik:' ,sredniy_ball3)
ocenki4 = [5,5,5,4,5]
summa_ocenok4 = sum([5,5,5,4,5])
kol_ocenok4 = len([5,5,5,4,5])
sredniy_ball4 = summa_ocenok4/kol_ocenok4
print('Steve:' ,sredniy_ball4)
students.update({'Aaron': 4.0,
                 'Bilbo': 2.25,
                 'Johnny': 4.0,
                 'Khendrik': 3.6666666666666665,
                 'Steve': 4.8})
print(students)