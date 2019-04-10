from pynput.mouse import Button, Controller
from time import sleep


mouse = Controller()


def click_points():
    print("Waiting 5 secs")
    sleep(5)
    # Defining clicink points
    position1 = (636, 497)
    position2 = (638, 531)
    position3 = (650, 583)

    print("Click first button")
    mouse.position = position1
    mouse.click(Button.left)
    print("Waiting 1.5 secs")
    sleep(1.5)

    print("Click second button")
    mouse.position = position2
    mouse.click(Button.left)
    print("Waiting 1.5 secs")
    sleep(1.5)

    print("Click last button")
    mouse.position = position3
    mouse.click(Button.left)
    print("Waiting 1.5 secs")
    sleep(1.5)


def reading_mouse_position():
    while True:
        print("Current positions is: {0}".format(mouse.position))
        sleep(0.5)


# click_points()
# reading_mouse_position()
