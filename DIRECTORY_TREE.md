# 📂 Project Directory Tree

## Complete Visual Structure

```
student-performance-prediction/
│
├── 📄 .gitignore                      # Git ignore rules
├── 📄 app.py                          # Streamlit web application (16.6 KB)
├── 📄 requirements.txt                # Python dependencies
├── 📄 run_training.bat               # Windows training script
├── 📄 README.md                      # Main project documentation
├── 📄 PROJECT_STRUCTURE.md           # Structure documentation
├── 📄 CLEANUP_SUMMARY.md             # Cleanup details
│
├── 📂 data/                          # Datasets (2 files)
│   ├── 📊 student-mat.csv            # Original UCI dataset (395 students)
│   └── 📊 student-combined.csv       # Augmented dataset (1,544 students)
│
├── 📂 models/                        # Production Models (5 files)
│   ├── 🤖 model_minimal.pkl          # Best model - 96.20% accuracy ⭐
│   ├── 📏 scaler_minimal.pkl         # StandardScaler for normalization
│   ├── 📋 features_minimal.pkl       # 7 minimal features list
│   ├── 📊 model_results_minimal.pkl  # Complete performance metrics
│   └── 📈 feature_importance.csv     # Feature importance rankings
│
├── 📂 scripts/                       # Python Scripts (4 files)
│   ├── 🎯 train_minimal_features.py  # PRIMARY: Train with 7 features
│   ├── 🌐 fetch_and_train.py         # Download data and train
│   ├── 🚀 achieve_925_accuracy.py    # Advanced PSO training
│   └── 🧪 test_model.py              # Model testing suite
│
├── 📂 docs/                          # Documentation (6 files)
│   ├── 📖 README.md                  # Documentation overview
│   ├── 📊 FINAL_COMPARISON.md        # Model vs Research Paper
│   ├── 🚀 DEPLOYMENT_READY.md        # Production deployment guide
│   ├── 📈 MINIMAL_FEATURES_RESULTS.md # Complete results analysis
│   ├── ⚡ QUICK_START.md             # Quick reference guide
│   └── 🔬 DATA_AUGMENTATION_GUIDE.md # Data augmentation methodology
│
└── 📂 archive/                       # Backup Models (7 files)
    ├── 🤖 model_925.pkl              # 94.94% accuracy (21 features)
    ├── 🤖 model.pkl                  # 85.76% accuracy (old model)
    ├── 📏 scaler_925.pkl             # Scaler for 925 model
    ├── 📏 scaler.pkl                 # Scaler for old model
    ├── 📋 features_925.pkl           # Features for 925 model
    ├── 📋 features.pkl               # Features for old model
    └── 📊 model_results.pkl          # Results for old model
```

---

## 📊 Statistics

### File Count by Directory
```
Root:     7 files
data/:    2 files
models/:  5 files
scripts/: 4 files
docs/:    6 files
archive/: 7 files
─────────────────
Total:   31 files
```

### Size Distribution
```
📂 data/        ~2.5 MB  (datasets)
📂 models/      ~500 KB  (trained models)
📂 scripts/     ~50 KB   (Python scripts)
📂 docs/        ~100 KB  (documentation)
📂 archive/     ~1.5 MB  (backup models)
```

---

## 🎯 Key Files Quick Reference

### To Run Application
```bash
streamlit run app.py
```
**File**: `app.py` (16.6 KB)

### To Test Model
```bash
python scripts/test_model.py
```
**File**: `scripts/test_model.py`

### To Train Model
```bash
python scripts/train_minimal_features.py
```
**File**: `scripts/train_minimal_features.py`

### Production Model
**File**: `models/model_minimal.pkl`
- Accuracy: 96.20%
- Features: 7 minimal
- Algorithm: PSO-Optimized Ensemble

---

## 📋 File Purposes

### Root Level
| File | Purpose |
|------|---------|
| app.py | Main Streamlit application |
| requirements.txt | Python package dependencies |
| run_training.bat | Quick training batch script |
| README.md | Complete project documentation |
| PROJECT_STRUCTURE.md | This structure guide |
| CLEANUP_SUMMARY.md | Cleanup details |
| .gitignore | Git version control rules |

### Data Folder
| File | Records | Purpose |
|------|---------|---------|
| student-mat.csv | 395 | Original UCI dataset |
| student-combined.csv | 1,544 | Augmented dataset |

### Models Folder (Production)
| File | Purpose |
|------|---------|
| model_minimal.pkl | Best trained model (96.20%) |
| scaler_minimal.pkl | Feature normalization |
| features_minimal.pkl | Feature list (7 features) |
| model_results_minimal.pkl | Performance metrics |
| feature_importance.csv | Feature rankings |

### Scripts Folder
| File | Purpose |
|------|---------|
| train_minimal_features.py | PRIMARY training script |
| fetch_and_train.py | Download and train |
| achieve_925_accuracy.py | Advanced PSO training |
| test_model.py | Model testing |

### Docs Folder
| File | Purpose |
|------|---------|
| README.md | Documentation overview |
| FINAL_COMPARISON.md | Model vs Paper analysis |
| DEPLOYMENT_READY.md | Deployment guide |
| MINIMAL_FEATURES_RESULTS.md | Results analysis |
| QUICK_START.md | Quick reference |
| DATA_AUGMENTATION_GUIDE.md | Data methodology |

---

## ✅ Organization Status

- ✅ Clean root directory (7 files only)
- ✅ Logical folder structure
- ✅ No redundant files
- ✅ Clear naming conventions
- ✅ Production-ready
- ✅ Well-documented
- ✅ Version control ready

---

## 🚀 Quick Navigation

```bash
# View structure
tree /F

# List root files
dir /B

# Check data files
dir data /B

# Check model files
dir models /B

# Check scripts
dir scripts /B

# Check documentation
dir docs /B
```

---

**Last Updated**: 2024  
**Status**: ✅ Clean & Organized  
**Total Files**: 31 (optimized from 53)
