import wpilib
from phoenix6 import hardware, controls

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize joystick on port 0 (USB port in Driver Station)
        self.joystick = wpilib.Joystick(0)

        # Initialize TalonFX motor controllers
        self.motor6 = hardware.TalonFX(6, "rio")  # Motor 6
        self.motor5 = hardware.TalonFX(5, "rio")  # Motor 5

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

if __name__ == "__main__":
    wpilib.run(TestRobot)
