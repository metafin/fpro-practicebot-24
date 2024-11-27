import wpilib

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize joystick on port 0 (USB port in Driver Station)
        self.joystick = wpilib.Joystick(0)

        # Dictionary to manage lights and their states
        # Key: Button number, Value: Tuple (DIO port, DigitalOutput object, state)
        self.lights = {
            1: {"port": 0, "output": wpilib.DigitalOutput(0), "state": False},  # Button 1 controls red light
            2: {"port": 1, "output": wpilib.DigitalOutput(1), "state": False},  # Button 2 controls green light
            3: {"port": 2, "output": wpilib.DigitalOutput(2), "state": False},  # Button 3 controls blue light
        }

    def teleopPeriodic(self):
        # Iterate through each light in the dictionary
        for button, light in self.lights.items():
            # Check if the button assigned to this light is pressed
            if self.joystick.getRawButtonPressed(button):
                # Toggle the light's state
                light["state"] = not light["state"]
                light["output"].set(light["state"])

                # Optional: Print the current state for debugging
                print(f"Light on port {light['port']} (Button {button}) state: {light['state']}")

if __name__ == "__main__":
    wpilib.run(TestRobot)
