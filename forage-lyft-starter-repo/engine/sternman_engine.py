from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    # function to check if engine should be serviced
    # Condition: Only when the warning indicator is on
    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
