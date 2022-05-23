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
                          turn_K_p),

            #drivetrain.m_left_encoder.getPosition,
            drivetrain.gyro.getYaw,
            RotSetDeg,

            drivetrain.turn,
            [drivetrain])
        self.getController().setTolerance(10)
        self.drivetrain = drivetrain
    def isFinished(self):
        print("Heelo Wooorld")
        print(self.drivetrain.gyro.getYaw())
        if(self.getController().atSetpoint()):
            print("Hi. This Turn is finished.")
        return self.getController().atSetpoint();
        