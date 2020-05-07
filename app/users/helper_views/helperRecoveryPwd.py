from core.encoder.tokens import decode_user_id
from core.models.queries.queryUser import HelperUser


class HelperRecoveryPWD:
    """
    helper to recovery password confirm
    """
    def helperUpdate(self, request, serializerClass):
        uid = decode_user_id(request.data.get('uid'))
        token = request.data.get('token')
        current_user = HelperUser.is_DeleteUserID(self, uid)
        if current_user.is_activate and token:
            serializer = serializerClass(
                data=request.data,
                partial=True
            )
            if serializer.is_valid(raise_exception=True):
                current_user.set_password(request.data.get('password'))
                current_user.save()
                return current_user
        return False
