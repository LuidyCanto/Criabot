# Discord Bot com Integração OpenAI

Este projeto é um bot para Discord que utiliza a API da OpenAI para fornecer respostas inteligentes aos comandos dos usuários. O bot é construído usando a biblioteca `discord.py` e integra a API da OpenAI para processar texto de forma assíncrona.

## Funcionalidades
- Respostas automáticas utilizando a inteligência artificial da OpenAI.
- Comandos customizados do Discord.
- Integração completa com variáveis de ambiente para gerenciamento seguro de tokens.

## Pré-requisitos

- Python 3.8 ou superior
- Conta no Discord e um bot configurado com o token
- Chave da API da OpenAI
- As seguintes bibliotecas devem ser instaladas:
  - `discord.py`
  - `python-dotenv`
  - `openai`

## Instalação

1. Clone este repositório:
     ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Crie um arquivo .env na raiz do projeto e adicione as seguintes variáveis de ambiente:
    ```makefile
    DISCORD_BOT_TOKEN=seu-token-do-discord
    OPENAI_API_KEY=sua-chave-da-api-openai
    ```
## Uso
Para iniciar o bot, execute o seguinte comando:
```bash
    python main.py
```
O bot estará disponível no seu servidor Discord para responder aos comandos.

## Personalização
 Você pode adicionar mais comandos no arquivo main.py usando o decorator @bot.command() e a funcionalidade de sua escolha.

## Contribuição

 Sinta-se à vontade para contribuir com o projeto. Para isso, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua nova funcionalidade:
    ```bash
    git checkout -b feature/nova-funcionalidade
    ```
3. Faça commit das suas alterações:
    ```bash
    git commit -m 'Adiciona nova funcionalidade'
    ```
4. Faça push para a branch:
    ```bash
    git push origin feature/nova-funcionalidade
    ```
6. Abra um Pull Request.
