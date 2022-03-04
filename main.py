import interfaces, dados, resumo, imagens, formatar, word


def Main():
    TopicoPesquisado, QuantidadeParagrafos, Parafrasear, SitesSelecionados, ImagensSelecionadas, IndiceSites = interfaces.Interface()
    listaTextos, Titulo = dados.ObtencaoDados(SitesSelecionados, IndiceSites, TopicoPesquisado)
    TextoResumido = resumo.ResumirTexto(listaTextos)
    Imagens = imagens.SalvarImagens(ImagensSelecionadas)
    TextoFormatado = formatar.formatarTexto(TextoResumido, QuantidadeParagrafos)
    word.SalvarNoWord(TextoFormatado, Titulo, Imagens)


Main()