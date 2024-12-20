# Base builder
from abc import ABC, abstractmethod

class PCBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_cpu(self, cpu=None):
        pass

    @abstractmethod
    def set_gpu(self, gpu=None):
        pass

    @abstractmethod
    def set_ram(self, ram=None):
        pass

    @abstractmethod
    def set_storage(self, storage=None):
        pass

    @abstractmethod
    def set_motherboard(self, motherboard=None):
        pass

    @abstractmethod
    def set_case(self, case=None):
        pass

    @abstractmethod
    def set_psu(self, psu=None):
        pass
