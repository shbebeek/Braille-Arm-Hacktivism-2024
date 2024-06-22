# Motor controller CAN IDs
kTurretCANID = 1
kArmExtensionCANID = 2
kArmLiftCANID = 3

# Motor controller names if need simulator
kTurretName = "Turret Motor"
kArmExtensionName = "Arm Extension Motor"
kArmLiftName = "Arm Lift Motor"

# PID Gains
kTurretPGain = 0.1
kTurretIGain = 0.0
kTurretDGain = 0.0

kArmExtensionPGain = 0.1
kArmExtensionIGain = 0.0
kArmExtensionDGain = 0.0

kArmLiftPGain = 0.1
kArmLiftIGain = 0.0
kArmLiftDGain = 0.0

# Motor Inversions
kTurretInverted = False
kArmExtensionInverted = False
kArmLiftInverted = False

# Positions/speeds (metrics are in degrees and centimeters)
kTurretMaxPosition = 180
kTurretMinPosition = -180

kArmMaxExtension = 100
kArmMinExtension = 0

kArmMaxLift = 100
kArmMinLift = 0

# Braille positions
kBrailleDotPositions = {
    1: (0, 0, 1),  # Dot 1
    2: (0, 1, 1),  # Dot 2
    3: (0, 2, 1),  # Dot 3
    4: (1, 0, 1),  # Dot 4
    5: (1, 1, 1),  # Dot 5
    6: (1, 2, 1),  # Dot 6
}

# Braille character mapping
kBrailleCharacters = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6]
}