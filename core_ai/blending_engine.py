#!/usr/bin/env python3
"""
Module: blending_engine.py
Tính toán tỷ lệ phối trộn tối ưu giữa các bồn nguyên liệu (Vats) 
để đạt cấu trúc hương vị đích (Target Profile) bằng thuật toán tối ưu hóa tuyến tính.
"""

import numpy as np
from scipy.optimize import minimize

class LiquorBlendingEngine:
    def __init__(self, target_vector):
        # Mảng chỉ số hương vị đích: [Độ cồn, Tannin, Este, Độ chua]
        self.target = np.array(target_vector)

    def optimize_blend_ratio(self, available_vats):
        """
        available_vats: Ma trận chứa chỉ số hóa học của các bồn rượu đang có trong kho
        Ví dụ: 3 bồn thô khác nhau về độ đậm đà.
        """
        vats_matrix = np.array([vat['profile'] for vat in available_vats]) # n x 4
        num_vats = len(available_vats)
        
        # Hàm mục tiêu: Giảm thiểu sai số bình phương giữa mẻ trộn và mẻ đích
        def objective(weights):
            current_blend = np.dot(weights, vats_matrix)
            return np.sum((current_blend - self.target) ** 2)

        # Ràng buộc: Tổng tỷ lệ các bồn phối trộn phải bằng 1.0 (100%)
        constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0})
        # Biên độ: Tỷ lệ mỗi bồn từ 0% đến 100%
        bounds = [(0, 1) for _ in range(num_vats)]
        
        # Điểm xuất phát ban đầu (chia đều)
        initial_weights = np.ones(num_vats) / num_vats
        
        res = minimize(objective, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        
        if res.success:
            return {f"Vat_{i}_Ratio": round(w * 100, 2) for i, w in enumerate(res.x)}
         "ERROR: Không tìm được tỷ lệ phối trộn tối ưu."

# Hệ thống chạy thử
# engine = LiquorBlendingEngine(target_vector=[40.0, 1.45, 2.85, 4.15])
# vats = [
#    {"id": "Vat_A", "profile": [42.0, 1.10, 2.30, 3.90]},
#    {"id": "Vat_B", "profile": [38.0, 1.80, 3.10, 4.40]}
# ]
# print(engine.optimize_blend_ratio(vats))
