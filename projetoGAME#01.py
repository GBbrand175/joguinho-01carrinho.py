import pygame

pygame.init()

#posição do carro ofc
x = 400
y = 300
#posição dos carros adicionais
pos_x = 200
pos_y = 300

#comando de velocidades dos carros
velocidade = 21
velo_2 = 17

 #Graficos/Imagens
fundo = pygame.image.load('PISTA_JOGO_OFC2.png')
carro = pygame.image.load('car_jogo_ofc.png')
car2 = pygame.image.load('carro_jogo_ofc2.png')
car3 = pygame.image.load('carro_jogo_ofc2.png')

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("#01 jogo em Python")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

#comandos do jogo
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    pos_y -= velo_2

    #repetidor do carro 2
    if pos_y <=-220:
        pos_y = 600


    janela.blit(fundo, (70, 0))
    janela.blit(carro, (x, y))
    janela.blit(car2, (pos_x, pos_y))
    janela.blit(car3, (pos_x + 240, pos_y))

    pygame.display.update()
pygame.quit()
