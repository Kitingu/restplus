import datetime
from flask_restplus import reqparse


class RideParser:
    parser = reqparse.RequestParser()
    parser.add_argument('start_point',
                        type=str,
                        required=True,
                        location='json',
                        help="Please enter a valid starting point")
    parser.add_argument('destination',
                        type=str,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
    parser.add_argument('seats_available',
                        type=int,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
    parser.add_argument('date',
                        type=lambda x: datetime.datetime.strptime(x, '%d/%m/%Y').strftime('%d/%m/%Y'),
                        required=True,
                        location='json',
                        help="please enter a valid date using format")
    parser.add_argument('time',
                        type=lambda x: datetime.datetime.strptime(x, '%H:%M').strftime('%H:%M'),
                        required=True,
                        location='json',
                        help="Use 24 hour clock system")
