from users.helper_models.helperUser import HelperUser


class HelperUpdateUser:
    """class helper update user"""
    def UpdateUser(self, request, serializerClass):
        current_user = HelperUser.is_DeleteUser(self, request)
        serializer = serializerClass(
            current_user,
            data=request.data,
            partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return current_user
        return False
