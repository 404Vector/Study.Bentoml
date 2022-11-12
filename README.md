# Study.Bentoml

## Requirements

- git lfs

```shell
sudo apt-get update
sudo apt install curl
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
```

## 환경 설정

```shell
poetry install
# or
pip install -r requirements.txt
```

## Packing service
```shell
cd Service
python bento_packer.py
```

## Run Frontend

```shell
python -m streamlit run App/frontend.py
```

## Run Backend

```shell
bentoml serve MaskGenderAgeClassifierService:latest
```