# -*- coding: utf-8 -*-
"""Compute 15주차 theoretical expected values and emit _expected.json + paste-ready
cache lines. This is the per-week 'compute' artifact in the token-efficient workflow:
the main agent runs it instead of hand-typing ~100 values, and _verify_checklist.py
cross-checks 요구목록.md against the JSON it writes.

Physics (book circuit models + nameplate values + lecture-note E_s = 5 Vpp override,
ideal inductor R_l ~= 0). Keys MUST match the cache's table codes and unit-stripped
column names exactly, so verify's equality check is meaningful.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).parent


def f3(x): return f"{x:.3f}"
def f4(x): return f"{x:.4f}"
def f2(x): return f"{x:.2f}"
def f0(x): return f"{x:.0f}"


# ---- Table 14.2: parallel resonant, E_s -> R_s(100k) -> tank[(R+jXL)||(-jXC)] ----
Es, Rs, R142, L142, C142 = 5.0, 100e3, 4.7, 10e-3, 0.1e-6
F142 = [500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000,
        5033, 4900, 4980, 5100, 5200]
VC, VRs, Is, Zp = [], [], [], []
for f in F142:
    XL = 2 * math.pi * f * L142
    XC = 1 / (2 * math.pi * f * C142)
    Ztank = (complex(R142, XL) * complex(0, -XC)) / (complex(R142, XL) + complex(0, -XC))
    Im = abs(Es / (Rs + Ztank))
    VC.append(f3(Im * abs(Ztank)))
    VRs.append(f3(Im * Rs))
    Is.append(f4(Im * 1e3))
    Zp.append(f0(abs(Ztank)))

# ---- Table 15.2 / 15.3: HPF R=1k C=0.1u ----
Vi, Rh, Ch = 5.0, 1000.0, 0.1e-6
F152 = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 4.0, 5.0, 6.0,
        8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 40.0, 60.0, 100.0]
Vo152, Av152 = [], []
for fk in F152:
    XC = 1 / (2 * math.pi * fk * 1e3 * Ch)
    av = Rh / math.hypot(Rh, XC)
    Vo152.append(f3(av * Vi)); Av152.append(f4(av))
F153 = [0.1, 0.2, 0.6, 1, 2, 6, 10, 12, 20, 40, 60, 100]
TH = [f2(math.degrees(math.atan((1 / (2 * math.pi * fk * 1e3 * Ch)) / Rh))) for fk in F153]

# ---- Table 15.5: BPF series RLC R=100 L=10mH C=0.1u ----
Rb, Lb, Cb = 100.0, 10e-3, 0.1e-6
F155 = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 4.0, 4.30, 5.0,
        5.033, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 40.0, 60.0, 100.0]
Vo155, Av155 = [], []
for fk in F155:
    XL = 2 * math.pi * fk * 1e3 * Lb
    XC = 1 / (2 * math.pi * fk * 1e3 * Cb)
    av = Rb / math.hypot(Rb, XL - XC)
    Vo155.append(f3(av * Vi)); Av155.append(f4(av))

# ---- Table 15.7: band-stop parallel tank in series R=100 L=1mH C=0.2u ----
Rs2, Ls, Cs = 100.0, 1e-3, 0.2e-6
F157 = [0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 3.0, 4.0, 5.0, 6.0,
        7.957, 8.0, 10.0, 11.255, 12.0, 14.0, 15.916, 16.0, 18.0, 20.0, 40.0, 60.0, 100.0]
Vo157, Av157 = [], []
for fk in F157:
    XL = 2 * math.pi * fk * 1e3 * Ls
    XC = 1 / (2 * math.pi * fk * 1e3 * Cs)
    if abs(XC - XL) < 1e-9:
        av = 0.0
    else:
        Xt = XL * XC / abs(XC - XL)
        av = Rs2 / math.hypot(Rs2, Xt)
    Vo157.append(f3(av * Vi)); Av157.append(f4(av))

data = {
    "Table 14.2 (주파수 스윕)": {"V_C(p-p)": VC, "V_Rs(p-p)": VRs, "I_s(p-p)": Is, "Z_p": Zp},
    "Table 15.2 (V_o·A_v 스윕)": {"V_o(p-p)": Vo152, "A_v": Av152},
    "Table 15.3 (위상 θ)": {"θ (V_o lead)": TH},
    "Table 15.5 (V_o·A_v 스윕)": {"V_o(p-p)": Vo155, "A_v": Av155},
    "Table 15.7 (V_o·A_v 스윕)": {"V_o(p-p)": Vo157, "A_v": Av157},
    "_anchors": {
        "Table 14.2 (주파수 스윕)": {"f_p": "5033"},
        "Table 15.2 (V_o·A_v 스윕)": {"f_c": "1592"},
        "Table 15.5 (V_o·A_v 스윕)": {"f_s": "5033"},
        "Table 15.7 (V_o·A_v 스윕)": {"f_p": "11254"},
    },
}

out = HERE / "_expected.json"
out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"wrote {out}")
print("\n-- paste-ready expected lines (verify against 요구목록.md) --")
for code, cols in data.items():
    if code == "_anchors":
        continue
    print(f"[{code}]")
    for cname, vals in cols.items():
        print(f"  {cname} | expected: {', '.join(vals)}")
