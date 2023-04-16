import json

# 사용자명을 받아옴
username = "user1"  # 예시 사용자명

# 리스트에 있는 사용자명
user_list = ["user1", "user2", "user3"]  # 예시 사용자명 리스트

# 사용자명이 리스트에 없을 경우 JSON 응답을 보냄
if username not in user_list:
    response = {
        "status": "error",
        "message": "사용자명이 리스트에 없습니다.",
        "action": "start_guier"
    }
else:
    response = {
        "status": "success",
        "message": "사용자명이 리스트에 있습니다.",
        "action": "ban_user"
    }

# JSON 응답 출력
json_response = json.dumps(response)
print(json_response)
