import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

def apply_pca(df):
    df = df.drop(columns=["CustomerID"], errors='ignore')  # Optional identifier removal

    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    # Standardize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_imputed)

    # PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(scaled_data)
    pca_df = pd.DataFrame(data=principal_components, columns=["PC1", "PC2"])

    return pca_df
