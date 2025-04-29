# 🏨 Scraping de Hotéis no Booking.com usando Playwright (Python + Google Colab)

## 📋 Descrição do Projeto

Este notebook realiza o scraping de informações do site **Booking.com** para o município de **Teresópolis** (RJ), conforme as regras estabelecidas:

- **Local**: Teresópolis, Rio de Janeiro, Brasil
- **Número de Adultos**: 1 adulto
- **Datas**: 
  - **Check-in**: Amanhã
  - **Check-out**: Depois de amanhã

As informações extraídas de cada hotel são:

- **Nome do Hotel**
- **Preço da Hospedagem**
- **Quantidade de Quartos Disponíveis**

O projeto foi desenvolvido utilizando a biblioteca **Playwright**, que simula a navegação humana de forma eficiente e confiável, além do uso de técnicas para garantir o carregamento completo da página antes da extração.

---

## 🚀 Passo a Passo da Solução

1. **Instalação das Bibliotecas**: Utilização do `playwright` para automação de navegador em modo visual (`headless=False`).
2. **Geração Dinâmica de Datas**: Função `get_dates()` para calcular automaticamente o check-in (amanhã) e check-out (depois de amanhã).
3. **Configuração do Navegador**: Lançamento do navegador Chromium com user-agent customizado e viewport adaptada.
4. **Construção da URL de Busca**: Inserção dos parâmetros na URL para realizar a pesquisa conforme solicitado.
5. **Acesso e Espera**: Navegação até a página de resultados e espera explícita para garantir o carregamento dos cards de hotéis.
6. **Extração de Dados**:
    - Nome do hotel
    - Preço da hospedagem
    - Disponibilidade de quartos
7. **Tratamento de Erros**: Captura de exceções para evitar falhas em caso de mudanças no layout da página.
8. **Fechamento do Navegador**: Encerramento correto do navegador após a extração.

---

## 🤖 Observações

- **Inteligência Artificial aplicada**: A automação foi pensada para ser robusta e adaptável a mudanças pequenas no site.
- **Elegância e Organização**: Cada etapa foi cuidadosamente separada em blocos claros e bem documentados, seguindo boas práticas de scraping e automação.
- **Execução**: O código foi estruturado para funcionar no **Google Colab**, com pequenas adaptações para facilitar a execução no ambiente em nuvem.
