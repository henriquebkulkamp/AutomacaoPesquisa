import filtros

def ObtencaoDados(SitesSelecionados, IndiceSites, TopicoPesquisado):
    listaTextos = PegarTexto(SitesSelecionados, IndiceSites)
    titulo = PegarTitulo(TopicoPesquisado)
    return listaTextos, titulo


def PegarTexto(SitesSelecionados, IndiceSites):
    try:
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument('headless')
        driver = webdriver.Chrome(options=ChromeOptions)
    except:
        from selenium import webdriver
        ChromeOptions = webdriver.ChromeOptions()
        ChromeOptions.add_argument('headless')
        driver = webdriver.Chrome(options=ChromeOptions)

    parametros = ['Créditos de imagem', None, None, 'Questão 1', 'Leia também:']

    formaPegarTexto = [filtros.TextoTipo1,
                       filtros.TextoTipo3,
                       filtros.TextoTipo2,
                       filtros.TextoTipo1,
                       filtros.TextoTipo1
                       ]

    listaTextos = []

    for num, forma in enumerate(IndiceSites):
        driver.get(SitesSelecionados[num])
        listaParagrafos = driver.find_elements_by_tag_name('p')
        if parametros[forma] == None:
            texto = formaPegarTexto[forma](listaParagrafos)
            listaTextos.append(texto)
        else:
            texto = formaPegarTexto[forma](listaParagrafos, parametros[forma])
            listaTextos.append(texto)
    return listaTextos


def PegarTitulo(Topico):
    try:
        ChromeOptions = webdriver.ChromeOptions()
    except:
        from selenium import webdriver
        ChromeOptions = webdriver.ChromeOptions()

    ChromeOptions.add_argument('headless')
    driver = webdriver.Chrome(options=ChromeOptions)

    url = 'https://www.google.com.br/search?q=' + str(Topico).replace(' ', '+') + '+Wikipédia'
    driver.get(url)

    while True:
        try:
            driver.find_element_by_css_selector('.DKV0Md').click()
            break
        except:
            try:
                time.sleep(1)
            except:
                import time
                time.sleep(1)
    try:
        time.sleep(10)
    except:
        import time
        time.sleep(10)
    while True:
        try:
            titulo = driver.find_element_by_css_selector('#firstHeading').text
            break
        except:
            time.sleep(1)

    return titulo