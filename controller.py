import pygame as pg

import core.client as client
import core.joystick as joystick



window = pg.display.set_mode((500, 800))
clock = pg.time.Clock()

connection = client.Client()
connection.connect()

j1 = joystick.Joystick((200, 200))
j2 = joystick.Joystick((200, 600))

sendCooldown = 30

running = True
while running:
	window.fill((0, 0, 0))

	for event in pg.event.get():
		match event.type:
			case pg.QUIT: running = False

	sendCooldown -= 1
	if sendCooldown < 0 :
		sendCooldown = 30

	j1.render(window)
	j2.render(window)

	clock.tick(60)
	pg.display.flip()

connection.disconnect()