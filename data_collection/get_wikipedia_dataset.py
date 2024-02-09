from pathlib import Path

from datasets import load_dataset


FILEPATH=Path('data/simple_wikipedia.csv')
FILEPATH.parent.mkdir(exist_ok=True, parents=True)

dataset = load_dataset(
    'wikipedia',
    '20220301.simple',
    trust_remote_code=True,
)
dataset.data['train'].to_pandas().to_csv(FILEPATH)
