from flask_restplus import reqparse, inputs


class RequestParser:
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        location='json',
                        help="Please enter a valid starting point")
    parser.add_argument('email',
                        type=inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
                        action='append',
                        required=True,
                        location='json',
                        help="please enter a valid email address")
    parser.add_argument('number_of_seats',
                        type=int,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
    parser.add_argument('pick_up_point',
                        type=str,
                        required=True,
                        location='json',
                        help="Please enter a valid starting point")
    parser.add_argument('destination',
                        type=str,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
