# bento_service.py
import pandas as pd
import numpy as np
from modules import *
from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import ImageInput
from bentoml.frameworks.pytorch import PytorchModelArtifact

@env(infer_pip_packages=True) # 필요 package 자동 추론
@artifacts([PytorchModelArtifact('model')]) # 사용 모델 지정
class MaskGenderAgeClassifierService(BentoService):
    @api(input=ImageInput(), batch=True)
    def predict(self, data):
        images = transform_image(data)
        preds = self.artifacts.model.predict(images)
        return preds
