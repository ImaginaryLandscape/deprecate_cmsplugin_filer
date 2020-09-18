# deprecate_cmsplugin_filer
A small app with a migration for converting deprecated cmsplugin-filer objects to djangocms plugin objects

Things you'll want to evaluate before migrating:

- Whether any custom project-level templates are in use for the cmsplugin filer modules. Any special customizations may need to be re-implemented in the djangocms-[file/link/picture] templates.

- If you currently are using django config settings such as CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES or FILER_LINK_STYLES, you'll need to copy these as DJANGOCMS_PICTURE_TEMPLATES and DJANGOCMS_LINK_TEMPLATES, respectively. Note: there is a difference in behavior with FILER_LINK_STYLES and DJANGOCMS_LINK_TEMPLATES. The former would simply set a class while the latter expects a corresponding template to be created. Reference: https://github.com/divio/djangocms-link/#configuration

1. Before running the migration, you can run the following command to make sure you back up the old plugin tables for quick restoring if needed.
./manage.py dumpdata cmsplugin_filer_file cmsplugin_filer_folder cmsplugin_filer_image cmsplugin_filer_link > ~/cmsplugin_filer.json

2. Ensure you've installed the new plugins, added them to INSTALLED_APPS, and migrated:
pip install djangocms-file djangocms-link djangocms-picture
INSTALLED_APPS += (
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
)
./manage.py migrate

3. I recommend also running the following command before and after the migration to get an inventory of the site's plugins and ensure they've all been migrated.
./manage.py cms list plugins

4. Now the small app with the migration can be installed and run:
./manage.py migrate deprecate_cmsplugin_filer

5. If you once again run ./manage.py cms list plugins, you should see the cmsplugin-filer objects have been converted to djangocms-[file/link/picture] objects.

6. Do a spotcheck of plugins on the site. This is where you may see errors related to previous FILER_LINK_STYLES that are now expecting corresponding templates to be created for each style.
