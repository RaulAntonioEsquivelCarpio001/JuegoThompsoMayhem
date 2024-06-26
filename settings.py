class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (247, 220, 111)
        self.fps = 60
        self.player_speed = 2
        self.player_size = (50, 50)

        # Configuración de las balas
        self.bullet_speed = 5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 5

        # Configuración de los enemigos
        self.enemy_size = (50, 50)
        self.enemy_speed_x = 3  # Velocidad horizontal de los enemigos
        self.enemy_speed_y = 3  # Velocidad vertical de los enemigos

        
