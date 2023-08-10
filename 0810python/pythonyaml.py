import pandas as pd
import numpy as np
import yaml

with open('./0810python/data/vegetables.yml') as f :
    vegetables = yaml.load(f, Loader= yaml.FullLoader)
    print(vegetables)