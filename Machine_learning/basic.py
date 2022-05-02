'''
- 파일처리
    - 객체 생성 및 쓰기
    
        f = open( 'D:/새파일.txt', 'w' )
        for i in range( 1, 6 ):
            data = f'{i}번째 줄입니다.'
            f.write( data )
        f.close()
    
    - 추가
    
        f = open( 'D:/새파일.txt', 'a' )
        for i in range( 6, 11 ):
            data = f'{i}번째 줄 추가입니다.'
            f.write( data )
        f.close()
        
    - 읽기
        - list 형식
        
            f = open( 'D:/새파일.txt', 'r' )
            while 1:
                line = f.readline()
                if not line:
                    break
            f.close()
            
            f = open( 'D:/새파일.txt', 'r' )
            lines = f.readlines()
            for line in lines:
                print( lines )
            f.close()
            
        - 문자열 형식
        
            f = open( 'D:/새파일.txt', 'r' )
            data = f.read()
            print( data )
            f.close()
            
- 파일처리 후 파일 닫기

    with open( 'D:/새파일.txt', 'w' ) as f:
        f.write( 'Now is better than never.' )
    data = f.read() # ValueError: with open 이후 f가 닫혔기 때문에 오류
    
- csv 파일 읽기

    import csv
    f = open('file_name.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdf:
        print(line)
    f.close()
    
    with open('./train.csv') as csvfile:
    rdr = csv.DictReader(csvfile))
    for i in rdr:
        print(i)

#-------------------------------------------------------------------------------

- numpy
    - np.array( [ [ 1, 2, 3, 4, 5 ], [ 2, 3, 4, 5, 6 ] ] )
    - np.arange( 시작값, 끝값, 간격 )
    - np.array( [ 1, 2, 3, 4, 5] ).reshape( ( 3, 2 ) ) # 3행 2열로 생성
    - np.zeros( ( 2, 3 ) ) # 모든 값을 0으로 바꾸고 2행 3열 구조 생성

- numpy slicing
    - ar2[ 0:2, 0:2 ] # 2행 X 2열
     
'''