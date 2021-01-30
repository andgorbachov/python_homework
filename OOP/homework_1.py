class Element(object):
    element = ''
    freezing_point = 0
    evaporation_point = 0
    celsius_sign = '°C'
    fahrenheit_sign = '°F'
    kelvin_sign = '°K'

    def fahrenheit_to_celsius(self, t_fahrenheit):
        return round((t_fahrenheit - 32) / 1.8, 1)

    def celsius_to_fahrenheit(self, t_celsius):
        return round((t_celsius * 1.8) + 32, 1)

    def celsius_to_kelvin(self, t_celsius):
        return round(t_celsius + 273.15, 1)

    def kelvin_to_celsius(self, t_celsius):
        return round(t_celsius - 273.15, 1)

    def kelvin_to_fahrenheit(self, t_fahrenheit):
        return round(((t_fahrenheit - 273.15) * 1.8) + 32, 1)

    def fahrenheit_to_kelvin(self, t_fahrenheit):
        return round((t_fahrenheit - 32) / 1.8 + 273.15, 1)

    def agg_state_celsius(self, t_celsius):
        if t_celsius < self.freezing_point:
            print(f'As temperature is {t_celsius} {self.celsius_sign} the {self.element} currently is in solid state.')
        elif self.freezing_point <= t_celsius <= self.evaporation_point:
            print(f'As temperature is {t_celsius} {self.celsius_sign} The {self.element} currently is in liquid state.')
        else:
            print(f'As temperature is {t_celsius} {self.celsius_sign} The {self.element} currently is in gas state.')


class Oxygen(Element):
    element = 'Oxygen'
    freezing_point = -218.8
    evaporation_point = -183


oxygen = Oxygen()
print(oxygen.fahrenheit_to_celsius(98))
print(oxygen.celsius_to_fahrenheit(36.6))
print(oxygen.kelvin_to_celsius(100))
print(oxygen.celsius_to_kelvin(100))
print(oxygen.fahrenheit_to_kelvin(98))
print(oxygen.kelvin_to_fahrenheit(15))
print(oxygen.agg_state_celsius(98))
