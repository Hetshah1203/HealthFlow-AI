import pandas as pd
import io
import json
from typing import List

def load_data(content: bytes, filename: str) -> pd.DataFrame:
    """Load CSV or JSON data from uploaded file content.
    Args:
        content: Raw bytes from the uploaded file.
        filename: Original filename to infer type.
    Returns:
        pandas.DataFrame with the loaded data.
    """
    if filename.lower().endswith('.csv'):
        # CSV
        return pd.read_csv(io.BytesIO(content))
    elif filename.lower().endswith('.json'):
        # JSON – assume list of records
        data = json.loads(content.decode('utf-8'))
        return pd.DataFrame(data)
    else:
        raise ValueError('Unsupported file type: must be .csv or .json')

def preprocess_data(dfs: List[pd.DataFrame]) -> pd.DataFrame:
    """Simple preprocessing: concatenate, fill missing, encode categoricals.
    This is a placeholder – real pipelines would be more sophisticated.
    """
    if not dfs:
        raise ValueError('No dataframes provided for preprocessing')
    # Concatenate all dataframes
    df = pd.concat(dfs, ignore_index=True)
    # Basic cleaning: fill numeric NaNs with 0, categorical with 'unknown'
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(0)
        else:
            df[col] = df[col].fillna('unknown')
    # Simple one-hot encoding for categorical columns
    df = pd.get_dummies(df, drop_first=True)
    return df
