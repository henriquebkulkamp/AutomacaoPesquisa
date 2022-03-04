def TextoTipo1(listaparagrafos, parametro):
    texto = ''
    for p in listaparagrafos:
        para, usar = SelecaoTextoTipo1(p, parametro)

        if para == True:
            break

        if usar == True:
            texto += p.text
    return texto


def SelecaoTextoTipo1(p, parametro):
    try:
        p.text

    except:
        return False, False

    if parametro in p.text:
        a = True
    else:
        a = False

    if len(p.text) < 100:
        return a, False

    try:
        for c in p.find_elements_by_tag_name('strong'):
            c = c.text[-1]

        p.find_element_by_tag_name('strong').text
        p.find_element_by_tag_name('a').text

    except:
        return a, True

    for c in p.find_elements_by_tag_name('strong'):
        if c.text[-1] == ':':
            return a, False

    if len(p.find_element_by_tag_name('a').text) + len(p.find_element_by_tag_name('strong').text) == len(p.text):
        return a, False

    return a, True


def TextoTipo2(lista=list):
    texto = ''
    for p in lista:
        if SelecaoTextoTipo2(p) == True:
            texto += p.text
    return texto


def SelecaoTextoTipo2(p):
    try:
        if len(p.text) < 100:
            return False
    except:
        return False

    return True


def TextoTipo3(lista=list):
    texto = ''
    for p in lista:
        if SelecaoTextoTipo3(p) == True:
            texto += p.text
    ftexto = FormatacaoWikipedia(texto)
    return ftexto


def SelecaoTextoTipo3(p):
    try:
        if len(p.text) < 100:
            return False
    except:
        return False

    return True


def FormatacaoWikipedia(texto):
    fTexto = texto
    num = 0
    margemDeErro = 0
    while True:
        num += 1
        nota = f'[nota {num}]'
        if nota in fTexto:
            fTexto = fTexto.replace(nota, '')

        indice = f'[{num}]'
        if indice in fTexto:
            fTexto = fTexto.replace(indice, '')

        else:
            margemDeErro += 1
            if margemDeErro > 100:
                break
    return fTexto