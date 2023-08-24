from AirlineReservationSystem import AirlineReservationSystem
from AirlineReservationUI import AirlineReservationUI


if __name__ == "__main__":
    print("Welcome To Airline Reservation System")
    airlineSystem = AirlineReservationSystem()
    ui = AirlineReservationUI(airlineSystem)
    ui.run()
