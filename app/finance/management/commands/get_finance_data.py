from django.core.management.base import BaseCommand, CommandError
from app.finance import models
import yfinance as yf


class Command(BaseCommand):
    help = 'Get financial information for all the stocks in the list'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        stock_list = models.Stock.objects.all()
        for stock in stock_list:
            tickerData = yf.Ticker(stock.abbreviation)
            tickerDf = tickerData.history(period='1w', start='2019-01-01', end='2019-12-31')

            self.stdout.write(self.style.SUCCESS('Stock Loaded "%s"' % stock.name))
            self.stdout.write(self.style.SUCCESS(str(tickerData.info)))
            self.stdout.write(self.style.SUCCESS(str(tickerData.recommendations.describe())))
            self.stdout.write(self.style.SUCCESS(str(tickerDf.columns)))