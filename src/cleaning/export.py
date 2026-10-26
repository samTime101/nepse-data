from pathlib import Path

def _write_csv(df, output_path):
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False, date_format="%Y-%m-%d")
    return output_path

def export_cleaned_data(df, output_dir):
    return _write_csv(df, Path(output_dir) / "data.csv")

def export_rejected_data(df, output_dir, name):
    return _write_csv(df, Path(output_dir) / "rejected" / f"{name}.csv")
