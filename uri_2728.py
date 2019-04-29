while True:
    try:
        frase = input().lower()
        if len(frase) > 50:
            False

        separado = frase.split('-')
        temp = 'cobol'
        mensagem = ''
        for i in range(5):
            a = separado[i][0]
            b = separado[i][-1]
            c = temp[i]
            if a == temp[i] or b == temp[i]:
                mensagem = 'GRACE HOPPER'
            else:
                mensagem = 'BUG'
                break
        print(mensagem)

    except:
        break
