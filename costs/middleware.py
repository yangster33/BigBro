from user.models import MyUser

class ArchivesMixin:

    def get_context_data(self, **kargs):

        context = super().get_context_data(**kargs)
        user_archives = MyUser.objects.get(username=self.request.user)
        update_dict = dict(user_archives=user_archives)
        context.update(update_dict)

        return context