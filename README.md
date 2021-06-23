# AutointoZoom
수업시간에 귀찮게 줌을 안들어가도 자동으로 들어가는 시스템

Alpha version all things

Alpha 1.1v start time to json

Alpha 1.2v all five day's data to json

bata 1.0v exe file and fix -> no answer, overload

실행방법 폰트 파일에있는 폰트다운후 disk파일에 있는 "ATZ.exe" 실행 후 "datashool.json"파일에서 조회시간 ,줌 id , 몇교시인지 수정
    "0day" : # 월요일
        {
            "0": "your zoom class id1", #1교시
            "1": "your zoom class id2", #2교시
            "2": "your zoom class id3", #==
            "3": "your zoom class id4", #==
            "4": "your zoom class id5", #==
            "5": "your zoom class id6", #==
            "6": "your zoom class id7", #==
            "period": "6", #몇교시인지
            "freetime": "10", #쉬는시간
            "start_time_Lookup_after_hour": "9", #조회끝나고 수업시작하는 시간 (시)
            "start_time_Lookup_after_minute": "14" #조회끝나고 수업시작하는 시간 (분)
        },
