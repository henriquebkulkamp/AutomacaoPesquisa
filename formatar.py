def formatarTexto(TextoResumido, QuantidadeParagrafos):
    if TextoResumido[-1] == '.':
        TextoResumido = TextoResumido[0: len(TextoResumido) - 1]
    Texto = TextoResumido.replace('..', '.')
    Texto = Texto.replace('...', '@#RETICENCIAS#@')  # Para não tratar as reticências como três pontos separados
    textoSeparado = Texto.split('.')

    ColarParagrafos = []
    for i in range(len(textoSeparado)):
        ColarParagrafos.append(False)  # No momento não se colará nenhum paragrafo

    for indice, paragrafo in enumerate(textoSeparado):
        primeiroParenteses = segundoParenteses = 0
        for caractereParagrafo in paragrafo:
            if caractereParagrafo == '(':
                primeiroParenteses += 1

            if caractereParagrafo == ')':
                segundoParenteses += 1

        if primeiroParenteses == segundoParenteses:
            parentesesIguais = True
        else:
            parentesesIguais = False

        if len(paragrafo) > 100:
            tamanho = True
        else:
            tamanho = False

        if indice < (len(textoSeparado) - 1):
            for letrinha in textoSeparado[indice + 1]:
                if letrinha == ' ':
                    pass

                else:
                    if letrinha == letrinha.capitalize():
                        proximaMaiuscula = True
                        break

                    else:
                        proximaMaiuscula = False
                        break
        else:
            proximaMaiuscula = True

        if not(parentesesIguais and tamanho and proximaMaiuscula):  # Parametros para não colar os paragrafos
            if indice > 0:
                ColarParagrafos[indice - 1] = True

            if indice < (len(textoSeparado) - 1):
                ColarParagrafos[indice + 1] = True

            ColarParagrafos[indice] = True

    preParagrafosFormatados = []
    deveColar = 0
    for indice, paragrafo in enumerate(textoSeparado):
        if ColarParagrafos[indice] == False:
            preParagrafosFormatados.append(paragrafo)
            deveColar = 0

        else:
            if deveColar == 1:
                pass
            else:
                deveColar = 1
                numeroIndice = 0
                temp = ''
                while True:
                    try:
                        if ColarParagrafos[indice + numeroIndice] == True:
                            temp += textoSeparado[indice + numeroIndice]
                            numeroIndice += 1
                        else:
                            break
                    except:
                        break
                preParagrafosFormatados.append(temp)

    for i in range(len(preParagrafosFormatados) - 1, -1, -1):
        if preParagrafosFormatados[i] == '':
            preParagrafosFormatados.pop(i)  # Tirando os paragrafos vazios

    for indice, paragrafo in enumerate(preParagrafosFormatados):
        novoParagrafo = paragrafo.replace('@#RETICENCIAS#@',
                                          '...') + '.'  # Colocando as reticências e o ponto final de volta
        preParagrafosFormatados[indice] = novoParagrafo

    if len(preParagrafosFormatados) >= QuantidadeParagrafos:
        temp = []
        for i in range(int(QuantidadeParagrafos)):
            temp.append(preParagrafosFormatados[i])
        preParagrafosFormatados = temp

    return preParagrafosFormatados