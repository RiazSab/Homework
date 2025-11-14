def calc_damage(base_damage: float, multiplier: float, critical: bool) -> float | str:
    try:
        if not isinstance(base_damage, (float, int)):
            return "wrong types"
        
        if not isinstance(multiplier, (float, int)):
            return "wrong types"
        
        if not isinstance(critical, bool):
            return "wrong types"
        
        if base_damage < 0 or multiplier < 0:
            return "damage cannot be negative"
        
        damage = base_damage * multiplier
        
        if critical:
            damage = damage * 2
        return damage
        
    except:
        return "Ошибка"