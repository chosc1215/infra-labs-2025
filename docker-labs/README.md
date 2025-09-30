
Docker Labs 

1. 설치/버전 
- `curl -fsSL https://get.docker.com | sh`
- `docker --version` → Docker version 28.4.0, build d8eb465
- `docker compose version` → Docker Compose version v2.39.4

2. 테스트 
- `docker run --rm hello-world` → 도커 실행(스크린 샷)
- `docker run -d --name web -p 18080:80 nginx:stable`  → 컨테이너 안에 Nginx 웹서버를 띄우고, 내 PC에서 18080 포트로 접근 가능(스크린 샷)
- `curl -I http://localhost:18080` → 컨테이너가 뜨고, 포트 매핑도 제대로 됐다는 증거(스크린 샷)

3. 운영 기본
docker ps (실행중인 컨테이너), docker ps -a (실행 중 + 종료된 컨테이너 포함), docker logs -f web (접속 할때 로그 체크) , docker exec -it web bash (컨테이너로 직접 로그인)
,docker stop web (도커 정지), docker start web (도커 시작), docker rm -f web (-f는 강제 즉, 강제 지우기)

4. 트러블슈팅 메모
- Cannot connect to daemon → `sudo service docker start`, WSL systemd 활성화
- 8080 사용 중 포트충돌 발생  → 다른 포트로 `-p 18080:80` 변경

5. 깃허브
- git add → 어떤 파일을 올릴지 선택
- git commit -m "메시지" → 선택한 변경 사항을 “스냅샷”으로 기록
- git push origin main → 로컬에 기록한 걸 GitHub(원격)으로 올림

6.사진 저장
- \\wsl$\Ubuntu-22.04\home\chosc1215\infra-labs-2025\docker-labs\images

