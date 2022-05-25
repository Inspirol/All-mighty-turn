import commands2
from wpimath.controller import PIDController
from constants import movement_K_p, movement_K_I, movement_K_D
from subsytems.drivetrain import Drivetrain
import math

class DriveStraight(commands2.PIDCommand):
    # /**
    # * Creates a new DriveStraight.
    # */
    def __init__(self, distSetPt: float, drivetrain: Drivetrain):
        super().__init__(
            PIDController(movement_K_p, movement_K_I,
                          movement_K_D),

            drivetrain.m_left_encoder.getPosition,

            distSetPt,

            drivetrain.driveStraight,
            [drivetrain])
        self.drivetrain = drivetrain
        self.getController().setTolerance(40)
        self.drivetrain.m_left_encoder.setPosition(0)

    def initialize(self) -> None:
        self.drivetrain.m_left_encoder.setPosition(0)


    def isFinished(self):
        print(self.drivetrain.m_left_encoder.getPosition(), self.getController().getSetpoint())
        if(math.fabs(self.getController().getPositionError()) < 40):
            print("done")
        return (math.fabs(self.getController().getPositionError()) < 40)
