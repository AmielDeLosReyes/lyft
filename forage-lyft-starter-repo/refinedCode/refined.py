from abc import ABC, abstractmethod
from datetime import date, timedelta

# Interface for Serviceable objects
class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

# CarPart class for generic car parts
class CarPart(Serviceable):
    def __init__(self, last_service_date: date, service_interval: timedelta):
        self.last_service_date = last_service_date
        self.service_interval = service_interval

    def needs_service(self) -> bool:
        # Calculate the difference between the current date and the last service date
        time_since_last_service = date.today() - self.last_service_date

        # Check if the service interval has been exceeded
        return time_since_last_service >= self.service_interval

# Specific Engine implementations
class CapuletEngine(CarPart):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        # Set the service interval for Capulet Engine based on mileage
        service_interval = timedelta(miles=30000)
        super().__init__(last_service_date=date.today(), service_interval=service_interval)

    def needs_service(self) -> bool:
        return super().needs_service()

class WilloughbyEngine(CarPart):
    def __init__(self, last_service_mileage: int, current_mileage: int):
        # Set the service interval for Willoughby Engine based on mileage
        service_interval = timedelta(miles=60000)
        super().__init__(last_service_date=date.today(), service_interval=service_interval)

    def needs_service(self) -> bool:
        return super().needs_service()

class SternmanEngine(CarPart):
    def __init__(self, warning_light_on: bool):
        # Set the service interval for Sternman Engine when warning light is on
        service_interval = timedelta(days=0) if warning_light_on else timedelta(days=365)  # 0 days if warning light is on, else 1 year
        super().__init__(last_service_date=date.today(), service_interval=service_interval)

    def needs_service(self) -> bool:
        return super().needs_service()

# Specific Battery implementations
class SpindlerBattery(CarPart):
    def __init__(self):
        # Set the service interval for Spindler Battery based on years
        service_interval = timedelta(days=365 * 2)  # 2 years
        super().__init__(last_service_date=date.today(), service_interval=service_interval)

    def needs_service(self) -> bool:
        return super().needs_service()

class NubbinBattery(CarPart):
    def __init__(self):
        # Set the service interval for Nubbin Battery based on years
        service_interval = timedelta(days=365 * 4)  # 4 years
        super().__init__(last_service_date=date.today(), service_interval=service_interval)

    def needs_service(self) -> bool:
        return super().needs_service()

# Car class
class Car(Serviceable):
    def __init__(self, engine: CarPart, battery: CarPart):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        # Check if either the engine or battery needs service
        return self.engine.needs_service() or self.battery.needs_service()

# CarFactory class
class CarFactory:
    @staticmethod
    def create_calliope() -> Car:
        engine = CapuletEngine(last_service_mileage=0, current_mileage=0)
        battery = SpindlerBattery()
        return Car(engine, battery)

    @staticmethod
    def create_glissade() -> Car:
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=0)
        battery = SpindlerBattery()
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery()
        return Car(engine, battery)

    @staticmethod
    def create_rorschach() -> Car:
        engine = WilloughbyEngine(last_service_mileage=0, current_mileage=0)
        battery = NubbinBattery()
        return Car(engine, battery)

    @staticmethod
    def create_thovex() -> Car:
        engine = CapuletEngine(last_service_mileage=0, current_mileage=0)
        battery = NubbinBattery()
        return Car(engine, battery)

# Usage example
if __name__ == "__main__":
    # Creating a Calliope car using the CarFactory
    calliope_car = CarFactory.create_calliope()

    # Checking if the car needs service
    if calliope_car.needs_service():
        print("The Calliope car needs service.")
    else:
        print("The Calliope car does not need service.")
