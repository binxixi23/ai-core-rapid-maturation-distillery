#!/usr/bin/env python3
"""
Module: traceability_ledger.py
Tạo khối dữ liệu append-only (SHA-256) lưu trữ nguồn gốc nguyên liệu nông nghiệp
và các thông số CCP (Critical Control Points) phục vụ thanh tra an toàn thực phẩm.
"""

import datetime
import hashlib
import json

class TraceabilityLedger:
    def __init__(self, batch_id, operator_id):
        self.payload = {
            "batch_id": batch_id,
            "operator_id": operator_id,
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
            "ingredients": {
                "malt_barley_lot": "BARLEY-LOT-A482",
                "water_source_id": "AQUA-PURE-03",
                "enzyme_batch": "ALPHA-ENZ-991"
            },
            "safety_metrics": {
                "max_process_pressure_bar": 3.4,
                "ebeam_absorbed_dose_kgy": 5.42,
                "ccp_status": "PASSED"
            }
        }
        self.block_hash = self.generate_hash()

    def generate_hash(self):
        serialized = json.dumps(self.payload, sort_keys=True)
        return hashlib.sha256(serialized.encode('utf-8')).hexdigest()

    def export_ledger_node(self):
        self.payload["SHA256_Seal"] = self.block_hash
        return self.payload
