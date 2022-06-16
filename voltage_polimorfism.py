#This is an example for poliforfism using the ohm´s law.

class Voltage:

    def __init__(self, current, resistance):
        self.current = current
        self.resistance = resistance

    def voltage_calculator(self):
        return self.current * self.resistance

class Milivoltage(Voltage):

    def __init__(self, current, resistance):
        super().__init__(current, resistance)
    
    def voltage_calculator(self):
        return (self.current * self.resistance)*1000

def main():

    volts = Voltage(current= float(input("Enter the electric current value: ")), resistance= float(input("Enter the resistance value: ")))
    print(f"V: {volts.voltage_calculator()} ")

    milivolts = Milivoltage(current= float(input("Enter the electric current value: ")), resistance= float(input("Enter the resistance value: ")))
    print(f"mV: {milivolts.voltage_calculator()}")


if __name__ == "__main__":
    main()

   