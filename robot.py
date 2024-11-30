import wpilib
from phoenix6 import hardware, controls

class TestRobot(wpilib.TimedRobot):
    def robotInit(self):
        # Initialize joystick on port 0 (USB port in Driver Station)
        self.joystick = wpilib.Joystick(0)

        self.motor = hardware.TalonFX(6, "rio")

    def teleopPeriodic(self):
        # Create a duty cycle control object
        control_signal = controls.DutyCycleOut(0.5)
        # Apply the control to the motor
        self.motor.set_control(control_signal)



if __name__ == "__main__":
    wpilib.run(TestRobot)

