from big_sleep import Imagine

dream = Imagine(
    text = "an armchair in the form of pikachu|an armchair imitating pikachu|abstract",
    lr = 5e-2,
    save_every = 25,
    save_progress = True
)

dream()
