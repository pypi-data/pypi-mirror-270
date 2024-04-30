from pynput.mouse import Controller
import time


def main():
    eps = 1e-16
    mouse = Controller()
    while True:
        mouse.move(eps, 0)
        mouse.move(-eps, 0)
        time.sleep(280)


if __name__ == "__main__":
    main()
