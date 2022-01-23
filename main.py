import pygame as pg
from wargame import *

frame = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 2, 2, 0, 0],
                  [0, 0, 0, 1, 0, 0, 2, 0, 0],
                  [0, 0, 1, 0, 0, 2, 2, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0]])

cells = np.ndarray((9, 9, 3))

color_dict = {
    0: (255, 255, 255),
    1: (200, 0, 0),
    2: (0, 0, 200)
}

# défini la taille de l'ecran par rapport au nombre de case dans la frame
cellsize = 30
WIDTH = cells.shape[0] * cellsize
HEIGHT = cells.shape[1] * cellsize

# initialise pygame, defini la taille de l'écran, le titre du jeu
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("War Game")
clock = pg.time.Clock()

# game loop
running = True
while running:
    # défini le temps entre le changement de frame
    clock.tick(2)

    # attribue la valeur FALSE à running
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # copie frame dans cells avec les valeurs RGB correspondantes
    for i in range(cells.shape[0]):
        for j in range(cells.shape[1]):
            cells[i][j] = color_dict[frame[(j, i)]]

    # crée une surface à la taille de cells
    surf = pg.Surface((cells.shape[0], cells.shape[1]))
    # dessine cells sur la surface
    pg.surfarray.blit_array(surf, cells)
    # modifie la taille de la surface
    surf = pg.transform.scale(surf, (WIDTH, HEIGHT))

    # affiche surf sur l'ecran
    screen.blit(surf, (0, 0))

    pg.display.update()

    # calcul l'évolution de la frame
    frame = compute_next_frame(frame)

pg.quit()
