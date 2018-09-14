from flask_restplus import Namespace, Resource, fields
from restApi.models.rides import Rides
from .auth import token_required

from restApi.helpers.request_helper import RequestParser, ApproveParser

Ride_object = Rides()

request_api = Namespace("Requests", description="This namespace allows users to request to join existing rides")
request = request_api.model('Request', {'email': fields.String('email@example.com'),
                                        'username': fields.String('test_user'),
                                        'number_of_seats': fields.String('number_of_seats'),
                                        'pick_up_point': fields.String('pick_up_point'),
                                        'destination': fields.String('destination')})
approve = request_api.model('Approval', {'approval': fields.Boolean(default=True)})


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
                    return "Request made successfully", 201
                return "This ride is only limited to {} seats".format(
                    Ride_object.rides[ride_id]['seats_available']), 400
            return "Ride does not exists", 404


class Requests(Resource):
    def get(self):
        return Ride_object.requests


class Approve(Resource):
    @request_api.expect(approve)
    @token_required
    @request_api.doc(security='apikey')
    def post(self, ride_id):
        ride_request = Ride_object.check_request_exists(ride_id)
        if ride_request:
            data = ApproveParser.parser.parse_args()
            if data['approval'] == "True" or data['approval'] =="true":
                ride = Ride_object.get_single_ride(ride_id)
                if ride:
                    if Ride_object.rides[ride_id]['seats_available'] >= Ride_object.requests[ride_id]['number_of_seats']:
                        Ride_object.rides[ride_id]["seats_available"] -= Ride_object.requests[ride_id]["number_of_seats"]
                        return {"message":"Ride approved successfully"},202
                    return {"message":"seats available not sufficient"},200
                return {"message":"ride does not exist"},404
            return {"message":"Request declined"},401
        return {"message":"Ride request does not exist"},404


# self.rides[ride_id]["seats_available"] -= number_of_seats
request_api.add_resource(Request, '/rides/<int:ride_id>/requests')
request_api.add_resource(Requests, '/requests')
request_api.add_resource(Approve, '/requests/<int:ride_id>')
