from datasets import load_dataset

def downloader(links_data, last_name):
    """_summary_
    A function for downloading a dataset and saving it to a computer in a separate file csv.
    Args:
        links_data (str): Link to the database from the HugginFace website.
        last_name (str): The name of the file to save it.
    """
    # Downloading a dataset from Huggin Face
    dataset = load_dataset(links_data, trust_remote_code=True)
    print (dataset)

    # The division into educational training and verification samples
    # train_data = dataset['train']
    # test_data  = dataset['test']
    # # Save the dataset to CSV
    # train_data.to_csv(f"custom_data\machine_translation\data_example\{last_name}_train.csv", index=False)
    # test_data.to_csv (f"custom_data\machine_translation\data_example\{last_name}_test.csv" , index=False)
    
    # if 'validation' in dataset:
    #     val_data = dataset['validation']
    #     # Save the dataset to CSV
    #     val_data.to_csv  (f"custom_data\classifiction_text\data_example\{last_name}_val.csv"  , index=False)


# downloader("li2017dailydialog/daily_dialog", "daily")
# downloader("dair-ai/emotion", "dair-ai")
downloader("Helsinki-NLP/opus-100", "opus-100")
