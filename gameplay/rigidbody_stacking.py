import math

def solver_iterations(contacts, base):
    """迭代次数。"""
    raise NotImplementedError("TODO: solver_iterations")

def manifold_points(count):
    """接触流形点数。"""
    raise NotImplementedError("TODO: manifold_points")

def sleep_ok(linear, angular, lt, at):
    """休眠判定。"""
    raise NotImplementedError("TODO: sleep_ok")

def mass_ratio_clamp(m1, m2, maximum):
    """质量比钳制。"""
    raise NotImplementedError("TODO: mass_ratio_clamp")

def ccd_enabled(speed, threshold):
    """CCD 开关。"""
    raise NotImplementedError("TODO: ccd_enabled")

def fixed_step(dt, step):
    """固定步长。"""
    raise NotImplementedError("TODO: fixed_step")

def friction_cone(normal, mu):
    """摩擦锥。"""
    raise NotImplementedError("TODO: friction_cone")

def stable_order(ids):
    """稳定求解顺序。"""
    raise NotImplementedError("TODO: stable_order")

def sync_angular(omega):
    """同步角速度。"""
    raise NotImplementedError("TODO: sync_angular")

def cluster_count(count, limit):
    """分簇数量。"""
    raise NotImplementedError("TODO: cluster_count")

def penetration(depth, percent, slop):
    """穿透修正。"""
    raise NotImplementedError("TODO: penetration")

def contact_id(seed, index):
    """接触 id。"""
    raise NotImplementedError("TODO: contact_id")

def manifold_area(width, height):
    """流形面积。"""
    raise NotImplementedError("TODO: manifold_area")

def sleep_counter(frame, threshold):
    """休眠计数。"""
    raise NotImplementedError("TODO: sleep_counter")

def stack_height(levels):
    """堆叠高度。"""
    raise NotImplementedError("TODO: stack_height")
