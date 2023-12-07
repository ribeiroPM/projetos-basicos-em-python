import keyboard

def retorna_key_pressionada():
	teclas_possiveis = "1,2,3,4,5,6,7,8,9,0,+,-,/,*".split(",")
	for tecla in teclas_possiveis:
		if keyboard.is_pressed(tecla):
			return tecla

while True:
	tecla = retorna_key_pressionada()
	print(tecla)
	if tecla == "+":
		break
	