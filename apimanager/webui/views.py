# -*- coding: utf-8 -*-
"""
Views of config app
"""

import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from obp.api import API, APIError
from .forms import WebuiForm
from .forms import MethodRoutingForm
from django.urls import reverse_lazy

def error_once_only(request, err):
    """
    Just add the error once
    :param request:
    :param err:
    :return:
    """
    storage = messages.get_messages(request)
    if str(err) not in [str(m.message) for m in storage]:
        messages.error(request, err)

class IndexView(LoginRequiredMixin, FormView):
    """Index view for config"""
    template_name = "webui/index.html"
    form_class = WebuiForm
    success_url = reverse_lazy('webui-index')

    def dispatch(self, request, *args, **kwargs):
        self.api = API(request.session.get('obp'))
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        return context

    def get_form(self, *args, **kwargs):
        form = super(IndexView, self).get_form(*args, **kwargs)
        # Cannot add api in constructor: super complains about unknown kwarg
        fields = form.fields
        form.api = self.api
        try:
            fields['webui_props'].initial = ""

        except APIError as err:
            messages.error(self.request, err)
        except:
            messages.error(self.request, "Unknown Error")

        return form

    def form_valid(self, form):
        try:
            data = form.cleaned_data
            urlpath = '/management/webui_props'
            payload = {
                "name": data["name"],
                "value" : data["webui_props"]
            }
            result = self.api.post(urlpath, payload=payload)
        except APIError as err:
            error_once_only(self.request, err)
            return super(IndexView, self).form_invalid(form)
        except Exception as err:
            error_once_only(self.request, "Unknown Error")
            return super(IndexView, self).form_invalid(form)
        if 'code' in result and result['code']>=400:
            error_once_only(self.request, result['message'])
            return super(IndexView, self).form_valid(form)
        msg = 'Submission successfully!'
        messages.success(self.request, msg)
        return super(IndexView, self).form_valid(form)



class MethodRoutingView(LoginRequiredMixin, FormView):
    """Index view for config"""
    template_name = "methodrouting/index.html"
    form_class = MethodRoutingForm
    success_url = reverse_lazy('methodrouting-index')

    def dispatch(self, request, *args, **kwargs):
        self.api = API(request.session.get('obp'))
        return super(MethodRoutingView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MethodRoutingView, self).get_context_data(**kwargs)

        return context

    def get_form(self, *args, **kwargs):
        form = super(MethodRoutingView, self).get_form(*args, **kwargs)
        # Cannot add api in constructor: super complains about unknown kwarg
        fields = form.fields
        form.api = self.api
        try:
            fields['is_bank_id_exact_match'].initial = ""
            fields['method_name'].initial = ""


        except APIError as err:
            messages.error(self.request, err)
        except:
            messages.error(self.request, "Unknown Error")

        return form

    def form_valid(self, form):
        try:
            data = form.cleaned_data
            urlpath = '/management/method_routings'
            payload = {
                "is_bank_id_exact_match": data["is_bank_id_exact_match"],
                "method_name" : data["method_name"],
                "connector_name" : data["connector_name"],
                "bank_id_pattern" : data["bank_id_pattern"],
            }
            result = self.api.post(urlpath, payload=payload)
        except APIError as err:
            error_once_only(self.request, err)
            return super(MethodRoutingView, self).form_invalid(form)
        except Exception as err:
            error_once_only(self.request, "Unknown Error")
            return super(MethodRoutingView, self).form_invalid(form)
        if 'code' in result and result['code']>=400:
            error_once_only(self.request, result['message'])
            return super(MethodRoutingView, self).form_valid(form)
        msg = 'Submission successfully!'
        messages.success(self.request, msg)
        return super(MethodRoutingView, self).form_valid(form)