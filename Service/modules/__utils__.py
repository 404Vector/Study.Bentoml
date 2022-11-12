import io
import albumentations
import albumentations.pytorch
import numpy as np
import torch
from PIL import Image
    
def transform_image(data) :
    transform = albumentations.Compose([
            albumentations.Resize(height=384, width=384),
            albumentations.Normalize(mean=(0.5, 0.5, 0.5),
                                     std=(0.2, 0.2, 0.2)),
            albumentations.pytorch.transforms.ToTensorV2()
        ])
    image_array = np.array(data, np.float32)
    images = []
    for img in image_array:
        result = transform(image=img)['image']
        images.append(result)
    images = torch.cat(images)
    if images.dim() == 3:
        images = images.unsqueeze(0)
    return images