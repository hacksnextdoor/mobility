import requests

def get_all():
    '''Return list of instantiated bike objects.'''
    return [Jump(), FordBike()]

class BaseBikeClass:
   '''Base class for inheritance by bike provider.'''
   NAME = ''
   BASE_URL = ''
   METADATA = {}

   def all_bikes():
       '''To ensure all_bikes method from base bike class is not inherited.'''
       raise NotImplementedError

class Jump(BaseBikeClass):
   '''Jump bike class inheriting BaseBikeClass attributes and methods.'''
   def __init__(self):
      self.NAME = 'jumpbikes'
      self.BASE_URL = 'jumpbikes.com/opendata'
      self.METADATA = {}

   def all_bikes(self, region):
      if region not in ['atx', 'nyc', 'chi', 'sc', 'dc', 
                        'san', 'sac', 'pvd', 'mia']:
        return f'There are no bikes in {region.upper()}'
        
      url = f'https://{region}.{self.BASE_URL}/free_bike_status.json'
      r = requests.get(url)
      data = r.json()

      return data

class FordBike(BaseBikeClass):
   '''Ford bike class inheriting BaseBikeClass attributes and methods.'''
   def __init__(self):
      self.NAME = 'fordbike'
      self.BASE_URL = 'gbfs.fordgobike.com/gbfs/en/station_status.json'
      self.METADATA = {}

   def all_bikes(self, region):
      region = region.lower()
      # FordBikes is BayArea exclusive (Berkeley, San Francisco, San Jose, etc.)
      if region not in ['san']: 
        return f'There are no bikes in {region.upper()}'

      url = f'https://{self.BASE_URL}'
      r = requests.get(url)
      data = r.json()

      return data

