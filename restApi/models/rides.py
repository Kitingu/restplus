class Rides:
    rides = {}
    requests = {}

    def get_all_rides(self):
        return self.rides

    def create_rides(self, start_point, destination, seats_available, date, time):
        ride_id = len(self.rides) + 1
        self.rides[ride_id] = {"start_point": start_point,
                               "destination": destination,
                               "seats_available": seats_available,
                               "date": date,
                               "time": time}

    def get_single_ride(self, ride_id):
        if ride_id in self.rides:
            return self.rides[ride_id]

    def delete_ride(self, ride_id):
        del self.rides[ride_id]

    def update(self, ride_id, start_point, destination, seats_available, date, time):
        self.rides[ride_id] = {"start_point": start_point,
                               "destination": destination,
                               "seats_available": seats_available,
                               "date": date,
                               "time": time}
        return "Ride updated successfully"

    def join_request(self, ride_id, username, number_of_seats, pick_up_point, destination):
        self.requests["request"] = {"ride_id":ride_id,
                                    "username": username,
                                    "number_of_seats": number_of_seats,
                                    "pick_up_point": pick_up_point,
                                    "destination": destination}

        # self.rides[ride_id]["seats_available"] -= number_of_seats

# kas=Rides.create_rides("kiambu","nairobi",5,"02/02/2018","10:00")
# print(kas.get_all_rides())
# print(join_request(1,"kasee",1,3,"kiambu","nairobi"))
# print(delete_ride(1))
# print(get_single_ride(1))
