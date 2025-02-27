import pytest
import numpy as np
import pandas as pd

# This script contains tests for the cleaning functions and should be
# completed by you


@pytest.fixture
def sample_dirty_fname() -> str:
    fname = 'data/sample_dirty.csv'
    return fname


@pytest.fixture
def sample_formatted() -> pd.DataFrame:
    df = pd.DataFrame(
        data={
            'nom': ['Plateau sportif de GrammontTerrain 9, 10, 11',
                    'MEDIATHEQUE JEAN-JACQUES ROUSSEAU',
                    "Ecole maternelle Aliénor-d'Aquitaine - Ecole élémentaire Ronsard",
                    'Piscine centre nautique neptune',
                    'Ecole maternelle Paul-Eluard - Ecole élémentaire Jean Macé',
                    'Centre Culturel Rabelais',
                    'Poste de police Ecusson Centre ville',
                    pd.NA,
                    'EHPAD "Michel BELORGEOT"',
                    'DELL',
                    'Gymnase François Spinosi',
                    "Siège du CCAS (Banque d'Acceuil)",
                    'Vestiaire/tribune CLAUDE BEAL',
                    'Ecole élémentaire Winston Churchill - Ecole maternelle Marceline Desbordes-Valmore'],
            'adr_num': [pd.NA,
                        pd.NA,
                        '694 -700',
                        '-',
                        '219 - 289',
                        '29',
                        '19 bis',
                        '1 place Jacques Mirouse, MONTPELLIER',
                        '41',
                        '1',
                        pd.NA,
                        '125',
                        '419',
                        '424 - 460'],
            'adr_voie': ['avenue albert Einstein',
                         pd.NA,
                         'rue Jacques-Bounin',
                         '-',
                         'rue de Saint Hilaire 34000 Montpellier',
                         'boulevard Sarrail',
                         'rue durand',
                         '1 place Jacques Mirouse, MONTPELLIER',
                         'impasse des Moulins',
                         ' rond-point Benjamin Franklin',
                         'Rue Pierre Gilles de Gennes',
                         'place  Thermidor',
                         'avenue du Dr Jacques Fourcade 34000 Montpellier',
                         'rue du lavandin'],
            'com_cp': ['34000',
                       '0',
                       '34070',
                       '0',
                       '34000',
                       '34000',
                       '34000',
                       '34000',
                       '34000',
                       '0',
                       '34000',
                       '34000',
                       '34000',
                       '34070'],
            'com_nom': ['Montpellier',
                        pd.NA,
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        pd.NA,
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'MONTPELLIER',
                        'Montpellier'],
            'tel1': ['334 67 64 87 70',
                     pd.NA,
                     '334 67 27 46 12',
                     '-',
                     '334 67 64 40 54',
                     '334 67 34 71 33',
                     '334 67 34 70 89',
                     pd.NA,
                     '+334 67 40 04 44',
                     '06 58 57 85 24',
                     '334 67 15 90 35',
                     '+334 99  52 77 53',
                     '334 67 65 70 86',
                     '334 67 42 54 64'],
            'freq_mnt': ['tous les ans',
                         pd.NA,
                         'Tous les ans',
                         pd.NA,
                         'Tous les ans',
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         pd.NA,
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         'Tout les ans',
                         'Tous les ans'],
            'dermnt': [pd.to_datetime('2019-05-15'),
                       pd.NaT,
                       pd.to_datetime('2019-12-01'),
                       pd.NaT,
                       pd.to_datetime('2019-12-01'),
                       pd.NaT,
                       pd.to_datetime('2019-04-16'),
                       pd.NaT,
                       pd.NaT,
                       pd.NaT,
                       pd.to_datetime('2018-12-6'),
                       pd.NaT,
                       pd.to_datetime('2019-11-01'),
                       pd.to_datetime('2019-12-01')],
            'lat_coor1': [3.93392108647369,
                          np.NaN,
                          3.86476856812559,
                          3.81486877448227,
                          3.89640622981796,
                          3.88032026773112,
                          3.87860752258093,
                          3.86982233698134,
                          np.NaN,
                          3.91169364237597,
                          3.91771559166406,
                          np.Nan,
                          3.89668282061293,
                          3.85476904201268],
            'long_coor1': [43.6136351580956,
                           np.NaN,
                           43.5883499187015,
                           43.6203748790079,
                           43.5929214621688,
                           43.6106902122358,
                           43.6050174875771,
                           43.6127835439949,
                           np.NaN,
                           43.6184228878598,
                           43.5989740313524,
                           43.6020241317034,
                           43.5911769531706,
                           43.5995832643803]},
        dtype={'nom': 'string', 'adr_num': 'string', 'adr_voie': 'string',
               'com_cp': 'string', 'com_nom': 'string', 'tel1': 'string', 
               'freq_mnt': 'string', 'dermnt': 'string', 
               'lat_coor1': 'float', 'long_coor1': 'float'}
    )

    return df


@pytest.fixture
def sample_sanitized() -> pd.DataFrame:
    df = pd.DataFrame(
        data={
            'nom': ['Plateau sportif de GrammontTerrain 9, 10, 11',
                    'MEDIATHEQUE JEAN-JACQUES ROUSSEAU',
                    "Ecole maternelle Aliénor-d'Aquitaine - Ecole élémentaire Ronsard",
                    'Piscine centre nautique neptune',
                    'Ecole maternelle Paul-Eluard - Ecole élémentaire Jean Macé',
                    'Centre Culturel Rabelais',
                    'Poste de police Ecusson Centre ville',
                    pd.NA,
                    'EHPAD "Michel BELORGEOT"',
                    'DELL',
                    'Gymnase François Spinosi',
                    "Siège du CCAS (Banque d'Acceuil)",
                    'Vestiaire/tribune CLAUDE BEAL',
                    'Ecole élémentaire Winston Churchill - Ecole maternelle Marceline Desbordes-Valmore'],
            'adr_num': [pd.NA,
                        pd.NA,
                        '694-700',
                        pd.NA,
                        '219-289',
                        '29',
                        '19 bis',
                        '1',
                        '41',
                        '1',
                        pd.NA,
                        '125',
                        '419',
                        '424-460'],
            'adr_voie': ['avenue albert Einstein',
                         pd.NA,
                         'rue Jacques-Bounin',
                         pd.NA,
                         'rue de Saint Hilaire',
                         'boulevard Sarrail',
                         'rue Durand',
                         'place Jacques Mirouse',
                         'impasse des Moulins',
                         'rond-point Benjamin Franklin',
                         'Rue Pierre Gilles de Gennes',
                         'place Thermidor',
                         'avenue du Dr Jacques Fourcade',
                         'rue du lavandin'],
            'com_cp': ['34000',
                       pd.NA,
                       '34070',
                       pd.NA,
                       '34000',
                       '34000',
                       '34000',
                       '34000',
                       '34000',
                       pd.NA,
                       '34000',
                       '34000',
                       '34000',
                       '34070'],
            'com_nom': ['Montpellier',
                        pd.NA,
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        pd.NA,
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier',
                        'Montpellier'],
            'tel1': ['+33 4 67 64 87 70',
                     pd.NA,
                     '+33 4 67 27 46 12',
                     pd.NA,
                     '+33 4 67 64 40 54',
                     '+33 4 67 34 71 33',
                     '+33 4 67 34 70 89',
                     pd.NA,
                     '+33 4 67 40 04 44',
                     '+33 6 58 57 85 24',
                     '+33 4 67 15 90 35',
                     '+33 4 99 52 77 53',
                     '+33 4 67 65 70 86',
                     '+33 4 67 42 54 64'],
            'freq_mnt': ['tous les ans',
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         pd.NA,
                         pd.NA,
                         'tous les ans',
                         pd.NA,
                         'tout les ans',
                         'tous les ans'],
            'dermnt': [pd.to_datetime('2019-05-15'),
                       pd.NaT,
                       pd.to_datetime('2019-12-01'),
                       pd.NaT,
                       pd.to_datetime('2019-12-01'),
                       pd.NaT,
                       pd.to_datetime('2019-04-16'),
                       pd.NaT,
                       pd.NaT,
                       pd.NaT,
                       pd.to_datetime('2018-12-6'),
                       pd.NaT,
                       pd.to_datetime('2019-11-01'),
                       pd.to_datetime('2019-12-01')],
            'lat_coor1': [3.93392108647369,
                          np.NaN,
                          3.86476856812559,
                          3.81486877448227,
                          3.89640622981796,
                          3.88032026773112,
                          3.87860752258093,
                          3.86982233698134,
                          np.NaN,
                          3.91169364237597,
                          3.91771559166406,
                          np.Nan,
                          3.89668282061293,
                          3.85476904201268],
            'long_coor1': [43.6136351580956,
                           np.NaN,
                           43.5883499187015,
                           43.6203748790079,
                           43.5929214621688,
                           43.6106902122358,
                           43.6050174875771,
                           43.6127835439949,
                           np.NaN,
                           43.6184228878598,
                           43.5989740313524,
                           43.6020241317034,
                           43.5911769531706,
                           43.5995832643803]},
        dtype={'nom': 'string', 'adr_num': 'string', 'adr_voie': 'string',
               'com_cp': 'string', 'com_nom': 'string', 'tel1': 'string', 
               'freq_mnt': 'string', 'dermnt': 'string', 
               'lat_coor1': 'float', 'long_coor1': 'float'}
    
    )
    return df


@pytest.fixture
def sample_framed() -> pd.DataFrame:
    # TODO Complete the test case bellow
    df = pd.DataFrame(
        data=...,
        dtype=...
    )
    return df


def test_load_formatted_data(sample_dirty_fname, sample_formatted):
    from loader import load_formatted_data
    assert load_formatted_data(sample_dirty_fname).equals(sample_formatted)


def test_sanitize_data(sample_formatted, sample_sanitized):
    from loader import sanitize_data
    assert sanitize_data(sample_formatted).equals(sample_sanitized)


def test_frame_data(sample_sanitized, sample_framed):
    from loader import frame_data
    assert frame_data(sample_sanitized).equals(sample_framed)


def test_load_clean_data(sample_dirty_fname, sample_framed):
    from loader import load_clean_data
    assert load_clean_data(sample_dirty_fname).equals(sample_framed)


def assert_column_equal(clean, target, column):
    # utility function if you which to implement column-specific assertion tests
    assert clean[column].equals(
        target[column]), f"Result should be {clean[column]} but was {target[column]}"
