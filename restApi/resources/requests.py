from flask_restplus import Namespace, Resource, fields
from restApi.models.rides import Rides
from restApi.models.requests import Request
from restApi.helpers.request_helper import RequestParser

Ride_object = Rides()
Ride_object = Rides()
Request_object = Request()
request_api=Namespace("Requests",description="")
request = request_api.model('Request', {'email': fields.String('email@example.com'),
                                'username': fields.String('test_user'),
                                'number_of_seats': fields.String('number_of_seats'),
                                'pick_up_point': fields.String('pick_up_point'),
                                'destination': fields.String('destination')})


class Request(Resource):
    @request_api.expect(request)
    def post(self, ride_id):
        data = RequestParser.parser.parse_args()
        new_ride = Ride_object.get_single_ride(ride_id)
        for items in data.values():
            if items == "":
                return "Fields must not be blank"
            if new_ride:
                if Ride_object.rides[ride_id]["seats_available"] >= data['number_of_seats']:
                    Ride_object.join_request(ride_id, data['username'], data['number_of_seats'], data['pick_up_point'],
                                             data['destination'])
                    return "Request made successfully",201
                return "This ride is only limited to {} seats".format(Ride_object.rides[ride_id]['seats_available']),400
            return "Ride does not exists",404

class Requests(Resource):
    def get(self):
        return Ride_object.requests


request_api.add_resource(Request, '/rides/<int:ride_id>/requests')
request_api.add_resource(Requests, '/requests')
