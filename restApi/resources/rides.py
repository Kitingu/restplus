from flask_restplus import Resource, fields, Namespace
from restApi.models.rides import Rides
from restApi.helpers.ride_helpers import RideParser
# from restApi.helpers.user_validator import RideSchema

# from flask_jwt_extended import jwt_required
Ride_object = Rides()

ride_api = Namespace("rides", description="this are routes that allow users to create get or delete a ride")

ride_offer = ride_api.model('Rides', {'start_point': fields.String("nairobi"),
                                      'destination': fields.String("kiambu"),
                                      'seats_available': fields.String,
                                      'date': fields.String("10/02/2018"),
                                      'time': fields.String("10:21")
                                      })


class Ride(Resource):

    def get(self):
        response = Ride_object.get_all_rides()
        return response, 200

    @ride_api.expect(ride_offer)
    def post(self):
        data = RideParser.parser.parse_args()
        for items in data.values():
            if items == "":
                return "Fields must not be blank", 400
            Ride_object.create_rides(data['start_point'], data['destination'], data['seats_available'], data['date'],
                                     data['time'])
            return "Ride created successfully", 201





class Riide(Resource):
    # @jwt_required
    @ride_api.expect(ride_offer)
    def put(self, ride_id):
        data = RideParser.parser.parse_args()
        new_ride = Ride_object.get_single_ride(ride_id)
        for items in data.values():
            if items == "":
                return "Fields must not be blank", 400
            if new_ride:
                Ride_object.update(ride_id, data['start_point'], data['destination'], data['seats_available'],
                                   str(data['date']), str(data['time']))
                return "Ride updated successfully", 200
            return {"message": "Ride does not exist"}, 404

    def delete(self, ride_id):
        new_ride = Ride_object.get_single_ride(ride_id)
        if new_ride:
            Ride_object.delete_ride(ride_id)
            return "Ride deleted successfully", 200
        return "Ride does not exist", 404

    def get(self, ride_id):
        new_ride = Ride_object.get_single_ride(ride_id)
        if new_ride:
            return new_ride, 200
        return "Ride does not exist", 404


ride_api.add_resource(Ride, '/rides')
ride_api.add_resource(Riide, '/rides/<int:ride_id>')
