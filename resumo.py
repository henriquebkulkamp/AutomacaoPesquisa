def ResumirTexto(listaTextos):
    TextosResimidos = []
    for i in range(len(listaTextos)):
        try:
            chromeOptions = webdriver.ChromeOptions()
        except:
            from selenium import webdriver
            chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('headless')
        driver = webdriver.Chrome(options=chromeOptions)  # entrando no site
        driver.get('https://www.turbinetext.com/resumo')

        FecharAnuncio = driver.find_elements_by_class_name('modal-content')[1]  # fechando anúncio
        FecharAnuncio = FecharAnuncio.find_element_by_class_name('modal-footer')
        FecharAnuncio.find_element_by_class_name('btn-secondary').click()

        AreaDeTexto = driver.find_element_by_class_name('textarea-turbine')  # escrevendo o texto

        AreaDeTexto.send_keys(listaTextos[i])

        OpcoesDeResumo = driver.find_element_by_css_selector('#ddlResumirPor')
        OpcoesDeResumo.click()
        OpcoesDeResumo.find_elements_by_tag_name('option')[
            2].click()  # Troca de porcentagem para quantidade de paragrafos

        OpcoesDeTamanho = driver.find_element_by_css_selector('#ddlLinhas')
        OpcoesDeTamanho.click()
        OpcoesDeTamanho = OpcoesDeTamanho.find_elements_by_tag_name("option")
        OpcoesDeTamanho[20].click()

        driver.find_element_by_css_selector('#btnExecuteFunction').click()  # Esperando o resumo sair
        try:
            time.sleep(60)
        except:
            import time
            time.sleep(60)

        while True:
            try:
                driver.find_element_by_css_selector('#viewB').click()
                break
            except:
                time.sleep(1)

        while True:  # Obtendo o resumo e atribuindo a uma variável
            try:
                time.sleep(QuantidadeParagrafos)
                TextoParaTrabalho = driver.find_element_by_tag_name('textarea').text
                driver.find_element_by_tag_name('textarea').clear()
                break
            except:
                pass
        TextosResimidos.append(TextoParaTrabalho)
        driver.close()

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get('https://www.turbinetext.com/resumo')

    time.sleep(10)
    try:
        FecharAnuncio = driver.find_elements_by_class_name('modal-content')[1]  # fechando anúncio
        FecharAnuncio = FecharAnuncio.find_element_by_class_name('modal-footer')
        FecharAnuncio.find_element_by_class_name('btn-secondary').click()
    except:
        pass

    AreaDeTexto = driver.find_element_by_class_name('textarea-turbine')  # escrevendo o texto

    for i in TextosResimidos:
        AreaDeTexto.send_keys(i)

    OpcoesDeResumo = driver.find_element_by_css_selector('#ddlResumirPor')
    OpcoesDeResumo.click()
    OpcoesDeResumo.find_elements_by_tag_name('option')[2].click()

    OpcoesDeTamanho = driver.find_element_by_css_selector('#ddlLinhas')
    OpcoesDeTamanho.click()
    OpcoesDeTamanho = OpcoesDeTamanho.find_elements_by_tag_name("option")
    OpcoesDeTamanho[20].click()

    driver.find_element_by_css_selector('#btnExecuteFunction').click()  # Esperando o resumo sair
    time.sleep(60)

    while True:
        try:
            driver.find_element_by_css_selector('#viewB').click()
            break
        except:
            time.sleep(1)

    while True:  # Obtendo o resumo e atribuindo a uma variável
        try:
            time.sleep(QuantidadeParagrafos)
            TextoResumido = driver.find_element_by_tag_name('textarea').text
            break
        except:
            pass
    driver.close()

    return TextoResumido