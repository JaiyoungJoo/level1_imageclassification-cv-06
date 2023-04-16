import torch
import torch.nn as nn
import torchvision.models as models

from model.base_model import BaseModel


class MyModel(BaseModel):
    """
    Implement this module with your own idea
    """

    def __init__(self, num_classes=18):
        super(MyModel, self).__init__()
        self.my_resnet = models.resnet50(pretrained=True)
        self.my_resnet.fc = nn.Linear(2048, num_classes)

    def forward(self, x):
        x = self.my_resnet(x)

        return x


class EfficientNetB3(BaseModel):
    def __init__(self, num_classes=18):
        super(BaseModel, self).__init__()
        self.my_efficientnetb3 = torch.hub.load("rwightman/gen-efficientnet-pytorch", "efficientnet_b3", pretrained=True)
        self.my_efficientnetb3.classifier = nn.Linear(1536, num_classes)
        print("권장 크기는 300 * 300 size 입니다.")

    def forward(self, x):
        x = self.my_efficientnetb3(x)

        return x


class EfficientNetB4(BaseModel):
    def __init__(self, num_classes=18):
        super(BaseModel, self).__init__()
        self.my_efficientnetb4 = torch.hub.load("rwightman/gen-efficientnet-pytorch", "efficientnet_b4", pretrained=True)
        self.my_efficientnetb4.classifier = nn.Linear(1792, num_classes)
        print("권장 크기는 380 * 380 size 입니다.")

    def forward(self, x):
        x = self.my_efficientnetb4(x)

        return x


class SwinTransformerT(BaseModel):
    def __init__(self, num_classes=18) -> None:
        super().__init__()
        self.swin_t = models.swin_t(weights=models.Swin_T_Weights.IMAGENET1K_V1)
        self.swin_t.head = nn.Linear(self.swin_t.head.in_features, num_classes)
        print("Swin-T")

    def forward(self, x):
        x = self.swin_t(x)
        return x


class SwinTransformerS(BaseModel):
    def __init__(self, num_classes=18) -> None:
        super().__init__()
        self.swin_s = models.swin_s(models.Swin_S_Weights.IMAGENET1K_V1)
        self.swin_s.head = nn.Linear(self.swin_s.head.in_features, num_classes)
        print("Swin-S")

    def forward(self, x):
        x = self.swin_s(x)
        return x


class SwinTransformerB(BaseModel):
    def __init__(self, num_classes=18) -> None:
        super().__init__()
        self.swin_b = models.swin_b(models.Swin_B_Weights.IMAGENET1K_V1)
        self.swin_b.head = nn.Linear(self.swin_b.head.in_features, num_classes)
        print("Swin-B")

    def forward(self, x):
        x = self.swin_b(x)
        return x
