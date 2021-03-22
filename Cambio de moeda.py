letra = str(input("informe a inicial da moeda que o cliente deseja efetuar a compra: "))
valor = float(input("informe o valor total fornecido pelo cliente para efetuar a compra: "))

if letra == "e" or letra == "E":
    preco = 0.31
    print(f" o valor fornecido, convertido para a moeda desejada é: R${valor * preco}")

elif letra == "d" or letra == "D":
    preco = 0.42
    print(f" o valor fornecido, convertido para a moeda desejada é: R${valor * preco}")

elif letra == "m" or letra == "M":
    preco = 5.55
    print(f" o valor fornecido, convertido para a moeda desejada é: R${valor * preco}")

elif letra == "a" or letra == "A":
    preco = 2.84
    print(f" o valor fornecido, convertido para a moeda desejada é: R${valor * preco}")

elif letra == "l" or letra == "L":
    preco = 0.26
    print(f" o valor fornecido, convertido para a moeda desejada é: R${valor * preco}")

else:
    print("essa moeda  não existe")
