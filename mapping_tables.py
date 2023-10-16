"""
Mapping Tables for MovieLens Dataset

This module provides helper functions to map coded categorical data
from the MovieLens dataset to their descriptive labels. It aims to
enhance the interpretability and usability of the dataset by converting
numeric or coded categorical values to more understandable string representations.

Functions included are:
    - age_mapping(): Returns a mapping of age codes to descriptive labels.
    - occupation_mapping(): Returns a mapping of occupation codes to their descriptive labels.

Example usage:
    from mapping_tables import age_mapping, occupation_mapping

    age_label = age_mapping()[18]  # Returns '18-24'
    occupation_label = occupation_mapping()[7]  # Returns 'executive/managerial'

Note:
    These mappings are based on the documentation provided with the MovieLens 1M dataset.
    Any changes or updates to the dataset might necessitate updates to these mapping functions.

"""


def age_mapping() -> dict:
    """
    Returns a mapping of age codes to their descriptive labels.

    Returns:
    - age_map (dict): Dictionary mapping age codes to labels.
    """
    age_map = {
        1: "Under 18",
        18: "18-24",
        25: "25-34",
        35: "35-44",
        45: "45-49",
        50: "50-55",
        56: "56+"
    }
    return age_map


def occupation_mapping() -> dict:
    """
    Returns a mapping of occupation codes to their descriptive labels.

    Returns:
    - occupation_map (dict): Dictionary mapping occupation codes to labels.
    """
    occupation_map = {
        0: "other or not specified",
        1: "academic/educator",
        2: "artist",
        3: "clerical/admin",
        4: "college/grad student",
        5: "customer service",
        6: "doctor/health care",
        7: "executive/managerial",
        8: "farmer",
        9: "homemaker",
        10: "K-12 student",
        11: "lawyer",
        12: "programmer",
        13: "retired",
        14: "sales/marketing",
        15: "scientist",
        16: "self-employed",
        17: "technician/engineer",
        18: "tradesman/craftsman",
        19: "unemployed",
        20: "writer"
    }
    return occupation_map
