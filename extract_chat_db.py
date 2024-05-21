import sqlite3
import json


def export_user_data_to_json(user_id: str, db_path: str, output_json_path: str) -> None:
    # 데이터베이스 연결
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # 사용자 ID에 해당하는 데이터 추출
    query = """
    SELECT who_says, says_what
    FROM chatbot_sessions
    WHERE user = ?
    """
    cursor.execute(query, (user_id,))
    rows = cursor.fetchall()

    # 데이터를 JSON 형식으로 변환
    data = [{"who_says": row[0], "says_what": row[1]} for row in rows]

    # JSON 파일로 저장
    with open(output_json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    # 연결 종료
    connection.close()


# 함수 호출 예시
user_id = "b51c6482-ee04-4293-9f70-fb3b4d358aa1"
db_path = './submission/chatbot_v5.db'  # 데이터베이스 파일 경로
output_json_path = 'survey_data.json'  # 출력 JSON 파일 경로
export_user_data_to_json(user_id, db_path, output_json_path)
