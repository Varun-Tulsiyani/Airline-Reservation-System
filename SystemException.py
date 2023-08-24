class AccountNotFound(Exception):
    def __init__(self, message="Account Not Found"):
        self.message = message
        super().__init__(self.message)


class TicketNotFound(Exception):
    def __init__(self, message="Ticket Not Found"):
        self.message = message
        super().__init__(self.message)


class AccountAlreadyExists(Exception):
    def __init__(self, message="Account Already Exists"):
        self.message = message
        super().__init__(self.message)


class BookingError(Exception):
    def __init__(self, message="Error occurred while booking ticket"):
        self.message = message
        super().__init__(self.message)


class DatabaseError(Exception):
    def __init__(self, message="Database Error"):
        self.message = message
        super().__init__(self.message)
