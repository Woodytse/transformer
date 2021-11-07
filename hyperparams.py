class Hyperparams:
    """Hyperparameters"""

    # data
    # source_train ="corpora/cn.txt" #"corpora/cn_train_tokenized.txt"
    # target_train ="corpora/en.txt" #"corpora/en_train_tokenized.txt"
    # source_test = "corpora/cn.test.txt"#"corpora/cn_test_tokenized.txt"
    # target_test = "corpora/en.test.txt"#"corpora/en_test_tokenized.txt"

    source_train = "corpora/cn_train_tokenized_30k.txt"
    target_train = "corpora/en_train_tokenized_30k.txt"
    source_test =  "corpora/cn_test_tokenized_30k.txt"
    target_test = "corpora/en_test_tokenized_30k.txt"

    # training
    batch_size = 14 # alias = N
    batch_size_valid = 6
    lr = (
        0.0001  # learning rate. In paper, learning rate is adjusted to the global step.
    )
    logdir = "logdir"  # log directory

    model_dir = "./models/"  # saving directory

    # model
    maxlen = 50  # Maximum number of words in a sentence. alias = T.
    min_cnt = 0  # words whose occurred less than min_cnt are encoded as <UNK>.
    hidden_units = 512  # alias = C
    num_blocks = 12  # number of encoder/decoder blocks
    num_epochs = 50
    num_heads = 8
    dropout_rate = 0.4
    sinusoid = False  # If True, use sinusoid. If false, positional embedding.
    eval_epoch = 1  # epoch of model for eval
    eval_script = 'validate.sh'#'scripts/validate.sh'
    check_frequency = 10  # checkpoint frequency
