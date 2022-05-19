import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain

class Turn(commands2.PIDCommand):
    # /**
    # * Creates a new turn.
    # */
    def __init__(self, RotSetDeg: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(turn_K_p, turn_K_I,
                          turn_K_D),

            #drivetrain.m_left_encoder.getPosition,
            drivetrain.gyro,
            RotSetDeg,

            drivetrain.turn,
            [drivetrain])

    def isFinished(self):
        return self.getController().atSetpoint();
