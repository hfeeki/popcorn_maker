from django.db import models


class ProjectManager(models.Manager):

    def fork(self, project, user):
        """Duplicate the ``Project`` data fields and create a new one"""
        initial = {
            'author': user,
            'source': project,
            }
        for attr in ['name', 'description', 'template', 'metadata', 'html',
                     'status']:
            initial[attr] = getattr(project, attr)
        return self.create(**initial)

    def get_for_user(self, user):
        return self.filter(~models.Q(status=self.model.REMOVED), author=user)


class ProjectLiveManager(ProjectManager):

    def get_query_set(self):
        return (super(ProjectManager, self).get_query_set()
                .filter(status=self.model.LIVE, is_shared=True))


class TemplateManager(models.Manager):

    def get_query_set(self):
        return (super(TemplateManager, self).get_query_set()
                .filter(status=self.model.LIVE))
