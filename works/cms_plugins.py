from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from jonnsonaguirre.works.models import WorkPlugin, PublicationPlugin



class CMSWorkPlugin(CMSPluginBase):
    model = WorkPlugin
    name = _("Work")
    render_template = "works/work-plugin.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'work':instance.work,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSWorkPlugin)



class CMSPublicationPlugin(CMSPluginBase):
    model = PublicationPlugin
    name = _("Publication")
    render_template = "works/publication-plugin.html"
    
    def render(self, context, instance, placeholder):
        context.update({
            'publication':instance,
            'object':instance,
            'placeholder':placeholder
        })
        return context

plugin_pool.register_plugin(CMSPublicationPlugin)
