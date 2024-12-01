import wpilib
from phoenix6 import hardware, controls

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize joystick on port 0 (USB port in Driver Station)
        self.joystick = wpilib.Joystick(0)

        # Initialize TalonFX motor controllers
        self.motor6 = hardware.TalonFX(6, "rio")  # Motor 6
        self.motor5 = hardware.TalonFX(5, "rio")  # Motor 5

        # Dictionary to manage lights and their states
        # Key: Button number, Value: Tuple (DIO port, DigitalOutput object, state)
        self.lights = {
            1: {"port": 0, "output": wpilib.DigitalOutput(0), "state": False},  # Button 1 controls red light
            2: {"port": 1, "output": wpilib.DigitalOutput(1), "state": False},  # Button 2 controls green light
        }

    def teleopPeriodic(self):
        # Read the joystick axes
        left_y = -self.joystick.getRawAxis(1)  # Left joystick Y-axis
        right_x = self.joystick.getRawAxis(4)  # Right joystick X-axis

        # Scale the speed of motor 5 to 25%
        right_x_scaled = right_x * 0.25

        # Create duty cycle control signals from joystick inputs
        motor6_control = controls.DutyCycleOut(left_y)
        motor5_control = controls.DutyCycleOut(right_x_scaled)

        # Apply the controls to the respective motors
        self.motor6.set_control(motor6_control)
        self.motor5.set_control(motor5_control)

        # Iterate through each light in the dictionary
        for button, light in self.lights.items():
            # Check if the button assigned to this light is pressed
            if self.joystick.getRawButtonPressed(button):
                # Toggle the light's state
                light["state"] = not light["state"]
                light["output"].set(light["state"])

                # Optional: Print the current state for debugging
                # print(f"Light on port {light['port']} (Button {button}) state: {light['state']}")

if __name__ == "__main__":
    wpilib.run(TestRobot)
