# Project Structure

## 📁 Clean & Organized Directory Layout

```
student-performance-prediction/
│
├── 📄 app.py                          # Main Streamlit web application
├── 📄 requirements.txt                # Python dependencies
├── 📄 run_training.bat               # Quick training script
├── 📄 README.md                      # Main project documentation
├── 📄 PROJECT_STRUCTURE.md           # This file
│
├── 📂 data/                          # Dataset files
│   ├── student-mat.csv               # Original dataset (395 records)
│   └── student-combined.csv          # Augmented dataset (1,544 records)
│
├── 📂 models/                        # Trained models (BEST MODEL)
│   ├── model_minimal.pkl             # 96.20% accuracy model ⭐
│   ├── scaler_minimal.pkl            # Feature scaler
│   ├── features_minimal.pkl          # Feature list
│   ├── model_results_minimal.pkl     # Performance metrics
│   └── feature_importance.csv        # Feature importance scores
│
├── 📂 scripts/                       # Training and testing scripts
│   ├── train_minimal_features.py     # Train with 7 features (PRIMARY)
│   ├── fetch_and_train.py            # Fetch data and train
│   ├── achieve_925_accuracy.py       # Advanced training
│   └── test_model.py                 # Model testing
│
├── 📂 docs/                          # Documentation
│   ├── README.md                     # Documentation overview
│   ├── FINAL_COMPARISON.md           # Model vs Paper comparison
│   ├── DEPLOYMENT_READY.md           # Deployment guide
│   ├── MINIMAL_FEATURES_RESULTS.md   # Complete results analysis
│   ├── QUICK_START.md                # Quick reference guide
│   └── DATA_AUGMENTATION_GUIDE.md    # Data augmentation details
│
└── 📂 archive/                       # Old/alternative models
    ├── model_925.pkl                 # 94.94% accuracy (21 features)
    ├── model.pkl                     # 85.76% accuracy (large dataset)
    ├── scaler_925.pkl                # Scaler for 925 model
    ├── scaler.pkl                    # Scaler for old model
    ├── features_925.pkl              # Features for 925 model
    ├── features.pkl                  # Features for old model
    └── model_results.pkl             # Results for old model
```

---

## 🎯 File Purposes

### Root Level
- **app.py**: Main Streamlit application for predictions
- **requirements.txt**: All Python package dependencies
- **run_training.bat**: Windows batch script for quick training
- **README.md**: Complete project documentation

### Data Folder
- **student-mat.csv**: Original UCI dataset (395 students)
- **student-combined.csv**: Augmented dataset (1,544 students)

### Models Folder (PRODUCTION)
- **model_minimal.pkl**: Best model (96.20% accuracy, 7 features)
- **scaler_minimal.pkl**: StandardScaler for feature normalization
- **features_minimal.pkl**: List of 7 minimal features
- **model_results_minimal.pkl**: Complete performance metrics
- **feature_importance.csv**: Feature importance rankings

### Scripts Folder
- **train_minimal_features.py**: PRIMARY training script (7 features)
- **fetch_and_train.py**: Download data and train model
- **achieve_925_accuracy.py**: Advanced training with PSO
- **test_model.py**: Test model with sample cases

### Docs Folder
- **FINAL_COMPARISON.md**: Detailed comparison with research paper
- **DEPLOYMENT_READY.md**: Production deployment guide
- **MINIMAL_FEATURES_RESULTS.md**: Complete results and analysis
- **QUICK_START.md**: Quick reference for common tasks
- **DATA_AUGMENTATION_GUIDE.md**: Data augmentation methodology

### Archive Folder
- Old models and scalers for reference
- Not used in production

---

## 🚀 Quick Commands

### Run Application
```bash
streamlit run app.py
```

### Test Model
```bash
python scripts/test_model.py
```

### Train New Model
```bash
python scripts/train_minimal_features.py
```

### Quick Training (Windows)
```bash
run_training.bat
```

---

## ✅ Organization Status

- ✅ Removed redundant documentation files
- ✅ Cleaned up unnecessary data files
- ✅ Removed duplicate training scripts
- ✅ Kept only essential files
- ✅ Clear folder structure
- ✅ Production-ready organization

---

## 📊 File Count Summary

| Folder | Files | Purpose |
|--------|-------|---------|
| Root | 4 | Core application files |
| data/ | 2 | Essential datasets |
| models/ | 5 | Production model files |
| scripts/ | 4 | Training and testing |
| docs/ | 6 | Documentation |
| archive/ | 7 | Backup models |

**Total: 28 files** (clean and organized)

---

*Last Updated: 2024*
*SRM Institute of Science and Technology, NCR Campus*
