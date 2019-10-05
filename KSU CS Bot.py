import discord
import asyncio
from datetime import *

ROLES = {
    "graduate":630156483840966715,
    "alumni":555259582994317313,
    "llc":555472805823512596,
    "intro":630147867407024185,
    "cs1a":630149263216607252,
    "cs1b":630149292149047316,
    "cs2":630148032578584617,
    "cs3":630148378411401236,
    "discrete":630148422523158548,
    "architecture":630148469876850728,
    "operating":630148548566188052,
    "comm":630148607340838927,
    "software":630148736944832523,
    "database":630148797376233482,
    "structure":630149012565262367,
    "algorithms":630149067724554243,
    "capstone":630149199996125204,
#    "test":630126132838006794,
    }

#HELPER FUNCTIONS
def getRoleID(message):
    role = ""
    for x in message.content.split()[1:]:
        role = x.lower() + " "
    role = role.strip()
    
    
    if(role == "graduate" or role == "graduate student"):
        role = message.guild.get_role(ROLES['graduate'])
    elif(role == "alumni"):
        role = message.guild.get_role(ROLES['alumni'])
    elif(role == "llc" or role == "llc member"):
        role = message.guild.get_role(ROLES['llc'])
    elif(role == "intro" or role == "intro to cs"):
        role = message.guild.get_role(ROLES['intro'])
    elif(role == "cs1a"):
        role = message.guild.get_role(ROLES['cs1a'])
    elif(role == "cs1b"):
        role = message.guild.get_role(ROLES['cs1b'])
    elif(role == 'cs2'):
        role = message.guild.get_role(ROLES['cs2'])
    elif(role == "cs3"):
        role = message.guild.get_role(ROLES['cs3'])
    elif(role == "discrete" or role == "discrete structures" or role == 'ds'):
        role = message.guild.get_role(ROLES['discrete'])
    elif(role == "architecture" or role == "computer architecture" or role == "ca"):
        role = message.guild.get_role(ROLES['architecture'])
    elif(role == "operating" or role == "operating systems" or role == "os"):
        role = message.guild.get_role(ROLES['operating'])
    elif(role == "comm" or role == "computer communication networks" or role == "ccn" or role == "computer comm networks"):
        role = message.guild.get_role(ROLES['comm'])
    elif(role == "software" or role == "software engineering" or role == "se"):
        role = message.guild.get_role(ROLES['software'])
    elif(role == "database" or role == "intro to database design" or role == "intro to database" or role == "idd"):
        role = message.guild.get_role(ROLES['database'])
    elif(role == "structure" or role == "structure of programming languages" or role == "spl"):
        role = message.guild.get_role(ROLES['structure'])
    elif(role == "algorithms"):
        role = message.guild.get_role(ROLES['algorithms'])
    elif(role == "capstone"):
        role = message.guild.get_role(ROLES['capstone'])
    elif(role == "test"):
        role = message.guild.get_role(ROLES['test'])
    else:
        role = None

    return role


class MyClient(discord.Client):

    

    #ON MESSAGE
    async def on_message(self,message):
        #print(type(message.author))
        #await message.author.add_roles(message.guild.roles[1],atomic = True)
        if(message.content.startswith("/")):
            await self.process_commands(message)


    #PROCESS COMMANDS
    async def process_commands(self,message):
        command = message.content.split()[0].lower()
        if(command == "/help"):
            await self.help(message)
        elif(command == "/add_role" or command == "/add" or command == "/role"):
            await self.add_role(message)
        elif(command == "/remove_role" or command == "/rm" or command == "/rm_role"):
            await self.remove_role(message)



    #ADD_ROLE
    async def add_role(self,message):
        command = message.content.split()
        if(message.channel.name != "roles"):
            return

        if(len(command)==1):
            await message.channel.send("""List of all available roles are```
Alumni
LLC Member (llc)
Intro to CS (intro)
CS1A
CS1B
CS2
CS3
Discrete Structures (discrete, ds)
Computer Architecture (architecture, ca)
Operating Systems (operating, os)
Computer Communication Networks (ccn, computer comm networks)
Software Engineering (software, se)
Intro to Database Design (database, intro to database, idd)
Structure of Programming Languages (structure, spl)
Algorithms
Capstone
```""")
        else:
            print(str(message.author),"asked for the role",message.content.split()[1:])
            
            role = getRoleID(message)
            if(role == None):
                await message.channel.send("Invalid role. Do /role to view the list of roles.")
                return

            await message.author.add_roles(role,atomic = True)
            await message.channel.send("Role successfully added. "+message.author.mention)
            
            
    #REMOVE_ROLE
    async def remove_role(self,message):
        command = message.content.split()
        if(message.channel.name != "roles"):
            return
        if(len(command) == 1):
            await message.channel.send("Invalid usage. Correct usage:```/[rm|remove|rm_role] <role>```")
        else:
            print(str(message.author),"asked to remove the role",message.content.split()[1:])

            role = getRoleID(message)
            if(role == None):
                await message.channel.send("Invalid role. Do /role to view the list of roles.")
                return

            await message.author.remove_roles(role,atomic = True)
            await message.channel.send("Role successfully removed. "+message.author.mention)


    #HELP
    async def help(self,message):
        command = message.content.split()
        if(len(command) == 1):
            await message.channel.send(content = """```
Here is the list of my commands (Note: [] denotes multiple options, <> denotes a required parameter, and {} denotes an optional parameter):
    /help - shows this message or gives details on a command.
    /[add|add_role|role] <role> - grants yourself a role. Only works in #roles chat.
    /[rm|remove|remove_role] <role> - removes a role from yourself. Only works in #roles chat.
```""")
        else:
            await message.channel.send("Invalid usage. Correct usage:```/help <command>```")
        


    #WHEN READY
    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name = "/help"))
        print("Successfully set Bot's game status")


    #CONNECTION
    async def on_connect(self):
        print("Bot has connected to server at time:",datetime.now())
    
    #DISCONNECTION
    async def on_disconnect(self):
        print("Bot has disconnected from server at time:",datetime.now())

print("Starting KSU CS Bot")
bot = MyClient()
file = open("TOKEN.txt",'r')
TOKEN = file.read()
#print(TOKEN)
bot.run(TOKEN)
