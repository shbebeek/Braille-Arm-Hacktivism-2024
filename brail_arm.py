from rev import CANSparkMax, CANSparkMaxLowLevel
from commands2 import Subsystem
import constants
import wpilib

class DoubleJointedArmSubsystem(Subsystem):
    def __init__(self) -> None:
        super().__init__()
        self.setName(__class__.__name__)

        # Turret Motor (X-axis translation/rotation)
        self.turretMotor = CANSparkMax(
            constants.kTurretCANID, CANSparkMaxLowLevel.MotorType.kBrushless
        )
        self.turretMotor.setInverted(constants.kTurretInverted)
        self.turretPID = self.turretMotor.getPIDController()
        self.turretEncoder = self.turretMotor.getEncoder()
        self.turretPID.setP(constants.kTurretPGain)
        self.turretPID.setI(constants.kTurretIGain)
        self.turretPID.setD(constants.kTurretDGain)

        # Arm Extension Motor (Y-axis extension)
        self.armExtensionMotor = CANSparkMax(
            constants.kArmExtensionCANID, CANSparkMaxLowLevel.MotorType.kBrushless
        )
        self.armExtensionMotor.setInverted(constants.kArmExtensionInverted)
        self.armExtensionPID = self.armExtensionMotor.getPIDController()
        self.armExtensionEncoder = self.armExtensionMotor.getEncoder()
        self.armExtensionPID.setP(constants.kArmExtensionPGain)
        self.armExtensionPID.setI(constants.kArmExtensionIGain)
        self.armExtensionPID.setD(constants.kArmExtensionDGain)

        # Arm Lift Motor (Z-axis lift)
        self.armLiftMotor = CANSparkMax(
            constants.kArmLiftCANID, CANSparkMaxLowLevel.MotorType.kBrushless
        )
        self.armLiftMotor.setInverted(constants.kArmLiftInverted)
        self.armLiftPID = self.armLiftMotor.getPIDController()
        self.armLiftEncoder = self.armLiftMotor.getEncoder()
        self.armLiftPID.setP(constants.kArmLiftPGain)
        self.armLiftPID.setI(constants.kArmLiftIGain)
        self.armLiftPID.setD(constants.kArmLiftDGain)

    def periodic(self) -> None:
        # Log current positions for debugging
        wpilib.SmartDashboard.putNumber("Turret Position", self.getTurretPosition())
        wpilib.SmartDashboard.putNumber("Arm Extension", self.getArmExtension())
        wpilib.SmartDashboard.putNumber("Arm Lift", self.getArmLift())

    def setTurretPosition(self, position: float) -> None:
        if constants.kTurretMinPosition <= position <= constants.kTurretMaxPosition:
            self.turretPID.setReference(position, CANSparkMax.ControlType.kPosition)
        else:
            print("turret position out of bounds")

    def setArmExtension(self, extension: float) -> None:
        if constants.kArmMinExtension <= extension <= constants.kArmMaxExtension:
            self.armExtensionPID.setReference(
                extension, CANSparkMax.ControlType.kPosition
            )
        else:
            print("arm extension out of bounds")

    def setArmLift(self, lift: float) -> None:
        if constants.kArmMinLift <= lift <= constants.kArmMaxLift:
            self.armLiftPID.setReference(lift, CANSparkMax.ControlType.kPosition)
        else:
            print("arm lift out of bounds")

    def getTurretPosition(self) -> float:
        return self.turretEncoder.getPosition()

    def getArmExtension(self) -> float:
        return self.armExtensionEncoder.getPosition()

    def getArmLift(self) -> float:
        return self.armLiftEncoder.getPosition()

    def moveToBrailleDot(self, dot: int) -> tuple:
        if dot in constants.kBrailleDotPositions:
            x, y, z = constants.kBrailleDotPositions[dot]
            self.setTurretPosition(x)
            self.setArmExtension(y)
            self.setArmLift(z)
            return x, y, z
        else:
            print("invalid braille dot")
            return None

    def typeBrailleCharacter(self, char: str) -> None:
        if char in constants.kBrailleCharacters:
            for dot in constants.kBrailleCharacters[char]:
                pos = self.moveToBrailleDot(dot)
                if pos:
                    x, y, z = pos
                    # Simulate dot press
                    self.setArmLift(z - 1) # Press down
                    self.setArmLift(z) # Lift up
        else:
            print("invalid braille character")
