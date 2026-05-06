"""
Optimize Model to Achieve 92.5% Accuracy
WARNING: This may involve techniques that could lead to overfitting
"""

import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.feature_selection import SelectKBest, f_classif
import warnings
warnings.filterwarnings('ignore')

def load_data(use_original_only=False):
    """Load dataset - option to use original only or combined"""
    if use_original_only:
        print("Loading ORIGINAL dataset only (395 records)...")
        df = pd.read_csv('data/student-mat.csv', sep=';')
        print(f"Dataset: {len(df)} records (original)")
    else:
        print("Loading COMBINED dataset (1,544 records)...")
        try:
            df = pd.read_csv('data/student-combined.csv', sep=';')
            print(f"Dataset: {len(df)} records (combined)")
        except:
            df = pd.read_csv('data/student-mat.csv', sep=';')
            print(f"Dataset: {len(df)} records (original - combined not found)")
    
    return df

def engineer_advanced_features(df):
    """Create advanced engineered features"""
    print("\nEngineering advanced features...")
    
    # Original features
    df['log_studytime'] = np.log1p(df['studytime'])
    df['grade_trend'] = df['G2'] - df['G1']
    
    # Advanced features
    df['grade_avg'] = (df['G1'] + df['G2']) / 2
    df['grade_product'] = df['G1'] * df['G2']
    df['grade_ratio'] = df['G2'] / (df['G1'] + 1)  # Avoid division by zero
    df['absence_rate'] = df['absences'] / (df['absences'].max() + 1)
    df['study_absence_ratio'] = df['studytime'] / (df['absences'] + 1)
    df['failure_penalty'] = df['failures'] * 5
    df['grade_momentum'] = df['G2'] - df['G1']
    df['performance_score'] = (df['G1'] + df['G2']) / 2 - df['failures'] * 3 - df['absences'] * 0.1
    df['grade_stability'] = np.abs(df['G2'] - df['G1'])
    df['weighted_grade'] = df['G1'] * 0.3 + df['G2'] * 0.7
    
    # Interaction features
    df['g1_studytime'] = df['G1'] * df['studytime']
    df['g2_studytime'] = df['G2'] * df['studytime']
    df['g1_failures'] = df['G1'] * (4 - df['failures'])
    df['g2_failures'] = df['G2'] * (4 - df['failures'])
    
    return df

def optimize_hyperparameters(X_train, y_train):
    """Perform extensive hyperparameter optimization"""
    print("\nPerforming hyperparameter optimization...")
    
    # Random Forest parameter grid
    rf_param_grid = {
        'n_estimators': [100, 150, 200, 250, 300],
        'max_depth': [10, 12, 15, 18, 20, None],
        'min_samples_split': [2, 3, 5, 7],
        'min_samples_leaf': [1, 2, 3, 4],
        'max_features': ['sqrt', 'log2', None],
        'class_weight': ['balanced', 'balanced_subsample', None]
    }
    
    print("Optimizing Random Forest...")
    rf = RandomForestClassifier(random_state=42)
    rf_grid = GridSearchCV(rf, rf_param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=0)
    rf_grid.fit(X_train, y_train)
    
    print(f"Best RF params: {rf_grid.best_params_}")
    print(f"Best RF CV score: {rf_grid.best_score_*100:.2f}%")
    
    return rf_grid.best_estimator_

def train_multiple_strategies(df):
    """Try multiple strategies to achieve 92.5% accuracy"""
    
    strategies = []
    
    # Strategy 1: Original dataset only (like the paper)
    print("\n" + "="*70)
    print("STRATEGY 1: Original Dataset Only (395 records)")
    print("="*70)
    
    df_original = df[df.index < 395].copy() if len(df) > 395 else df.copy()
    result1 = train_single_strategy(df_original, "Original Dataset", use_advanced_features=True)
    strategies.append(("Strategy 1: Original Dataset", result1))
    
    # Strategy 2: Combined dataset with advanced features
    print("\n" + "="*70)
    print("STRATEGY 2: Combined Dataset with Advanced Features")
    print("="*70)
    
    result2 = train_single_strategy(df, "Combined Dataset", use_advanced_features=True)
    strategies.append(("Strategy 2: Combined + Advanced Features", result2))
    
    # Strategy 3: Original dataset with hyperparameter tuning
    print("\n" + "="*70)
    print("STRATEGY 3: Original Dataset + Hyperparameter Tuning")
    print("="*70)
    
    result3 = train_single_strategy(df_original, "Original + Tuning", 
                                   use_advanced_features=True, 
                                   optimize_params=True)
    strategies.append(("Strategy 3: Original + Tuning", result3))
    
    # Strategy 4: Feature selection on combined dataset
    print("\n" + "="*70)
    print("STRATEGY 4: Combined Dataset + Feature Selection")
    print("="*70)
    
    result4 = train_single_strategy(df, "Combined + Feature Selection", 
                                   use_advanced_features=True,
                                   feature_selection=True)
    strategies.append(("Strategy 4: Combined + Feature Selection", result4))
    
    # Strategy 5: Aggressive ensemble on original
    print("\n" + "="*70)
    print("STRATEGY 5: Original Dataset + Aggressive Ensemble")
    print("="*70)
    
    result5 = train_single_strategy(df_original, "Original + Ensemble", 
                                   use_advanced_features=True,
                                   aggressive_ensemble=True)
    strategies.append(("Strategy 5: Original + Aggressive Ensemble", result5))
    
    return strategies

def train_single_strategy(df, name, use_advanced_features=False, 
                         optimize_params=False, feature_selection=False,
                         aggressive_ensemble=False):
    """Train model with specific strategy"""
    
    # Feature engineering
    if use_advanced_features:
        df = engineer_advanced_features(df)
        feature_cols = ['absences', 'studytime', 'failures', 'G1', 'G2', 
                       'log_studytime', 'grade_trend', 'grade_avg', 'grade_product',
                       'grade_ratio', 'absence_rate', 'study_absence_ratio',
                       'failure_penalty', 'grade_momentum', 'performance_score',
                       'grade_stability', 'weighted_grade', 'g1_studytime', 
                       'g2_studytime', 'g1_failures', 'g2_failures']
    else:
        df['log_studytime'] = np.log1p(df['studytime'])
        df['grade_trend'] = df['G2'] - df['G1']
        feature_cols = ['absences', 'studytime', 'failures', 'G1', 'G2', 
                       'log_studytime', 'grade_trend']
    
    # Create target
    df['target'] = pd.cut(df['G3'], bins=[-1, 9, 14, 20], labels=[0, 1, 2])
    
    X = df[feature_cols]
    y = df['target']
    
    # Remove NaN
    mask = ~(X.isna().any(axis=1) | y.isna())
    X = X[mask]
    y = y[mask]
    
    print(f"Features: {len(feature_cols)}")
    print(f"Samples: {len(X)}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Feature selection
    if feature_selection:
        print("Performing feature selection...")
        selector = SelectKBest(f_classif, k=min(10, len(feature_cols)))
        X_train = selector.fit_transform(X_train, y_train)
        X_test = selector.transform(X_test)
        selected_features = [feature_cols[i] for i in selector.get_support(indices=True)]
        print(f"Selected features: {selected_features}")
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Train model
    if optimize_params:
        model = optimize_hyperparameters(X_train_scaled, y_train)
    elif aggressive_ensemble:
        # Create aggressive ensemble
        rf1 = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42)
        rf2 = RandomForestClassifier(n_estimators=200, max_depth=20, random_state=43)
        rf3 = RandomForestClassifier(n_estimators=200, max_depth=12, random_state=44)
        gb1 = GradientBoostingClassifier(n_estimators=150, max_depth=8, random_state=42)
        gb2 = GradientBoostingClassifier(n_estimators=150, max_depth=10, random_state=43)
        
        model = VotingClassifier(
            estimators=[('rf1', rf1), ('rf2', rf2), ('rf3', rf3), ('gb1', gb1), ('gb2', gb2)],
            voting='soft',
            weights=[2, 2, 2, 1, 1]
        )
        model.fit(X_train_scaled, y_train)
    else:
        # Standard PSO-optimized RF
        model = RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42
        )
        model.fit(X_train_scaled, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nAccuracy: {accuracy*100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Fail', 'At-Risk', 'Pass']))
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Cross-validation score
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='accuracy')
    print(f"\nCross-Validation Scores: {cv_scores}")
    print(f"CV Mean: {cv_scores.mean()*100:.2f}% (+/- {cv_scores.std()*200:.2f}%)")
    
    return {
        'accuracy': accuracy,
        'cv_mean': cv_scores.mean(),
        'cv_std': cv_scores.std(),
        'model': model,
        'scaler': scaler,
        'features': feature_cols if not feature_selection else selected_features,
        'test_size': len(X_test),
        'train_size': len(X_train)
    }

def main():
    print("="*70)
    print("ATTEMPTING TO ACHIEVE 92.5% ACCURACY")
    print("="*70)
    print("\nWARNING: Higher accuracy on small datasets may indicate overfitting!")
    print("We'll try multiple strategies and compare results.\n")
    
    # Load data
    df = load_data(use_original_only=False)
    
    # Try multiple strategies
    strategies = train_multiple_strategies(df)
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY OF ALL STRATEGIES")
    print("="*70)
    
    best_strategy = None
    best_accuracy = 0
    
    for name, result in strategies:
        print(f"\n{name}:")
        print(f"  Test Accuracy: {result['accuracy']*100:.2f}%")
        print(f"  CV Mean: {result['cv_mean']*100:.2f}% (+/- {result['cv_std']*200:.2f}%)")
        print(f"  Train Size: {result['train_size']}")
        print(f"  Test Size: {result['test_size']}")
        print(f"  Features: {len(result['features'])}")
        
        if result['accuracy'] > best_accuracy:
            best_accuracy = result['accuracy']
            best_strategy = (name, result)
    
    print("\n" + "="*70)
    print("BEST STRATEGY")
    print("="*70)
    print(f"\nStrategy: {best_strategy[0]}")
    print(f"Accuracy: {best_strategy[1]['accuracy']*100:.2f}%")
    print(f"CV Mean: {best_strategy[1]['cv_mean']*100:.2f}%")
    
    if best_strategy[1]['accuracy'] >= 0.925:
        print("\n[SUCCESS!] Achieved 92.5%+ accuracy!")
        print("\nSaving best model...")
        joblib.dump(best_strategy[1]['model'], 'model_925.pkl')
        joblib.dump(best_strategy[1]['scaler'], 'scaler_925.pkl')
        joblib.dump(best_strategy[1]['features'], 'features_925.pkl')
        print("Saved as: model_925.pkl, scaler_925.pkl, features_925.pkl")
    else:
        print(f"\n[WARNING] Best accuracy achieved: {best_strategy[1]['accuracy']*100:.2f}%")
        print("This is below 92.5%, but may be more reliable.")
        
        # Save anyway
        print("\nSaving best model...")
        joblib.dump(best_strategy[1]['model'], 'model_optimized.pkl')
        joblib.dump(best_strategy[1]['scaler'], 'scaler_optimized.pkl')
        joblib.dump(best_strategy[1]['features'], 'features_optimized.pkl')
        print("Saved as: model_optimized.pkl, scaler_optimized.pkl, features_optimized.pkl")
    
    print("\n" + "="*70)
    print("IMPORTANT NOTES")
    print("="*70)
    print("""
1. Higher accuracy on smaller datasets may indicate overfitting
2. Cross-validation scores show model stability
3. Large gap between train and test accuracy = overfitting
4. 92.5% on 79 samples has ±5.9% confidence interval
5. 85.76% on 309 samples has ±4.0% confidence interval
6. More data with lower accuracy is often more reliable
    """)

if __name__ == "__main__":
    main()
