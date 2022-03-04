def interface1():  # Pegar as informações principais, sobre a custimização da apresentação
    try:
        interfaceInicial = tk.Tk()
    except:
        import tkinter as tk
        interfaceInicial = tk.Tk()

    msgPesquisa = tk.Label(text="Escreva o que pesquisa:", font=23)
    msgPesquisa.grid(row=0, column=0, columnspan=2)

    boxTopicoPesquisado = tk.Entry()
    boxTopicoPesquisado.grid(row=1, column=0, columnspan=2)

    msgQuantidadeParagrafos = tk.Label(text='Quantidade de parágrafos', font=30)  # Obtendo a quantidade de paragrafos
    msgQuantidadeParagrafos.grid(row=2, column=0)
    boxQuantidadeParagrafos = tk.Entry()
    boxQuantidadeParagrafos.grid(row=2, column=1)

    def Enviar():
        global TopicoPesquisado
        global Parafrasear
        global QuantidadeParagrafos
        Parafrasear = varParafrasear.get()
        QuantidadeParagrafos = boxQuantidadeParagrafos.get()

        if str(QuantidadeParagrafos).isnumeric() and int(QuantidadeParagrafos) > 0:
            QuantidadeParagrafos = int(QuantidadeParagrafos)
        else:
            QuantidadeParagrafos = 10

        TopicoPesquisado = str(boxTopicoPesquisado.get())
        interfaceInicial.destroy()
        return

    botaoEnviar = tk.Button(text="Enviar", command=Enviar, font=20)
    botaoEnviar.grid(row=3, column=0, columnspan=2)

    interfaceInicial.mainloop()
    return TopicoPesquisado, QuantidadeParagrafos, Parafrasear


def interface2(TopicoPesquisado):  # Selecionar o sites que serão utilizados como fonte
    SitesSelecionados = []
    try:
        driver = webdriver.Chrome()

    except:
        from selenium import webdriver
        driver = webdriver.Chrome()

    def janela():

        try:
            Inteface2 = tk.Tk()
        except:
            import tkinter as tk
            Inteface2 = tk.Tk()

        def Sim(drive=driver, lista=SitesSelecionados, lista2=IndiceSites, i=indice):
            lista.append(drive.current_url)
            lista2.append(i)
            Inteface2.destroy()

        def Nao():
            Inteface2.destroy()

        confirmar = tk.Button(background='green', padx=25, pady=20, command=Sim)
        confirmar.grid(column=0, row=0)

        negar = tk.Button(background='red', padx=25, pady=20, command=Nao)
        negar.grid(column=1, row=0)

        Inteface2.mainloop()

    IndiceSites = []
    SitesParaPesquisar = ['Brasil+Escola', 'Wikipédia', 'Toda+Matéria', 'Mundo+Educação', 'InfoEscola']
    for indice, VariavelUrl in enumerate(SitesParaPesquisar):
        VariavelUrl = f'{TopicoPesquisado}'.replace(' ', '+') + f'+{VariavelUrl}'
        driver.get('https://www.google.com/search?q=' + VariavelUrl)
        janela()

    driver.close()
    return SitesSelecionados, IndiceSites


def interface3(TopicoPesquisado):  # Selecionar as imagens que serão utilizadas na apresentação
    ImagensSelecionadas = []
    try:
        driver = webdriver.Chrome()
    except:
        from selenium import webdriver
        driver = webdriver.Chrome()
    driver.get(
        'https://www.google.com/search?q=' + TopicoPesquisado + '&sxsrf=APq-WBuD-4GjU4pQ5MyIgTXjQ4f8U_ds4g:1645551696989&source=lnms&tbm=isch&')

    def intefaceimagem():
        global sai
        try:
            interface3 = tk.Tk()
        except:
            import tkinter as tk
            interface3 = tk.Tk()

        def selecionar(drive=driver, ImagensSelecionadas=ImagensSelecionadas):
            global sai
            sai = 0
            a = drive.find_element_by_css_selector('#Sva75c')
            b = a.find_elements_by_tag_name('img')
            src = b[2].get_attribute('src')
            ImagensSelecionadas.append(src)
            interface3.destroy()

        def sair(drive=driver):
            global sai
            sai = 1
            interface3.destroy()

        botaoSelecionar = tk.Button(background='green', padx=25, pady=20, command=selecionar)
        botaoSelecionar.grid(row=0, column=0)

        botaoSair = tk.Button(background='red', padx=25, pady=20, command=sair)
        botaoSair.grid(row=0, column=1)

        interface3.mainloop()

        return sai

    while True:
        sai = intefaceimagem()
        if sai == 1:
            break

    driver.close()

    return ImagensSelecionadas


def Interface():
    TopicoPesquisado, QuantidadeParagrafos, Parafrasear = interface1()  # Obter sobre o que é a pesquisa

    SitesSelecionados, indiceSites = interface2(TopicoPesquisado)  # Obter onde pesquisar

    ImagensSelecionadas = interface3(TopicoPesquisado)  # selecionar as imagens

    return TopicoPesquisado, QuantidadeParagrafos, Parafrasear, SitesSelecionados, ImagensSelecionadas, indiceSites