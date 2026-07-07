# MAGMA 가격 모니터링 리포트 (스타터)

경쟁 제품 가격을 **세그먼트별(저가·중가·프리미엄)** 로 모아 정적 웹 리포트로
배포하는 작은 프로젝트입니다. 이 강의에서 **git 과 GitHub 을 실전으로 익히기
위한 출발점**으로 씁니다.

## 무엇이 들어 있나

```
magma-price-report/
├─ build.py                 리포트 생성기 (표준 라이브러리만, 의존성 없음)
├─ templates/report.html.tmpl  리포트 HTML 틀
├─ data/
│  └─ mid.json             중가 세그먼트 (미리 채워진 예시)
├─ sources.md              데이터 출처 목록
└─ .github/workflows/
   ├─ check.yml            PR 마다 도는 자동 검문 (데이터·빌드 검사)
   └─ deploy.yml           main 에 합쳐지면 리포트를 GitHub Pages 로 배포
```

`data/budget.json`(저가) 과 `data/premium.json`(프리미엄) 은 **아직 없습니다.**
이 강의에서 여러분(과 여러분의 에이전트)이 채워 넣을 빈칸입니다.

## 직접 해보기

```bash
# 내려받기 (여러분 계정으로 복제)
gh repo fork --clone dandacompany/magma-price-report

# 리포트 한번 만들어 보기
cd magma-price-report
python3 build.py
open _site/index.html      # 만들어진 리포트를 브라우저로 열기
```

## 배포를 켜는 법 (한 번만)

저장소 **Settings → Pages → Source** 를 **GitHub Actions** 로 바꾸면,
이후 main 에 변경이 합쳐질 때마다 리포트가 자동으로 다시 배포됩니다.

배포 주소는 보통 `https://<your-id>.github.io/magma-price-report/` 입니다.

연습용 메모 한 줄
