

def get_part_by_id(inputID):
    return session.query(Part).filter(Part.ProductNum == inputID).first()