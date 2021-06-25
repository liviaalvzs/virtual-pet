class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 10
        self.saude = 80
        self.idade = 1
    def MudarNome(self, novoNome):
        self.nome = novoNome
    def MudarFome(self, valorF):
        self.fome += valorF
        if self.fome > 100:
            self.fome = 100
        elif self.fome < 0:
            self.fome = 0
    def MudarSaude(self, valorS):
        self.saude += valorS
        if self.saude > 100:
            self.saude = 100
        elif self.saude < 0:
            self.saude = 0
    def MudarIdade(self):
        self.idade += 1
    def RetornarNome(self):
        return self.nome
    def RetornarFome(self):
        return self.fome
    def RetornarSaude(self):
        return self.saude
    def RetornarIdade(self):
        return self.idade
    def RetornarHumor(self):
        humor = self.saude + self.fome 
        return humor

nomeB = input('\nOi! Qual o nome você quer colocar no seu pet? ')
Pet = Pet(nome = nomeB)
while (Pet.saude > 0) and (Pet.fome < 100):
    Pet.MudarFome(+2)
    Pet.MudarSaude(-2)
    Pet.MudarIdade()
    resposta = input(f"""------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`
     \nOi!! Eu me chamo {Pet.nome}. 
    \nMinhas informações: 
    Minha felicidade: {Pet.RetornarHumor()} | Minha idade: {Pet.RetornarIdade()}
    Minha fome: {Pet.RetornarFome()} | Meus pontos de saude: {Pet.RetornarSaude()}
    \nO que você vai fazer comigo? \n1- Alimentar com Fruta (-10 de fome e +1 ponto de saude)\n2- Alimentar com doce (-12 de fome e -2 pontos de saude)\n3- Dormir (+8 pontos de saude)\n4- Mudar nome\nResposta: """)
    if resposta == '1':
        Pet.MudarFome(-10)
        Pet.MudarSaude(+1)
        print('Hmm... Isso foi muito bom!')
    elif resposta == '2':
        Pet.MudarFome(-12)
        Pet.MudarSaude(-2)
        print('Hmm... Isso foi muito bom! <3 Amo doces!')
    elif resposta == '3':
        Pet.MudarSaude(+8)
        print('ZzZzZzZz......Ufa! Me sinto melhor agora!')
    elif resposta == '4':
        nomeatualizado = input('Qual o meu novo nome? ')
        Pet.MudarNome(nomeatualizado)
    else:
        print('Escolha uma opção válida!')
else:
    print("""\n------------------------------------------\n __         __
/  \.-" "-./  \.
\    -   -    /
 |   X   X   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`\bVocê não cuidou bem de mim, agora eu morri :( \n""")