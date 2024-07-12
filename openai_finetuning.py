import openai

# 파인튜닝 작업
openai.FineTuningJob.create(training_file="file", model="gpt-3.5-turbo")

# 전체 작업 확인하기 (최대 10개)
openai.FineTuningJob.list(limit=10)

# 개별 작업 진행상황 확인하기
openai.FineTuningJob.retrieve("xxxxx")

# 파인 튜닝 된 모델로 질문 하기
response = openai.ChatCompletion.create(
    model = "ft:gpt-3.5-turbo-0613:xxxxx::xxxxx",
    messages = [
        {"role": "system", "content": "Kakao Friends Assistant Bot."},
        {"role": "user", "content": "Who is Chunshik in Kakao Friends?"}
    ])