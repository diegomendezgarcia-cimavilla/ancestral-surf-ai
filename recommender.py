from ancestral_knowledge import knowledge

def recommend(energy,stress,mood):

    rec=[]

    if energy<4:
        rec+=knowledge["low_energy"]

    if stress>7:
        rec+=knowledge["high_stress"]

    if energy>7:
        rec+=knowledge["good_energy"]

    if mood>7:
        rec+=knowledge["creative_state"]

    return list(set(rec))
