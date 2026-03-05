def calculate_activity_score(walking, running, standing, sitting, sleeping):

    total_time = walking + running + standing + sitting + sleeping

    score = ((running * 3) + (walking * 2) + (standing * 1)) / total_time * 100

    if score >= 85:
        grade = "A"
        recommendation = "Excellent activity level. Maintain your routine."
    elif score >= 70:
        grade = "B"
        recommendation = "Good activity level. Add some light exercise."
    elif score >= 55:
        grade = "C"
        recommendation = "Moderate activity. Increase walking time."
    else:
        grade = "D"
        recommendation = "Low activity level. Reduce sedentary behaviour."

    return score, grade, recommendation