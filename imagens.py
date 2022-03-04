def SalvarImagens(ImagensSelecionadas):
    try:
        Path(r'C:/Users/Henrique/Desktop')
    except:
        from pathlib import Path
        Path(r'C:/Users/Henrique/Desktop')

    try:
        Path(r'C:/Users/Henrique/Desktop/trabalho').mkdir()
    except:
        ArquivosVelhos = Path(r'C:/Users/Henrique/Desktop/trabalho').iterdir()
        for arquivo in ArquivosVelhos:
            arquivo.unlink()

    try:
        chromeOptions = webdriver.ChromeOptions()
    except:
        from selenium import webdriver
        chromeOptions = webdriver.ChromeOptions()

    chromeOptions.add_argument('headless')
    driver = webdriver.Chrome(options=chromeOptions)

    Imagens = []

    for i in range(len(ImagensSelecionadas)):
        driver.get(ImagensSelecionadas[i])
        driver.find_element_by_tag_name('img').screenshot(
            r'C:\Users\Henrique\Desktop\trabalho\Imagem' + f'{i + 1}' + '.png')
        Imagens.append(r'C:\Users\Henrique\Desktop\trabalho\Imagem' + f'{i + 1}' + '.png')

    driver.close()
    return Imagens