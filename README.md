# Bot de Gerenciamento de Jogos do Discord

Este é um bot do Discord que permite aos usuários cadastrar e consultar os jogos que eles jogam.

## Configuração

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure o token do bot:
- Crie um bot no [Portal de Desenvolvedores do Discord](https://discord.com/developers/applications)
- Copie o token do bot
- Cole o token no arquivo `.env` substituindo "seu_token_aqui"

3. Execute o bot:
```bash
python bot.py
```

## Comandos

- `!cadastrar [jogos]`: Cadastra os jogos que você joga
  Exemplo: `!cadastrar LOL, Valorant, CS:GO`

- `!jogos [@usuário]`: Lista os jogos de um usuário
  Se nenhum usuário for mencionado, mostra seus próprios jogos

## Hospedagem

Você pode hospedar este bot em várias plataformas:

1. **Heroku**:
   - Gratuito para projetos pequenos
   - Fácil de configurar
   - [Tutorial de deploy no Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

2. **Railway**:
   - Plataforma moderna e fácil de usar
   - Oferece plano gratuito
   - [Railway.app](https://railway.app/)

3. **DigitalOcean**:
   - Mais robusto e profissional
   - Droplets a partir de $5/mês
   - [DigitalOcean](https://www.digitalocean.com/)

4. **Replit**:
   - Gratuito para projetos pequenos
   - Ideal para iniciantes
   - [Replit](https://replit.com/)
