import os
import discord

class bitree:
    def __init__(self, value, is_number, lchild, rchild):
        self.value = value
        self.is_number = is_number
        self.lchild = lchild
        self.rchild = rchild
        
    def __repr__(self):
        toprint = ""
        if self.lchild == None and self.rchild == None:
            return str(self.value)
        else:
            return '('+repr(self.lchild) + '<' + str(self.value) + '>' + repr(self.rchild)+')'
        
def equation_to_bitree(eqn):
    level = 0
    numbers = ['1','2','3','4','5','6','7','8','9','0','.']
    operators = ['+', '-', '*', '/', '^']
    length = len(eqn)
    for i in range(0,length):
        current = eqn[i]
        if current == '(':
            level += 1
        elif current == ')':
            level -= 1
        elif current in operators and level == 1:
            return bitree(current, False, equation_to_bitree(eqn[1:i]), equation_to_bitree(eqn[i + 1:length - 1]))
        elif (current in numbers) and (level == 0):
            return bitree(float(eqn), True, None, None)
        elif current not in operators and current not in numbers:
            raise NameError("Invalid character")
        else:
            continue
    
def solvebitree(eqn):
    current = eqn.value
    
    if eqn.is_number:
        return float(current)
    elif current == '+':
        return float(solvebitree(eqn.lchild)) + float(solvebitree(eqn.rchild))
    elif current == '-':
        return float(solvebitree(eqn.lchild)) - float(solvebitree(eqn.rchild))
    elif current == '*':
        return float(solvebitree(eqn.lchild)) * float(solvebitree(eqn.rchild))
    elif current == '/':
        return float(solvebitree(eqn.lchild)) / float(solvebitree(eqn.rchild))
    elif current == '^':
        return float(solvebitree(eqn.lchild)) ** float(solvebitree(eqn.rchild))


TOKEN = 'ODAyMTg1ODMyNzAxNzU1NDMz.YArjxg.0tY4AjVSQH21VdUHXOG6ZCgNrYk'
        
client = discord.Client()
    
@client.event
async def on_ready():
    print(f'{client.user.name} Online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    text = message.content.lower()
    if text[:6] == '!solve':
        try:
            await message.channel.send(solvebitree(equation_to_bitree(text[7:])))
        except NameError:
            await message.channel.send("Invalid Character")
        except:
            await message.channel.send("Invalid Expression")
    
        
client.run(TOKEN)
