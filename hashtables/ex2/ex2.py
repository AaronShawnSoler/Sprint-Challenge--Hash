#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"({self.source}, {self.destination})"


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    print("TICKETS: ", tickets)
    result = [None] * length
    trips = {}
    for ticket in tickets:
        trips[ticket.source] = ticket.destination

    result[0] = trips['NONE']
    for index in range(1, length):
        result[index] = trips[result[index-1]]

    return result
