import pandas as pd
import minsearch


def build_index(documents):
    index = minsearch.Index(
        text_fields=['question', 'answer', 'video_id'],
        keyword_fields=[]
    )
    index.fit(documents)
    return index


def get_transcripts_dataframe():
    file_path = "youtube_transcripts/dataset.json"
    df = pd.read_json(file_path)
    
    return df.to_dict(orient='records')