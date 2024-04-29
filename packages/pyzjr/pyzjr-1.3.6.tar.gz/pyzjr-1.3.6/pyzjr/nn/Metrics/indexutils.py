import torch
import numpy as np
from scipy.ndimage import _ni_support, binary_erosion, distance_transform_edt, generate_binary_structure

def _surface_distances(y_pred, y, voxelspacing=None, connectivity=1):
    """
    计算两个二值对象中表面体素之间的距离
    """
    y_pred = np.atleast_1d(y_pred.astype(np.bool_))
    y = np.atleast_1d(y.astype(np.bool_))
    if voxelspacing is not None:
        voxelspacing = _ni_support._normalize_sequence(voxelspacing, y_pred.ndim)
        voxelspacing = np.asarray(voxelspacing, dtype=np.float64)
        if not voxelspacing.flags.contiguous:
            voxelspacing = voxelspacing.copy()

    # binary structure
    footprint = generate_binary_structure(y_pred.ndim, connectivity)

    # test for emptiness
    if 0 == np.count_nonzero(y_pred):
        raise RuntimeError(
            "The first supplied array does not contain any binary object."
        )
    if 0 == np.count_nonzero(y):
        raise RuntimeError(
            "The second supplied array does not contain any binary object."
        )
    result_border = y_pred ^ binary_erosion(y_pred, structure=footprint, iterations=1)
    reference_border = y ^ binary_erosion(
        y, structure=footprint, iterations=1
    )
    dt = distance_transform_edt(~reference_border, sampling=voxelspacing)
    sds = dt[result_border]

    return sds

def hd(y_pred, y, voxelspacing=None, connectivity=1):
    """
    Hausdorff Distance.
    Hausdorff距离衡量了两个点集之间的最大不匹配程度。在此函数中，它用于计算两个二值图像（result和reference）的表面体素之间的最大不匹配距离。

    Args:
        y_pred (array_like): 预测的二值图像，形状与参考图像（y）相同。
        y (array_like): 参考的二值图像，形状与预测图像（y_pred）相同。
        voxelspacing (array_like, optional): 形状为（N，）的数组，表示每个维度上的体素间距。默认为None。
        connectivity (int, optional): 表面距离计算中使用的连接性。默认为1，表示3D中的26连通（在3D情况下）或2D中的8连通（在2D情况下）。

    Returns:
        float: Hausdorff距离，即两个图像表面体素之间的最大不匹配距离。
    """
    hd1 = _surface_distances(y_pred, y, voxelspacing, connectivity).max()
    hd2 = _surface_distances(y, y_pred, voxelspacing, connectivity).max()
    hausdorff = max(hd1, hd2)
    return hausdorff

def hd95(y_pred, y, voxelspacing=None, connectivity=1):
    """
    计算 Hausdorff 距离的 95% 的数据点的值
    """
    hausdorff = hd(y_pred, y, voxelspacing, connectivity)
    return np.percentile(hausdorff, 95)

def ignore_background(y_pred, y):
    """
    Used to remove the background (first channel) of "yyred" and "y".
    Args:
        y_pred: predictions. As for classification tasks, `y_pred` should has the shape [BN] where N is larger than 1. As for segmentation tasks,
        the shape should be [BNHW] or [BNHWD].
        y: ground truth, the first dim is batch.
    """
    y = y[:, 1:] if y.shape[1] > 1 else y
    y_pred = y_pred[:, 1:] if y_pred.shape[1] > 1 else y_pred
    return y_pred, y


if __name__=="__main__":
    y_pred = np.random.randint(0, 3, size=(100, 100))
    y = np.random.randint(0, 3, size=(100, 100))
    hausdorff_distance = hd95(y_pred, y)
    print("Hausdorff Distance:", hausdorff_distance)

    batch_size = 1
    num_channels = 3
    depth = 2
    height = 2
    width = 2

    y_pred = torch.rand(batch_size, num_channels, depth, height, width)
    y_true = torch.rand(batch_size, num_channels, depth, height, width)
    print("Shape of y_pred:", y_pred.shape)
    print("Shape of y_true:", y_true.shape)