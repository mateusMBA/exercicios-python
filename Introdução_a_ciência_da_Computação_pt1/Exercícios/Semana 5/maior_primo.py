def primo (n):
	for i in range (2,n//2):
		if (n % i == 0):
			return False
	return True
	
def maior_primo(n):
	nao_primo = True
	while (nao_primo):
		if primo(n):
			nao_primo = False
		else:
			n -= 1
			
	return n