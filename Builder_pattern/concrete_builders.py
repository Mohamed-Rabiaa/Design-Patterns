# concrete builders
from pc_builder import PCBuilder
from pc import PC

class GamingPCBuilder(PCBuilder):
    def __init__(self):
        self.pc = None
        self.reset()

    def reset(self):
        self.pc = PC()     

    def set_cpu(self, cpu='Ryzen 7 9800X3D'):
        self.pc.cpu = cpu

    def set_gpu(self, gpu='Nvidia GeForce RTX 4090'):
        self.pc.gpu = gpu

    def set_ram(self, ram='G.Skill Trident Z5 Neo RGB DDR5-6000 (2 x 16GB)'):
        self.pc.ram = ram

    def set_storage(self, storage='Samsung 990 Pro 1tb'):
        self.pc.storage = storage

    def set_motherboard(self, motherboard='Gigabyte X670 AORUS ELITE AX'):
        self.pc.motherboard = motherboard
    
    def set_case(self, case='Fractal Design North'):
        self.pc.case = case

    def set_psu(self, psu='Corsair SF1000 (2024) CP-9020257'):
        self.pc.psu = psu

    def get_pc(self):
        pc = self.pc
        return pc

class OfficePCBuilder(PCBuilder):
    def __init__(self):
        self.pc = None
        self.reset()

    def reset(self):
        self.pc = PC()     

    def set_cpu(self, cpu='Intel Core i5 1300'):
        self.pc.cpu = cpu

    def set_gpu(self, gpu='NVIDIA GTX 1650/RTX 3050'):
        self.pc.gpu = gpu

    def set_ram(self, ram='16GB DDR4 or DDR5'):
        self.pc.ram = ram

    def set_storage(self, storage='512GB SSD'):
        self.pc.storage = storage

    def set_motherboard(self, motherboard='ASUS Prime B760M-A D4'):
        self.pc.motherboard = motherboard

    def set_case(self, case='Cooler Master Q300L'):
        self.pc.case = case

    def set_psu(self, psu='Seasonic Focus GX-550'):
        self.pc.psu = psu

    def get_pc(self):
        pc = self.pc
        return pc


    

