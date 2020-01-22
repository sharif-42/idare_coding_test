def parse_requested_data_and_get_result(data):
    Pipe_Outside_Diameter_value_inch = float(*data[3][1:2])
    Pipe_Wall_Thickness_inch = float(*data[4][1:2])
    Pipe_Density_feet = float(*data[5][1:2])
    Corrosion_Allowance_inch = float(*data[6][1:2])

    print(Pipe_Outside_Diameter_value_inch, Pipe_Wall_Thickness_inch, Pipe_Density_feet, Corrosion_Allowance_inch)
    Coating_No, Description, Thickness_in, Density = list(data[9])[:4]

    print("Coating_No, Description, Thickness_in, Density", Coating_No, Description, Thickness_in, Density)

    Air = float(*data[13][2:3])
    Water = float(*data[14][2:3])
    Sea_Water = float(*data[15][2:3])
    print(Air,Water,Sea_Water)

