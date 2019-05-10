import requests

def get_all():
    return [Jump()]

class BaseBikeClass:
   NAME = ''
   BASE_URL = ''
   METADATA = {}

   def all_bikes():
       raise NotImplementedError

class Jump(BaseBikeClass):
   def __init__(self):
      self.NAME = 'jumpbikes'
      self.BASE_URL = 'jumpbikes.com/opendata'
      self.METADATA = {}

   def all_bikes(self, region):
      if region not in ['atx', 'nyc', 'chi', 'sc', 'dc', 'san', 'sac', 'pvd', 'mia']:
        raise Exception("There are no bikes in {0}".format(region))
      url = "https://{0}.{1}/free_bike_status.json".format(region, self.BASE_URL)
      r = requests.get(url)
      data = r.json()
      return data