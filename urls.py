from django.conf.urls.defaults import *

from views import (homepage, list_model, view_item, add_edit_item,
                   add_device_esign, usecasepages)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Gets to landing page
    url(r'^$',
        homepage,
        name='asset_inventory_index',
    ),
    
    # lists of all entries for each part of the inventory database,
    # regEX determines which model is being listed
    #
    # lists needed: systems, jobs, location, esign, purchase, person
    # 1 parameter: which model to access (model_name)
    url(r'^list/(?P<model_name>[A-Za-z]{3,8})/$',
        list_model,
        name='asset_inventory_list_model',
    ),

    # lists a single item
    url(r'list/(?P<model_name>[A-Za-z]{3,8})/(?P<model_id>[0-9]{1,5})/',
        view_item,
        name='asset_inventory_view_item',
    ),

    # add/edit item page for each part of inventory database, uses 
    # regEx to determine which model is being effected.
    #
    # 3 parameters: which model to access (model_name), which process
    # to execute (add_edit), check if not 'new', which item to edit (edit_id)  
    url(r'^(?P<model_name>[A-Za-z]{3,8})/(?P<add_edit>add|edit)/(?P<edit_id>[0-9]{1,5}|[a-z]{1,5})/$',
        add_edit_item,
        name='asset_inventory_add_edit_item',
    ),
    
    # adds a machine to an esign record, to facilitate the many to many
    # relationship required for associating devices with an esign form.
    url(r'^Esign/(?P<esign_id_number>[0-9]{1,5})/AddDevice/$',
        add_device_esign,
        name='asset_inventory_add_device_esign',
    ),

    #special pages for primary use cases
    url(r'^inventory/(?P<use_case_type>[A-Za-z]{3,4})/$',
        usecasepages,
        name='asset_inventory_usecasepages',
    ),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
