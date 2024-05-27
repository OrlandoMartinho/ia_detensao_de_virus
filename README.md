**Detecção de Sites Maliciosos com Flask e Análise de Dados**

Este é um projeto que utiliza o framework Flask para criar uma API capaz de detectar sites maliciosos com base em dados de análise. Inclui um processo de treinamento de modelos de IA para classificação de sites e fornece endpoints para interagir com a API.

### Estrutura do Projeto

- **app.py**: O arquivo principal que define a aplicação Flask e seus endpoints.
  
- **script**: Contém os arquivos de treinamento e teste da IA, bem como a limpeza do dataset.
  
- **data**: Contém o dataset em formato CSV utilizado para treinar e testar os modelos. [Link para o dataset](https://www.kaggle.com/datasets/satyaganeshkumar/phishing-websites)

- **AI models**: Contém os modelos treinados e testados pela IA.

### Configuração e Instalação

1. Clone o repositório para sua máquina local:

    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    ```

2. Instale as dependências necessárias. Você pode usar o `pip` para instalar as dependências listadas no arquivo `requirements.txt`:

    ```
    pip install -r requirements.txt
    ```

### Uso

1. Inicie o servidor Flask executando o arquivo `app.py` na raiz do projeto:

    ```
    python app.py
    ```

2. Acesse os endpoints da API para interagir com a aplicação e obter previsões sobre a maliciosidade dos sites.

### Contribuição

Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

Este é um esboço do README. Sinta-se à vontade para personalizá-lo com mais detalhes sobre a implementação, os modelos de IA utilizados, como os endpoints da API funcionam e qualquer outra informação relevante para os usuários e contribuidores do projeto.