# Constants (extra requirement ⭐)
EARTH_ACCELERATION_OF_GRAVITY = 9.80665
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    return tower_height + (3 * tank_height / 4)


def pressure_gain_from_water_height(height):
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


def pressure_loss_from_pipe(d, L, f, v):
    return (-f * L * WATER_DENSITY * v**2) / (2000 * d)


def pressure_loss_from_fittings(v, n):
    return (-0.04 * WATER_DENSITY * v**2 * n) / 2000


def reynolds_number(d, v):
    return (WATER_DENSITY * d * v) / WATER_DYNAMIC_VISCOSITY


def pressure_loss_from_pipe_reduction(D, v, R, d):
    k = (0.1 + (50 / R)) * ((D / d)**4 - 1)
    return (-k * WATER_DENSITY * v**2) / 2000


# EXTRA ⭐ convertir kPa a psi
def kpa_to_psi(kpa):
    return kpa * 0.145038


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    pipe_length = float(input("Length of supply pipe from tank to lot (meters): "))
    fittings = int(input("Number of 90° angles in supply pipe: "))
    house_pipe_length = float(input("Length of pipe from supply to house (meters): "))

    diameter = 0.28687
    house_diameter = 0.048692
    friction = 0.013
    velocity = 1.65

    height = water_column_height(tower_height, tank_height)

    pressure = pressure_gain_from_water_height(height)

    pressure += pressure_loss_from_pipe(diameter, pipe_length, friction, velocity)
    pressure += pressure_loss_from_fittings(velocity, fittings)

    reynolds = reynolds_number(diameter, velocity)

    pressure += pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, house_diameter)
    pressure += pressure_loss_from_pipe(house_diameter, house_pipe_length, friction, velocity)

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()