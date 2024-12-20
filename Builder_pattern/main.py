from concrete_builders import GamingPCBuilder, OfficePCBuilder
from director import Director

if __name__ == '__main__':
    gaming_pc_builder = GamingPCBuilder()
    director = Director()

    # Building a gaming pc
    director.make_pc(gaming_pc_builder)

    gaming_pc = gaming_pc_builder.get_pc()
    print(gaming_pc)

    office_pc_builder = OfficePCBuilder()

    # Building an office pc
    director.make_pc(office_pc_builder)

    office_pc = office_pc_builder.get_pc()
    print(office_pc)

    # Building a custom gaming pc
    director.make_custom_pc(
        gaming_pc_builder,
        'Intel Core i9-13900K',
        'NVIDIA GeForce RTX 4070',
        'Corsair Vengeance DDR5 32GB',
        'Samsung 980 Pro 2TB SSD',
        'ASUS ROG Maximus Z790 Hero',
        'Lian Li PC-O11 Dynamic',
        'Corsair RM1000x (1000W)'
    )
    custom_gaming_pc = gaming_pc_builder.get_pc()
    print(custom_gaming_pc)



