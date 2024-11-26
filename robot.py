import wpilib

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize a digital output on port 0
        self.led = wpilib.DigitalOutput(0)
        # Initialize joystick on port 0 (USB port in Driver Station)
        self.joystick = wpilib.Joystick(0)
        # Track the LED state
        self.led_state = False

    def teleopPeriodic(self):
        # Check if "A" button (button 1 on most joysticks) is pressed
        if self.joystick.getRawButtonPressed(1):  # Button 1 corresponds to "A" on many joysticks
            # Toggle the LED state
            self.led_state = not self.led_state
            self.led.set(self.led_state)

        # Optional: Print the current LED state for debugging
        print(f"LED state: {self.led_state}")

if __name__ == "__main__":
    wpilib.run(TestRobot)
