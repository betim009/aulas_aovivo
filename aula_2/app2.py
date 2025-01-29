import time
import pyautogui

"""
como escrever método
nome()
tipo.nome()

strings
strings possuem posicao
string[posicao] string[4]
string[:3] string[3:]



"""
#                 400  300  299  200
check_points_y = [400, 300, 299, 200]
#                 0    1    2    3

check_points_x = [100, 200, 399, 400]


"""
For => element
For Ennumerate => element e index
For Range => index

listComprehension
"""
for index, element in enumerate(check_points_x):
    pyautogui.click(100, 200)
    time.sleep(2)