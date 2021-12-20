<h1>ShinYoung-Kim's Opensource Term-Project : "Study With Me"</h1>

![header](https://capsule-render.vercel.app/api?type=waving&color=0:EEFF00,100:a82da8&height=120&section=header&text=Study%20With%20Me&fontSize=90&animation=twinkling)
<h2>1. "Study With Me"를 만들게 된 계기</h2>
시험 기간에 밤을 새며 공부하다 보면 이 새벽까지 깨어있는 사람이 나 혼자인 것 같은 기분에 외로움을 느꼈습니다. 그러던 중 우연히 친구와 인스타 라이브를 통해서 서로 공부하는 모습을 공유해보았는데, 누군가 공부하는 모습이 보여서 혼자만 노력하고 있는 것이 아니라는 생각에 크게 위안을 얻었습니다. 그 이후 저는 종종 Study With Me라는 유튜브 영상들을 틀어놓고 공부하곤 합니다. 이번 오픈소스 과제의 주제를 고민하던 중 이런 Study with Me 영상처럼 혼자 공부할 때 위안이 되어줄 수 있고 공부에 자극이 될 수 있는 프로그램을 만들어 보고 싶다는 생각을 하게 되었습니다. 
<h2>2. 주제 구체화 과정</h2>
(1) REC 버튼<br>
예전에 한 친구는 본인만의 공부 비법으로 핸드폰으로 본인이 공부하는 모습을 동영상으로 찍는 것이라고 말해주었습니다. 그 친구는 동영상을 찍으며 스스로가 유튜브 혹은 방송 출연자라고 생각을 하면 누군가 그 영상을 통해 자신의 모습을 지켜보고 있다는 생각에 집중하지 않을 수 없다고 말하였습니다. 그래서 처음에 이 프로젝트의 내용으로 과제나 공부를 하는 동안 화면 중앙 상단에 빨간색 동그라미와 REC 글씨가 떠 있으면 어떨까 고민을 해보았습니다.<br>
![image](https://user-images.githubusercontent.com/83866983/146740643-8ee14afd-02a6-4076-82ca-14de5c3c9843.png)<br>
<참고하려던 영상> https://www.youtube.com/watch?v=K1ryq4vG_Pg<br>
하지만 이를 텀 프로젝트의 주제로 정하기에는 형태가 너무 단순하고, 수업시간에 배운 것을 잘 활용하지 못한다는 생각이 들었습니다.<br>
(2) 채팅창<br>
어느날 여유시간에 게임 유튜버의 영상을 보던 중 하단의 채팅창이 눈에 띄었습니다.<br>
![image](https://user-images.githubusercontent.com/83866983/146741335-8870dab2-388d-41da-bf96-e415e73fb8e7.png)<br>
<출처> 우주하마 유튜브(https://www.youtube.com/watch?v=Oes6zwsuQNs)<br>
가끔 유튜브에서 즐겨보던 Study with Me 영상도 실시간으로 진행되면 우측 댓글란에 실시간 출석이나 반응을 확인할 수 있었던 것처럼 실시간 채팅창을 띄워주는 프로그램이 있다면 원하던 대로 누군가 지켜보는 듯한 느낌에 집중하게 만들기도 하면서 동시에 외롭지 않고 재미있게 과제할 수 있는 프로젝트가 되지 않을까 생각하게 되었습니다.<br>
<h2>3. 제작 단계</h2>
(1) 댓글 준비시키기<br>
기존에 존재하는 영상에서 댓글을 불러와 랜덤하게 뽑아내는 방법과 그런 댓글들로 학습을 시켜 유사한 문장을 만들어내게 하는 방법을 고민해 보았습니다. 전자가 더 쉬운 방법이겠지만 이번 과목에서 배운 내용을 좀 더 사용하고 싶다는 생각에 후자의 방법을 선택하였습니다.<br>
**댓글 불러오기(유튜브 댓글 크롤링)** <br>
검색을 해보니 파이썬에서 크롤링이라는 기능을 이용하면 유튜브 댓글을 불러올 수 있다는 사실을 알게 되었습니다. 더 정확한 문장을 만들어내기 위해선 더 많은 문장이 있으면 좋지 않을까 하는 생각에 제가 봤던 Study with Me 영상 중 가장 댓글이 많은 영상에서 댓글 크롤링을 해보았습니다. <br>
<출처> 연고티비(https://www.youtube.com/watch?v=HMyn6eMV0OA)<br>
<참고한 링크> https://pbj0812.tistory.com/259<br>
**댓글 다듬기** <br>
막상 엑셀파일로 받아보니 사진과 같이 html 태그를 포함한 형태의 댓글들이 꽤 많이 보였습니다. 모든 댓글이 그런 형태로 모여진 것이 아닌 것으로 보아 댓글 하단에 달린 덧글 형태가 html 태그를 포함한 형태로 모인 것이 아닐까 생각이 들었습니다. 덧글은 댓글에 대해 달린 말이라 영상에 대한 내용과 거리가 멀 수도 있으리라 판단하여 html의 br과 a 태그를 포함하고 있는 항목은 삭제하였습니다. <br>
![image](https://user-images.githubusercontent.com/83866983/146743222-ef514968-d559-4bfe-828b-35c3ee6ae519.png)<br>
**학습 전 한 파일에 모으기** <br>
크롤링으로 모은 댓글들은 댓글의 내용뿐만 아니라 아이디나, 날짜, 좋아요 수까지 모아졌습니다. 그래서 수업시간 배웠던 파일 입출력을 이용하여 엑셀에서 댓글의 항목만 텍스트파일로 만들어주었습니다.<br> 
(2) 댓글 학습하기<br>
<참고한 링크 목록><br>
https://wikidocs.net/45101<br>
https://www.youtube.com/watch?v=FQ0vq2CBaL4<br>
https://www.youtube.com/watch?v=QxgXZNoqQrY<br>
https://wikidocs.net/85739<br>
https://omicro03.medium.com/%EC%9E%90%EC%97%B0%EC%96%B4%EC%B2%98%EB%A6%AC-nlp-12%EC%9D%BC%EC%B0%A8-rnn-2-97f1650678b0<br>
찾아보니 문장을 생성하는 방식에는 마르코프체인과 LSTM/RNN 방식이 있었습니다. 마르코프체인 방식은 확률에 기반하여 문장을 생성해내기 때문에 연관성이 떨어지는 문장이 만들어질 수 있다고 하여 RNN 방식으로 문장을 생성하였습니다. 댓글만 모으고 단어집합 형성->훈련 데이터 구성->예측할 단어에 해당되는 레이블 분리->모델 설계의 과정을 거쳐 문장을 생성해보았습니다. 참고하였던 페이지에서 epoch을 200으로 설정해두었는데 학습하는 시간만 해도 2시간 가까이 거리게 되었습니다. 그래서 epoch을 10에서 100까지 세부적으로 조정해보며 관찰해보니 epoch이 50일때부터 100일때까지 loss는 눈에 보일 정도로 감소하긴 하지만 accuracy는 큰 변화없이 0.8대를 유지하는 것을 알게 되었습니다. 그래서 epoch을 50으로 수정해주었습니다. 또한, 특정 단어가 있어야지 그 단어 뒤에 올 단어를 추측하며 문장을 생성해내는 방식이다 보니 매번 단어를 집어넣어줘야 하는 문제가 있었습니다. 그래서 크롤링했던 문장들 중 중립적이거나 긍정적인 뉘앙스의 단어이면서 자주 등장하는 20개의 단어를 골라 seed에 저장하고, sentence_generation 함수를 사용할 때 random을 이용하여 랜덤하게 고르도록 하였습니다.<br>

(3) 댓글창 만들고 띄우기<br>
<참고한 링크 목록><br>
https://deep-eye.tistory.com/44<br>
https://deep-eye.tistory.com/43<br>
https://mr-doosun.tistory.com/10<br>
https://bskyvision.com/1209<br>
https://stackoverflow.com/questions/12328251/how-would-i-draw-a-shadow-under-a-widget-in-qt<br>
https://doc.qt.io/qt-5/qgraphicsdropshadoweffect.html<br>
https://stackoverflow.com/questions/52066040/using-qgraphicsdropshadoweffect-with-multiple-widgets<br>
https://www.geeksforgeeks.org/pyqt5-multi-line-label/<br>
https://kin.naver.com/qna/detail.naver?d1id=1&dirId=10402&docId=360376594&qb=cHlxdDUgbGFiZWwg67OA6rK9&enc=utf8&section=kin.ext&rank=1&search_sort=0&spq=0<br>
https://wikidocs.net/38522<br>
https://stackoverflow.com/questions/57378076/local-variable-count-defined-in-enclosing-scope-on-line-10-referenced-before-a<br>
https://github.com/kairess/animated-wallpaper-sticker/blob/master/Sticker.py<br>

pyqt5를 이용하여 채팅창을 만들고 화면에 띄웠습니다. 먼저 qt designer를 이용하여 ID가 들어갈 자리에 label을 만들어주었습니다. ID와 채팅 글씨에 그림자를 주어 배경이 없어도 화면에서 보이도록 만들었고, 링크를 참고하여 드래그하여 채팅창의 위치를 바꿀 수 있도록 하였습니다. commentChange함수를 만들어 두번재 채팅이 첫번째로, 세번째 채팅은 두번째로 지정해주어 채팅이 위로 올라가는 듯한 효과를 주었고, 세번재 채팅 자리에는 새로운 채팅이 생성되도록 설정하였습니다. 각각의 채팅이 자리를 넘어가도 내용이 짤리지 않고 볼 수 있도록 setWordWrap을 활용하였습니다.<br>
<h2>4. 완성본</h2>
<스크린샷> ![image](https://user-images.githubusercontent.com/83866983/146756263-8028e835-8377-4fba-b3a8-eb06636ce103.png)<br>
<영상(영상 크기가 초과되어서 gif 파일로 올렸습니다.)> ![MainWindow 2021-12-20 22-57-03](https://user-images.githubusercontent.com/83866983/146818202-83968612-a315-489a-ab43-41d43161f7e6.gif)<br>
<h2>:anguished:후에 다시 이 프로그램을 만든다면...(=아쉬운 점):anguished:</h2>
(1) 학습 방식의 변화<br>
생성된 문장이 생각보다 자연스럽지 않았습니다. 하지만 epoch을 늘리기에는 시간이 너무 오래 걸려서 더 나은 학습 데이터를 선정하든 더 나은 학습 방식을 선정하든 하여 더 정제된 문장을 생성해내면 좋을 것 같습니다.<br>
(2) 감성분석<br>
크롤링으로 수집된 문장들이 생각보다 좋은 문장만 가지고 있는 것이 아니었어서 감성분석을 시도하였습니다. 직접 감성 사전을 만들어 보는 방법도 시도해보고, 인터넷에서 구할 수 있는 감성 사전을 이용하여 감성분석을 시도해보았으나 몇 번의 실패를 겪고 감성분석을 제외하고 프로그램을 만들게 되었습니다. 후에 이 프로그램을 다시 시도해본다면 처음 자료에서 감성분석을 통해 부정으로 분류되는 문장을 제거하고 진행한다면 좀 더 힘이 되고 일관성있는 문장이 만들어지지 않을까 생각합니다.<br>
+)고민<br>
이 py 파일을 디버깅할 때 마다 새로 학습을 시작하던데 다시 실행하면 기존에 학습한 내용은 유지하고, 채팅창을 띄우는 부분만 다시 실행할 수는 없을까?<br>
<감성분석 및 다른 학습 방식 시도 흔적 스크린샷><br>
![image](https://user-images.githubusercontent.com/83866983/146761232-a16ca5ed-0886-4f02-a61e-f7348f3e0784.png)<br>
![image](https://user-images.githubusercontent.com/83866983/146761315-aff0dac3-082a-43e7-9b3a-e55fc5572b96.png)<br>
![image](https://user-images.githubusercontent.com/83866983/146761407-790ca2aa-a4ae-4c71-a38d-e0a9107cd7a6.png)<br>
![image](https://user-images.githubusercontent.com/83866983/146761485-f1a46331-9315-4a4a-a1cc-c45a28242257.png)<br>
![image](https://user-images.githubusercontent.com/83866983/146761535-ede09111-e8b4-469c-a21d-faade4ad72ee.png)<br>


