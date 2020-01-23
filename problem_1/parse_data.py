from math import pi as PI


def parse_requested_data_and_get_result(data):
    Pipe_Outside_Diameter = float(*data[3][1:2])
    Pipe_Wall_Thickness = float(*data[4][1:2])
    Pipe_Density = float(*data[5][1:2])
    # Corrosion_Allowance_inch = float(*data[6][1:2])

    Coating_No, Description, Thickness_in, Density = list(data[9])[:4]
    print(Density)

    Air = float(*data[13][2:3])
    Water = float(*data[14][2:3])
    # Sea_Water = float(*data[15][2:3])

    r1 = round((Pipe_Outside_Diameter - 2 * Pipe_Wall_Thickness) / 2, 2)
    r2 = round(Pipe_Outside_Diameter / 2, 4)
    r3 = round(r2 + Thickness_in, 4)
    total = round(r3 * 2, 2)
    data = {
        "r1": r1,
        "r2": r2,
        "r3": r3,
        "total": total
    }
    total_weight = round((PI * (r2 ** 2 - r1 ** 2) / 144 * Pipe_Density + PI * (r3 ** 2 - r2 ** 2) / 144 * Density), 2)
    unit_length = round(PI * (r2 ** 2) / 144 * Water, 2)
    data2 = {
        "pipe_wieght": round(PI * (r2 ** 2 - r1 ** 2) / 144 * Pipe_Density, 2),
        "coating_weight": round(PI * (r3 ** 2 - r2 ** 2) / 144 * Density, 2),
        "contents_weight": PI * r1 ** 2 / 144 * Air,
        "total_weight": total_weight,
        "unit_length": unit_length
    }

    submerged_weight = round((total_weight - unit_length), 2)
    submerged_specific = round(total_weight / unit_length, 2)
    data3 = {
        "submerged_weight": submerged_weight,
        "submerged_specific": submerged_specific,
    }
    return data, data2, data3
