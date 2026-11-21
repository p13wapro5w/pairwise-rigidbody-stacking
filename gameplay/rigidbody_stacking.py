import math


def solver_iterations(contacts, base):
    """迭代次数按接触数自适应。

    固定迭代次数在高层堆叠接触力尚未收敛时就结束本帧求解，箱子会自己抖。
    每个接触至少分配两轮冲量迭代，接触越多需要的迭代越多，但不低于基线。
    """
    return max(base, contacts * 2)


def manifold_points(count):
    """接触流形保留多点（箱体最多保留底面四个角点）。

    物体对只缓存一个接触点时箱底四角只解一个，扭矩约束不足。流形点数随
    实际接触数给出，并钳制在 1..4（凸多边形流形的标准上限）。
    """
    return max(1, min(count, 4))


def sleep_ok(linear, angular, lt, at):
    """休眠判定：线速度和角速度同时低于各自阈值才允许休眠。

    只看线速度会让缓慢自旋的物体提前睡着，被撞后又醒来，造成堆叠抖动。
    """
    return bool(linear <= lt and angular <= at)


def mass_ratio_clamp(m1, m2, maximum):
    """质量比钳制。

    质量比跨三个数量级时轻箱子会被重箱子挤穿。取两质量的较大比值并钳制
    在 maximum 之内，返回求解器实际使用的有效质量比。
    """
    ratio = max(m1 / m2, m2 / m1)
    return float(min(ratio, maximum))


def ccd_enabled(speed, threshold):
    """CCD 开关：速度达到阈值即开启连续碰撞检测。

    堆叠底层虽慢，但只要相对速度达到阈值同样开启，避免缓慢穿透无人处理。
    """
    return bool(speed >= threshold)


def fixed_step(dt, step):
    """物理固定步长。

    物理步长不跟随渲染帧 dt，帧率抖动时始终按固定 step 推进（渲染插值在
    调用侧处理），堆叠高度不会随帧率周期性起伏。
    """
    return step


def friction_cone(normal, mu):
    """摩擦锥：给定法向力与摩擦系数，返回摩擦锥允许的最大摩擦力。

    多方向摩擦锥在切平面内各向同性地施加 |ft| <= mu * fn 的约束，替代
    单方向近似，斜推整摞箱子时不会整体滑走。
    """
    return mu * normal


def stable_order(ids):
    """稳定求解顺序：按稳定 id 排序，替代哈希表遍历顺序。

    哈希表遍历顺序每帧不同会导致求解结果不确定；按 id 排序保证逐帧确定、
    可复现的接触求解顺序。
    """
    return sorted(ids)


def sync_angular(omega):
    """网络同步角速度。

    同步报文必须携带角速度，客户端不能只靠位置自行推算，否则箱子会自己转。
    原样回传以纳入同步通道。
    """
    return omega


def cluster_count(count, limit):
    """分簇数量：物体数超限时分簇求解而不是禁用碰撞。

    向上取整的均分簇数，保证每簇不超过 limit，且所有物体仍参与碰撞。
    """
    return (count + limit - 1) // limit


def penetration(depth, percent, slop):
    """穿透修正（Baumgarte 风格）。

    修正量 = max(depth - slop, 0) * percent，slop 以内的微穿透不修正，
    避免物体持续抖动。
    """
    return max(depth - slop, 0.0) * percent


def contact_id(seed, index):
    """接触点稳定 id：物体对 seed 加流形内点位 index，格式 "seed:index"。"""
    return "{}:{}".format(seed, index)


def manifold_area(width, height):
    """流形覆盖面积，用于评估多点流形的接触支撑范围。"""
    return width * height


def sleep_counter(frame, threshold):
    """休眠计数：低速状态累计帧数达到阈值才真正休眠。"""
    return bool(frame >= threshold)


def stack_height(levels):
    """堆叠高度（层数）。层数即堆叠级别，用于分簇与稳定性统计。"""
    return levels
