# Edge AI Pipeline Starter

Project nay mo phong mot pipeline Edge AI/CI-CD co the hoc va mo rong:

1. Train model tu data mau
2. Optimize model thanh artifact deploy duoc
3. Test inference
4. Deploy len "device" gia lap
5. Observe prediction logs
6. Rollback khi model loi

## Cau truc

- `data/train.csv`: du lieu train 2D don gian
- `src/train.py`: train model centroid classifier
- `src/optimize.py`: tao artifact deploy
- `src/infer.py`: chay inference tren edge
- `src/observe.py`: thong ke log prediction
- `tests/test_pipeline.py`: test train + optimize + infer
- `scripts/deploy.sh`: deploy model moi len device
- `scripts/rollback.sh`: quay lai version truoc
- `.github/workflows/edge-ai.yml`: CI pipeline mau

## Chay local

```bash
python3 src/train.py
python3 src/optimize.py
python3 -m unittest discover -s tests
./scripts/deploy.sh
python3 src/infer.py --x 1.0 --y 1.1
python3 src/observe.py
```

## Flow mapping voi hinh

- Plan & Code: sua code, data, workflow
- Build: `train.py` + `optimize.py`
- Test: `tests/test_pipeline.py`
- AI: `src/infer.py`
- Deploy: `scripts/deploy.sh`
- Observe & Operate: `src/observe.py` + `scripts/rollback.sh`

## Ban se hoc duoc gi

- Cach chia artifact train/deploy
- Cach version model cho edge device
- Cach them test truoc khi deploy
- Cach rollback model theo version
- Cach them observability co ban

## Nang cap tiep theo

1. Thay JSON model bang ONNX.
2. Dong goi inference service bang Docker.
3. Day artifact len registry.
4. OTA that su cho Raspberry Pi/Jetson.
5. A/B testing bang 2 version model tren device.

## Lo trinh hoc de di dung thu tu

1. Hieu CI/CD co ban cho app thuong.
2. Hieu khac biet giua model artifact va app artifact.
3. Chay starter nay den khi rollback duoc.
4. Thay classifier nay bang model Python that.
5. Xuat ONNX va benchmark latency.
6. Dua pipeline len GitHub Actions va Docker.
# edge-ai-pipeline
