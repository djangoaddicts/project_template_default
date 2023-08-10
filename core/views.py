from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from handyhelpers.views import HandyHelperIndexView


class RegisterUser(generic.CreateView):
    """add a new user"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register_user.html"


class Index(HandyHelperIndexView):
    """render the project index page"""
    title = """Welcome to <span class="text-primary">{{ PROJECT_NAME }}</span><span class="text-secondary"></span>!"""
    subtitle = "Select an option below to get started"
    item_list = [
        {
            "url": "/rest/",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List available RESTful APIs",
        },
    ]
    protected_item_list = [
        {
            "url": "/admin",
            "icon": "fab fa-python",
            "title": "Django Console",
            "description": "Access the django administrator console",
        },
    ]
    protected_group_name = "admin"
