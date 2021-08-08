# Lambda 및 DynamoDB 를 사용한 CRUD API 구축

### DynamoDB 테이블에서 항목을 조작하는 서버리스 API 생성

- 구현 순서
    1. [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) 콘솔을 사용하여 DynamoDB 테이블 생성
    2. AWS Lambda 콘솔을 사용하여 [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 함수 생성
    3. API Gateway 콘솔을 사용하여 REST API 생성
    4. API 테스트
- 실행 순서
    - 사용자가 REST API 를 호출하면, API Gateway 는 요청을 Lambda 함수로 라우팅
    - Lambda 함수는 DynamoDB 와 상호 작용하고, API Gateway 에 대한 응답을 반환
    - API Gateway 는 Lambda 로부터 받은 응답을 사용자에게 반환
