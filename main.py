import discord
import os
#from replit import db

# Discord Bot Quickstart from discord.py documentation
#-------------------------------------------------#
intents = discord.Intents.default()
intents.message_content = True
                                                    
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
#-------------------------------------------------#


# Rules for messages posted in server
#---------------------------------------------------------------------------------------#
@client.event
async def on_message(message):
    
  # Ignore messages from the bot
    if message.author == client.user:
        return
    
    # Create Role from Message
    args = message.content.split(" ")[2:] # 2: because prefix contains space
    if message.content.lower().startswith("as createrole"):
        role = await message.guild.create_role(name=" ".join(args))
        await message.author.add_roles(role)
        await message.channel.send(f"Successfully created and assigned {role.mention}!")
       
    # $hello: Have Bot say "Hello!"
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
#---------------------------------------------------------------------------------------#


# Rules for Reactions to Posts
#--------------------------------------------------------------#
# Role Assignment Dictionary
roledict = {}
roledict[r"<:praisesun:1151173101183316158>"] = 1151185214165499954
roledict[r"👀"] = 0

# Event definition
@client.event
async def on_reaction_add(reaction, user):

  # Role opt ins from specific channel
  if reaction.message.channel.id == 1151125159244214336:
    rolekey = str(reaction.emoji)
  
    try:
      role = reaction.message.guild.get_role(roledict[rolekey])
      await user.add_roles(role)
    except KeyError:
      print(f"rolekey unrecognised: {rolekey}")
    except AttributeError:
      print(f"the roleid {roledict[rolekey]} does not exist")
#--------------------------------------------------------------#

# Run the bot
client.run(os.environ['TOKEN'])