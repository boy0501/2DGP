1.

-제목 I WANNA DO BOSSRUSH (IWDB) (원작 I WANNA BE THE BOSHY (IWBTB))



![보시](res\보시.png)



-게임의 목적은 패턴을 피하며 총알을 발사해

보스를 잡는것입니다.

---

2. **GAMESTATE(SCENE)의 수 및 각각의 이름**

Scene의 수 : 6개

a.Logo Scene

b.게임 시작 전 Scene

c.보스 선택 가능 Scene

d.보스와의 싸움 Scene

e.랭킹 Scene

f.일시중지 Scene

---

3.

각 Scene 끼리의 이동 가능 도시화

![도식화](res\도식화.png)



a.게임 시작전 Scene

게임시작,랭킹,게임종료 3가지 선택을 할 수 있는 Scene 

![게임시작전](res\게임시작전.png)

b. 보스 선택 Scene

보스를 선택하는 Scene

Enter 시 보스 싸움 Scene으로 간다.  하지만 난 보스 한개만 만들것이다.

![보스선택](res\보스선택.png)

c. 보스와의 싸움 Scene

본격적으로 보스와 싸울수 있는 Scene이다.

공격시 총알이 직진으로 나간다.

![보스](res\보스.png)

d. 일시중지 Scene

여러가지 Scene으로 이동 가능한 Pause Scene이다.

![일시정지](res\일시정지.png)

e.

랭킹 Scene

![랭크](res\랭크.png)

f. Logo Scene

별다를건 없이 kpu 로고를 보여주며

2초뒤 게임 시작 전 Scene으로 넘어간다. 

---

4.

**다른과목에서 배운 기술**

* 이미지 바운딩 충돌처리

---

**기대되는 기술**

* 제가 뭘 배울지 잘 모르겠습니다.

* 맵 툴 관련 대해서는 배울것같은데 기대됩니다.

---

**수업에서 다루면 좋을것 같은 기술들**

* win32 api 에서는 alphablend() 를 통해 이미지를 투명화 시켜줄 수 있었는데

pico2d에서는 어떻게 하는 지 궁금합니다.

* 또한 win32 api 에서는 bitblt() 를 이용하여 큰 이미지를 로드해서 일부분만 읽는게 가능했는데

pico2d 에서는 어떻게 하는지 궁금합니다.

* 또한 win32 api 에서는 TransparenBlt() 함수를 이용하여 이미지파일에서 특정 색을 무시할 수 있었는데 pico2d에서는 어떻게 하는지 궁급합니다.

* 또한 sound effect 같은걸 추출하는법이 있다면 알고싶습니다.

