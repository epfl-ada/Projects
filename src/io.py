import json
import pandas as pd
from dotmap import DotMap
from pathlib import Path

_DEFAULT_PATHS = {
    "emission_intensity": "global-food-agriculture-statistics/raw_files/Environment_Emissions_intensities_E_All_Data_(Normalized).csv"
}


def load_em_intensity(filepath):
    return None



_DFS = {
    "emission_intensity": load_em_intensity,

}

def load_df(data_dir, *df_names):
    data_dir = Path(data_dir)
    path_file = data_dir / "df_paths.json"
    if not path_file.exists():
        with path_file.open('w') as f:
            json.dump(_DEFAULT_PATHS, f, indent=4, sort_keys=True)
        df_path = {}
    else:
        with path_file.open() as f:
            df_path = json.load(f)
    
    result = DotMap(_dynamic=False)
    for df_name in df_names:
        df_path = df_path.get(df_name) or _DEFAULT_PATHS.get(df_name)
        if df_path is None:
            raise ValueError(f'Unknown dataframe {df_name}')
        func = _DFS.get(df_name)
        if func is None:
            raise ValueError(f"Could not load {df_name}, no loading function found")
        result[df_name] = func(df_path)
    
    return result
