# core/tests/utils.py
from decimal import Decimal

from django.contrib.auth import get_user_model

from core.models import Recipe


def create_user(
        email='user@example.com',
        password='testpass123',
        **extra_fields
):
    """Helper function to create and return a new user."""
    return get_user_model().objects.create_user(
        email=email,
        password=password,
        **extra_fields,
    )


def create_recipe(user, **params):
    defaults = {
        'title': 'Sample recipe title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdf'
    }
    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe
