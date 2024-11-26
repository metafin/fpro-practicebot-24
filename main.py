import wpilib
import time

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize a digital output on port 0
        self.led = wpilib.DigitalOutput(0)

    def robotPeriodic(self):
        # Blink the LED on and off
        current_time = time.time()
        # Blink every 0.5 seconds
        self.led.set(int(current_time * 2) % 2)

if __name__ == "__main__":
    wpilib.run(TestRobot)