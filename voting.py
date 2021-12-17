def vote(models, accuracies, x):
    votes = {}
    for i in range(len(models)):
        model = models[i]
        model_vote = model.predict(x)
        if model_vote in a_dict:
            a_dict[model_vote] += accuracies[i]
        else:
            a_dict[model_vote] = accuracies[i]

    highest_weight = 0
    highest_key = False
    for key in votes:
        if votes[key] > highest_weight:
            highest_key = key
    return highest_key


def voting_classify(models, accuracies, data):
    """
    Produces a classification of the data based on a weighted voting system
    where the predictions of the models are weighted by their accuracy.

    @param (List) models: list containing the models that should be used.
    @param (List) accuracies: List of accuracy scores for each model
    @param (List) data: Objects that should be classified
    """
    output = []
    first = True

    for x in data:
        output.append(vote(models, accuracies, x))
    return output
