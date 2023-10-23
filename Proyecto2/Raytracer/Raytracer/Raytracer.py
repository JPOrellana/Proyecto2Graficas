import pygame
from pygame.locals import *
from rt import Raytracer
from figures     import *
from lights import *
from materials import *

width = 1000
height = 440

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

raytracer = Raytracer(screen)

raytracer.environmentMap = pygame.image.load("Fondo/bicho2.jpg")

raytracer.rtClearColor(0.25, 0.25, 0.25)

# Crear Texturas

TexturaOro  = pygame.image.load("Texturas/oro.jpg")
TexturaOrito  = pygame.image.load("Texturas/orito.jpg")
TexturaBronce  = pygame.image.load("Texturas/bronce.jpg")
TexturaPlata  = pygame.image.load("Texturas/plata.jpg")
TexturaMarmol  = pygame.image.load("Texturas/marmol.jpg")

marmolin = Material(spec = 64, Ks = 0.2, matType = REFLECTIVE, texture = TexturaMarmol)

# Crear Materiales

oro = Material(spec = 64, Ks = 0.2, texture = TexturaOro)
orito = Material(spec = 64, Ks = 0.2, texture = TexturaOrito)
bronce = Material(spec = 64, Ks = 0.2, texture = TexturaBronce)
plata = Material(spec = 64, Ks = 0.2, texture = TexturaPlata)
marmol = Material(spec = 64, Ks = 0.2, texture = TexturaMarmol)



# Crear Figuras

raytracer.scene.append(Sphere(position = [-4.5,   -0.5, -5], radius = 0.5, material = oro))
raytracer.scene.append(Sphere(position = [-2.3, -0.5, -5], radius = 0.5, material = oro))
raytracer.scene.append(Sphere(position = [-0.1,  -0.5, -5], radius = 0.5, material = oro))
raytracer.scene.append(Sphere(position = [2.1,  -0.5, -5], radius = 0.5, material = oro))
raytracer.scene.append(Sphere(position = [4.3,  -0.5, -5], radius = 0.5, material = oro))


raytracer.scene.append(Triangle(v0=[-5.5, -1.5, -5], v1=[ -3.5, -1.5, -5],  v2=[ -4.5,  -1 , -5], material = bronce))
raytracer.scene.append(Triangle(v0=[-3.3, -1.5, -5], v1=[ -1.3, -1.5, -5],  v2=[ -2.3,  -1 , -5], material = plata))
raytracer.scene.append(Triangle(v0=[-1.1, -1.5, -5], v1=[ 0.9,  -1.5, -5],  v2=[ -0.1,  -1 , -5], material = orito))
raytracer.scene.append(Triangle(v0=[1.1,  -1.5, -5], v1=[ 3.1,  -1.5, -5],  v2=[ 2.1,   -1 , -5], material = plata))
raytracer.scene.append(Triangle(v0=[3.3,  -1.5, -5], v1=[ 5.3,  -1.5, -5],  v2=[ 4.3,   -1 , -5], material = bronce))

raytracer.scene.append(Rectangle(v0 = [-5.7, -1.5, -5], v1 = [-5.7, -4, -5],  v2 = [5.5, -1.5, -5], v3 = [5.5, -4, -5], material = marmol))

# Luces
raytracer.lights.append(AmbientLight(intensity=0.9))


raytracer.rtClear()
raytracer.rtRender()

print("\n Render Time: ", pygame.time.get_ticks() / 1000, "secs")

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_ESCAPE:
                isRunning = False


rect = pygame.Rect(0, 0, width, height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "output.jpg")

pygame.quit()