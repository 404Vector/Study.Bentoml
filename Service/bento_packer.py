# bento_packer.py
from modules import *

savepoint = load_savepoint("../Assets/vit_save.tar")
model = load_model(savepoint)

# bento_service.py에서 정의한 IrisClassifier
from bento_service import MaskGenderAgeClassifierService

# IrisClassifier 인스턴스 생성
service = MaskGenderAgeClassifierService()

# Model Artifact를 Pack
service.pack('model', model)

# Model Serving을 위한 서비스를 Disk에 저장
service.save()
