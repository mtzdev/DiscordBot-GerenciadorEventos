# Gerenciador de Convidados para Eventos (Bot Discord)

O Gerenciador de Convidados é um bot simples e prático para o Discord que facilita o gerenciamento de uma lista de convidados para eventos, festas ou qualquer outra ocasião que precise registrar ou aprovar as pessoas que estarão no evento. Com este bot, você pode controlar, buscar e visualizar convidados de forma rápida, fácil e sincronizada. Permitindo que outros usuários tenham acesso a lista simultaneamente e façam alterações em tempo real com um único comando!

## Funcionalidades Principais:
- **Adicionar Convidado:** Adicione novos convidados à lista através do seu nome com facilidade.
- **Remover Convidado:** Remova convidados existentes da lista conforme necessário.
- **Checar Convidado:** Busca pelo início ou pelo nome completo se um convidado está na lista.
- **Visualizar Lista:** Visualiza a lista inteira de todos os convidados registrados, e a quantia total deles.

## Pré-requisitos e Instalação:
- Tenha Python instalado (recomendado Python 3.9 ou superior)
1. Clone o repositório usando **`git clone https://github.com/mtzdev/DiscordBot-GerenciadorEventos.git`**
2. Instale as dependências do projeto executando **`pip install -r requirements.txt`**.
3. Crie uma aplicação no [site de desenvolvedores do Discord](https://discord.com/developers/applications).
4. Vá até a categoria Bot (localizada canto esquerdo), clique em Reset Token, e copie o novo Token criado
5. Na mesma página, localize as configurações `PRESENCE INTENT`, `SERVER MEMBERS INTENT` e `MESSAGE CONTENT INTENT`, e habilite todas elas.
6. Abra o arquivo `config.json`, delete onde está escrito *`insira_seu_token_aqui`* e substitua pelo token que você copiou anteriormente.
7. Execute o programa usando: **`python main.py`**
8. Convide o bot para algum servidor e utilize o comando /lista para visualizar o painel do bot.

## Como Usar:
1. Use o comando /lista em algum canal de texto.
2. Utilize as funções através dos botões existentes na mensagem
3. Cada botão possui uma descrição informando o que faz, que está contida na mensagem

## Contribuições e Licença
Este é um projeto que foi desenvolvido para um amigo meu, mas atualmente não está mais em uso, então resolvi publica-lo e deixar código aberto, sinta-se a vontade de melhorar o código, abrir problemas ou enviar solicitações de pull!
<br>
Este projeto é licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](https://github.com/mtzdev/DiscordBot-GerenciadorEventos/blob/main/LICENSE) para obter detalhes.