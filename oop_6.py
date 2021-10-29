class PersonalComputer:
    def __init__(self, memory_size, disk_size, model, cpu):
        self.memory_size = memory_size
        self.disk_size = disk_size
        self.model = model
        self.cpu = cpu

    def __str__(self):
        return f"{self.memory_size}, {self.disk_size}, {self.model}, {self.cpu},"


class DesktopPc(PersonalComputer):

    def __init__(self, memory_size, disk_size, model, cpu, screen, keyboard, headset):
        super().__init__(memory_size, disk_size, model, cpu)
        self.screen = screen
        self.keyboard = keyboard
        self.headset = headset

    def __str__(self):
        return super(DesktopPc, self).__str__() + f" {self.screen}, {self.keyboard}, {self.headset}"

class Laptop(PersonalComputer):

    def __init__(self, memory_size, disk_size, model, cpu, dimensions, diagonal):
        super().__init__(memory_size, disk_size, model, cpu)
        self.dimensions = dimensions
        self.diagonal = diagonal

    def __str__(self):
        return super(Laptop, self).__str__() + f" {self.dimensions}, {self.diagonal}"

pc1 = DesktopPc(8, 216, 2.33, 2.77, 150, 'hhhh', 'tttt')
laptop = Laptop(16, 512, 8.33, 3.02, 'hhh', 100)

print(pc1)
print(laptop)