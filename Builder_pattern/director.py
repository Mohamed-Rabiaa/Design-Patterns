# Director

class Director():
    def make_pc(self, builder):
        builder.reset()
        builder.set_cpu()
        builder.set_gpu()
        builder.set_ram()
        builder.set_storage()
        builder.set_motherboard()
        builder.set_case()
        builder.set_psu()


    def make_custom_pc(self, builder, cpu, gpu, ram, storage, motherboard,
                case, psu):
        builder.reset()
        builder.set_cpu(cpu)
        builder.set_gpu(gpu)
        builder.set_ram(ram)
        builder.set_storage(storage)
        builder.set_motherboard(motherboard)
        builder.set_case(case)
        builder.set_psu(psu)

