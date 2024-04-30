from pynput.mouse import Controller
import time


def main():
    mouse = Controller()
    while True:
        mouse.move(1, -1)
        time.sleep(1)
        mouse.move(-1, 1)
        time.sleep(280)


if __name__ == "__main__":
    main()
