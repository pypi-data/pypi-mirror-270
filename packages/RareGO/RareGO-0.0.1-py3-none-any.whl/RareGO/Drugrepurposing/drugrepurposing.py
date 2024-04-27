
from pykeen import predict
import pandas as pd
from pickle import load, dump
import torch



def repurposebytargedIDs(model,model2, targets=['Q8WXI7','Q14982' ,'P42336', 'P35222'], relation="DPI"):
    drug_list=[]
    for tid in targets:
         drugs=predict.predict_target(model=model, tail=tid, relation=relation, triples_factory=model2).df 
         drug_list.append(drugs)
    return pd.concat(drug_list)
    pass
    

def repurposebyGeneIDs(model,model2, targets=['P19544'], relation="GO_MF"):
    drug_list=[]
    for hid in targets:
         drugs=predict.predict_target(model=model, head=hid, relation=relation, triples_factory=model2).df 
         drug_list.append(drugs)
    return pd.concat(drug_list)
    pass

def repurposebyGeneIDsBP(model,model2, targets=['P19544'], relation="GO_BP"):
    drug_list=[]
    for hid in targets:
         drugs=predict.predict_target(model=model, head=hid, relation=relation, triples_factory=model2).df 
         drug_list.append(drugs)
    return pd.concat(drug_list)
    pass

def repurposebyGeneIDsCC(model,model2, targets=['P19544'], relation="GO_CC"):
    drug_list=[]
    for hid in targets:
         drugs=predict.predict_target(model=model, head=hid, relation=relation, triples_factory=model2).df 
         drug_list.append(drugs)
    return pd.concat(drug_list)
    pass
#Q8WXI7 for the ovarian
    #'Q14982' ,'P42336', 'P35222'
        
def repurposebydiseaseID(model,model2, diseaseID=['D010051'], relation="DRUG_DISEASE_ASSOCIATION"):
    disease_drug=[]
    for tid in diseaseID:
        drugs=predict.predict_target(model=model, tail=tid, relation=relation, triples_factory=model2).df 
        disease_drug.append(drugs)
    return pd.concat(disease_drug)
    
    

def repurposebydrugIDs(model,model2,drugs=['DB00112','DB00441','DB01042'], relation="DRUG_DISEASE_ASSOCIATION"):
    drug_disease=[]
    for hid in drugs:
        drugs=predict.predict_target(model=model, head=hid, relation=relation, triples_factory=model2).df 
        drug_disease.append(drugs)
    return pd.concat(drug_disease)
    pass
    
    

def repurposebyFDAdrugNames(model,model2,FDADrugs=['DB00488','DB01042','DB00112','DB00441','DB01042'], relation="DRUG_DISEASE_ASSOCIATION"):
    drugs_FDA=[]
    for hid in FDADrugs:
        drugs=predict.predict_target(model=model, head=hid, relation=relation, triples_factory=model2).df 
        drugs_FDA.append(drugs)
    return pd.concat(drugs_FDA)
    pass
    
    
    
    
    




def main():
    model_file = torch.load('C:/Users/bpatton23/Downloads/Drugrepurposing/quate_model/trained_model.pkl')
    print(model_file)
    model_file2 = torch.load('C:/Users/bpatton23/Downloads/Drugrepurposing/quate_model/quate_training')
    print(model_file2)
    print(type(model_file))
    model= model_file
    model2=model_file2
    #model_drugs=repurposebytargedIDs(model,model2)
    disease_drug=repurposebydiseaseID(model,model2)
    #drugID_drugs=repurposebydrugIDs(model,model2)
    #FDA_drugs=repurposebyFDAdrugNames(model,model2)
    #Gene=repurposebyGeneIDs(model,model2)
    #GeneBP=repurposebyGeneIDsBP(model,model2)
    #GeneCC=repurposebyGeneIDsCC(model,model2)
    #print(model_drugs)
    print(disease_drug)
    #print(drugID_drugs)
    #print(FDA_drugs)
    #print(Gene)
    #print(GeneBP)
    #print(GeneCC)
    #model_drugs.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/proje_model/proje_drugs_ovarian', index=False, sep='\t')
    disease_drug.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/quate_model/disease_drugs_ovarian', index=False, sep='\t')
    #drugID_drugs.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/quate_model/drugID_disease_ovarian', index=False, sep='\t')
    #FDA_drugs.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/proje_model/drugFDA_disease_ovarian', index=False, sep='\t')
    #Gene.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/crosse_model_gene/Gene_IDMF_meso', index=False, sep='\t')
    #GeneBP.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/crosse_model_gene/Gene_IDBP_meso', index=False, sep='\t')
    #GeneCC.to_csv('C:/Users/bpatton23/Downloads/Drugrepurposing/crosse_model_gene/Gene_IDCC_meso', index=False, sep='\t')

if __name__=="__main__":

    main()



