
class GaleShapley:
    @staticmethod
    def stable_matching(n, menPreferences, womenPreferences):
        return n
    @staticmethod
    def stableMatching(n, menPreferences, womenPreferences):
        # Do not change the function definition line.

        # Initially, all n men are unmarried
        unmarriedMen = list(range(n))
        # None of the men has a spouse yet, we denote this by the value None
        manSpouse = [None] * n
        # None of the women has a spouse yet, we denote this by the value None
        womanSpouse = [None] * n
        # Each man made 0 proposals, which means that
        # his next proposal will be to the woman number 0 in his list
        nextManChoice = [0] * n

        # While there exists at least one unmarried man:
        while unmarriedMen:
            # Pick an arbitrary unmarried man
            he = unmarriedMen[0]
            # Store his ranking in this variable for convenience
            hisPreferences = menPreferences[he]
            # Find a woman to propose to
            she = hisPreferences[nextManChoice[he]]
            # Store her ranking in this variable for convenience
            herPreferences = womenPreferences[she]
            # Find the present husband of the selected woman (it might be None)
            currentHusband = womanSpouse[she]

            # Write your code here
            if currentHusband is None:
                womanSpouse[she] = he
                manSpouse[he] = she
                unmarriedMen.pop(0)
            elif herPreferences.index(he) < herPreferences.index(currentHusband):
                womanSpouse[she] = he
                manSpouse[he] = she
                unmarriedMen.pop(0)
                manSpouse[currentHusband] = None
                unmarriedMen.append(currentHusband)

            nextManChoice[he] = nextManChoice[he] + 1
        return manSpouse
