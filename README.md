# lf-stitch
Image stitching for large format film scans

![](docs/diagram.png)

### Quick Start


Clone and install locally with
```bash
pip install -e .
```

Store all scans in a separate directory e.g., `scans`
```bash
scans
├── img01.jpg
└── img02.jpg
```

Stitch all scans together by running

```bash
stitch --dir="scans"
```
