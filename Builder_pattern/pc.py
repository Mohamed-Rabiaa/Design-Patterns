class PC:
    cpu = gpu = ram = storage = motherboard = case = psu = None
    def __str__(self):
        return f"The PC specifications are:\n\tCPU: {self.cpu} \
        \n\tGPU: {self.gpu} \
        \n\tRAM: {self.ram} \
        \n\tStorage: {self.storage} \
        \n\tMotherboard: {self.motherboard} \
        \n\tCase: {self.case} \
        \n\tPSU: {self.psu}"