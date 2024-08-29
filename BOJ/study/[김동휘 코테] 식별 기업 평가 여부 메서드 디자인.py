corporate_status_index = {
    "분할합병해산" : 0,
    "합병해산" : 1,
    "청산종결" : 2,
    "회생절차" : 3,
    "해산간주" : 4,
    "보전관리" : 5,
    "기타폐쇄" : 6,
    "분할해산" : 7,
    "청산종결간주" : 8,
    "조직변경해산" : 9,
    "파산" : 10,
    "살아있는동기" : 11,
    "해산" : 12,
    "Null" : 13
}
termination_index = {
    "TAXPAYER" : 0,
    "SIMPLIFIED_TAXPAYER" : 1,
    "DUTY_FREE" : 2,
    "ETC" : 3,
    "CLOSED" : 4,
    "CLOSE_TEMPORARILY" : 5,
    "NO_DATA" : 6,
    "Null" : 7
}

false_cases = [ # 이걸 이차원 배열로
    (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4),
]

def make_result(corporate_status, termination):
    corporate_status = corporate_status_index[corporate_status]
    termination = termination_index[termination]

    cur = (corporate_status, termination)

    if cur in false_cases:
        return False
    else:
        return True
