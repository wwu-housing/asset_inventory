import datetime

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from wwu_housing.decorators import has_perm

from models import (Location, Job, Person, Status, Esign,
                                    Purchase, Device, Esign_Sys)
from forms import (JobForm, LocationForm, PersonForm,
                                   PurchaseForm, StatusForm, EsignForm,
                                   Esign_SysForm, DeviceForm)

# global variables
MODEL_NAMES = ['Device', 'Location', 'Status', 'Purchase', 'Job', 'Person', 'Esign']


# models
def _listModel():
    """helper function that lists MODEL_NAMES"""
    return MODEL_NAMES

def _checkModel(model_name):
    """helper function that checks for model_name membership in MODEL_NAMES"""
    list_models = _listModel()
    for model in _listModel():
        if (model_name == model):
            return True
    return False

@login_required
@has_perm("asset_inventory.device.can_add_device")
def homepage(request):
    """Landing Page for inventory site"""
    list_Models = _listModel()
    return render_to_response('asset_inventory/index.html',
                              {'model_list': list_Models})

@login_required
@has_perm("asset_inventory.device.can_add_device")
def list_model(request, model_name):
    """Listings Page for inventory site"""
    directory = "asset_inventory/list_Pages/"
    if not _checkModel(model_name):
        raise Http404()
    elif (model_name == "Status"):
        templateFile = directory + "listStatus.html"
        status = Status.objects.all()
    elif (model_name == "Device"):
        templateFile = directory + "listDevices.html"
        devices = Device.objects.all()
    elif (model_name == "Job"):
        templateFile = directory + "listJobs.html"
        jobs = Job.objects.all()
    elif (model_name == "Location"):
        templateFile = directory + "listLocations.html"
        locations = Location.objects.all()
    elif (model_name == "Purchase"):
        templateFile = directory + "listPurchases.html"
        purchases = Purchase.objects.all()
    elif (model_name == "Person"):
        templateFile = directory + "listPeople.html"
        people = Person.objects.all()
    elif (model_name == "Esign"):
        templateFile = directory + "listEsigns.html"
        esigns = Esign.objects.all()
    else:
        render_to_response('index.html')
    return render_to_response(templateFile, locals())

@login_required
@has_perm("asset_inventory.device.can_add_device")
def view_item(request, model_name, model_id):
    """View Page for individual items in the inventory"""
    directory = "asset_inventory/list_Pages/Individual_Items/"
    if not _checkModel(model_name):
        raise Http404()
    elif (model_name == "Device"):
        templateFile = directory + "listDevice.html"
        device = Device.objects.get(id=model_id)
    elif (model_name == "Status"):
        templateFile = directory + "listStatus.html"
        status = Status.objects.get(id=model_id)
    elif (model_name == "Esign"):
        templateFile = directory + "listEsign.html"
        esign = Esign.objects.get(id=model_id)
        associated_machines = Esign_Sys.objects.filter(esign_ID=model_id)
    elif (model_name == "Purchase"):
        templateFile = directory + "listPurchase.html"
        purchase = Purchase.objects.get(id=model_id)
    elif (model_name == "Location"):
        templateFile = directory + "listLocation.html"
        location = Location.objects.get(id=model_id)
    else:
        render_to_response('asset_inventory/index.html')
    return render_to_response(templateFile, locals())

@login_required
@has_perm("asset_inventory.device.can_add_device")
def add_edit_item(request, model_name, add_edit, edit_id):
    """Add/Edit page for the inventory"""
    if(add_edit == "add"):
        edit_id = None
    if(_checkModel(model_name)):
        directory = "asset_inventory/add_edit_Pages/"
        # Adding or Editing a Job
        if (model_name == "Job"):
            templateFile = directory + "Job.html"
            post_data = request.POST or None

            try:
                Job_Instance = Job.objects.get(pk=edit_id)
            except Job.DoesNotExist:
                Job_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Job', 'add', 'new']))

            Job_Form = JobForm(post_data, instance=Job_Instance)

            if(Job_Form.is_valid()):
                Job_Occurance = Job_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Job']))
            return render_to_response(templateFile,
                                      {'form': Job_Form},
                                       context_instance=RequestContext(request))
        # Adding or Editing a Location
        elif (model_name == "Location"):
            templateFile = directory + "Location.html"
            post_data = request.POST or None
            
            try:
                Location_Instance = Location.objects.get(pk=edit_id)
            except Location.DoesNotExist:
                Location_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Location', 'add', 'new']))
            
            Location_Form = LocationForm(post_data, instance=Location_Instance)

            if(Location_Form.is_valid()):
                Location_Occurance = Location_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Location']))

            return render_to_response(templateFile,
                                      {'form': Location_Form},
                                      context_instance=RequestContext(request))
    
        # Adding or Editing a Person
        elif (model_name == "Person"):
            templateFile = directory + "Person.html"
            post_data = request.POST or None
            
            try:
                Person_Instance = Person.objects.get(pk=edit_id)
            except Person.DoesNotExist:
                Person_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Person', 'add', 'new']))
            
            Person_Form = PersonForm(post_data, instance=Person_Instance)

            if(Person_Form.is_valid()):
                Person_Occurance = Person_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Person']))

            return render_to_response(templateFile,
                                      {'form': Person_Form},
                                      context_instance=RequestContext(request))

        # Adding or Editing a Purchase
        elif (model_name == "Purchase"):
            templateFile = directory + "Purchase.html"
            post_data = request.POST or None
            
            try:
                Purchase_Instance = Purchase.objects.get(pk=edit_id)
            except Purchase.DoesNotExist:
                Purchase_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Purchase', 'add', 'new']))
            
            Purchase_Form = PurchaseForm(post_data, instance=Purchase_Instance)

            if(Purchase_Form.is_valid()):
                Purchase_Occurance = Purchase_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Purchase']))

            return render_to_response(templateFile,
                                      {'form': Purchase_Form},
                                      context_instance=RequestContext(request))
        # Adding or Editing a Status
        elif (model_name == "Status"):
            templateFile = directory + "Status.html"
            post_data = request.POST or None
            
            try:
                Status_Instance = Status.objects.get(pk=edit_id)
            except Status.DoesNotExist:
                Status_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Status', 'add', 'new']))
            
            Status_Form = StatusForm(post_data, instance=Status_Instance)

            if(Status_Form.is_valid()):
                Status_Occurance = Status_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Status']))

            return render_to_response(templateFile,
                                      {'form': Status_Form},
                                      context_instance=RequestContext(request))
        # Adding or Editing a Esign
        elif (model_name == "Esign"):
            templateFile = directory + "Esign.html"
            post_data = request.POST or None
            
            try:
                Esign_Instance = Esign.objects.get(pk=edit_id)
            except Esign.DoesNotExist:
                Esign_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Esign', 'add', 'new']))
            
            Esign_Form = EsignForm(post_data, instance=Esign_Instance)

            if(Esign_Form.is_valid()):
                Esign_Occurance = Esign_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Esign']))

            return render_to_response(templateFile,
                                      {'form': Esign_Form},
                                      context_instance=RequestContext(request))
        # Adding or Editing a Device
        elif (model_name == "Device"):
            templateFile = directory + "Device.html"
            post_data = request.POST or None
            
            try:
                Device_Instance = Device.objects.get(pk=edit_id)
            except Device.DoesNotExist:
                Device_Instance = None
                if(add_edit == "edit"):
                    return HttpResponseRedirect(reverse('asset_inventory_add_edit_item',
                                                        args=['Device', 'add', 'new']))
            
            Device_Form = DeviceForm(post_data, instance=Device_Instance)

            if(Device_Form.is_valid()):
                Device_Occurance = Device_Form.save()
                return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                                    args=['Device']))

            return render_to_response(templateFile,
                                      {'form': Device_Form},
                                      context_instance=RequestContext(request))
    # This is a catch all response, if some unforseen error manages
    # to occur with the calling of add/edit pages
    else:
        render_to_response(reverse('homepage'))

@login_required
@has_perm("asset_inventory.device.can_add_device")
def add_device_esign(request, esign_id_number):
    """Add a Esign instance"""
    directory = "asset_inventory/add_edit_Pages/"
    templateFile = directory + "add_Esign.html"
    post_data = request.POST or None
    
    esign = Esign.objects.get(pk=esign_id_number)


    Esign_Sys_Form = Esign_SysForm(post_data)

    if(Esign_Sys_Form.is_valid()):
        Esign_Sys_Occurance = Esign_Sys_Form.save(commit=False)
        Esign_Sys_Occurance.esign_ID = esign
        Esign_Sys_Occurance.save()
        return HttpResponseRedirect(reverse('asset_inventory_list_model',
                                    args=['Esign']))

    return render_to_response(templateFile,
                              {'form': Esign_Sys_Form, 'esign': esign},
                              context_instance=RequestContext(request))

@login_required
@has_perm("asset_inventory.device.can_add_device")
def usecasepages(request, use_case_type):
    """Use case pages, inventory printout page, aged inventory list"""
    if(use_case_type == 'aged'):
        device = Device.objects.order_by('purchase_ID__purchase_date').all()
        return render_to_response('asset_inventory/use_case_pages/agedInventory.html',
                                  locals())
    if(use_case_type == 'inv'):
        device = Device.objects.order_by('Location_ID__building').order_by('Location_ID__location_type').all()
        count = 0
        for items in device:
            count = count + 1
        return render_to_response('asset_inventory/use_case_pages/printableInventory.html',
                                  locals())
