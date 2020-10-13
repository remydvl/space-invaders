import pygame

MAX_LEVEL = 2

# --------- PLAYER -----------

PLAYER_IMAGES_LEVEL = [
    pygame.image.load("./assets/images/level-1/vaisseau.png"),
    pygame.image.load("./assets/images/level-2/vaisseau.png"),
]

PLAYER_SHOOT_IMAGES_LEVEL = [
    pygame.image.load("./assets/images/level-1/shoot.png"),
    pygame.image.load("./assets/images/level-2/vaisseauShoot.png")
]

PLAYER_SHOOT_DESTROY_IMAGES_LEVEL = [
    pygame.image.load("./assets/images/level-1/explosion.png"),
    pygame.image.load("./assets/images/level-2/vaisseauExplosion.png"),
]

# --------- ALIENS -----------

# Pour chaque niveaux supplementaire, un alien supplementaire doit etre ajouté
ALIENS_IMAGES_LEVEL = [
    {
        "1_0": pygame.image.load("./assets/images/level-1/alien_1_0.png"),
        "1_1": pygame.image.load("./assets/images/level-1/alien_1_1.png"),
        "2_0": pygame.image.load("./assets/images/level-1/alien_2_0.png"),
        "2_1": pygame.image.load("./assets/images/level-1/alien_2_1.png")
    },
    {
        "1_0": pygame.image.load("./assets/images/level-2/alien_1_0.png"),
        "1_1": pygame.image.load("./assets/images/level-2/alien_1_1.png"),
        "2_0": pygame.image.load("./assets/images/level-2/alien_2_0.png"),
        "2_1": pygame.image.load("./assets/images/level-2/alien_2_1.png"),
        "3_0": pygame.image.load("./assets/images/level-2/alien_3_0.png"),
        "3_1": pygame.image.load("./assets/images/level-2/alien_3_1.png")
    }
]

ALINE_SHOOT_IMAGES_LEVEL = [
    [
        pygame.image.load("./assets/images/level-1/shootAlien.png"),
        pygame.image.load("./assets/images/level-1/shootAlien.png"),
    ],
    [
        pygame.image.load("./assets/images/level-2/enemyShoot_1.png"),
        pygame.image.load("./assets/images/level-2/enemyShoot_2.png"),
        pygame.image.load("./assets/images/level-2/enemyShoot_3.png"),
    ]
]

ALIEN_SHOOT_DESTROY_IMAGES_LEVEL = [
    [
        pygame.image.load("./assets/images/level-1/explosion.png"),
        pygame.image.load("./assets/images/level-1/explosion.png"),
    ],
    [
        pygame.image.load("./assets/images/level-2/explosion_1.png"),
        pygame.image.load("./assets/images/level-2/explosion_2.png"),
        pygame.image.load("./assets/images/level-2/explosion_3.png")
    ]
]

# --------- LEVEL -----------

BACKGROUND_IMAGES_LEVEL = [
    None,
    pygame.image.load("./assets/images/level-2/fond.png")
]

LIFE_IMAGES_LEVEL = [
    pygame.image.load("./assets/images/level-1/coeur.png"),
    pygame.image.load("./assets/images/level-2/coeur.png")
]
