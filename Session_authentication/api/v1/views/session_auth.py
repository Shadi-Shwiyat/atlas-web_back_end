#!/usr/bin/env python3
""" Views for session authentication
"""
from flask import jsonify, make_response, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login',
                 methods=['POST'],
                 strict_slashes=False)
def login() -> dict:
    '''Retreiving user object using
        login email and pwd'''
    user_email = request.form.get('email')
    # print(user_email)
    user_password = request.form.get('password')
    # print(user_password)

    if (not user_email):
        return jsonify({ "error": "email missing" }), 400
    if (not user_password):
        return jsonify({ "error": "password missing" }), 400
    
    user_cls = User(email=user_email)
    user_cls.password = user_password

    matching_users = user_cls.search(attributes={'email': user_email})
    if matching_users:
        for user in matching_users:
            if user.is_valid_password(user_password):
                from api.v1.app import auth
                session_id = auth.create_session(user.id)
                # print('sessoin id is:',session_id)
                cookie_name = os.getenv('SESSION_NAME')
                # print('sessoin cookie name is:',cookie_name)
                # cookie_value = request.cookies.get('_my_session_id')
                # print('session cookie value is:', cookie_value)
                json_user = user.to_json()
                response = jsonify(json_user)
                response = make_response(response)
                response.set_cookie(cookie_name, session_id)
                # print(response)

                return response
        return jsonify({ "error": "wrong password" }), 401
    elif not matching_users:
        # print("User not found.")
        return jsonify({ "error": "no user found for this email" }), 404
