from rest_framework.permissions import BasePermission

class BenefactorPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user is None:
            return False
        if not request.user.is_authenticated:
            return False

        return request.user.is_benefactor


class CharityPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user is None:
            return False
        if not request.user.is_authenticated:
            return False

        return request.user.is_charity

