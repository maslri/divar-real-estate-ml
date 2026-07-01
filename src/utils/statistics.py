def interpret_cohens_d(d):
    d = abs(d)

    if d < 0.2:
        return "Negligible"

    elif d < 0.5:
        return "Small"

    elif d < 0.8:
        return "Medium"

    return "Large"
