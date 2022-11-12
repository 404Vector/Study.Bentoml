import torch
import yaml

class SavePoint():
    def __init__(self, loaded_dict:dict):
        self.weights = loaded_dict['model']
        self.optim = loaded_dict['optim']
        self.args = loaded_dict['args']
        self.save_time = loaded_dict['save_time']

def load_savepoint(path:str) -> SavePoint:
    savepoint = torch.load(path, map_location='cpu')
    return SavePoint(savepoint)

def save_savepoint(savepoint, target_path:str):
    torch.save({
        'model': savepoint.weights, 
        'optim': savepoint.optim, 
        'args': savepoint.args, 
        'save_time': savepoint.save_time,
    }, target_path)