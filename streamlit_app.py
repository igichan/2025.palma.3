import streamlit as st
import pandas as pd

# 반별 알파벳 과목 매칭
class_alphabets = {
    "3-1": sorted(["C", "I", "B", "F", "D", "E", "J", "G", "H"]),
    "3-2": sorted(["I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-3": sorted(["C", "I", "A", "B", "F", "E", "J", "G", "H"]),
    "3-4": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-5": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-6": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-7": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"]),
    "3-8": sorted(["C", "I", "A", "B", "F", "D", "E", "J", "G", "H"])
}

# 반별 시간표 데이터
timetable_template = {
    "3-1": {"월": ["자율", "C", "I", "진로", "B", "F", "D"],
            "화": ["F", "E", "음악", "D", "화작", "영2", "스생"],
            "수": ["영1", "I", "H", "화작", "창체", "창체"],
            "목": ["D", "E", "B", "J", "C", "스생", "G"],
            "금": ["H", "B", "C", "공강", "G", "음악", "화작"]},
    "3-2": {"월": ["자율", "진로", "I", "A", "B", "F", "D"],
            "화": ["F", "E", "스생", "D", "공강", "화작", "A"],
            "수": ["화작", "I", "H", "영1", "창체", "창체"],
            "목": ["D", "E", "B", "J", "음악", "A", "G"],
            "금": ["H", "B", "음악", "스생", "G", "화작", "영2"]}
}

# Streamlit UI 생성
st.title("📅 팔마 3학년 시간표 생성")

# 반 선택
class_number = st.selectbox("반을 선택하세요", list(timetable_template.keys()))

# 사용자 이름 입력
user_name = st.text_input("이름을 입력하세요")

if user_name:
    # 과목 입력
    subject_mapping = {}
    classroom_mapping = {}

    st.write(f"{class_number} 반에 해당되는 수업: {', '.join(class_alphabets[class_number])}")
    
    for alpha in class_alphabets[class_number]:
        subject_mapping[alpha] = st.text_input(f"{user_name} 님의 {alpha} 과목:", key=f"subject_{alpha}")
        classroom_mapping[alpha] = st.text_input(f"{user_name} 님의 {alpha} 과목 교실:", key=f"classroom_{alpha}")

    # 시간표를 과목명 + 교실 정보로 변환
    def convert_timetable_with_classroom(timetable, subject_map, classroom_map):
        return {
            day: [
                f"{subject_map.get(sub, sub)}<br><small>{classroom_map.get(sub, '교실 미정')}</small>"
                if sub in subject_map else sub
                for sub in subjects
            ]
            for day, subjects in timetable.items()
        }

    # 시간표 HTML 테이블 생성
    def generate_timetable_html(timetable):
        days = ["월", "화", "수", "목", "금"]
        periods = ["1교시", "2교시", "3교시", "4교시", "5교시", "6교시", "7교시"]

        html = "<table style='border-collapse: collapse; width: 100%; text-align: center;'>"
        html += "<tr><th>교시</th>" + "".join(f"<th>{day}</th>" for day in days) + "</tr>"

        for i, period in enumerate(periods):
            html += f"<tr><td>{period}</td>"
            for day in days:
                subject = timetable.get(day, [""] * 7)[i]  # 해당 요일의 i번째 과목 가져오기
                html += f"<td style='border: 1px solid black; padding: 5px;'>{subject}</td>"
            html += "</tr>"

        html += "</table>"
        return html

    # 변환된 시간표 적용
    final_timetable = convert_timetable_with_classroom(timetable_template[class_number], subject_mapping, classroom_mapping)

    # HTML로 변환하여 출력
    st.write(f"### 🏫 {class_number}반 {user_name}의 시간표")
    st.markdown(generate_timetable_html(final_timetable), unsafe_allow_html=True)

st.write("")
st.write("")
st.write("Beta Test")
st.write("@liobadoil")
