import wpilib
import phoenix5

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

        self.motor = phoenix5.TalonSRX(6)  # Replace with your motor controller class if different
        self.motor.setNeutralMode(phoenix5.NeutralMode.Brake)  # Set motor to brake when not running (optional)

    def teleopPeriodic(self):
        # Iterate through each light in the dictionary
        for button, light in self.lights.items():
            # Check if the button assigned to this light is pressed
            if self.joystick.getRawButtonPressed(button):
                # Toggle the light's state
                light["state"] = not light["state"]
                light["output"].set(light["state"])

                # Optional: Print the current state for debugging
                # print(f"Light on port {light['port']} (Button {button}) state: {light['state']}")

        if self.joystick.getRawButton(4):  # Button 4 runs the motor
            self.motor.set(phoenix5.ControlMode.PercentOutput, 0.5)  # Run motor at 50% power
        else:
            self.motor.set(phoenix5.ControlMode.PercentOutput, 0.0)  # Stop the motor


if __name__ == "__main__":
    wpilib.run(TestRobot)
