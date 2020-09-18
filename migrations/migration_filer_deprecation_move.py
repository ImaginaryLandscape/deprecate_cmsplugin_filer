from django.apps import apps as global_apps
from django.db import migrations
from djangocms_file.models import get_templates as get_file_templates
from djangocms_picture.models import get_templates as get_picture_templates


def forwards_filer_file(apps, schema_editor):
    try:
        CMSPluginFilerFile = apps.get_model('cmsplugin_filer_file',
                                            'FilerFile')
        cmsplugin_filer_file = True
    except LookupError:
        cmsplugin_filer_file = False
    if cmsplugin_filer_file:
        DjangoCMSFileFile = apps.get_model('djangocms_file', 'File')
        for old_object in CMSPluginFilerFile.objects.all():
            old_cmsplugin_ptr = old_object.cmsplugin_ptr
            new_object = DjangoCMSFileFile(
                file_name=old_object.title,
                file_src=old_object.file,
                # defaults for fields that don't exist in the old_object
                link_target='',
                template=get_file_templates()[0][0],
                show_file_size=1,
                # fields for the cms_cmsplugin table
                position=old_cmsplugin_ptr.position,
                language=old_cmsplugin_ptr.language,
                plugin_type='FilePlugin',
                creation_date=old_cmsplugin_ptr.creation_date,
                changed_date=old_cmsplugin_ptr.changed_date,
                parent=old_cmsplugin_ptr.parent,
                placeholder=old_cmsplugin_ptr.placeholder,
                depth=old_cmsplugin_ptr.depth,
                numchild=old_cmsplugin_ptr.numchild,
                path=old_cmsplugin_ptr.path,
            )
            old_object.delete()
            new_object.save()
    return cmsplugin_filer_file


def forwards_filer_folder(apps, schema_editor):
    try:
        CMSPluginFilerFolder = apps.get_model('cmsplugin_filer_folder',
                                              'FilerFolder')
        cmsplugin_filer_folder = True
    except LookupError:
        cmsplugin_filer_folder = False
    if cmsplugin_filer_folder:
        DjangoCMSFileFolder = apps.get_model('djangocms_file', 'Folder')
        for old_object in CMSPluginFilerFolder.objects.all():
            old_cmsplugin_ptr = old_object.cmsplugin_ptr
            new_object = DjangoCMSFileFolder(
                folder_src=old_object.folder,
                # defaults for fields that don't exist in the old_object
                template=get_file_templates()[0][0],
                link_target='',
                show_file_size=0,
                # fields for the cms_cmsplugin table
                position=old_cmsplugin_ptr.position,
                language=old_cmsplugin_ptr.language,
                plugin_type='FolderPlugin',
                creation_date=old_cmsplugin_ptr.creation_date,
                changed_date=old_cmsplugin_ptr.changed_date,
                parent=old_cmsplugin_ptr.parent,
                placeholder=old_cmsplugin_ptr.placeholder,
                depth=old_cmsplugin_ptr.depth,
                numchild=old_cmsplugin_ptr.numchild,
                path=old_cmsplugin_ptr.path,
            )
            old_object.delete()
            new_object.save()
    return cmsplugin_filer_folder


def forwards_filer_image(apps, schema_editor):
    try:
        CMSPluginFilerImage = apps.get_model('cmsplugin_filer_image',
                                             'FilerImage')
        cmsplugin_filer_image = True
    except LookupError:
        cmsplugin_filer_image = False
    if cmsplugin_filer_image:
        DjangoCMSPicture = apps.get_model('djangocms_picture', 'Picture')
        for old_object in CMSPluginFilerImage.objects.all():
            old_cmsplugin_ptr = old_object.cmsplugin_ptr
            attributes = {}
            if old_object.alt_text:
                attributes.update({'alt': old_object.alt_text})
            new_object = DjangoCMSPicture(
                caption_text=old_object.caption_text,
                external_picture=old_object.image_url
                if old_object.image_url else '',
                use_automatic_scaling=old_object.use_autoscale,
                width=old_object.width,
                height=old_object.height,
                use_crop=old_object.crop,
                use_upscale=old_object.upscale,
                alignment=old_object.alignment if old_object.alignment else '',
                picture=old_object.image,
                thumbnail_options=old_object.thumbnail_option,
                attributes=attributes,
                link_attributes=old_object.link_attributes,
                # defaults for fields that don't exist in the old_object
                use_no_cropping=0,
                template=get_picture_templates()[0][0],
                # fields for the cms_cmsplugin table
                position=old_cmsplugin_ptr.position,
                language=old_cmsplugin_ptr.language,
                plugin_type='PicturePlugin',
                creation_date=old_cmsplugin_ptr.creation_date,
                changed_date=old_cmsplugin_ptr.changed_date,
                parent=old_cmsplugin_ptr.parent,
                placeholder=old_cmsplugin_ptr.placeholder,
                depth=old_cmsplugin_ptr.depth,
                numchild=old_cmsplugin_ptr.numchild,
                path=old_cmsplugin_ptr.path,
            )
            old_object.delete()
            new_object.save()
    return cmsplugin_filer_image

def forwards_filer_link(apps, schema_editor):
    try:
        CMSPluginFilerLink = apps.get_model('cmsplugin_filer_link',
                                            'FilerLinkPlugin')
        cmsplugin_filer_link = True
    except LookupError:
        cmsplugin_filer_link = False
    if cmsplugin_filer_link:
        DjangoCMSLink = apps.get_model('djangocms_link', 'Link')
        for old_object in CMSPluginFilerLink.objects.all():
            old_cmsplugin_ptr = old_object.cmsplugin_ptr
            new_object = DjangoCMSLink(
                name=old_object.name,
                external_link=old_object.url or '',
                internal_link=old_object.page_link or None,
                mailto=old_object.mailto or '',
                template=old_object.link_style,
                target='_blank' if old_object.new_window else '',
                file_link=old_object.file,
                attributes=old_object.link_attributes,

                # fields for the cms_cmsplugin table
                position=old_cmsplugin_ptr.position,
                language=old_cmsplugin_ptr.language,
                plugin_type='LinkPlugin',
                creation_date=old_cmsplugin_ptr.creation_date,
                changed_date=old_cmsplugin_ptr.changed_date,
                parent=old_cmsplugin_ptr.parent,
                placeholder=old_cmsplugin_ptr.placeholder,
                depth=old_cmsplugin_ptr.depth,
                numchild=old_cmsplugin_ptr.numchild,
                path=old_cmsplugin_ptr.path,
            )
            old_object.delete()
            new_object.save()
    return cmsplugin_filer_link


def forwards(apps, schema_editor):
    cmsplugin_filer_file = forwards_filer_file(apps, schema_editor)
    cmsplugin_filer_folder = forwards_filer_folder(apps, schema_editor)
    # move all inherited plugins first, then the parents
    cmsplugin_filer_link = forwards_filer_link(apps, schema_editor)
    cmsplugin_filer_image = forwards_filer_image(apps, schema_editor)

    if not cmsplugin_filer_file and not cmsplugin_filer_folder and not \
        cmsplugin_filer_image and not cmsplugin_filer_link:
        return


class Migration(migrations.Migration):
    '''
    Move data from filer-plugins to the new djangocms-*-plugins. Inspiration:
    https://docs.djangoproject.com/en/2.0/howto/writing-migrations/
    #migrating-data-between-third-party-apps
    '''
    operations = [
        migrations.RunPython(forwards, migrations.RunPython.noop),
    ]
    dependencies = [
        #('djangocms_file', '0010_removed_null_fields'),
        #('djangocms_picture', '0007_fix_alignment'),
    ]
