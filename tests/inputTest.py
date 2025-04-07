import pygame
import tkinter as tk

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

loopnum = 0

def updates():
    global loopnum
    pygame.event.pump()

    throttle = -joystick.get_axis(1)
    pitch = -joystick.get_axis(3)
    roll = joystick.get_axis(2)
    yaw = joystick.get_axis(0)

    loopnum += 1

    thrLabel.config(text=f"Throttle: {round(throttle,5)}")
    pitchLabel.config(text=f"Pitch: {round(pitch,5)}")
    rollLabel.config(text=f"Roll: {round(roll,5)}")
    yawLabel.config(text=f"Yaw: {round(yaw,5)}")
    num.config(text=loopnum)

    root.after(100, updates)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x400")
    root.title('Inputs')

    thrLabel = tk.Label(text="Throttle")
    thrLabel.pack(fill=tk.X)
    pitchLabel = tk.Label(text='Pitch')
    pitchLabel.pack(fill=tk.X)
    rollLabel = tk.Label(text='Roll')
    rollLabel.pack(fill=tk.X)
    yawLabel = tk.Label(text='Yaw')
    yawLabel.pack(fill=tk.X)
    num = tk.Label(text=loopnum)
    num.pack(fill=tk.X)

    updates()
    root.mainloop()