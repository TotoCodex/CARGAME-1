import csv
import re
import pygame
import random
import pygame.mixer

def getSuperficies(path,filas,columnas):
    lista=[]
    sprite_sheet = pygame.image.load(r'pygames_sound_png\spritesheet-512px-by197px-per-frame.png')
    frame_width = int(sprite_sheet.get_width() / columnas)
    frame_height = int(sprite_sheet.get_height() / filas)


    
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * frame_width
            y = fila * frame_height
            superficie_fotograma = sprite_sheet.subsurface(x, y, frame_width-105, frame_height)
            lista.append(superficie_fotograma)
    return lista

    
    
class Turbo(pygame.sprite.Sprite):
        def __init__(self,pos_x,pos_y):
            super().__init__()
            self.active= False
            self.sprites = getSuperficies(r'pygames_sound_png\spritesheet-512px-by197px-per-frame.png',2,3)
            scaled_sprites=[]
            for sprite in self.sprites:
                scaled_sprite = pygame.transform.scale(sprite,(100,70))
                scaled_sprites.append(scaled_sprite)
            self.sprites = scaled_sprites
            
            
            self.current_sprite = 0
            self.ciclo=0
            self.image = self.sprites[self.current_sprite]
            self.original_image = self.image
            self.rect = self.image.get_rect()
            self.rect.topleft = [pos_x,pos_y]

        def update(self):
            if self.active == False:
                self.image.set_alpha(0)#la imagen es transparente cuando no esta activo
                return None
            else:
                self.current_sprite += 0.2

                if self.current_sprite >= len(self.sprites):
                    self.current_sprite = 0
                    
                if self.current_sprite == 0:
                    self.ciclo += 1
                if self.ciclo == 500:    
                    self.active=False
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                    self.angulo_turbo=-20
                    self.rect = (posicion_auto[0]-145,posicion_auto[1]-68)
                elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                    self.angulo_turbo=20
                    self.rect = (posicion_auto[0]-135,posicion_auto[1]-2)
                else:
                    self.angulo_turbo=0
                    self.rect = (posicion_auto[0]-137,posicion_auto[1]-23)

                self.image = pygame.transform.rotate(self.sprites[int(self.current_sprite)],self.angulo_turbo)
                #para que esté anclado al auto 
COLOR_TURQUESA=(128,128,128)
COLOR_X=(0,200,0)
ANCHO_VENTANA= 1300
ALTO_VENTANA= 800
COLOR_BLANCO=(0,0,0)
posicion_top_bush=[500,50]
posicion_buttom_bush=[0,750]

posicion_auto5=[1000,500]
posicion_auto4=[1000,650]

posicion_auto3=[700,200]
posicion_auto2=[700,300]
posicion_auto=[0,250]

posicion_top_pipe=[700,100]
posicion_bottom_pipe=[250,700]
posicion_middle_pipe=[3000,391]

posicion_oil=[3000,600]



pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()

acumulador_text = 1
font = pygame.font.Font(None,36)

#rectangulo font de 
turbo=Turbo(20000,20000)#lo coloco fuera del rango cosa de que si esta inactivo no se vea, ahora si aprieto la x arranca mi class
moving_sprites= pygame.sprite.Group()#VAN ANTES DEL WHILE
moving_sprites.add(turbo)


imagen=pygame.image.load(r"pygames_sound_png\car_1.png")
imagen= pygame.transform.scale(imagen,(80,50))
imagen_rect=imagen.get_rect()


imagen2=pygame.image.load(r"pygames_sound_png\yellow_car.png")
imagen2= pygame.transform.scale(imagen2,(90,50))
imagen2_rect=imagen2.get_rect()

imagen3=pygame.image.load(r"pygames_sound_png\red_car.png")
imagen3= pygame.transform.scale(imagen3,(90,55))
imagen3_rect=imagen3.get_rect()


imagen_white_car=pygame.image.load(r"pygames_sound_png\white_car.png")
imagen_white_car= pygame.transform.scale(imagen_white_car,(90,50))
imagen_white_car_rect=imagen_white_car.get_rect()

imagen_gold_car=pygame.image.load(r"pygames_sound_png\gold _car.png")
imagen_gold_car= pygame.transform.scale(imagen_gold_car,(100,50))
imagen_gold_car_rect=imagen_gold_car.get_rect()


imagen_top_bush=pygame.image.load(r"pygames_sound_png\bush.png")
imagen_top_bush= pygame.transform.scale(imagen_top_bush,(200,80))
imagen_top_bush_rect=imagen_top_bush.get_rect()

imagen_buttom_bush=pygame.image.load(r"pygames_sound_png\bush rotado.png")
imagen_buttom_bush= pygame.transform.scale(imagen_buttom_bush,(200,80))
imagen_buttom_bush_rect=imagen_buttom_bush.get_rect()

imagen_top_pipe=pygame.image.load(r"pygames_sound_png\PIPE.png")
imagen_top_pipe= pygame.transform.scale(imagen_top_pipe,(1000000,20))
imagen_top_pipe_rect=imagen_top_pipe.get_rect()

imagen_bottom_pipe=pygame.image.load(r"pygames_sound_png\PIPE.png")
imagen_bottom_pipe= pygame.transform.scale(imagen_bottom_pipe,(1000000,20))
imagen_bottom_pipe_rect=imagen_bottom_pipe.get_rect()

imagen_middle_pipe=pygame.image.load(r"pygames_sound_png\PIPE.png")
imagen_middle_pipe= pygame.transform.scale(imagen_middle_pipe,(1500,30))
imagen_middle_pipe_rect=imagen_middle_pipe.get_rect()

imagen_oil=pygame.image.load(r"pygames_sound_png\oil_stain.png")
imagen_oil= pygame.transform.scale(imagen_oil,(90,50))
imagen_oil_rect=imagen_oil.get_rect()

imagen_menu = pygame.image.load(r"pygames_sound_png\Chevrolet_trio_2010_WTCC_Race_of_Japan_(Qualify_1).jpg")
imagen_menu = pygame.transform.scale(imagen_menu,(1300,800))
imagen_menu_rect = imagen_menu.get_rect()

imagen_wasted = pygame.image.load(r"pygames_sound_png\wasted.png")
imagen_wasted = pygame.transform.scale(imagen_wasted,(300,400))
imagen_wasted_rect = imagen_menu.get_rect()

imagen_nickname = pygame.image.load(r"pygames_sound_png\NICKNAME.png")
imagen_nickname = pygame.transform.scale(imagen_nickname,(500,200))
imagen_nickname_rect = imagen_nickname.get_rect()

pygame.display.set_caption("Racing 1.0")  

pantalla = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))





booster = 1

move_car_yellow=pygame.USEREVENT + 0
pygame.time.set_timer(move_car_yellow,10)


move_car_red=pygame.USEREVENT + 1
pygame.time.set_timer(move_car_red,15)


move_top_bush=pygame.USEREVENT + 2
pygame.time.set_timer(move_top_bush,5)

move_buttom_bush=pygame.USEREVENT + 3
pygame.time.set_timer(move_buttom_bush,5)

move_top_pipe=pygame.USEREVENT + 4
pygame.time.set_timer(move_top_pipe,5)

move_bottom_pipe=pygame.USEREVENT + 5
pygame.time.set_timer(move_bottom_pipe,5)

move_middle_pipe=pygame.USEREVENT + 6
pygame.time.set_timer(move_middle_pipe,8)

move_white_car=pygame.USEREVENT + 7
pygame.time.set_timer(move_white_car,6)

move_gold_car=pygame.USEREVENT + 8
pygame.time.set_timer(move_gold_car,6)

move_oil=pygame.USEREVENT + 9
pygame.time.set_timer(move_oil,10)

#v8_sound=pygame.mixer.Sound(r"pygames_sound_png\Mustang Drive Acceleration Sound Effect [No Copyright] (mp3cut.net).wav")

input_font=pygame.font.Font(None,50)
input_text=''
input_rect = pygame.Rect(520,400,400,50)
color = pygame.Color('BLACK')
active=False



velocidad=0.7


angulo = 0
anguloB= -20
anguloC= 20

lista_score_nickname=[]
scores=[]

lista_top_5=[]
contador_named_ranked=0

with open(r"pygames_sound_png\pygame.csv", "r") as file:
            reader = csv.reader(file)
            for elemento in reader:
                score = (elemento[1])  # Assuming the score column is named "Score"
                scores.append(int(score[6:]))
                name_ranked= elemento[0]
            lista_scores=sorted(scores,reverse=True)#para guardar todo en una lista nueva SE DEBE USAR SORTED NO sort()
            for scores in lista_scores:
                    file.seek(0)
                    for elemento in reader:
                        if str(scores) in elemento[1] and contador_named_ranked < 5:
                            record_text="{0}..........{1}".format((elemento[0][9:]),scores)
                            lista_top_5.append(record_text)
                            contador_named_ranked += 1
            ranking_1=lista_scores[0]
            file.seek(0)#para acomodar denuevo el archivo
            for elemento in reader:
                if elemento[1] == ("Score:"+ str(ranking_1)):
                    nickname_ranking_1=(elemento[0][9:])
                    
    
contador_named_ranked=0


acumulador_colisiones=5

if acumulador_colisiones > 0:
        soundtrack_file=r"pygames_sound_png\superstar.mp3"
        soundtrack=pygame.mixer.Sound(soundtrack_file)
        soundtrack.set_volume(0.4)
        soundtrack.play()

wasted_flag=False


max_caracteres=10

flag_correr = True

while flag_correr:
    
    pantalla.fill(COLOR_TURQUESA)
    
    pygame.draw.rect(pantalla,(86,150,70),(0,0,ANCHO_VENTANA,100))
    
    pygame.draw.rect(pantalla,(255,255,255),(0,240,ANCHO_VENTANA,5))#linea blanca
    
    pygame.draw.rect(pantalla,(255,255,0),(0,380,ANCHO_VENTANA,5))#linea amarilla
    pygame.draw.rect(pantalla,(255,255,0),(0,400,ANCHO_VENTANA,5))#linea amarilla
    
    pygame.draw.rect(pantalla,(255,255,255),(0,540,ANCHO_VENTANA,5))#linea blanca x2

    pygame.draw.rect(pantalla,(86,150,70),(0,700,ANCHO_VENTANA,100))

    

    
    exclamation ="!"
    
    lista_eventos=pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:#ver si esta activo o NO
            flag_correr= False
            
        
        
        if evento.type == move_car_yellow:
            if (posicion_auto2[0] > 0):
                posicion_auto2[0] = posicion_auto2[0] - 2*booster
            else:
                posicion_auto2[0] = ANCHO_VENTANA 
                posicion_auto2[1] = random.randint(140,300)
                
        
        
        if evento.type == move_car_red:
            if (posicion_auto3[0] > 0):
                posicion_auto3[0] = posicion_auto3[0] - 2*booster
            else:
                posicion_auto3[0] = ANCHO_VENTANA
                posicion_auto3[1] = random.randint(140,300)
            
        
        if evento.type == move_white_car:
            if (posicion_auto4[0] > 0):
                posicion_auto4[0] = posicion_auto4[0] - 3.3*booster
            else:
                posicion_auto4[0] = ANCHO_VENTANA
                posicion_auto4[1] = random.randint(430,610)
        
        if evento.type == move_gold_car:
            if (posicion_auto5[0] > 0):
                posicion_auto5[0] = posicion_auto5[0] - 3*booster
            else:
                posicion_auto5[0] = ANCHO_VENTANA
                posicion_auto5[1] = random.randint(430,610)

        if evento.type == move_oil:
            if (posicion_oil[0] > 0):
                posicion_oil[0] = posicion_oil[0] - 3.5*booster
            else:
                posicion_oil[0] = ANCHO_VENTANA
                posicion_oil[1] = random.randint(430,610) 

        if evento.type == move_top_bush:
            if (posicion_top_bush[0] > 0):
                posicion_top_bush[0] = posicion_top_bush[0] - 5*booster
            else:
                posicion_top_bush[0] = ANCHO_VENTANA + 200

        if evento.type == move_buttom_bush:
            if (posicion_buttom_bush[0] > 0):
                posicion_buttom_bush[0] = posicion_buttom_bush[0] - 5*booster
            else:
                posicion_buttom_bush[0] = ANCHO_VENTANA + 100
        
        if evento.type == move_top_pipe:
            if (posicion_top_pipe[0] > 0):
                posicion_top_pipe[0] = posicion_top_pipe[0] - 4*booster
            else:
                posicion_top_pipe[0] = ANCHO_VENTANA

        if evento.type == move_bottom_pipe:
            if (posicion_bottom_pipe[0] > 0):
                posicion_bottom_pipe[0] = posicion_bottom_pipe[0] - 4*booster
            else:
                posicion_bottom_pipe[0] = ANCHO_VENTANA
        if evento.type == move_middle_pipe:
            if (posicion_middle_pipe[0] > -750):#pipe width: tiene que llegar hasta - 750 la posicion, ya que 1500 es lo q mide completo y el center llega a 0 y corta y el center tendria que llegar a -750
                #posicion_middle_pipe: equivale al centro de posicion, si el centro de la pipe es mayor a -750 entonces que el frame siga comiendo pipe hasta que el centro llegue a -750
                posicion_middle_pipe[0] = posicion_middle_pipe[0] - 5*booster
            else:
                posicion_middle_pipe[0] = ANCHO_VENTANA + 2000 # aparece mas lejos entonces la transicion es mas smooth del middle pipe
        if acumulador_colisiones==0:
                                    active=True
        if evento.type == pygame.KEYDOWN:    
                                    if active == True:
                                        if evento.key == pygame.K_BACKSPACE:# el += es para que recuerde las letras anteriores
                                                input_text = input_text[:-1]
                                        elif evento.key == pygame.K_RETURN:
                                            nickname = input_text
                                            score = acumulador_text
                                            with open(r"pygames_sound_png\pygame.csv","a") as file:
                                                file.write(f"Nickname:{nickname},Score:{score}\n")
                                            flag_correr=False
                                        else:
                                            if len(input_text) < max_caracteres:
                                                input_text += evento.unicode
                                    
    




    lista_teclas = pygame.key.get_pressed()

    if True in lista_teclas:
            #SETEO LIMITES DEL MOVIMIENTO Y ESTABLEZCO CUANTO SE MUEVE EL AUTO A PARTIR DE SUMARLE UN NUMERO A MI POSICION INCIAL
            
            if lista_teclas[pygame.K_RIGHT]:
                posicion_auto[0] = posicion_auto[0] + velocidad
                if posicion_auto[0] > 500  :  # Right boundary
                    posicion_auto[0] = 500 
            if lista_teclas[pygame.K_LEFT]:
                posicion_auto[0] = posicion_auto[0] - velocidad
                if posicion_auto[0] < 0:  # Left boundary
                    posicion_auto[0] = 0
            

            if lista_teclas[pygame.K_UP]:
                posicion_auto[1] = posicion_auto[1] - velocidad
                if posicion_auto[1] < 133 :  # Top boundary
                    posicion_auto[1] = 133
                if imagen_rect.colliderect(imagen_middle_pipe_rect) and posicion_auto[1] > 391:
                        posicion_auto[1] = 435 # los numeros difieren porque cuando colisionan la posicion excede un poco el numero al estar en diagonal
                
            if lista_teclas[pygame.K_DOWN]:
                posicion_auto[1] = posicion_auto[1] + velocidad
                if posicion_auto[1] > 670 :  # Bottom boundary
                    posicion_auto[1] = 670
                if imagen_rect.colliderect(imagen_middle_pipe_rect) and posicion_auto[1] < 391:
                        posicion_auto[1] = 345     
                                
            if lista_teclas[pygame.K_ESCAPE]:
                flag_correr=False

            if lista_teclas[pygame.K_x]:
                if acumulador_colisiones == 0:
                    turbo.active=False
                else:
                    turbo.active = True
                    booster=2
                    velocidad=1
                    v8_sound_file=r"pygames_sound_png\Mustang Drive Acceleration Sound Effect [No Copyright] (mp3cut.net).wav"
                    v8_sound = pygame.mixer.Sound(v8_sound_file) 
                    v8_sound.set_volume(0.4)
                    v8_sound.play()


    score_multiplier=0
    
    if acumulador_colisiones > 0:
        if turbo.active == True:

            text=font.render("SCORE: "+ str(acumulador_text) + exclamation +"x2",True,(255,215,0)) #el true actua como antialising para smoothear los edges
            acumulador_text += 2
            text_rect=text.get_rect()
            text_rect.center=(150,50)
        else:
            text=font.render("SCORE: "+ str(acumulador_text),  True,(255,255,255))
            acumulador_text += 1
            text_rect=text.get_rect()
            text_rect.center=(150,50)
        
    vidas=font.render("VIDAS: "+ str(acumulador_colisiones) , True,(0,0,0)) #el true actua como antialising para smoothear los edges
    vidas_rect=vidas.get_rect()
    vidas_rect.center=(1090,27)

    record=font.render("HIGHEST RECORD: "+ str(ranking_1), True,(0,0,0)) #el true actua como antialising para smoothear los edges
    record_rect=record.get_rect()
    record_rect.center=(1090,50)

    record_nombre=font.render("BEST PLAYER: "+ str(nickname_ranking_1), True,(0,0,0)) #el true actua como antialising para smoothear los edges
    record_nombre_rect=record_nombre.get_rect()
    record_nombre_rect.center=(1098,73)

    imagen_rect.center = posicion_auto
    imagen2_rect.center = posicion_auto2
    imagen3_rect.center = posicion_auto3
    imagen_white_car_rect.center= posicion_auto4
    imagen_gold_car_rect.center = posicion_auto5
    imagen_top_bush_rect.center=posicion_top_bush
    imagen_buttom_bush_rect.center=posicion_buttom_bush
    imagen_bottom_pipe_rect.center=posicion_bottom_pipe
    imagen_top_pipe_rect.center=posicion_top_pipe
    imagen_middle_pipe_rect.center=posicion_middle_pipe
    imagen_oil_rect.center=posicion_oil
    
    #contiene rect object dentro del frame
    imagen_rect.clamp_ip(pantalla.get_rect())

    pantalla.blit(imagen_buttom_bush,imagen_buttom_bush_rect)
    pantalla.blit(imagen_top_bush, imagen_top_bush_rect)

    pantalla.blit(imagen_oil,imagen_oil_rect) 
    pantalla.blit(imagen2, imagen2_rect)
    pantalla.blit(imagen3, imagen3_rect)
    pantalla.blit(imagen_gold_car, imagen_gold_car_rect)
    pantalla.blit(imagen_white_car, imagen_white_car_rect)
    pantalla.blit(imagen_bottom_pipe,imagen_bottom_pipe_rect)
    pantalla.blit(imagen_top_pipe,imagen_top_pipe_rect)
    pantalla.blit(imagen_middle_pipe,imagen_middle_pipe_rect)
    
    pantalla.blit(vidas,vidas_rect)
    pantalla.blit(text,text_rect)
    pantalla.blit(record,record_rect)
    pantalla.blit(record_nombre,record_nombre_rect)

    pygame.draw.rect(pantalla,(0,0,0),(920,7,350,80),3) # ese 3 es un parametro extra para que dibuje bordes, si esta en 0 aparece un rectangulo filled, si hay valor mayor a 0 tira rect vacio con bordes
    
    #pantalla.blit(frame_0,(0,0))x
    #BLIT ORDER MATTERS, asi como el fill screen va arriba de todo el blit tiene que ser lo ultimo antes del flip, y si tengo condiciones con el blit lo pongo abajo tambien, como los siguientes IF enganchados


        
    if imagen_rect.colliderect(imagen_oil_rect) :
                oil_flag=False
                if collision_flag==False:
                    oil_file=r"pygames_sound_png\Car drifting sound effects (mp3cut.net).mp3"
                    oil=pygame.mixer.Sound(oil_file)
                    oil.set_volume(0.4)
                    oil.play()
                    oil_flag=True
                angulo += 10
                distraccion=pygame.transform.rotate(imagen,angulo)
                distraccion_rect=distraccion.get_rect()
                distraccion_rect.center=posicion_auto
                pantalla.blit(distraccion,distraccion_rect)
                turbo.active=False
                booster=1
                if posicion_auto[0] > 200:
                        posicion_auto[0]=posicion_auto[0]-1 
                
                        

                    

    elif lista_teclas[pygame.K_DOWN] and lista_teclas[pygame.K_RIGHT]: 
                        rotated_car_down = pygame.transform.rotate(imagen, anguloB)
                        rotated_car_down_rect = rotated_car_down.get_rect()
                        rotated_car_down_rect.center = posicion_auto
                        pantalla.blit(rotated_car_down, rotated_car_down_rect)
                        
                        
                        if rotated_car_down_rect.colliderect(imagen_oil_rect):
                                oil_flag=False
                                if collision_flag==False:
                                            oil_file=r"pygames_sound_png\Car drifting sound effects (mp3cut.net).mp3"
                                            oil=pygame.mixer.Sound(oil_file)
                                            oil.set_volume(0.4)
                                            oil.play()
                                            oil_flag=True
                                anguloB += 10
                                distraccion2=pygame.transform.rotate(imagen,anguloB)
                                distraccion2_rect=distraccion2.get_rect()
                                distraccion2_rect.center=posicion_auto
                                pantalla.blit(distraccion2,distraccion2_rect)
                                if posicion_auto[0] > 200:
                                    posicion_auto[0]=posicion_auto[0]-1 
                                
                        else:
                            anguloB = -20
    elif lista_teclas[pygame.K_UP] and lista_teclas[pygame.K_RIGHT]:# elif cambia todo, si lo saco me lo toma como 2 operaciones diferentes entonces para enganchanrlos tiene que estar
                    rotated_car_up = pygame.transform.rotate(imagen, anguloC)
                    rotated_car_up_rect = rotated_car_up.get_rect()
                    rotated_car_up_rect.center = posicion_auto
                    pantalla.blit(rotated_car_up, rotated_car_up_rect)
                    
                    
                    if rotated_car_up_rect.colliderect(imagen_oil_rect):
                                oil_flag=False
                                if collision_flag==False:
                                            oil_file=r"pygames_sound_png\Car drifting sound effects (mp3cut.net).mp3"
                                            oil=pygame.mixer.Sound(oil_file)
                                            oil.set_volume(0.4)
                                            oil.play()
                                            oil_flag=True
        
                                anguloC += 10
                                distraccion1=pygame.transform.rotate(imagen,anguloC)
                                distraccion1_rect=distraccion1.get_rect()
                                distraccion1_rect.center=posicion_auto
                                pantalla.blit(distraccion1,distraccion1_rect)
                    
                                if posicion_auto[0] > 200:
                                    posicion_auto[0]=posicion_auto[0]-1 
                                
                                    
                                    
                                
                                
                    else:
                        anguloC = 20

    else:
        pantalla.blit(imagen,imagen_rect)

    

    if imagen2_rect.colliderect(imagen3_rect):
        posicion_auto2[1]=posicion_auto2[1]+50
    if posicion_auto2[1]>380 :
            posicion_auto2[1]=380
    if posicion_auto3[1]>380:
            posicion_auto3[1]=380
    if imagen_white_car_rect.colliderect(imagen_gold_car_rect):
        posicion_auto4[1]=posicion_auto4[1]+40

    

    collision_flag=False
    if imagen_rect.colliderect(imagen2_rect) or imagen_rect.colliderect(imagen3_rect) or imagen_rect.colliderect(imagen_gold_car_rect) or imagen_rect.colliderect(imagen_white_car_rect):
        if collision_flag==False:
                collision_file=r"pygames_sound_png\CAR CRASH.mp3"
                collision=pygame.mixer.Sound(collision_file)
                collision.set_volume(0.4)
                collision.play()
                collision_flag=True
                
        turbo.active=False
        booster=1
        acumulador_colisiones -= 1
        posicion_auto[0]=0
    
    
    if acumulador_colisiones == 0:
            posicion_auto[1]=0
            acumulador_text += 0
            soundtrack.stop()
        
            if wasted_flag==False:
                wasted_file=r"pygames_sound_png\wasted_sound.mp3"
                wasted=pygame.mixer.Sound(wasted_file)
                wasted.set_volume(0.4)
                wasted.play()
                wasted_flag=True
            pantalla.blit(imagen_menu,imagen_menu_rect)
            pantalla.blit(imagen_wasted,(500,140))
            
            pygame.draw.rect(pantalla,(255,255,255),(490,460,300,170),3)
            
            record_nombre_rank1=font.render(str(lista_top_5[0]), True,(255,255,255)) #el true actua como antialising para smoothear los edges
            record_nombre_rank1_rect=record_nombre_rank1.get_rect()
            record_nombre_rank1_rect.center=(640,480)
            pantalla.blit(record_nombre_rank1,record_nombre_rank1_rect)
            
            record_nombre_rank2=font.render(str(lista_top_5[1]), True,(255,255,255)) #el true actua como antialising para smoothear los edges
            record_nombre_rank2_rect=record_nombre_rank2.get_rect()
            record_nombre_rank2_rect.center=(640,510)
            pantalla.blit(record_nombre_rank2,record_nombre_rank2_rect)

            record_nombre_rank3=font.render(str(lista_top_5[2]), True,(255,255,255)) #el true actua como antialising para smoothear los edges
            record_nombre_rank3_rect=record_nombre_rank3.get_rect()
            record_nombre_rank3_rect.center=(640,540)
            pantalla.blit(record_nombre_rank3,record_nombre_rank3_rect)


            record_nombre_rank4=font.render(str(lista_top_5[3]), True,(255,255,255)) #el true actua como antialising para smoothear los edges
            record_nombre_rank4_rect=record_nombre_rank4.get_rect()
            record_nombre_rank4_rect.center=(640,570)
            pantalla.blit(record_nombre_rank4,record_nombre_rank4_rect)

            record_nombre_rank5=font.render(str(lista_top_5[4]), True,(255,255,255)) #el true actua como antialising para smoothear los edges
            record_nombre_rank5_rect=record_nombre_rank5.get_rect()
            record_nombre_rank5_rect.center=(640,600)
            pantalla.blit(record_nombre_rank5,record_nombre_rank5_rect)

            pantalla.blit(imagen_nickname,(400,330))

            relleno_nickname=font.render("ENTER NICKNAME",True,(255,255,255)) #el true actua como antialising para smoothear los edges
            relleno_nickname_rect=relleno_nickname.get_rect()
            relleno_nickname_rect.center=(650,425)
            
            text_surface=input_font.render(input_text,True,(0,0,0))
            input_rect.w = text_surface.get_width()+10# +10 PAR ALARGAR BORDESporque sino el rectangulo draw lo recorta                         
            
            if len(input_text) < 1:
                pantalla.blit(relleno_nickname,relleno_nickname_rect)
            else:
                pantalla.blit(text_surface,(input_rect[0] + 25 ,input_rect[1] + 5))
            


           
            

                
        # pantalla.fill((0,0,0))
        #colision_image=pantalla.blit(colision,col_rect)
        #colision_sound.set_volume(0.4)
        #colision_sound.play()

    

    moving_sprites.draw(pantalla)
    moving_sprites.update()
    


    pygame.display.flip()#siempre al final
    
clock.tick(60)
pygame.quit()
"""
            
            if evento.key == pygame.K_RIGHT:
                posicion_circulo[0]=posicion_circulo[0] + 10
            if evento.key == pygame.K_LEFT:
                posicion_circulo[0]=posicion_circulo[0] - 10
            if evento.key == pygame.K_UP:
                posicion_circulo[1]=posicion_circulo[1] - 10
            if evento.key == pygame.K_DOWN:
                posicion_circulo[1]=posicion_circulo[1] + 10
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_circulo= list(evento.pos)
        
        if evento.type == timer_segundos:
            if (posicion_circulo[0] < ANCHO_VENTANA+RADIO):
                posicion_circulo[0] = posicion_circulo[0] + 10
            else:
                posicion_circulo[0] = 0
        """
    
    #pantalla.fill(COLOR_TURQUESA)
    #pygame.draw.rect(pantalla,COLOR_BLANCO,(posicion_rectangulo))
    #pygame.draw.circle(pantalla,COLOR_X,posicion_circulo,50)
    
    #mostrar los cambios de la pantalla
    

