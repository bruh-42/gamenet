def on_button_pressed_a():
    sprite.change(LedSpriteProperty.X, 1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, 1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, 1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global sprite
    sprite = game.create_sprite(2, 2)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, 1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    sprite.change(LedSpriteProperty.X, -1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, -1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, -1)
    basic.pause(500)
    sprite.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.B, on_button_pressed_b)

sprite: game.LedSprite = None
music.play_melody("C5 A E G C E B G ", 57776757523232332)