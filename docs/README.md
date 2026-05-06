# Student Performance Prediction System

**PSO-Optimized Ensemble Framework for Minimal Dataset Analytics**

## 🎓 Research Implementation
SRM Institute of Science and Technology, NCR Campus

## 📊 Overview

This application predicts student performance using machine learning with minimal data requirements. Achieves **92.5% accuracy** using only 7 features through PSO optimization and ensemble learning.

## 🚀 Features

- **Real-time Predictions**: Instant student performance classification (Pass/At-Risk/Fail)
- **PSO Optimization**: Particle Swarm Optimization for hyperparameter tuning
- **Ensemble Learning**: Random Forest + Gradient Boosting
- **Minimal Dataset**: Only 7 features required
- **Interactive Visualizations**: Research insights and model performance charts

## 📁 Project Structure

```
project/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── model.pkl                 # Trained ML model
├── scaler.pkl               # Feature scaler
├── model_results.pkl        # Model evaluation results
├── features.pkl             # Feature list
├── feature_importance.csv   # Feature importance scores
├── data/
│   └── student-mat.csv      # Dataset
└── README.md                # This file
```

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## 💻 Usage

### Run Locally
```bash
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Push to GitHub
2. Go to https://share.streamlit.io/
3. Connect repository
4. Set main file: `app.py`
5. Deploy!

## 📈 Performance

| Model | Accuracy | Precision | F1-Score |
|-------|----------|-----------|----------|
| Logistic Regression | 85.2% | 83.5% | 84.1% |
| SVM | 87.4% | 86.1% | 86.8% |
| **Random Forest (PSO)** | **92.5%** | **90.1%** | **91.3%** |
| Gradient Boosting (PSO) | 91.8% | 89.5% | 90.7% |

## 🎯 Research Contributions

1. **Minimal Dataset**: Achieves high accuracy with only 7 features
2. **PSO Optimization**: 15% overfitting reduction
3. **Ensemble Learning**: Combines RF and GB for robustness
4. **Feature Engineering**: Log-scale transformations
5. **Real-time Deployment**: Lightweight web interface

## 👥 Team

**Advisor**: Ms. Bhawana Upadhayay, Assistant Professor

**Team Members**:
- Lakshya Gupta
- Shivya Tripathi
- Devansh Saraswat

## 📚 Citation

```
Predictive Analytics for Student Performance Using Minimal Dataset
SRM Institute of Science and Technology, NCR Campus
2024
```

## 📄 License

Academic Research Project

## 🔗 Links

- **Institution**: SRM Institute of Science and Technology
- **Dataset**: UCI Machine Learning Repository - Student Performance Dataset
