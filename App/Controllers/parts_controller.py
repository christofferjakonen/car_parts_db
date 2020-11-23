import Data.Repository.parts_repository as pr


def get_all_parts():
    return pr.get_all_parts()


def get_part_by_id(inputID):
    part = pr.get_part_by_id(inputID)
    result = part if part else "No part was found"
    return result
