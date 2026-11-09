# schomeguard-db — 슈크인의 홈 PC 프로텍터 위협 데이터

[SCHomeGuard](https://github.com/supercre/schomeguard)(슈크인의 홈 PC 프로텍터 — 슈퍼크리에이티브 구성원의 **개인 집 PC 전용**)가 받아 쓰는 위협 정보입니다.
슈퍼크리에이티브 보안관제(SOC)가 **확인한** 위협만 올리고, 모든 항목에 **출처**를 적습니다.

| 파일 | 내용 |
|---|---|
| `intel/bph.txt` | 방탄호스팅 차단 대역 (SOC 방화벽 목록과 동일) |
| `intel/ioc.json` | 확인된 IOC — 도메인·IP·해시·서명자·지속성 흔적 (NIKKE 런처 공급망 공격, DeskRest 프록시웨어 등) |
| `intel/sites.json` | 위험 사이트(끼워팔기 다운로드·악성 서버) — 홈가드가 브라우저 정책으로 차단. 항목마다 분류·이유·출처 |
| `intel/proxyware.json` | 프록시웨어 탐지 정의(이름 패턴·SDK DLL) — 새 브랜드는 클라이언트 업데이트 없이 추가 |
| `models/` (예정) | 온디바이스 판정 모델(임베딩·LoRA)·벡터 DB 차분 패키지 |
| `manifest.json` / `manifest.sig` | 파일 목록·SHA-256과 RSA-SHA256 서명. 홈가드는 서명을 확인한 뒤에만 반영합니다 |

Spamhaus DROP·ASN-DROP처럼 공개 출처가 있는 목록은 여기에 다시 올리지 않고, 홈가드가 원 출처에서 직접 받습니다.
개인 접속 기록 같은 내부 데이터는 올리지 않습니다.

## 갱신
SOC 서버가 `tools/build_manifest.py --key <서명키>`로 manifest를 만들고 서명해 커밋합니다(저장소 전용 deploy key).
서명 키는 SOC 서버에만 있습니다.

## 라이선스
CC0-1.0 (데이터). 오탐·누락 신고는 SOC로 알려 주세요.
