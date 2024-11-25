import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.declarative import declarative_base

# Carregar variáveis de ambiente
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configurar o bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Configurar o banco de dados
Base = declarative_base()
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    discord_id = Column(String, unique=True)
    games = Column(String)  # Lista de jogos separados por vírgula

# Criar tabelas
Base.metadata.create_all(engine)

@bot.event
async def on_ready():
    print(f'{bot.user} está online!')

@bot.command(name='cadastrar')
async def register_games(ctx, *, games):
    """Cadastra os jogos que você joga. Exemplo: !cadastrar LOL, Valorant, CS:GO"""
    session = Session()
    
    try:
        # Verificar se usuário já existe
        user = session.query(User).filter_by(discord_id=str(ctx.author.id)).first()
        
        if user:
            user.games = games
            message = "Seus jogos foram atualizados!"
        else:
            new_user = User(discord_id=str(ctx.author.id), games=games)
            session.add(new_user)
            message = "Cadastro realizado com sucesso!"
            
        session.commit()
        await ctx.send(message)
        
    except Exception as e:
        await ctx.send("Ocorreu um erro ao cadastrar seus jogos.")
        print(f"Erro: {e}")
    finally:
        session.close()

@bot.command(name='jogos')
async def list_games(ctx, member: discord.Member = None):
    """Lista os jogos de um usuário. Se nenhum usuário for especificado, mostra seus próprios jogos."""
    session = Session()
    
    try:
        target_id = str(member.id if member else ctx.author.id)
        user = session.query(User).filter_by(discord_id=target_id).first()
        
        if user:
            username = member.name if member else ctx.author.name
            embed = discord.Embed(
                title=f"Jogos de {username}",
                description=user.games,
                color=discord.Color.blue()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("Este usuário ainda não cadastrou nenhum jogo.")
            
    except Exception as e:
        await ctx.send("Ocorreu um erro ao buscar os jogos.")
        print(f"Erro: {e}")
    finally:
        session.close()

# Iniciar o bot
bot.run(TOKEN)
