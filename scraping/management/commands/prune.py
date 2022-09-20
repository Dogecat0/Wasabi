from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Prune scraped data older than X"
