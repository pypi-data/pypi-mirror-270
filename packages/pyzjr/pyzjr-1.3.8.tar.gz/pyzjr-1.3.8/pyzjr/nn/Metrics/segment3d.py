import torch
import torch.nn as nn
import numpy as np
from pyzjr.nn.Metrics.indexutils import hd

class PPV(nn.Module):
    def __init__(self, include_background=True, reduction='mean', eps=1e-5):
        super().__init__()
        self.include_background = include_background
        self.reduction = reduction
        self.eps = eps

    def forward(self, y_pred, y):
        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().detach().numpy()
        if isinstance(y, torch.Tensor):
            y = y.cpu().detach().numpy()
        y_pred_binary = (y_pred > 0.5).astype(int)
        y_binary = (y > 0.5).astype(int)

        tp = np.sum((y_pred_binary == 1) & (y_binary == 1))
        fp = np.sum((y_pred_binary == 1) & (y_binary == 0))
        # tn = np.sum((y_pred_binary == 0) & (y_binary == 0))
        # fn = np.sum((y_pred_binary == 0) & (y_binary == 1))

        numerator, denominator = tp, (tp + fp + self.eps)
        ppv = numerator / (denominator + 1e-5)
        if self.reduction == 'mean':
            ppv = ppv.mean()
        elif self.reduction == 'sum':
            ppv = ppv.sum()
        elif self.reduction == 'none':
            return ppv
        return ppv

class DiceMetric3d(nn.Module):
    def __init__(self, include_background=True, reduction='mean', eps=1e-5):
        super(DiceMetric3d, self).__init__()
        self.include_background = include_background
        self.reduction = reduction
        self.eps = eps

    def forward(self, y_pred, y):
        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().detach().numpy()
        if isinstance(y, torch.Tensor):
            y = y.cpu().detach().numpy()
        y_pred = (y_pred > 0.5).astype(int)
        y = (y > 0.5).astype(int)
        # Compute Dice coefficient
        intersection = np.sum(y_pred * y, axis=(1, 2, 3, 4))
        denominator = np.sum(y_pred, axis=(1, 2, 3, 4)) + np.sum(y, axis=(1, 2, 3, 4))
        dice = (2. * intersection + self.eps) / (denominator + self.eps)

        if not self.include_background:
            dice = dice[1:]

        if self.reduction == 'mean':
            dice = np.mean(dice)
        elif self.reduction == 'sum':
            dice = np.sum(dice)
        elif self.reduction == 'none':
            return dice
        return dice

class MeanIoU3d(nn.Module):
    def __init__(self, include_background=True, reduction='mean', eps=1e-5):
        super(MeanIoU3d, self).__init__()
        self.include_background = include_background
        self.reduction = reduction
        self.eps = eps

    def forward(self, y_pred, y):
        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().detach().numpy()
        if isinstance(y, torch.Tensor):
            y = y.cpu().detach().numpy()

        y_pred_binary = (y_pred > 0.5).astype(int)
        y_binary = (y > 0.5).astype(int)

        intersection = (y_pred_binary & y_binary).sum(axis=(1, 2, 3, 4))
        union = (y_pred_binary | y_binary).sum(axis=(1, 2, 3, 4))

        iou = intersection / (union + self.eps)

        if not self.include_background:
            iou = iou[1:]

        if self.reduction == 'mean':
            iou = np.mean(iou)
        elif self.reduction == 'sum':
            iou = np.sum(iou)
        elif self.reduction == 'none':
            return iou
        return iou

class JaccardMetric3d(MeanIoU3d):
    def __init__(self, include_background=True, reduction='mean', eps=1e-5):
        super(JaccardMetric3d, self).__init__(
            include_background,
            reduction,
            eps
        )

class HausdorffDistanceMetric3d(nn.Module):
    def __init__(self, percentile=95, include_background=True, reduction='mean'):
        super(HausdorffDistanceMetric3d, self).__init__()
        self.percentile = percentile
        self.reduction = reduction
        self.include_background = include_background

    def forward(self, y_pred, y):
        if isinstance(y_pred, torch.Tensor):
            y_pred = y_pred.cpu().detach().numpy()
        if isinstance(y, torch.Tensor):
            y = y.cpu().detach().numpy()

        y_pred_binary = (y_pred > 0.5).astype(int)
        y_binary = (y > 0.5).astype(int)

        distances = hd(y_pred_binary, y_binary)
        hausdorff_distance = np.percentile(distances, self.percentile)
        if isinstance(hausdorff_distance, np.ndarray) and not self.include_background:
            hausdorff_distance = hausdorff_distance[1:]

        if self.reduction == 'mean':
            hausdorff_distance = np.mean(hausdorff_distance)
        elif self.reduction == 'sum':
            hausdorff_distance = np.sum(hausdorff_distance)
        elif self.reduction == 'none':
            return hausdorff_distance

        return hausdorff_distance

if __name__=="__main__":
    batch_size = 2
    num_classes = 3
    depth = 10
    height = 20
    width = 30
    y_pred = np.random.rand(batch_size, num_classes, depth, height, width)
    y = np.random.randint(0, num_classes, (batch_size, num_classes, depth, height, width))  # 这里注意形状为 (batch_size, num_classes, depth, height, width)
    print(y_pred.shape, y.shape)
    y_pred = torch.from_numpy(y_pred)
    y = torch.from_numpy(y)
    dice_metric = DiceMetric3d(include_background=True, reduction="mean")
    miou_metric = MeanIoU3d(include_background=True, reduction="mean")
    hd95_metric = HausdorffDistanceMetric3d(include_background=True, reduction="mean")
    ppv_metric = PPV(include_background=True, reduction="mean")
    dice = dice_metric(y_pred, y)
    miou = miou_metric(y_pred, y)
    hd95 = hd95_metric(y_pred, y)
    ppv = ppv_metric(y_pred, y)
    print(dice, miou, hd95, ppv)