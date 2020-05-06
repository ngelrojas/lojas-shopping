from core.models.user import User


class HelperUser:
    """helper queries to user"""
    def is_DeleteUser(self, request):
        """verify if user is deleted"""
        user = User.objects.get(
            id=request.user.id,
            is_delete=False)
        return user

    def is_DeleteUserID(self, userID):
        user = User.objects.get(
            id=userID,
            is_delete=False)
        return user

    def get_user_email(self, email):
        """get user email"""
        user = User.objects.get(
            email=email)
        return user

    def re_activate_account(self, userID):
        """activate account using send email"""
        user = User.objects.get(id=userID)
        user.is_activate = True
        user.save()
        return user

    def get_user_ID(self, userID):
        user = User.objects.get(id=userID)
        return user

    def delete_user(self, request):
        current_user = self.is_DeleteUser(request)
        current_user.is_delete = True
        current_user.is_activate = False
        current_user.save()
        return current_user
