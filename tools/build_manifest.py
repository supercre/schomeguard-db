#!/usr/bin/env python3
"""manifest.json 생성 + 서명 (SOC 서버에서 실행).

manifest.json = {product, version(YYYYMMDD.N), files:[{path, sha256, size}]}
manifest.sig  = RSA-SHA256(PKCS#1 v1.5) 서명 — 홈가드는 내장 공개키로 확인한 뒤에만 반영한다.
사용: build_manifest.py --key <private.pem>   (키는 SOC 서버에만 둔다. 저장소에 올리지 않는다)
"""
import argparse, datetime, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INCLUDE = ["intel/bph.txt", "intel/ioc.json", "intel/proxyware.json", "intel/sites.json"]  # 모델·벡터DB는 추가 예정 (models/)

ap = argparse.ArgumentParser()
ap.add_argument("--key", required=True)
a = ap.parse_args()
old = json.loads((ROOT / "manifest.json").read_text()) if (ROOT / "manifest.json").exists() else {}
today = datetime.date.today().strftime("%Y%m%d")
n = int(old.get("version", "0.0").split(".")[1]) + 1 if old.get("version", "").startswith(today) else 1
files = []
for p in INCLUDE + sorted(str(f.relative_to(ROOT)) for f in (ROOT / "models").glob("**/*") if f.is_file()) if (ROOT / "models").exists() else INCLUDE:
    b = (ROOT / p).read_bytes()
    files.append({"path": p, "sha256": hashlib.sha256(b).hexdigest(), "size": len(b)})
m = {"product": "schomeguard-db", "version": f"{today}.{n}", "published": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "files": files}
(ROOT / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
subprocess.run(["openssl", "dgst", "-sha256", "-sign", a.key, "-out", str(ROOT / "manifest.sig"), str(ROOT / "manifest.json")], check=True)
print("manifest", m["version"], len(files), "files")
