 
import os

frequency = 1000 # Hertz
duration  = 2000 # milliseconds
class sound:
    def playWorkSound():
        if os.name == "nt":
            import winsound
            winsound.Beep(frequency, duration)
        else:
            os.system('say "Break Time"')
            os.system('say "back to work"')

    def playBreakSound():
        if os.name == "nt":
            import winsound 

            oneDBHigher = 300
            winsound.Beep(frequency+oneDBHigher, duration)

        else:
            os.system('say "break time"')
            os.system('say "back to work"')


if __name__ == "__main__":
    sound.playWorkSound()
    sound.playBreakSound()