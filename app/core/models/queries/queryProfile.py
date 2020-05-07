from core.models.profile import ProfileBuyer
from core.models.profile import ProfileSeller
from core.models.queries.queryUser import HelperUser


class HelperProfile:
    """queries profile"""
    def getProfile(self, request, tuser):
        """
        get profile current user buyer
        """
        user = HelperUser.is_DeleteUser(self, request)
        profile = ProfileBuyer.objects.get(
            users=user, typeuser=tuser)
        return profile


class HelperProfileSeller:
    """queries about profile seller"""
    def getProfileSeller(self, request, tuser):
        user = HelperUser.is_DeleteUser(self, request)
        profile = ProfileSeller.objects.get(
            users=user, typeuser=tuser)
        return profile
