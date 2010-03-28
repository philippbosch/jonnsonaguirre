from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from tinymce import models as tinymce_models

class Work(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    slug = models.SlugField(verbose_name=_("slug"))
    text = tinymce_models.HTMLField(verbose_name=_("text"), blank=True)
    date = models.CharField(verbose_name=_("date"), max_length=50, blank=True)
    display_image = models.ImageField(verbose_name=_("display image"), upload_to='uploads/')
    
    class Meta:
        verbose_name=_("work")
        verbose_name_plural=_("works")
    
    def __unicode__(self):
        return u"%s" % self.name



class MediaFile(models.Model):
    work = models.ForeignKey(Work, verbose_name=_("work"))
    name = models.CharField(verbose_name=_("name"), max_length=255, blank=True)
    file = models.FileField(verbose_name=_("file"), upload_to='uploads/')
    caption = tinymce_models.HTMLField(verbose_name=_("caption"), blank=True)
    
    class Meta:
        verbose_name=_("media file")
        verbose_name_plural=_("media files")
    
    def __unicode__(self):
        return u"%s" % self.name



class WorkPlugin(CMSPlugin):
    work = models.ForeignKey(Work, verbose_name=_("work"))
    
    def __unicode__(self):
        return u"%s" % self.work

class PublicationPlugin(CMSPlugin):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    abstract = tinymce_models.HTMLField(verbose_name=_("abstract"), blank=True)
    issuu_document_id = models.CharField(verbose_name=_("issuu document id"), max_length=255)
    
    def __unicode__(self):
        return u"%s" % self.name

