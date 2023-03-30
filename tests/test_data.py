import os

def test_data_folder_exists():
    assert os.path.exists("data/translation"), "data/translation folder does not exist"

def test_data_files_are_text():
    file_names = ["train.en", "train.ki"]
    for file_name in file_names:
        with open(f"data/translation/{file_name}") as f:
            for line in f:
                assert isinstance(line, str), f"Expected text but got {type(line)} in {file_name}"

def test_data_can_be_loaded():
    file_names = ["train.en", "train.ki"]
    for file_name in file_names:
        with open(f"data/translation/{file_name}") as f:
            data = f.readlines()
        assert len(data) > 0, f"No data loaded from {file_name}"
