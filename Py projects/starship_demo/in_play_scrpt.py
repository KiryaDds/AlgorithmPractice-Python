# It doesn't work

# 4 https://py2.codeskulptor.org/#user49_mGGZXIB87eICKJ4.py

# program template for Spaceship
 from tkinter import *
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

angular_velocity = 2 * math.pi / 60
friction = 0.03


class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
# soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")

menu_soundtrack = simplegui.load_sound('https://www.dropbox.com/s/18qdm3say9sm85e/menu_soundtrack.mp3?dl=1')
menu_soundtrack.set_volume(.5)
soundtracks_list = [
    simplegui.load_sound('https://www.dropbox.com/s/k61pt3rg8bapo97/hard_sound.mp3?dl=1'),
    simplegui.load_sound('https://www.dropbox.com/s/gt0bzmuyit97vp2/kosmos_sound.mp3?dl=1'),
    simplegui.load_sound('https://www.dropbox.com/s/gxs8x4vgcfu48ps/Nostalgicnotmelody_sound.mp3?dl=1'),
    simplegui.load_sound('https://www.dropbox.com/s/88f037dhttngbgr/travelnotmelody_sound.mp3?dl=1'),
    simplegui.load_sound('https://www.dropbox.com/s/9vvvcrj6qcr6fza/funnynotmelodyloop_sound.mp3?dl=1')
]
# my own soundtracks should be here

missile_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")


# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
# soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.thrust:
            self.image_center[0] = 135
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
            self.image_center[0] = 45
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        global WIDTH, HEIGHT, friction
        size = [WIDTH, HEIGHT]

        self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)

        for v in range(2):
            self.pos[v] = (self.pos[v] + self.vel[v]) % size[v]
            if self.thrust:
                self.vel[v] += forward[v] * (.4 - friction)
            self.vel[v] *= (1 - friction)

    def shoot(self):
        global missle_group
        forward = angle_to_vector(self.angle)
        missle_group.add(Sprite(
            [self.pos[0] + forward[0] * self.image_size[0] / 2, self.pos[1] + forward[1] * self.image_size[1] / 2], \
            [self.vel[0] + 10 * forward[0], self.vel[1] + 10 * forward[1]], \
            self.angle, -self.angle_vel, missile_image, missile_info, missile_sound))

    def thursters_switch(self, sw):
        if sw:
            self.thrust = True
        else:
            self.thrust = False

    def key_down(self, key):
        possible_keys = {'up': True,
                         'left': -angular_velocity,
                         'right': angular_velocity,
                         'space': 'shoot'}
        for k in possible_keys.keys():
            if key == simplegui.KEY_MAP[k] and \
                    not (key == simplegui.KEY_MAP['left'] and \
                         key == simplegui.KEY_MAP['right']):
                if isinstance(possible_keys[k], bool):
                    self.thrust = possible_keys[k]
                elif isinstance(possible_keys[k], str):
                    global my_ship;
                    my_ship.shoot()
                else:
                    self.angle_vel += possible_keys[k]

        if self.thrust: ship_thrust_sound.play()

    def key_up(self, key):
        possible_keys = {'up': False,
                         'left': 0,
                         'right': 0}
        for k in possible_keys.keys():
            if key == simplegui.KEY_MAP[k] and \
                    not (key == simplegui.KEY_MAP['left'] and \
                         key == simplegui.KEY_MAP['right']):
                if isinstance(possible_keys[k], bool):
                    self.thrust = possible_keys[k]
                else:
                    self.angle_vel = possible_keys[k]

        if not (self.thrust): ship_thrust_sound.rewind()


# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self, canvas):
        global explosion
        if self.animated:
            canvas.draw_image(explosion_image,
                              [explosion_info.get_center()[0] + self.age * explosion_info.get_size()[0],
                               explosion_info.get_center()[1]],
                              explosion_info.get_size(), self.pos, explosion_info.get_size())
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        global WIDTH, HEIGHT
        size = [WIDTH, HEIGHT]
        self.angle += self.angle_vel
        for i in range(2):
            self.pos[i] = (self.pos[i] + self.vel[i]) % size[i]

        self.age += 1
        return True if self.age >= self.lifespan else False

    def get_position(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def collide(self, other):
        d = dist(self.get_position(), other.get_position())
        return True if d <= self.get_radius() + other.get_radius() else False


def process_sprite_group(sp_set, canvas):
    fin_sp_set = set(sp_set)
    for s in fin_sp_set:
        if s.update():
            sp_set.remove(s)
        else:
            s.draw(canvas)


def group_collide(group, obj):
    fin_group = set(group)
    f = True
    for i in fin_group:
        if i.collide(obj):
            explosion = Sprite(obj.get_position(), [0, 0], 0, 0, explosion_image, explosion_info, sound=explosion_sound)
            explosion_group.add(explosion)
            group.remove(i)
            f = False
            return True
    if f:
        return False


def group_group_collide(group, other_group):
    fin_group = set(group)
    amount = 0
    for i in fin_group:
        if group_collide(other_group, i):
            group.discard(i)
            amount += 1
    return amount


def draw(canvas):
    global time, started, sf

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    if started:
        global lives, score
        global rock_group, missle_group
        global sound_toplay

        if lives == 0:
            sound_toplay.pause();
            sound_toplay.rewind()
            menu_soundtrack.rewind();
            menu_soundtrack.play()
            started = False
            my_ship.pos = [WIDTH / 2, HEIGHT / 2]
            my_ship.vel = [0, 0]
            my_ship.angle = -math.pi / 2
            rock_group = set()
            missle_group = set()
            score = 0
            lives = 3

        # draw and update ship and sprites
        my_ship.draw(canvas);
        my_ship.update()
        process_sprite_group(rock_group, canvas)
        process_sprite_group(missle_group, canvas)
        process_sprite_group(explosion_group, canvas)

        if group_collide(rock_group, my_ship): lives -= 1

        score += group_group_collide(rock_group, missle_group)

        # updates text
        canvas.draw_text("Lives: " + str(lives), (WIDTH / 20, HEIGHT / 10), 30, 'White', 'monospace')
        canvas.draw_text("Score: " + str(score), (WIDTH * 8 / 10, HEIGHT / 10), 25, 'White', 'monospace')

    # draw splash screen if not started
    else:
        canvas.draw_image(splash_image, splash_info.get_center(),
                          splash_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                          splash_info.get_size())


# mouseclick handlers that reset UI and conditions whether splash image is drawn
def click(pos):
    global started, soundtracks_list, sound_toplay
    center = [WIDTH / 2, HEIGHT / 2]
    size = splash_info.get_size()
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)
    if (not started) and inwidth and inheight:
        started = True
        sound_toplay = random.choice(soundtracks_list)
        menu_soundtrack.pause();
        sound_toplay.set_volume(0.7)
        sound_toplay.play()


# timer handler that spawns a rock
def rock_spawner():
    allowed_num = 12 - len(rock_group)
    for i in range(allowed_num):
        rock_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
        rock_vel = [random.random() * .6 - .3, random.random() * .6 - .3]
        rock_avel = random.random() * .2 - .1
        rock = Sprite(rock_pos, rock_vel, 0, rock_avel, asteroid_image, asteroid_info)
        if not (rock.collide(my_ship)) and started and dist(my_ship.get_position(), rock.get_position()) > 2 * (
                my_ship.get_radius() + rock.get_radius()):
            rock_group.add(rock)


# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], -math.pi / 2, ship_image, ship_info)
# a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, -0.5], 0, 0.1, asteroid_image, asteroid_info)
rock_group = set([])
# a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)
missle_group = set([])

explosion_group = set([])

menu_soundtrack.rewind();
menu_soundtrack.play()
# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(my_ship.key_down)
frame.set_keyup_handler(my_ship.key_up)
frame.set_mouseclick_handler(click)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
