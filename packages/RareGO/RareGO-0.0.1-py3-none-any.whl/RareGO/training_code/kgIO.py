import pykeen
from pykeen.triples import TriplesFactory
from pykeen.datasets import PathDataset



#print(torch.cuda.is_available())


def triple_factory_from_csv(csvpath):
    return TriplesFactory.from_path(csvpath, create_inverse_triples=False)

def pykeen_dataset_from_csv(csvpath):
    return PathDataset.from_path(csvpath)

def train_test_val_split_from_csv(csvpath, splits_ratio=[0.8, 0.1, 0.1]):
    kg=triple_factory_from_csv(csvpath)
    train, test, val=kg.split(splits_ratio)
    return train, test, val




