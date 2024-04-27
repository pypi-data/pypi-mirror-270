################################################################################
############################### Library Imports ################################
import pandas as pd
import numpy as np

################################################################################


class RiskPredictor:
    """
    A class to represent a risk predictor for chronic kidney disease (CKD).

    This class uses the Tangri risk prediction model, which calculates risk
    based on various patient parameters. Results are accurate for both males
    and females, but the original paper calculated risk specifically for males.

    Attributes:
    data (DataFrame): The patient data.
    columns (dict): Dictionary to map expected parameter names to actual column
    names in the data.

    Methods:
    predict(years, use_extra_vars): Predicts the risk of CKD for the given
    number of years, optionally using extra variables for the prediction.
    """

    def __init__(
        self,
        data=None,
        columns=None,
    ):
        """
        Constructs the necessary attributes for the RiskPredictor object.

        Parameters:
        data (DataFrame): The patient data.
        columns (dict): A dictionary specifying the column names in the dataset
        that correspond to the required parameters.
        Example: {'age': 'Age', 'sex': 'Gender', 'eGFR': 'eGFR',
        'uACR': 'Albumin_Ratio', 'region': 'Region', 'dm': 'Diabetes',
        'htn': 'Hypertension'}
        apply_conversions (bool, optional): Flag to apply unit conversions.
        Default is False.
        """
        self.data = data
        self.columns = columns

    def perform_conversions(self, reverse=False):
        """
        Applies or reverses unit conversions to the biochemical markers in the dataset.

        Parameters:
        - reverse (bool): If True, perform reverse conversions. Defaults to False.

        Converts:
        - uPCR from mmol to mg/g or vice versa
        - Calcium from mmol to mg/dL or vice versa
        - Phosphate from mmol to mg/dL or vice versa
        - Albumin from g/L to g/dL or vice versa
        """
        if not reverse:
            # Conversions from units in the dataset to standard units
            # 0.11312 g creatinine/1 mg protein = 8.84
            conversion_factor = 1 / 0.11312
            self.data["uPCR (mg/g)"] = (
                self.data[self.columns["uPCR_mmol"]] * conversion_factor
            )
            self.data["Calcium (mg/dL)"] = self.data[self.columns["calcium_mmol"]] * 4
            self.data["Phosphate (mg/dL)"] = (
                self.data[self.columns["phosphate_mmol"]] * 3.1
            )
            self.data["Albumin (g/dL)"] = (
                self.data[self.columns["albumin_g_per_l"]] / 10
            )
        else:
            # Reverse conversions from standard units back to units in the dataset
            # 0.11312 g creatinine/1 mg protein = 8.84
            self.data[self.columns["uPCR_mmol"]] = (
                self.data["uPCR (mg/g)"] / conversion_factor
            )
            self.data[self.columns["calcium_mmol"]] = self.data["Calcium (mg/dL)"] / 4
            self.data[self.columns["phosphate_mmol"]] = (
                self.data["Phosphate (mg/dL)"] / 3.1
            )
            self.data[self.columns["albumin_g_per_l"]] = (
                self.data["Albumin (g/dL)"] * 10
            )

    def predict_kfre(
        self,
        years,
        is_north_american,
        use_extra_vars=False,
        num_vars=4,
    ):
        """
        Predicts the risk of chronic kidney disease (CKD) over a specified
        number of years using the Tangri risk prediction model. This method
        supports the basic 4-variable model as well as the extended 6-variable
        and 8-variable models if additional patient data is available.

        Parameters:
        - years (int): The number of years over which the risk assessment is
          projected.
        - is_north_american (bool): Flag indicating whether the patient is from
          North America, which affects the model's constants.
        - use_extra_vars (bool, optional): Determines if additional variables
          (such as diabetes and hypertension status for the 6-variable model, or
          biochemical markers for the 8-variable model) should be used in the
          risk calculation. Defaults to False.
        - num_vars (int, optional): Specifies the number of variables to use in
          the prediction model (4, 6, or 8). Defaults to 4.

        Returns:
        - float: A probability value between 0 and 1 representing the patient's
          risk of CKD development within the specified timeframe.

        Raises:
        - ValueError: If `num_vars` is set to an unsupported number.

        Notes:
        - The 6-variable model includes diabetes and hypertension status in
          addition to the base parameters.
        - The 8-variable model includes serum albumin, phosphorous, bicarbonate,
          and calcium levels in addition to the parameters used in the
          6-variable model.
        - It is important to provide accurate mappings in the `columns`
          dictionary upon class instantiation for the method to correctly locate
          the necessary data in the DataFrame.
        """
        # Basic required columns
        necessary_cols = [
            self.columns["age"],
            self.columns["sex"],
            self.columns["eGFR"],
            self.columns["uACR"],
        ]

        # Retrieve data only once
        data = self.data[necessary_cols].copy()

        # Convert sex to numeric in a vectorized way
        data[self.columns["sex"]] = (
            data[self.columns["sex"]].str.lower() == "male"
        ).astype(int)

        # Extract basic parameters from the DataFrame
        age = data[self.columns["age"]]
        sex = data[self.columns["sex"]]
        eGFR = data[self.columns["eGFR"]]
        uACR = data[self.columns["uACR"]]

        if use_extra_vars:
            if num_vars == 6:
                # Extend columns for 6-variable model
                necessary_cols.extend([self.columns["dm"], self.columns["htn"]])
                data = self.data[necessary_cols].copy()
                dm = data[self.columns["dm"]]
                htn = data[self.columns["htn"]]
                return risk_pred(
                    age, sex, eGFR, uACR, is_north_american, dm, htn, years=years
                )
            elif num_vars == 8:
                # Extend columns for 8-variable model
                necessary_cols.extend(
                    [
                        self.columns["albumin"],
                        self.columns["phosphorous"],
                        self.columns["bicarbonate"],
                        self.columns["calcium"],
                    ]
                )
                data = self.data[necessary_cols].copy()
                albumin = data[self.columns["albumin"]]
                phosphorous = data[self.columns["phosphorous"]]
                bicarbonate = data[self.columns["bicarbonate"]]
                calcium = data[self.columns["calcium"]]
                return risk_pred(
                    age,
                    sex,
                    eGFR,
                    uACR,
                    is_north_american,
                    None,
                    None,
                    albumin,
                    phosphorous,
                    bicarbonate,
                    calcium,
                    years=years,
                )
        else:
            # Call the function with basic parameters for the 4-variable model
            return risk_pred(age, sex, eGFR, uACR, is_north_american, years=years)

    def kfre_person(
        self,
        age,
        is_male,
        eGFR,
        uACR,
        is_north_american,
        years=2,
        dm=None,
        htn=None,
        albumin=None,
        phosphorous=None,
        bicarbonate=None,
        calcium=None,
    ):
        """
        Predicts CKD risk for an individual patient based on provided clinical
        parameters.

        Parameters:
        - age (float): Age of the patient.
        - is_male (bool): True if the patient is male, False if female.
        - eGFR (float): Estimated Glomerular Filtration Rate.
        - uACR (float): Urinary Albumin to Creatinine Ratio.
        - is_north_american (bool): True if the patient is from North America,
          False otherwise.
        - years (int): Time horizon for the risk prediction (default is 2 years).
        - dm (float, optional): Diabetes mellitus indicator (1=yes; 0=no).
        - htn (float, optional): Hypertension indicator (1=yes; 0=no).
        - albumin (float, optional): Serum albumin level.
        - phosphorous (float, optional): Serum phosphorous level.
        - bicarbonate (float, optional): Serum bicarbonate level.
        - calcium (float, optional): Serum calcium level.

        Returns:
        - float: The computed risk of developing CKD.
        """
        # Use is_male directly, since it's already a boolean
        # Call the risk prediction function with the parameters
        risk_prediction = risk_pred(
            age=age,
            sex=is_male,
            eGFR=eGFR,
            uACR=uACR,
            is_north_american=is_north_american,
            years=years,
            dm=dm,
            htn=htn,
            albumin=albumin,
            phosphorous=phosphorous,
            bicarbonate=bicarbonate,
            calcium=calcium,
        )
        return risk_prediction


################################################################################
################################ uPCR to uACR ##################################
################################################################################


def upcr_uacr(
    row,
    sex_col,
    diabetes_col,
    hypertension_col,
    upcr_col,
    female_str,
):
    """
    Converts urinary protein-creatinine ratio (uPCR) to urinary
    albumin-creatinine ratio (uACR) using a specified formula that considers
    patient demographics and conditions.

    Parameters:
    - row (pd.Series): A single row from a pandas DataFrame representing one
      patient's data.
    - sex_col (str): Column name containing the patient's gender.
    - diabetes_col (str): Column name indicating whether the patient has
      diabetes (1 for yes, 0 for no).
    - hypertension_col (str): Column name indicating whether the patient has
      hypertension (1 for yes, 0 for no).
    - upcr_col (str): Column name containing the urinary protein-creatinine ratio.
    - female_str (str): The exact string used in the dataset to identify a
      patient as female, critical for accurate calculations.

    Returns:
    - float: The computed urinary albumin-creatinine ratio (uACR).

    This function applies a complex logarithmic and exponential calculation to
    derive the uACR from the uPCR, adjusting for factors such as gender,
    diabetes, and hypertension status. The accuracy of the function relies on
    the exact match of the 'female_str' with the dataset's representation of
    female gender.

    Notes: Conversion from uPCR to uACR can be independently verified using the
    calculator on `https://ckdpcrisk.org/pcr2acr/`
    """
    upcr = row[upcr_col]
    female = 1 if row[sex_col] == female_str else 0
    diabetic = row[diabetes_col]
    hypertensive = row[hypertension_col]

    # Applying the provided formula
    uacr = np.exp(
        5.2659
        + 0.2934 * np.log(np.minimum(upcr / 50, 1))
        + 1.5643 * np.log(np.maximum(np.minimum(upcr / 500, 1), 0.1))
        + 1.1109 * np.log(np.maximum(upcr / 500, 1))
        - 0.0773 * female
        + 0.0797 * diabetic
        + 0.1265 * hypertensive
    )
    return uacr


################################################################################
############################## KFRE Risk Predictor #############################
################################################################################


def risk_pred(
    age,
    sex,
    eGFR,
    uACR,
    is_north_american,
    dm=None,
    htn=None,
    albumin=None,
    phosphorous=None,
    bicarbonate=None,
    calcium=None,
    years=2,
):
    """
    Calculates the risk of chronic kidney disease progression based on a range
    of clinical parameters using the Tangri risk prediction model. This model
    can use 4, 6, or 8 variables for prediction based on the data available.
    The coefficients and constants used in the calculations are selected based
    on the geographic region of the patient (North American or not) and the time
    horizon for the risk prediction (2 or 5 years).

    Parameters:
    - age (float): Age of the patient in years.
    - sex (int): Biological sex of the patient (0 for female, 1 for male).
    - eGFR (float): Estimated Glomerular Filtration Rate, indicating kidney
      function.
    - uACR (float): Urinary Albumin to Creatinine Ratio, showing kidney damage
      level.
    - is_north_american (bool): Indicates if the patient is from North America.
    - dm (float, optional): Indicates if the patient has diabetes (0 or 1).
    - htn (float, optional): Indicates if the patient has hypertension (0 or 1).
    - albumin (float, optional): Serum albumin level, required for the
      8-variable model.
    - phosphorous (float, optional): Serum phosphorous level, required for the
      8-variable model.
    - bicarbonate (float, optional): Serum bicarbonate level, required for the
      8-variable model.
    - calcium (float, optional): Serum calcium level, required for the
      8-variable model.
    - years (int, default=2): The number of years over which the risk is
      redicted (2 or 5 years).

    Returns:
    - risk_prediction (float): A probability value between 0 and 1 representing
      the patient's risk of developing chronic kidney disease within the
      specified number of years.

    Notes:
    The function accounts for the patient's geographic location by adjusting the
    alpha constants in the risk calculation. It defaults to coefficients for the
    4-variable model unless additional parameters are provided, in which case it
    switches to the 6-variable or 8-variable models.
    """

    # Define the alpha values and risk factor coefficients for each model
    if dm is not None and htn is not None:
        # 6-variable model
        alpha_values = {
            (True, 2): 0.9750,
            (True, 5): 0.9240,
            (False, 2): 0.9830,
            (False, 5): 0.9370,
        }
        risk_factors = {
            "age": -0.2218,  # Adjusted for 6-var model
            "sex": 0.2553,  # Adjusted for 6-var model
            "eGFR": -0.5541,  # Adjusted for 6-var model
            "uACR": 0.4562,  # Adjusted for 6-var model
        }
        dm_factor = -0.1475  # DM risk factor coefficient
        htn_factor = 0.1426  # HTN risk factor coefficient
    elif (
        albumin is not None
        and phosphorous is not None
        and bicarbonate is not None
        and calcium is not None
    ):
        # 8-variable model
        alpha_values = {
            (True, 2): 0.9780,
            (True, 5): 0.9301,
            (False, 2): 0.9827,
            (False, 5): 0.9245,
        }
        risk_factors = {
            "age": -0.1992,  # Adjusted for 8-var model
            "sex": 0.1602,  # Adjusted for 8-var model
            "eGFR": -0.4919,  # Adjusted for 8-var model
            "uACR": 0.3364,  # Adjusted for 8-var model
        }
        # Extra risk factors for the 8-variable model
        albumin_factor = -0.3441
        phosph_factor = +0.2604
        bicarb_factor = -0.07354
        calcium_factor = -0.2228
    else:
        # 4-variable model
        alpha_values = {
            (True, 2): 0.9750,
            (True, 5): 0.9240,
            (False, 2): 0.9832,
            (False, 5): 0.9365,
        }
        risk_factors = {
            "age": -0.2201,
            "sex": 0.2467,
            "eGFR": -0.5567,
            "uACR": 0.4510,
        }

    # Ensure uACR is positive to avoid log(0)
    uACR = np.maximum(uACR, 1e-6)
    log_uACR = np.log(uACR)

    # Compute the base risk score using the coefficients
    risk_score = (
        risk_factors["age"] * (age / 10 - 7.036)
        + risk_factors["sex"] * (sex - 0.5642)
        + risk_factors["eGFR"] * (eGFR / 5 - 7.222)
        + risk_factors["uACR"] * (log_uACR - 5.137)
    )

    # Adjust risk score for the 6-variable model if DM and HTN data is provided
    if dm is not None and htn is not None:
        risk_score += dm_factor * (dm - 0.5106) + htn_factor * (htn - 0.8501)

    # Adjust risk score for the 8-variable model if additional data is provided
    if (
        albumin is not None
        and phosphorous is not None
        and bicarbonate is not None
        and calcium is not None
    ):
        risk_score += (
            albumin_factor * (albumin - 3.997)
            + phosph_factor * (phosphorous - 3.916)
            + bicarb_factor * (bicarbonate - 25.57)
            + calcium_factor * (calcium - 9.355)
        )

    # Select alpha based on region and years
    alpha = alpha_values[(is_north_american, years)]

    # Compute the risk prediction
    risk_prediction = 1 - alpha ** np.exp(risk_score)
    return risk_prediction
