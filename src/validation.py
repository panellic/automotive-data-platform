def validate_vehicles(df):
    missing_values = df.isnull().sum().sum()
    duplicate_vins = df["vin"].duplicated().sum()
    invalid_model_years = (
        (df["model_year"] < 2000) |
        (df["model_year"] > 2030)
    ).sum()

    print("Invalid model years:", invalid_model_years)
    print("Missing values:", missing_values)
    print("Duplicate VINs:", duplicate_vins)

    is_valid = (
        missing_values == 0
        and duplicate_vins == 0
        and invalid_model_years == 0
    )

    if is_valid:
        print("Validation PASSED")
    else:
        print("Validation FAILED")

    return bool(is_valid)
 