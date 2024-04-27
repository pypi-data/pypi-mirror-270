import numpy as np
import pandas as pd
from pickle import dump, load

import torch
import torch.optim as optim
import pykeen
from pykeen.pipeline import pipeline
from pykeen.pipeline import plot
from pykeen import predict
from pykeen.hpo import hpo_pipeline
from pykeen.losses import MarginRankingLoss
from pykeen.losses import BCEWithLogitsLoss, NSSALoss, SoftplusLoss
from pykeen.evaluation import RankBasedEvaluator
from optuna.samplers import GridSampler
from pykeen.sampling import NegativeSampler
from pykeen.datasets import Nations
from pykeen.models import TransE,DistMult,TransH,HolE,RotatE,KG2E

from kgIO import train_test_val_split_from_csv 

from pickle import load, dump 
from pykeen.triples import TriplesFactory


Model_Zoo=['autosf', 'boxe', 'compgcn', 'complex', 'complexliteral', 'conve',
           'convkb', 'cooccurrencefiltered', 'cp', 'crosse', 'distma', 'distmult',
           'distmultliteral', 'distmultliteralgated', 'ermlp', 'ermlpe', 'fixedmodel',
           'hole', 'inductivenodepiece', 'inductivenodepiecegnn', 'kg2e', 'mure',
           'nodepiece', 'ntn', 'pairre', 'proje', 'quate', 'rescal', 'rgcn',
           'rotate', 'se', 'simple', 'toruse', 'transd', 'transe', 'transf',
           'transh', 'transr', 'tucker', 'um']
    

def kge_end2end_pipeline(csvpath=None,split=[0.8, 0.1, 0.1],
                         model_name="autosf",
                         lr=0.001,
                         embedding_dim=1024,
                         n_epochs=200,
                         batchsize=1024,
                         loss="bcewithlogits",
                         negative_sampler='basic', 
                        optimizer='Adam', 
                        training_loop='sLCWA',
                        num_negs_per_pos=10):
      if csvpath is not None:
           train, test, val = train_test_val_split_from_csv(csvpath, splits_ratio=split)
           torch.save(train, 'train')
           torch.save(test,'test')
           torch.save(val, 'valid')
      else:
          train = torch.load('train')
          test = torch.load('test')
          val = torch.load('valid')
    
      result=pipeline(
        random_seed=2000000,
        model=model_name,
        training=train,
        testing=test,
        validation=val,
        
        model_kwargs=dict(embedding_dim=embedding_dim, loss=loss),
    
        
        training_kwargs=dict(num_epochs=n_epochs, batch_size=batchsize),
        
        negative_sampler=negative_sampler,
        negative_sampler_kwargs={'num_negs_per_pos': num_negs_per_pos,},
        
       )
       
      return result

def kge_end2end_pipeline_from_tf(training, testing, validation=None,model_name="autosf",embedding_dim=1024, n_epochs=10, batchsize=1024):
    result=pipeline(
        random_seed=2000000,
        model=model_name,
        training=training,
        testing=testing,
        validation=validation,
        epochs=n_epochs,
        loss=MarginRankingLoss(margin=0.1),
        training_kwargs=dict(num_epochs=n_epochs, batch_size=batchsize),
        negative_sampler='basic',
        negative_sampler_kwargs={'num_negs_per_pos': 10},
        #evaluation_kwargs=dict( batch_size=1024, slice_size=30),
        
       )
    return result


def display_metrics(result, metrics=['mean_rank','mean_reciprocal_rank'], hit_k=[1,5,10]):
    for m in metrics:
        print(f"{m}->{result.metric_results.get_metric(m)}")
    for k in hit_k:
        hits_at_k = result.metric_results.get_metric(f'hits_at_{k}')
        print(f"Hits@{k} -> ", hits_at_k)

def plot_training_error(result):
    plot(result)



def main():
    kgpath="R25KG-Rare - Copy.tsv"
    #ev=kge_end2end_pipeline_from_tf(training=Nations().training, testing=Nations().testing)
    ev=kge_end2end_pipeline(kgpath, model_name="autosf",
                            split=[0.8, 0.1, 0.1],
                            lr=0.001,
                            embedding_dim=1024,
                            n_epochs=200,
                            batchsize=1024,
                            loss="bcewithlogits",
                            negative_sampler='basic', 
                            #optimizer='ADAM',
                            training_loop='sLCWA',
                            num_negs_per_pos=10)

    #dump(ev, open("boxe_bcel_sgd_slwa_200.pyk", 'wb'))
    ev.save_to_directory('autosf_model_gene')
    torch.save(ev.training, 'autosf_training_gene')
    #display_metrics(distma_drug)
    #plot_training_error(ev)
    


if __name__=='__main__':
    #ev=load(open("complexe_bcel_sgd_slwa_200.pyk", 'rb'))
    #display_metrics(ev)
    main()
    