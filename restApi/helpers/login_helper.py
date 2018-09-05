from flask_restplus import reqparse, inputs


class LoginParser:
    parser = reqparse.RequestParser()

    parser.add_argument('email',
                        type=inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
                        action='append',
                        required=True,
                        location='json',
                        help="please enter a valid email address")

    parser.add_argument('password',
                        type=str,
                        required=True,
                        location='json',
                        help="Please enter a valid starting point")