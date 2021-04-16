# twit-pipeline

## 개요
[토크온 세미나 (GCP 기반 데이터 엔지니어링)](https://www.youtube.com/watch?v=0TOjxSDsH7k&ab_channel=SKplanetTacademy) 를 듣고 따라 만들어봄.  
Twitter API 를 이용해 실시간으로 트윗을 스트리밍하여 GCP PUBSUB 으로 트윗을 송신하는 데이터 파이프라인.

## 프로젝트 구조
```
Twitter --> Python --> PUB/SUB --> Clound Function --> BigQuery
```
* Python 스크립트를 이용하여 twitter API 를 호출하고 사용자 twit 데이터를 불러옴
* Twit 데이터를 PUB/SUB 으로 publish.
* Cloud Function 은 PUB/SUB 의 topic 을 구독하고 있다가 데이터가 들어오면 BigQuery 로 데이터를 전송.
* BigQuery 에서 쿼리 실행 및 데이터 조회.

## Configuration
[resources](./resources) 디렉토리에 설정 파일 존재. [```config.example.yaml```](./resources/config.example.yaml) 을 ```config.yaml``` 로 수정하고 설정 값을 적절히 수정해주자.  
그리고 본인 google credential JSON 파일을 [resources](./resources) 디렉토리에 넣어줘야 함.

```
twit:
  api_key: "API_KEY"
  api_secret_key: "API_SECRET_KEY"
  access_token: "ACCESS_TOKEN"
  access_token_secret: "ACCESS_TOKEN_SECRET"

google:
  credential-file-name: 'YOUR_GOOGLE_CREDENTIAL_JSON_FILE_NAME'
  pubsub_topic: 'YOUR_PUBSUB_TOPIC'
```

* ```twit.*```: Twitter API 사용시 필요한 라이센스.
* ```google.credential-file-name```: 구글 credential JSON 파일명.
* ```google.pubsub_topic```: GCP pubsub topic 명.

## Import conda env
```
$ conda env create -n twit-pipeline -f conda.yaml \
    && conda activate twit-pipeline
```

## RUN
```
$ python -m twitpipeline.main
```

## LINT
```
$ pylint twitpipeline
```

## Type check
```
$ mypy --check-untyped-defs --ignore-missing-imports twitpipeline
```

## TODO
현재 파이프라인에서는 ```GCP PUBSUB``` 으로 트윗 데이터를 송신한 다음 subscription 을 ```GCP cloud function``` 으로 처리하고 있다. 개인적으로 ```GCP cloud function``` 은 디버깅하기 힘들어서 별로인 것 같다. 한번 배포한 함수를 수정하는 기능도 없고, 테스트 기능도 부실하다. 그나마 이번 프로젝트에서는 subscriber 코드가 간단해서 cloud function 을 사용하긴 했는데 subscriber 의 기능이 복잡해지면  
cloud function 을 사용하는 것 보다는 직접 구축하는게 나을 것 같다. 디버깅하기 힘들어서 유동적으로 대응하기 힘듬. ```GCP PUBSUB``` 대신 ```Kafka``` 또는 ```RabbitMQ``` 을 사용하고, subscriber 를 python 으로 구현 한 뒤
데이터 웨어하우스를 ```ODB``` 를 사용해보자.

## 소감
데이터 처리에는 python 이 유리하다고 해서 python 으로 구현을 해봤다. 평소에 spring 을 쓰다가 python 을 쓰려니  
DI 가 안돼서 불편했다. 그래도 python 이 컴파일은 하지 않아도 돼서 java 와 다르게 가볍게 실행되는점이 좋은 것 같다. 다음에는  
spring java (아니면 kotlin) 으로 데이터 처리를 해보고 python 과 비교를 해봐야 겠다.
