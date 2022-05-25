import commands2
from wpimath.controller import PIDController
from constants import turn_K_p, turn_K_I, turn_K_D
from subsytems.drivetrain import Drivetrain

class turn(commands2.PIDCommand):
    # /**
    # * Creates a new turn.
    # */
    def __init__(self, RotSetDeg: float, drivetrain: Drivetrain):
        
        #drivetrain.gyro.setYaw(0)
        super().__init__(
            PIDController(turn_K_p, turn_K_I,
                          turn_K_D),

            #drivetrain.m_left_encoder.getPosition,
            drivetrain.gyro.getYaw,
            RotSetDeg,

            drivetrain.turn,
            [drivetrain])
        self.getController().setTolerance(10)
        self.drivetrain = drivetrain
    
    def initialize(self) -> None:
        self.drivetrain.gyro.setYaw(0)

    def isFinished(self):
        print(self.drivetrain.gyro.getYaw(), self.getController().getSetpoint())
        return self.getController().getPositionError() < 3
    
    def end(self, interrupted: bool) -> None:
        print("Turn done.")
        