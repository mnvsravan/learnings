import uuid
from datetime import datetime


class Vehicle:
    def __init__(self, number, v_type, fuel):
        self.vehicle_number = number
        self.vehicle_type = v_type
        self.fuel_type = fuel

    @property
    def vehicle_number(self):
        return self._vehicle_number

    @vehicle_number.setter
    def vehicle_number(self, value):
        if len(value) < 6:
            raise ValueError("Vehicle number too short")
        if not any(c.isalpha() for c in value):
            raise ValueError("Must contain letters")
        if not any(c.isdigit() for c in value):
            raise ValueError("Must contain numbers")
        self._vehicle_number = value

    @property
    def vehicle_type(self):
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        if value.upper() not in ["CAR", "BIKE"]:
            raise ValueError("Vehicle type must be CAR or BIKE")
        self._vehicle_type = value.upper()

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        if value.upper() not in ["PETROL", "DIESEL"]:
            raise ValueError("Fuel type must be PETROL or DIESEL")
        self._fuel_type = value.upper()

    def details(self):
        return f"{self.vehicle_number} | {self.vehicle_type} | {self.fuel_type}"


class ParkingToll:
    def __init__(self, car_limit=100, bike_limit=200):
        self.car_limit = car_limit
        self.bike_limit = bike_limit

        self.cars = 0
        self.bikes = 0

        self.tickets = {}

    def entry(self, vehicle):
        if vehicle.vehicle_type == "CAR" and self.cars >= self.car_limit:
            print("No space for cars")
            return None

        if vehicle.vehicle_type == "BIKE" and self.bikes >= self.bike_limit:
            print("No space for bikes")
            return None

        ticket = str(uuid.uuid4())[:8]

        self.tickets[ticket] = {
            "vehicle": vehicle,
            "time": datetime.now()
        }

        if vehicle.vehicle_type == "CAR":
            self.cars += 1
        else:
            self.bikes += 1

        print(f"Entry done. Ticket: {ticket}")
        return ticket

    def exit(self, ticket):
        if ticket not in self.tickets:
            print("Invalid ticket")
            return

        data = self.tickets.pop(ticket)
        vehicle = data["vehicle"]
        entry_time = data["time"]

        duration = (datetime.now() - entry_time).total_seconds() / 3600
        hours = max(1, round(duration))

        cost = self._cost(vehicle.vehicle_type, hours)

        if vehicle.vehicle_type == "CAR":
            self.cars -= 1
        else:
            self.bikes -= 1

        print(f"Exit done for {vehicle.vehicle_number}")
        print(f"Time: {hours} hour(s)")
        print(f"Cost: Rs {cost}")

    def _cost(self, v_type, hours):
        return hours * 50 if v_type == "CAR" else hours * 20


if __name__ == "__main__":
    toll = ParkingToll()

    v1 = Vehicle("AP01AB1234", "car", "petrol")
    v2 = Vehicle("AP02XY5678", "bike", "diesel")

    t1 = toll.entry(v1)
    t2 = toll.entry(v2)

    toll.exit(t1)
    toll.exit(t2)