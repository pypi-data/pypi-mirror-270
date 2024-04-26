import numpy as np


def perlin2d(h, w, seed=0):
    """2维Perlin噪声

    :param:h       2维数组，对应每个像素的h坐标
    :param:w       2维数组，对应每个像素的w坐标
    :param:seed    随机数种子
    """
    assert len(h.shape) == len(w.shape) == 2
    n = len(h)
    # 排列表
    np.random.seed(seed)
    ptable = np.arange(n, dtype=int)
    np.random.shuffle(ptable)
    ptable = np.stack([ptable, ptable]).flatten()
    # 格点梯度
    hi, wi = h.astype(int), w.astype(int)
    id00 = ptable[ptable[hi % n] + wi % n] % 4
    id01 = ptable[ptable[hi % n] + wi % n + 1] % 4
    id10 = ptable[ptable[hi % n + 1] + wi % n] % 4
    id11 = ptable[ptable[hi % n + 1] + wi % n + 1] % 4
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
    g00 = vectors[id00]
    g01 = vectors[id01]
    g10 = vectors[id10]
    g11 = vectors[id11]
    # 坐标转化
    hf0, wf0 = h - hi, w - wi
    hf1 = 6 * hf0 ** 5 - 15 * hf0 ** 4 + 10 * hf0 ** 3
    wf1 = 6 * wf0 ** 5 - 15 * wf0 ** 4 + 10 * wf0 ** 3
    # 格点影响力
    c00 = g00[:, :, 0] * hf0 + g00[:, :, 1] * wf0
    c01 = g01[:, :, 0] * hf0 + g01[:, :, 1] * (wf0 - 1)
    c10 = g10[:, :, 0] * (hf0 - 1) + g10[:, :, 1] * wf0
    c11 = g11[:, :, 0] * (hf0 - 1) + g11[:, :, 1] * (wf0 - 1)
    # 插值
    y1 = c00 + hf1 * (c10 - c00)
    y2 = c01 + hf1 * (c11 - c01)
    out = y1 + wf1 * (y2 - y1)
    return out
