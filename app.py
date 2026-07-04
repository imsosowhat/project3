import streamlit as st

# 1. 반응형 및 커스텀 색상(진한 초록, 베이지)을 위한 CSS 설정
st.markdown(
    """
    <style>
    /* 전체 배경 및 중앙 정렬 */
    .stApp {
        background-color: #FAFAFA;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* 계산기 전체 컨테이너 (모바일 대응 반응형 최대 너비 설정) */
    .calculator-container {
        width: 100%;
        max-width: 400px;
        margin: auto;
        padding: 10px;
    }

    /* 1. 출력창 스타일 (진한 초록색 배경, 흰색 글자, 비율 1) */
    .display-screen {
        background-color: #004D40 !important;
        color: #FFFFFF !important;
        padding: 20px;
        border-radius: 12px;
        text-align: right;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0px 4px 8px rgba(0,0,0,0.3);
        margin-bottom: 15px;
        min-height: 120px; /* 화면 비율 유지를 위한 최소 높이 */
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* 수식 표시 (작은 글씨) */
    .expression-text {
        font-size: 16px;
        color: #A7FFEB !important;
        opacity: 0.8;
        min-height: 24px;
        word-wrap: break-word;
    }
    
    /* 결과값 표시 (큰 글씨) */
    .result-text {
        font-size: 32px;
        font-weight: bold;
        margin-top: 5px;
        word-wrap: break-word;
    }

    /* 2. 자판 구역 스타일 (베이지색 테마, 비율 2) */
    .stButton > button {
        width: 100% !important;
        background-color: #F5F5DC !important; /* 베이지색 */
        color: #424242 !important; /* 진한 회색 글자 */
        font-size: 22px !important;
        font-weight: bold !important;
        border: 1px solid #E0D0C0 !important;
        border-radius: 10px !important;
        padding: 15px 0px !important;
        box-shadow: 0px 3px 5px rgba(0,0,0,0.1);
        transition: all 0.1s ease;
    }
    
    /* 버튼 눌림 효과 */
    .stButton > button:active {
        transform: scale(0.95);
        background-color: #E6E6FA !important;
    }

    /* 특수 버튼 색상 구별 (선택 사항: 연산자나 기능 버튼 스타일링) */
    div[data-testid="stActionButton"] button {
        background-color: #EEDC82 !important; /* 조금 더 짙은 베이지 */
    }
    </style>
    """,
    interactive=False,
    unsafe_allow_html=True
)

# 2. 계산기 상태 관리를 위한 세션 초기화
if "expr" not in st.session_state:
    st.session_state.expr = ""  # 현재 입력 중인 수식
if "result" not in st.session_state:
    st.session_state.result = "0"  # 화면에 표시될 결과값
if "history" not in st.session_state:
    st.session_state.history = ""  # 계산 완료 후 위에 작게 띄울 직전 수식

# 3. 버튼 클릭 이벤트 처리 함수
def press(key):
    if key == "C":
        st.session_state.expr = ""
        st.session_state.result = "0"
        st.session_state.history = ""
    elif key == "◀":
        st.session_state.expr = st.session_state.expr[:-1]
        st.session_state.result = st.session_state.expr if st.session_state.expr else "0"
    elif key == "=":
        if st.session_state.expr:
            try:
                # 일반적인 수학 연산 우선순위로 계산 진행 (eval 사용)
                # 안전한 계산을 위해 나눗셈 기호등 예외 처리 고려
                raw_res = eval(st.session_state.expr)
                
                # 결과값이 소수인 경우 소수점 아래 10자리까지 포맷팅 (불필요한 0 제거)
                if isinstance(raw_res, float):
                    res_str = f"{raw_res:.10f}".rstrip('0').rstrip('.')
                else:
                    res_str = str(raw_res)
                
                st.session_state.history = st.
