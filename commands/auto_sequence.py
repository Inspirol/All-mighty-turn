import imp
import commands2
from commands.turn import turn
from commands.drivestraight import DriveStraight
from subsytems.drivetrain import Drivetrain
import math


class AutoSequence(commands2.SequentialCommandGroup):
    def __init__(self, drivetrain:Drivetrain):
        super().__init__(
            DriveStraight(5 * 12 / (4 * math.pi) * 360, drivetrain),
            turn(180, drivetrain),
            DriveStraight(5 * 12 / (4 * math.pi) * 360, drivetrain),
            turn(180, drivetrain)
        )