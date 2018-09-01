from flask_restplus import reqparse,inputs


class UserParser:
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        location='json',
                        help="Please enter a valid starting point")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
    parser.add_argument('confirm_password',
                        type=str,
                        required=True,
                        location='json',
                        help="This field cannot be blank")
    parser.add_argument('email',
                        type=inputs.regex('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'),
                        required=True,
                        location='json',
                        help="please enter a valid date")
