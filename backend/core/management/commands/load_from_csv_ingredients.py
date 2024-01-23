import logging

from recipes.models import Ingredients

from core.management.commands.load_from_csv import LoadCSVData


logger = logging.getLogger(__name__)


class Command(LoadCSVData):
    logger = logger
    model = Ingredients
    file_path = './test_data/ingredients.csv'
    fields = [
        'name',
        'measurement_unit'
    ]
