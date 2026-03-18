def calculate_risk(menu, user_allergy, allergen_labels, menu_uncertainty):
    total_score = 0.0
    max_score = 0.0
    
    if menu not in menu_uncertainty:
        return {"error" : "menu not found"}
    
    for allergen, prob in menu_uncertainty[menu].items():  # แก้ .items()
        if allergen not in allergen_labels:
            continue
        
        severity = allergen_labels[allergen]["severity_score"]
        prevalence = allergen_labels[allergen]["prevalence"]
        
        # สูตรคำนวณ score
        score = prob * severity * (1 + prevalence / 5)
        
        # max_score
        max_possible = 1 * severity * (1 + prevalence / 5)
        max_score += max_possible
        
        if allergen in user_allergy:
            total_score += score
     
    # normalize to percent       
    if max_score == 0:
        risk_percent = 0
    else:
        risk_percent = (total_score / max_score) * 100
        
    # risk level
    if risk_percent >= 70:
        level = "HIGH"
    elif risk_percent >= 40:
        level = "MEDIUM"
    else:
        level = "LOW"
        
    return {
        "Menu": menu,
        "Risk score": round(total_score, 2),
        "Risk percent": round(risk_percent, 2),
        "Risk level": level
    }