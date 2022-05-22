
def expand_summary(score_summary):
    """
    given an ordered summary of scores, returns a list of the game outcomes.
    score_summary: array c_i containing count (c) of times score i was reached.
    """
    game_outcomes = []
    for guesses, count in enumerate(score_summary):
        for game in range(count):
            game_outcomes.append(guesses+1)
    return game_outcomes


def simply_weighted(scores):
    """
    given a list of raw scores, this applies the simple weighing by the amount of 
    information available. to compute the simply weighted scores (see text).
    the weight of each is score is score-1
    """
    return [ score * (score - 1) for score in scores ]


summary_scores_a = [  0,  3, 31, 49, 15,  2]
summary_scores_b = [  0,  2, 37, 36, 22,  3]

scores_a = expand_summary(summary_scores_a)
scores_b = expand_summary(summary_scores_b)

weighted_scores_a = simply_weighted(scores_a)
weighted_scores_b = simply_weighted(scores_b)


# statistical testing
from scipy import stats
# student's t-test
stats.ttest_ind(scores_a, scores_b, equal_var=True)
stats.ttest_ind(scores_a, scores_b, equal_var=False)
stats.ttest_ind(weighted_scores_a, weighted_scores_b, equal_var=True)
stats.ttest_ind(weighted_scores_a, weighted_scores_b, equal_var=False)
# kolmogorov-smirnov
stats.ks_2samp(scores_a, scores_b)
stats.ks_2samp(weighted_scores_a, weighted_scores_b)
