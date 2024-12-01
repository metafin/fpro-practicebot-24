# TestRobot Project

This project is a simple start for our practice robot, testing to see if we can control the motors and DIO ports.

## Getting Started

### Prerequisites

We need to be working in Python 10 or 11. Some of the dependencies don't work with higher versions. I chose 10. Based on
reading, 11 might work too.

### Installation

```bash
pip install pyfrc wpilib pyntcore robotpy-hal robotpy-wpimath robotpy-wpinet robotpy-wpiutil robotpy-commands-v2 robotpy-ctre robotpy-halsim-gui robotpy-installer
```

```bash
pip install phoenix6
```

Key commands

- Deploy to Rio

```bash
robotpy deploy
```

- Simulation

I'm not sure what this does exactly, but it brings up a new window with a log of data and options. I think this is some
way to test the code locally.

```bash
- robotpy sim
```

### roboRio Installation

pyproject.toml

- defines packages installed on Rio at deploy.
- Needs to include Phoenix6
- others may need to be added

robotpy-installer

- I'm not sure if this was required. The pyproject.toml might have taken care of this.
- Install the robotpy-installer tool on your computer:
  -- pip install robotpy-installer
- Use robotpy-installer to install robotpy-ctre on the RoboRIO:
  -- robotpy-installer download robotpy-ctre
  -- robotpy-installer install robotpy-ctre

