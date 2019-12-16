import connexion
import six

from crm.models.user import User  # noqa: E501
from crm import util
from crm.service.user_service import UserService

def user_get():  # noqa: E501
    """사용자 조회

    # noqa: E501

    """
    response = []

    user_service = UserService()
    response = user_service.user_get()

    return response

def user_post(body):  # noqa: E501
    """사용자 등록

    # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    user_service = UserService()
    user = body.to_dict()
    response = user_service.user_post(user)

    return response

def user_put(body):  # noqa: E501
    """사용자 수정

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: User
    """
    if connexion.request.is_json:
        body = User.from_dict(connexion.request.get_json())  # noqa: E501

    user_service = UserService()
    user = body.to_dict()
    response = user_service.user_put(user)
    
    return response

def user_id_delete(id):  # noqa: E501
    """사용자 삭제

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """

    user_service = UserService()
    response = user_service.user_delete(id)
    print(response)

    return response