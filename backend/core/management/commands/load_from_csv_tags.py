import logging

from recipes.models import Tags

from core.management.commands.load_from_csv import LoadCSVData


logger = logging.getLogger(__name__)


class Command(LoadCSVData):
    logger = logger
    model = Tags
    file_path = './test_data/tags.csv'
    fields = [
        'name',
        'color',
        'slug'
    ]
