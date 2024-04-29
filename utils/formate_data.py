def hours_to_hh_mm(hours : float) -> str:

    hh = int(hours)
    mm = int((hours - hh) * 60)
    
   
    # hh_str = str(hh).zfill(2)  
    mm_str = str(mm).zfill(2)  
    
    return f"{hh} hours {int(mm_str)} minutes"



