# from flask import jsonify, request, make_response
# from functools import wraps
# import jwt
#
# from instance.config import Config
#
#
# def token_required(f):
#     """Checks for authenticated users with valid token in the header"""
#
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         """validate token provided"""
#         token = None
#
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#
#         if token is None:
#             return make_response(jsonify({"txt": "Please Register and Login"}), 401)
#
#         try:
#             data = jwt.decode(token, Config.SECRET)
#         except():
#             return make_response(jsonify({"txt": "Please, provide a valid token."}), 401)
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# @jwt.expired_token_loader
# def my_expired_token_callback():
#     return {
#                'status': 401,
#                'sub_status': 42,
#                'msg': 'The token has expired'
#            }, 401
#
#
# blacklist = set()
#
#
# @jwt.token_in_blacklist_loader
# def check_if_token_in_blacklist(decrypted_token):
#     '''check if token is blacklisted'''
#     jti = decrypted_token['jti']
#     return jti in blacklist
