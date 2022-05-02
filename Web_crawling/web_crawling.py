'''
CRUD: Create, Read, Update, Delete
     : POST, GET, PUT, Delete
     
# 응답코드
    - 1xx: 조건부응답
    - 2xx: 성공
    - 3xx: 리다이렉션 (새로고침) 완료
    - 4xx: 요청 (클라이언트) 오류
    - 5xx: 서버 (서버) 오류

# URL
    - 프로토콜://주소 또는 IP:포트번호/리소스 경로?쿼리스트링
        - 포트번호는 http를 사용할 경우 80번 포트를 사용한다는 의미가 되므로 생략 가능
        - 리소스 경로: 한 사이트에서 페이지를 옮길 때마다 다르게 표현, 데이터를 포함하기도 함
        - 쿼리스트링: 데이터가 포함되는 부분, 변수=데이터&변수=데이터 의 형식
        
# 웹 페이지 구성 요소
    - HTML: 하이퍼텍스트 마크업 언어
    
            <!DOCTYPE html>
            <html lang = 'en'></html>
            <head>
                <meta charset = 'UTF-8'
                <title>Title</title>
            </head>
            <body>
                <h1>
                    <p>1문단</p>
                    <p>2문단</p>
                    <p>3문단</p>
                </h1>
                <ul>
                    <li>2</li>
                </ul>
                <ol>
                    <li>3</li>
                </ol>
            </body>
            </html>
            
            style, link 태그: css 코드가 담겨있는 태그
            script 태그: Javascript 코드가 포함된 태그
            
            <meta name = '', content = ''>: 문서의 정보
            <h1, h2, ...>: 글자 크기 조정, 숫자가 작을수록 크기 커짐
            <p></p> = <span></br><span>: 문단으로 글 쓰기
            <ul><li>: 리스트 만들기 (점으로 표현)
            <ol><li>: 리스트 만들기 (숫자로 표현)
            <table>: 표를 표현, thead, tbody를 가지고 있을 수 있고 , tr을 이용하여 행표현
                     th (가운데정렬, 굵은 글씨체), td를 이용해 행의 컬럼 표현
            <input>: 데이터를 넣을 수 있는 폼 생성 ex) <input type='text' value = 'test1'>, 닫는 태그 없음
                     type에 button을 넣으면 버튼 생성 가능
            <button>: 버튼 만들기, <button>bt1</button>
            <select>: 선택 리스트 만들기
                      <select name = 'address'>
                        <option value=''>주소선택</option>
                        <option value='파주'>파주</option>
                        <option value='혜화'>혜화</option>
            a 태그: 다른 페이지로 이동
                    
                    # 주소입력
                    <ul>
                        <li>
                            <a href='http://www.naver.com'>네이버로 이동하기</a>
                        </li>
                    </ul>
                    
                    # 상대경로, 절대경로
                    - 상대경로
                        <a href='a'>: 현재 내가 있는 www.option.com에서 www.option.com/a 로 이동
                    - 절대경로
                        <a href='/a'>: 어느 페이지에 있던지 www.option.com/a 로 이동
            <img src='frog.png' alt='개구리'>: 이미지 포함, alt = 이미지 오류 시 대체 문구
            <div>: 페이지 레이아웃을 잡는 용도, 중첩하여 사용할 경우 상위 돔, 하위 돔으로 나눠서 부름
              
    2. CSS
        
        웹 사이트를 꾸며주는 역할
        
        Selector: 꾸미기 위해 특정 요소에 접근하는 것, .으로 class 선언, #으로 id 선언
                  selector.class 방식으로 선언하여 해당 class가 붙은 것에만 적용
                  class는 여러개일수 있으나 id는 페이지당 하나 
        <head>
            <title>Title</title>
            <style>
                p.p-target{
                    font_size: 17px;
                    color: blue;
                }       
                
                #target1{
                    list-style-type: none;
                }
            </style>
        </head>
        <body>
            <p class = 'p-target'>p 태그2</p>
            
        div#container div#wrap1 h3: id가 container인 div 태그 아래 아이디가 wrap1인 태그 중 h3태그 찾기
                                    자식 태그는 띄어쓰기로 표현 
            







'''
