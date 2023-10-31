import pygame

# Initialize pygame library
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check the number of connected joysticks
joystick_count = pygame.joystick.get_count()
print("Number of joysticks:", joystick_count)

# If there is a joystick, then initialize
if joystick_count > 0:
    # Index of joystick, 0 will be the first one
    joystick_id = 0
    # Creating a joystick object so it can be interacted with
    joystick = pygame.joystick.Joystick(joystick_id)
    # Initialize the joystick
    joystick.init()

# Test for when button is pressed on joystick
while True: 
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            button = event.button
            print(f"Button {button} pressed")
        
        if event.type == pygame.JOYBUTTONUP:
            button = event.button
            print(f"Button {button} pressed")

        if event.type == pygame.JOYAXISMOTION:
            axis = event.axis
            value = event.value
            print(f"Axis {axis} moved to {value : .2f}")

        if event.type == pygame.JOYHATMOTION:
            hat = event.hat
            value = event.value
            print(f"Hat {hat} move to {value}")

# Reading the joystick input
x_axis = joystick.get_axis(0)
button_O = joystick.get_button(0)
hat_position = joystick.get_hat(0)
        